from tkinter import messagebox
from googletrans import Translator
import clipboard


# Functions
def translate():
    word = "Hello world"
    translator = Translator()
    translation = translator.translate(word, src='en', dest="ar")
    print(f"Translated Word: {translation.text}")
    
translate()
# translator = Translator()
# a =translator.translate('veritas lux mea', src='la', dest='ru')
# print(a)

# def copy():
#     clipboard.copy(text)
# messagebox.showinfo("Success", "Text Copied!")


