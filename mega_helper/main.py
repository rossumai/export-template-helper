import argparse

from mega_helper.commands import generate_settings, process

def main():
    parser = argparse.ArgumentParser(description="Process Jinja2 template with Rossum annotation payload and generate extension config.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-p", "--process", help="process a local Jinja2 template with Rossum annotation payload", action="store_true"),
    group.add_argument("-g", "--generate", help="generate MEGA extension configuration using a local Jinja2 template", action="store_true")
    parser.add_argument("-t", "--templatePath", help="path to local Jinja2 template", type=str)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-l", "--payloadPath", help="path to local file with Rossum annotation payload", type=str)
    group.add_argument("-a", "--annotationId", help="annotation ID to fetch payload from Rossum API", type=int)
    parser.add_argument("-n", "--token", help="Rossum API token", type=str)
    parser.add_argument("-o", "--hookId", help="Rossum hook ID", type=int)
    parser.add_argument("-u", "--url", help="Rossum base API URL", type=str)
    parser.add_argument("-k", "--key", help="Export reference key", type=str)

    args = parser.parse_args()

    if (args.process):
        if not args.templatePath:
            raise Exception("Template path missing")
        if not args.payloadPath and (not args.annotationId or not args.token or not args.hookId or not args.url):
            raise Exception("Payload path or annotationId, hookId, base URL and token missing")
        process(args.templatePath, args.payloadPath, args.annotationId, args.token, args.hookId, args.url)

    elif (args.generate):
        if not args.templatePath:
            raise Exception("Template path missing")
        if not args.key:
            raise Exception("Export reference key missing")
        generate_settings(args.templatePath, args.key)
    
    else:
        raise Exception("Command missing")
    
# For debugging purposes
if __name__ == "__main__":
    main()