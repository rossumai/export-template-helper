def generate_settings(templatePath, key):
    f = open(templatePath)
    data = f.read().splitlines()
    template = []

    for i, line in enumerate(data):
        template.append(f"""\"{line.replace('"', '\\"')}\"{"" if i+1 == len(data) else ","}""")
        
    header = f"""
{{
    \"export_configs\": [{{
        "export_reference_key": "{key}",
        "file_content_template_multiline": [
            {'\n            '.join(template)}
        ]
    }}]
}}"""
    print(header)