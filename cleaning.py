import MeCab
import urllib.request
import bs4
from bs4 import BeautifulSoup

# 形態素解析
# Ochasenは動かないので，必要な際はTerminalからお願いします

def morph_analysis(infile, outfile) : # infileの文章を解析して，結果をoutfileに出力
    # t = MeCab.Tagger('-Owakati') # 分かち書きのみ
    t = MeCab.Tagger('-F\s%f[6] -U\s%m -E\\n') # 動詞を基本形に直す
    fin = open(infile, 'r') # 解析対象
    fout = open(outfile, 'w') # 解析結果
    out_file = t.parse(fin.read()) # 読み込んで解析           
    fout.write(out_file) # 書き出し
    fin.close() # ファイルを閉じる
    fout.close()
    return outfile


