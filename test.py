
import googletrans

print(googletrans.LANGUAGES)


from googletrans import Translator
#
translator = Translator()

# translator = Translator(service_urls=[
#       'translate.google.com',
#       'translate.google.co.kr',
#     ])
# #
result = translator.translate('Mitä sinä teet')

# translator.translate('hello', src='en', dest='uk')
# translator.translate('안녕하세요.', dest='ja')
# translator.translate('veritas lux mea', src='la')