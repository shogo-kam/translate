from googletrans import Translator
translator = Translator()

trans_de_ja = translator.translate('hello', dest='ja')
print(trans_de_ja.text)

