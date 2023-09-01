import abc


class NlpEngine(abc.ABC):
    def __init__(self, vulnerability):
        self.prompts = {
            "vulnerability_description": f"describe the following bug {vulnerability} with details to technical and non technical people",
            "impact_description": f"what is the impact of this {vulnerability} and how it might affect the company",
            "suggestions": f"what do you suggest to fix this {vulnerability} write full details"
        }


    @abc.abstractmethod
    def get_contents(self):
        pass