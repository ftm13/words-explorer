import json
import pynlpir
import re
from tinydb import TinyDB, Query
import zhon

class Parser():
    def __init__(self, sentences):
        self.sentences = sentences

    def get_tokenised_parts(self):
        pynlpir.open()
        for s in self.sentences:
            sen_parts = re.split('[?!.,。，？!]', s)
            for sen_part in sen_parts:
                tokens = pynlpir.segment(sen_part)
                yield tokens


def format_singapore_data():
    """
    pathToFile : string
    returns: [sentences]
    """
    with open("../data/smsCorpus_zh.json", mode="r", encoding="utf-8") as f:
        data = json.loads(f.read())

    not_zh_re = re.compile('[^%s%s]' % (zhon.unicode.HAN_IDEOGRAPHS, zhon.unicode.PUNCTUATION))
    messages = data['smsCorpus']['message']
    for m in messages:
        try:
            text = m['text']['$']
            not_zh = not_zh_re.findall(text)
            if " " in not_zh:
                not_zh.remove(" ")
            if len(not_zh) == 0:
                yield text
        except KeyError:
            continue
        except TypeError:
            continue



def populate_db(sentences):
    db = TinyDB('../data/tiny_db_2.json')
    db.purge_tables()
    sentenceTable = db.table('sentences')
    parser = Parser(sentences)
    bigrams = {}
    for tokens in parser.get_tokenised_parts():
        for i in range(0, len(tokens) - 1):
            (word1, pos1) = tokens[i]
            (word2, pos2) = tokens[i+1]
            bigram = (word1, word2) 
            freq = bigrams.get(bigram)
            if freq is None:
                bigrams[bigram] = 1
            else:
                bigrams[bigram] = freq + 1

    bigramsTable = db.table('bigrams')
    for bigram, freq in bigrams.items():
        (w1, w2) = bigram
        bigramsTable.insert({"word1": w1, "word2": w2, "freq": freq})
    
    db.close()

def get_word_context():
    word = "我"
    db = TinyDB('../data/tiny_db.json')
    bigramsTable = db.table('bigrams')

    User = Query()
    print(bigramsTable.search((User.word1 == word) & (User.freq > 100)))
    
if __name__ == '__main__':
    gen = format_singapore_data()
    populate_db(gen)
    # get_word_context()