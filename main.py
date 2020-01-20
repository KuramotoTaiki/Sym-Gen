from pykakasi import kakasi
import gather
import tkinter
from tkinter import filedialog
import codecs

def createDictionary(file_path):
    kakas = kakasi()
    kakas.setMode('J', 'H')
    conv = kakas.getConverter()
    word_list = gather.gather()
    print("> ", gather.search_word)
    hiragana = conv.do(gather.search_word)
    for word in word_list:
        print(word)
        word = hiragana + "\t" + word + "\t" + '名詞' + "\t"
        with codecs.open(str(file_path), 'a', encoding='utf-8') as dicfile:
            dicfile.write(word + '\n')
    

if '__main__' == __name__:
    root = tkinter.Tk()
    root.overrideredirect(1)
    root.withdraw()
    fileName = filedialog.askopenfilename(
       filetypes=(('IME Dictionary File', '*.txt'), ('All files', '*.*')))
    print('Selected IME Dictionary File(*.txt): ' + fileName)
    while True:
        createDictionary(fileName)
