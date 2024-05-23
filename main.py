import argparse, yaml, os
from jinja2 import Environment, FileSystemLoader

def parse_args():
    parser = argparse.ArgumentParser(description="Generate Kubernetes Manifest file")
    parser.add_argument('--template', type=str, required=True, help='Choose between minimal or complex')
    parser.add_argument('--kind', type=str, required=True, help='Resources Kind such us Pod, Deployment, Service, etc')
    parser.add_argument('--name', type=str, required=True, help='Name of Resources')
    parser.add_argument('--label', type=str, required=True, help='Label of Resources')
    parser.add_argument('--labelValue', type=str, required=True, help='Value of Label')
    parser.add_argument('--containerName', type=str, required=True, help='Container Name')
    parser.add_argument('--imageName', type=str, required=True, help='Image Name')
    parser.add_argument('--port', type=str, required=True, help='Port')
    parser.add_argument('--output', type=str, required=True, help='Output file name')

    return parser.parse_args()

def render_template(template_name, output_path, context):
    template_dir = os.path.join(os.path.dirname(__file__), 'templates')
    env = Environment(loader=FileSystemLoader(template_dir))

    if template_name == 'minimal':
        template_path = 'minimal_pod.yaml'
    elif template_name == 'complex':
        template_path = 'complex_pod.yaml'
    else:
        raise ValueError("Invalid template name. Choose between 'minimal' or 'complex'.")

    template = env.get_template(template_path)
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

    render_template(args.template , args.output, context)