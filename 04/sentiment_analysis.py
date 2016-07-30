import sys
import MeCab
import codecs
import re
import pprint

mecab = MeCab.Tagger()
pp = pprint.PrettyPrinter(indent=2)

dict_affective = []
dict_degree_adv = []
dict_negative = []
AFFECTIVE_DICT_PATH = 'dict/affective.dic'
DEGREE_ADV_DICT_PATH = 'dict/degree_adv.dic'
NEGATIVE_DICT_PATH = 'dict/negative.dic'

def _load_dicts():
    '''辞書データを読み込む'''
    # 感情語辞書の読み込み
    a = codecs.open(AFFECTIVE_DICT_PATH, encoding='shift=JIS', errors='ignore')
    for i, line in enumerate(a):
        data = line.split(':')
        data = _remove_LFCR(data)
        dict_affective.append(data)

    # 程度副詞辞書の読み込み
    d = codecs.open(DEGREE_ADV_DICT_PATH, encoding='utf-8', errors='ignore')
    for i, line in enumerate(d):
        data = line.split(':')
        data = _remove_LFCR(data)
        dict_degree_adv.append(data)

    # 否定語辞書の読み込み
    n = codecs.open(NEGATIVE_DICT_PATH , encoding='utf-8', errors='ignore')
    for i, line in enumerate(n):
        data = line.split(':')
        data = _remove_LFCR(data)
        dict_negative.append(data)

def _tokenize(sent):
    '''文章を単語に分割する'''
    tagger = MeCab.Tagger('-Owakati')
    token = tagger.parse(sent).split(' ')
    return _remove_LFCR(token)

def _remove_LFCR(list_data):
    '''改行を除去する'''
    LFCR = ['\n', '\r', '\r\n']
    for l in LFCR:
        if(list_data.count(l) != 0):
            list_data.remove(l)
        for i, item in enumerate(list_data):
            list_data[i] = re.sub(l, '', item)
    return list_data

def _get_direction_word(word):
    '''単語の見出し語を取得する'''
    tagger = MeCab.Tagger('-F"%f[6] " -E"\n" ')
    word = tagger.parse(word).replace('"', '')
    return word

def get_word_polarity(word):
    '''単語の極性を取得する'''
    word = _get_direction_word(word)
    polarities = []
    for data in dict_affective:
        if data[0] == word:
            polarities.append(data[3])
    # 辞書から複数の語が見つかった場合は、最大値を取得する
    if(len(polarities) != 0):
        polarity = max(polarities)
    else:
        polarity = 0
    return polarity

# def get_sent_polarity(sent):
#     '''文章の極性を取得する'''
#     return False

def get_degree_adv_value(word):
    dict_data = [x for x in dict_degree_adv if x[0] == word]
    if len(dict_data) > 0:
        val = float(dict_data[0][1])
    else:
        val = float(0)
    return val

def get_degree_adv_target(word):
    target = 'hoge'
    return target

def get_pos(word):
    # TODO: 辞書から複数候補が見つかった場合に、文章で用いられている候補とは異なる候補の品詞を抽出していることがある。文章で用いられている候補を抽出するように修正する
    tagger = MeCab.Tagger('-F"%f[0] " -E"\n" ')
    pos = tagger.parse(word).replace('"', '')
    return pos

if __name__ == '__main__':
    sent = sys.argv[1]
    token = _tokenize(sent) 
    _load_dicts()
    result = []

    print(mecab.parse(sent))

    # 語レベル解析
    for word in token:
        result.append({
            'word': word,
            'pos': get_pos(word),
            'polarity': get_word_polarity(word),
            'degree_adv': {
                'value': get_degree_adv_value(word),
                'target': get_degree_adv_target(word)
            }
        })

    print(pp.pprint(result))

