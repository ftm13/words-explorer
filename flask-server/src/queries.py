from db_models import Bigrams

def getBigramContext(word, lim):
    """ word:string
        lim:int
        return a json obj with incoming and outgoing words
        {incoming:[{'word': '给', 'freq': 288}], outgoing:[{'word': '还', 'freq': 201}]}
    """
    incoming = (Bigrams
                .filter(Bigrams.word2 == word)
                .select(Bigrams.word1.alias('word'), Bigrams.freq)
                .order_by(-Bigrams.freq)
                .limit(lim)).dicts()
    
    outgoing = (Bigrams
                .filter(Bigrams.word1 == word)
                .select(Bigrams.word2.alias('word'), Bigrams.freq)
                .order_by(-Bigrams.freq)
                .limit(lim)).dicts()
    
    incomingDict = []
    outgoingDict = []
    print("Incoming for " + word)
    for bigram in incoming:
        print(bigram)
        incomingDict.append(bigram)

    print("Outgoing for " + word)
    for bigram in outgoing:
        print(bigram)
        outgoingDict.append(bigram)

    return {'incoming':incomingDict, 'outgoing':outgoingDict}

if __name__ == '__main__':
    getBigramContext("礼物", 10)