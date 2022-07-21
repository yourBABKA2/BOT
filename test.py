import googletrans
from googletrans import Translator

translator = Translator()
result = translator.translate('Привет', src='ru', dest='en')
print(result.text)