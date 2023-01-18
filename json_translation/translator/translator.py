import abc


class Translator(abc.ABC):
    @abc.abstractmethod
    def translate(self, text: str, lang_from: str, lang_to: str) -> str:
        pass
