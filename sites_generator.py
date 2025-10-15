from jinja2 import Environment, FileSystemLoader
from pathlib import Path

TEMPLATES_DIR = Path("templates")
OUTPUT_DIR = Path("./output")

env = Environment(loader=FileSystemLoader("templates"))

for template_path in TEMPLATES_DIR.glob("*.html"):
    if template_path.name == "main.html":
        continue

    template = env.get_template(template_path.name)
    rendered = template.render()

    output_file = OUTPUT_DIR / template_path.name
    output_file.write_text(rendered, encoding="utf-8")

    print(f"generated {template_path.name}")

