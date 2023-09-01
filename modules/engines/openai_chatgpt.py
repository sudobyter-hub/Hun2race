import openai
from modules.engines.nlp_engine import NlpEngine
import os


class OpenaiChatgpt(NlpEngine):

    def __init__(self, vulnerability, api_key, max_tokens=2500, engine="text-davinci-002"):
        super().__init__(vulnerability)
        self.prompts = {
            "vulnerability_description": f"describe the following bug {vulnerability} with details to technical and non technical people",
            "impact_description": f"what is the impact of this {vulnerability} and how it might affect the company",
            "suggestions": f"what do you suggest to fix this {vulnerability} write full details"
        }
        openai.api_key = api_key
        self.max_tokens = max_tokens
        self.engine = engine

    def __get_vulnerability_description(self):
        response = openai.Completion.create(model=self.engine, prompt=self.prompts['vulnerability_description'], max_tokens=self.max_tokens)
        return response.choices[0].text.strip()

    def __get_impact_description(self):
        response = openai.Completion.create(model=self.engine, prompt=self.prompts['impact_description'], max_tokens=self.max_tokens)
        return response.choices[0].text.strip()

    def __get_suggestions(self):
        response = openai.Completion.create(model=self.engine, prompt=self.prompts['suggestions'], max_tokens=self.max_tokens)
        return response.choices[0].text.strip()