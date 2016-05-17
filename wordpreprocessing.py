import MeCab

def word2id(source):
    m = MeCab.Tagger('-Owakati')
    words = m.parse(source).split(' ')
    raise NotImplementedError

#テキストファイルのエンコーディングを返す
def getEncoding(path):
    encodings = ('utf_8', 'euc_jp', 'euc_jis_2004', 'euc_jisx0213', 'shift_jis', 'shift_jis_2004','shift_jisx0213', 'iso2022jp', 'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_3', 'iso2022_jp_ext','latin_1', 'ascii')
    encoding = ''
    for enc in encodings:
        try:
            f = open(path, encoding = enc)
            f.read()
            encoding = f.encoding
            break
        except UnicodeDecodeError:
            pass
    if encoding is not '':
        return encoding
    else:
        raise LookupError
