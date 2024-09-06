import requests


def generate_settings(templatePath, key):
    f = open(templatePath)
    data = f.read().splitlines()
    template = []

    for i, line in enumerate(data):
        template.append(f"""\"{line.replace('"', '\\"')}\"{"" if i+1 == len(data) else ","}""")
        
    header = f"""
{{
  \"export_configs\": [
    {{
      "export_reference_key": "{key}",
      "file_content_template_multiline": [
        {'\n        '.join(template)}
      ]
    }}
  ]
}}"""
    print(header)
    
def parse_settings(templatePath, hookId, url, token):
        r = requests.get(f"{url}/hooks/{hookId}", headers={"Authorization": f"Bearer {token}"})
        payload = r.json()
        settings = payload["settings"]
        if "export_configs" not in settings:
            raise Exception("export_configs missing in extension settings")
        if len(settings) != 1:
            raise Exception("Multiple export_configs found in extension settings. Only single export config is supported.")
        if "file_content_template" not in settings["export_configs"][0] and "file_content_template_multiline" not in settings["export_configs"][0]:
            raise Exception("No template content in export config found")
        template = ""
        if "file_content_template_multiline" in settings["export_configs"][0]:
            template = "\n".join(settings["export_configs"][0]["file_content_template_multiline"])
        else:
            template = settings["export_configs"][0]["file_content_template"]
        
        f = open(templatePath, "w")
        f.write(template)
        f.close()

        print(f"Template {templatePath} saved, export reference key: {settings["export_configs"][0]["export_reference_key"]}")
    