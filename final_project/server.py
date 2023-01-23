"""
    App Routes for French to English / English to French translations
"""
from flask import Flask, render_template, request
import machinetranslation

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    """
        English to French
    """
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    translated_response = machinetranslation.translator.english_to_french(text_to_translate)
    return f"Translated text to French return as: {translated_response}"

@app.route("/frenchToEnglish")
def french_to_english():
    """
        French to English
    """
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    translated_response = machinetranslation.translator.french_to_english(text_to_translate)
    return f"Text translated to English returned as: {translated_response}"

@app.route("/")
def render_index_page():
    """
        Renders Index
    """
    # Write the code to render template
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
