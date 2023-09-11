from modules.documentors.template import Template
from modules.documentors.image_provider import ImageProvider

class Latex:
    def __init__(self, use_case, vulnerability_type, targeted_domain, vulnerability_desc, proof_of_concept,
                 impact_description, suggestions, images_urls):
        self.use_case = use_case
        self.vulnerability_type = vulnerability_type
        self.targeted_domain = targeted_domain
        self.vulnerability_desc = vulnerability_desc
        self.proof_of_concept = proof_of_concept
        self.impact_desc = impact_description
        self.suggestions = suggestions
        self.images_urls = images_urls

    def attach_images(self):
        """Generates LaTeX code to embed multiple images."""
        image_latex = ""
        images_paths = []
        if self.images_urls:
            images_paths += ImageProvider().get_images_from_urls(self.images_urls)
        for path in images_paths:
            image_latex += r"\includegraphics[width=\linewidth]{" + path + "}\n\\newpage\n"
        return image_latex


    def generate_report(self):
        """Generates a LaTeX report based on the provided information."""
        template = Template().get_template(self.use_case)

        image_latex = self.attach_images()

        report = template.format(
            vulnerability=self.vulnerability_type,
            host=self.targeted_domain,
            vulnerability_desc=self.vulnerability_desc,
            proof_of_concept=self.proof_of_concept,
            impact_description=self.impact_desc,
            suggestions=self.suggestions,
            image_latex=image_latex
        )
        return report