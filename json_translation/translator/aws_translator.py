from .translator import Translator
import boto3
import botocore


class AWSTranslator(Translator):
    def __init__(self, **kwargs) -> None:
        config = botocore.client.Config(max_pool_connections=150)
        self.__client = boto3.client("translate", config=config, **kwargs)

    def translate(self, text: str, lang_from: str, lang_to: str) -> str:
        return self.__client.translate_text(
            Text=text, SourceLanguageCode=lang_from, TargetLanguageCode=lang_to
        )["TranslatedText"]
