import json
from jinja2 import FileSystemLoader, Environment
import requests
from mega_helper.helpers.payload_transformer import build_context_dict

def process(templatePath, payloadPath, annotationId, token, hookId, url):
    env = Environment(
        loader=FileSystemLoader(".")
    )
    template = env.get_template(templatePath)

    payload = ""
    if (payloadPath):
        f = open(payloadPath)
        payload = json.load(f)
    elif (annotationId and hookId and url and token):
        api_payload = {
            "event": "annotation_content",
            "action": "export",
            "annotation": f"{url}/annotations/{annotationId}",
            "previous_status": "confirmed",
            "status": "exporting"
        }
        r = requests.post(f"{url}/hooks/{hookId}/generate_payload", data=api_payload, headers={"Authorization": f"Bearer {token}"})
        payload = r.json()
    else:
        raise Exception("Payload missing")
        
    data = build_context_dict(payload["annotation"])
    print(template.render({"field": data, "payload": payload}))