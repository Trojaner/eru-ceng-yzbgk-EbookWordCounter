#!/usr/bin/env python3

"""
   EbookWordCounter - Enes Sadık Özbek 2018

   'books' klasöründeki kitaplarda ./data/encok.txt'deki kelimerin ne kadar çok geçtiğini sayar
ve dosya-adı-count.txt'e kaydeder.
   Regex harflerin başka bir kelimenin içinde mi, yoksa kendi başına kelime oluşturduğu mu ayırt edilir.
Kelimenin cümle sonunda boşluk olup olmadığını dikkate alınır (yani ardından boşluk olması şart değil).
Kesme işareti ile ayrılan ekleri de ayırt edebilir.
   Şu regexe göre her kelimenin ne kadar çok geçtiğini bulunur: (?i)\s\QKELİME\E(\s|\.|!|\?|\')
   Sadece UTF-8 bazlı dosyalar için çalışır ve PDF, EPUB, docx ve txt dosyaları desteklenir.

   Normal ekleri ayırt edemez. Örneğin: 'olmadı' ve 'olmadığı' ayrı kelime diye algılanır.
"""

from os import listdir
import os.path
from bookutil import get_text
from bookutil import count_words_in_text

path = "./books"
files = [f for f in listdir(path) if os.path.isfile(os.path.join(path, f))]
words = open("./data/encok.txt", "r", encoding="utf-8").readlines()

for file in files:
    if file.endswith("-count.txt"):
        continue

    print("Processig: " + file)
    word_count = count_words_in_text(get_text(path + "/" + file), words)
    if word_count is None:
        continue

    word_count_file = open(path + "/" + file + "-count.txt", "w", encoding="utf-8")
    word_count_file.write(word_count)
