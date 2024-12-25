from pathlib import Path

class TemplateEngine:
    def render(self, template_name, **kwargs):
        template_path = Path(__file__).parent / "../templates" / template_name
        with open(template_path, "r") as f:
            template_content = f.read()

        for key, value in kwargs.items():
            template_content = template_content.replace(f"{{{{ {key} }}}}", str(value))
        
        return template_content
