from utils import format_singapore_data, Parser
from db_models import Bigrams, Sentences, Words

Bigrams.create_table()
Sentences.create_table()
Words.create_table()

def populate_db_bigrams(sentences):
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

    for bigram, freq in bigrams.items():
        (w1, w2) = bigram
        dbEntry = Bigrams(word1=w1, word2=w2, freq=freq)
        dbEntry.save()

def populate_db_sentences(sentences):
    for s in sentences:
        dbEnty = Sentences(sentence = s)
        dbEnty.save()

def populate_db_words(sentences):
    parser = Parser(sentences)
    words = {}
    for tokens in parser.get_tokenised_parts():
        for (word, pos) in tokens: 
            freq = words.get(word)
            if freq is None:
                words[word] = 1
            else:
                words[word] = freq + 1

    for word, freq in words.items():
        dbEntry = Words(word=word, freq=freq)
        dbEntry.save()

def populate_db(sentences):
    populate_db_bigrams(sentences)
    populate_db_sentences(sentences)
    populate_db_words(sentences)

for ex in Sentences.select().dicts():
     print (ex)

if __name__ == '__main__':
    gen = format_singapore_data()
    populate_db(gen)