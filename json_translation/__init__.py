from concurrent.futures import ThreadPoolExecutor
import os
from .translator import Translator, AWSTranslator
from .json_handler import JsonHandler
from typing import Any, Dict, List
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


class JsonTranslator:
    def __init__(
        self,
        translator: Translator = AWSTranslator(),
        threads: int = 1,
    ) -> None:
        """
        Json translator base class

        Args:
            translator (Translator, optional): Translator object to perform the translation. Defaults to AWSTranslator().
            threads (int, optional): Number of threads to process the keys concurrently. Defaults to 1.
        """
        self.translator = translator
        self.json_handler = JsonHandler()
        self.threads = threads

    def translate_json(
        self,
        input_path: str,
        from_language: str,
        target_languages: List[str],
        output_dir: str = "translations",
        exclude_keys: List = [],
    ):
        """
        Translate your json values

        Args:
            input_path (str): the path to the json file that needs to be translated
            from_language (str): the language code of the original json values
            target_languages (List[str]): a list of language codes to translate the json values to
            output_dir (str, optional): the directory where the translated json files will be saved. Defaults to "translations".
            exclude_keys (List, optional): a list of keys in the json file that should not be translated. Defaults to [].
        """
        source_object = self.json_handler.open_json(input_path)
        for language in target_languages:
            logging.debug(f"Translating file from [{from_language}] to [{language}]")
            translated_object = self._translate_object(
                source_object, from_language, language, exclude_keys
            )
            self.json_handler.save_json(
                translated_object,
                os.path.join(
                    output_dir,
                    self.json_handler.translation_path(input_path, language),
                ),
            )

    def _translate_value(
        self, value: Any, from_language: str, to_language: str, exclude_keys: List
    ):
        """
        Get the translation for the given value

        Args:
            value (Any): the value to be translated, can be a string or a json object
            from_language (str): the language code of the original value
            to_language (str): the language code to translate the value to
            exclude_keys (List): a list of keys in the json object that should not be translated

        Returns:
            str: the translated value
        """
        if isinstance(value, str):
            return self.translator.translate(value, from_language, to_language)
        if isinstance(value, dict):
            return self._translate_object(value, to_language, exclude_keys)
        elif isinstance(value, list):
            return [
                self._translate_value(val, from_language, to_language, exclude_keys)
                for val in value
            ]

        else:
            return value

    def _translate_object(
        self,
        obj: Dict[str, Any],
        from_language: str,
        to_language: str,
        exclude_keys: List,
    ) -> Dict[str, Any]:
        """
        Translate the given json object

        Args:
            obj (Dict[str, Any]): the json object to be translated
            from_language (str): the language code of the original json object
            to_language (str): the language code to translate the json object to
            exclude_keys (List): a list of keys in the json object that should not be translated

        Returns:
            Dict[str, Any]: the translated json object
        """

        translation = {}

        def executor_translate(key: str, value: Any, translation: Dict) -> None:
            if key not in exclude_keys:
                translation[key] = self._translate_value(
                    value, from_language, to_language, exclude_keys
                )
            else:
                translation[key] = value

        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            results = executor.map(
                lambda item: executor_translate(*item, translation), obj.items()
            )
            list(results)

            return translation
