import os

class Template:
    def __init__(self):
        pass

    def get_available_templates(self):
        return [
            "bug_bounty",
            "pentesting"
        ]

    def get_template(self, template_name):
        try:
            path = os.path.join(os.getcwd(), "modules", "documentors", "templates", f"{template_name}.txt")
            return open(path, "r").read()
        except FileNotFoundError:
            print(f"Template {template_name} not found.")
            return None