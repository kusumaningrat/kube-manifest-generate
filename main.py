import argparse
import os
from jinja2 import Environment, FileSystemLoader

def parse_args():
    parser = argparse.ArgumentParser(description="Generate Kubernetes Manifest file")
    parser.add_argument('--kind', type=str, required=True, help='Resources Kind such us Pod, Deployment, Service, etc')
    parser.add_argument('--name', type=str, required=True, help='Name of Resources')
    parser.add_argument('--label', type=str, required=True, help='Label of Resources')
    parser.add_argument('--labelValue', type=str, required=True, help='Value of Label')
    parser.add_argument('--containerName', type=str, required=True, help='Container Name')
    parser.add_argument('--imageName', type=str, required=True, help='Image Name')
    parser.add_argument('--port', type=str, required=False, help='Port')
    parser.add_argument('--output', type=str, required=True, help='Output file name')

    return parser.parse_args()

def render_template(kind, output_path, context):
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    env = Environment(loader=FileSystemLoader(template_dir))

    # Define the template filename based on the provided kind
    template_filename = f"{kind.lower()}.yaml"
    template_path = os.path.join(template_dir, template_filename)

    try:
        # Load the template from the file
        template = env.get_template(template_filename)
    except Exception as e:
        raise ValueError(f"No template found for '{kind}'. Please make sure to choose a valid resource name.") from e
    
    rendered_content = template.render(context)

    with open(output_path, 'w') as file:
        file.write(rendered_content)
    print(f"Manifest file is generated and saved to {output_path}")

if __name__ == '__main__':
    args = parse_args()

    context = {
        'kind': args.kind,
        'name': args.name,
        'label': args.label,
        'labelValue': args.labelValue,
        'imageName': args.imageName,
        'containerName': args.containerName,
        'port': args.port
    }

    try:
        render_template(args.kind, args.output, context)
    except ValueError as ve:
        print(ve)
