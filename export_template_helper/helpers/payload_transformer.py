def build_context_dict(annotation) -> dict[str, any]:
    context: dict[str, any] = {}
    for section in annotation["content"]:
        context.update(_build_node_dict(section["children"]))
    return context


def _build_node_dict(
    children
) -> dict[str, any]:
    return {node["schema_id"]: _build_node_value(node) for node in children}


def _build_node_value(
    content_element
) -> any:
    match content_element["category"]:
        case "datapoint":
            return content_element["content"]["normalized_value"] if "normalized_value" in content_element["content"] and content_element["content"]["normalized_value"] else content_element["content"]["value"]

        case "tuple":
            return _build_node_dict(content_element["children"])

        case "multivalue":
            children = content_element["children"]
            if not children:
                return []

            if children[0]["category"] == "datapoint":
                return _build_node_dict(children)

            return [_build_node_value(node) for node in children]