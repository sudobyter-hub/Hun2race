class NlpEngine:
    def __init__(self, vulnerability):
        self.prompts = {
            "vulnerability_description": f"describe the following bug {vulnerability} with details to technical and non technical people",
            "impact_description": f"what is the impact of this {vulnerability} and how it might affect the company",
            "suggestions": f"what do you suggest to fix this {vulnerability} write full details"
        }

    def __get_vulnerability_description(self):
        pass

    def __get_impact_description(self):
        pass

    def __get_suggestions(self):
        pass

    def get_contents(self):
        vulnerability_desc = self.__get_vulnerability_description()
        impact_desc = self.__get_impact_description()
        suggestions = self.__get_suggestions()
        return vulnerability_desc, impact_desc, suggestions
