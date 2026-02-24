from deep_translator import GoogleTranslator

def translate_to_kannada(text):
    try:
        translated = GoogleTranslator(source='en', target='kn').translate(text)
        return translated
    except Exception as e:
        return f"Error: {e}"

# Take user input
english_word = input("Enter English word or sentence: ")

# Translate
kannada_word = translate_to_kannada(english_word)

print("Kannada Translation:", kannada_word)