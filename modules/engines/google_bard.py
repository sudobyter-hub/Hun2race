from bardapi import Bard
from modules.engines.nlp_engine import NlpEngine
import os


class GoogleBard(NlpEngine):

    def __init__(self, vulnerability, api_key):
        super().__init__(vulnerability)
        self.bard = Bard()
        os.environ["_BARD_API_KEY"] = api_key

    def __get_vulnerability_description(self):
        bard_response = Bard().get_answer(str(self.prompts['vulnerability_description']))
        return bard_response.get('content')

    def __get_impact_description(self):
        bard_response = Bard().get_answer(str(self.prompts['impact_description']))
        return bard_response.get('content')

    def __get_suggestions(self):
        bard_response = Bard().get_answer(str(self.prompts['suggestions']))
        return bard_response.get('content')
