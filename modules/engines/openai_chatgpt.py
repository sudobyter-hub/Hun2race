import openai
from modules.engines.nlp_engine import NlpEngine


class OpenaiChatgpt(NlpEngine):

    def __init__(self, vulnerability, api_key, max_tokens=2500, model="text-davinci-002"):
        super().__init__(vulnerability)
        openai.api_key = api_key
        self.max_tokens = max_tokens
        self.model = model

    def __get_vulnerability_description(self):
        response = openai.Completion.create(model=self.model, prompt=self.prompts['vulnerability_description'], max_tokens=self.max_tokens)
        return response.choices[0].text.strip()

    def __get_impact_description(self):
        response = openai.Completion.create(model=self.model, prompt=self.prompts['impact_description'], max_tokens=self.max_tokens)
        return response.choices[0].text.strip()

    def __get_suggestions(self):
        response = openai.Completion.create(model=self.model, prompt=self.prompts['suggestions'], max_tokens=self.max_tokens)
        return response.choices[0].text.strip()

    def get_contents(self):
        vulnerability_desc = self.__get_vulnerability_description()
        impact_desc = self.__get_impact_description()
        suggestions = self.__get_suggestions()
        return vulnerability_desc, impact_desc, suggestions