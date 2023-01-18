## Json Translation

Json translation is a package for translating json files from one language to multiple languages.


### Motivation
This project was motivated by the need to translate a full website from English to several languages. The website had many json files containing the text that needed to be translated, and the process needed to be automated.

### Setup
To install the package, run the following command:

```bash
git clone https://github.com/agusmdev/json-translation
cd json-translation
pip install -e .
```

### Usage
Here is an example of how to use the package:

```python
from json_translation import JsonTranslator

# Create a JsonTranslator instance
json_translator = JsonTranslator()

# Translate a json file
input_path = "path/to/input.json"
from_language = "en"
target_languages = ["fr", "es"]
output_dir = "path/to/output"
exclude_keys = ["exclude_me"]

json_translator.translate_json(input_path, from_language, target_languages, output_dir, exclude_keys)
```

This will translate the json file located at input_path from English to French and Spanish, and save the translations in the specified output_dir directory. The keys in the json file named "exclude_me" will not be translated.

`WARNING:` The default translator is the translation method provided by AWS, you can extend the Translator abstract class and create your own, or setup your aws credentials and permissions to use the default one.

### License

This package is licensed under the MIT License.

### Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.