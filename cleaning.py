import MeCab
import urllib.request
import bs4
from bs4 import BeautifulSoup

# ストップワードのurl->リスト
my_sw = ['う','お','か','が','さ','し','た','だ','て','で','と',
          'に','ぬ','の','は','ば','へ','も','や','を','ヶ','ヵ','カ'
          'あの','および','この','これら','こんな','しか','しかし','その','それら','そんな',
         'たい','だけ','ただ','為','たり','だり','って','です','という','として','どの','どの'
         'ながら','において','における','にて','により','による','ので',
         'ます','また','又','または','れる','られる',
         '、','，','。','．','-','『', '』','゛','゜','-']
url = 'http://svn.sourceforge.jp/svnroot/slothlib/CSharp/Version1/SlothLib/NLP/Filter/StopWord/word/Japanese.txt'
soup = bs4.BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
sw_list = str(soup).split('\r\n')
sw_list.extend(my_sw)

# 形態素解析
# ついでにストップワードも除去
# Ochasenは動かないので，必要な際はTerminalからお願いします
def morph_analysis(infile, outfile) : # infileの文章を解析して，結果をoutfileに出力
    # t = MeCab.Tagger('-Owakati') # 分かち書きのみ
    t = MeCab.Tagger('-F\s%f[6] -U\s%m -E\\n') # 動詞を基本形に直す
    fin = open(infile, 'r') # 解析対象
    fout = open(outfile, 'w') # 解析結果
    out_file = t.parse(fin.read()) # 読み込んで解析
    for sw in sw_list:
        out_file = out_file.replace(' '+sw+' ', ' ')
    fout.write(out_file) # 書き出し
    fin.close() # ファイルを閉じる
    fout.close()
    return outfile

if __name__ == '__main__':
    
    morph_analysis('infile', 'outfile')
