"""
    Translator authentication and translation functions
"""

import os
import json
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2019-04-30',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

language_translator.set_disable_ssl_verification(True)

def english_to_french(string_in_english):
    """
    Translate Text From English To French
    """
    translated_to_french = language_translator.translate(
        text=string_in_english,
        model_id='en-fr').get_result()
    print(json.dumps(translated_to_french.get("translations")[0].get(
        "translation"), indent=2, ensure_ascii=False))
    if not string_in_english:
        return None
    return translated_to_french("translations")[0].get("translation")


def french_to_english(string_in_french):
    """
    Translate Text From French To English
    """
    translated_to_english = language_translator.translate(
        text=string_in_french,
        model_id='fr-en').get_result()
    print(json.dumps(translated_to_english.get("translations")[0].get(
        "translation"), indent=2, ensure_ascii=False))
    if not string_in_french:
        return None
    return translated_to_english.get("translations")[0].get("translation")
