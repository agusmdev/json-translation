import json
import pathlib
from typing import Any, Dict


class JsonHandler:
    @staticmethod
    def open_json(path: str) -> Dict:
        with open(path, "r") as f:
            return json.loads(f.read())

    @staticmethod
    def save_json(o: Dict[str, Any], path: str) -> None:
        pathlib.Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(o, f, indent=4, ensure_ascii=False)

    @staticmethod
    def translation_path(original_path: str, language: str) -> str:
        name = pathlib.Path(original_path).stem
        return f"{name}.{language}.json"