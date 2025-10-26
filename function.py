#正規化するためのライブラリimport
import re

#整数をマイナスにする関数の定義
def minus(x:int):
    y = -x
    return y 

#二つの整数の積を求める関数の定義
def multiple(a:int, b:int):
    y = a * c
    return y

#テキストから漢字を削除する関数の定義 
#\u4E00-\u9FFF はUnicode上の「基本漢字ブロック（現代日本語でよく使う漢字）」をすべて削除する正規表現

def delete_kanji(text:str):
    res = re.sub(r'[\u4E00-\u9FFF]', '', txt)
    return res
    