from translate import Translator
translator = Translator(to_lang='ja')
translation = translator.translate("Hello I am joel")
print(translation)