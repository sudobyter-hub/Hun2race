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
            return open(f"modules/documentors/templates/{template_name}.txt", "r").read()
        except FileNotFoundError:
            print(f"Template {template_name} not found.")
            return None