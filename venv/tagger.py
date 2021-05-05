import nltk
from nltk.corpus import indian
from nltk.tag import tnt
import string

'''
def download():
    nltk.download('indian')
    nltk.download('punkt')
'''
pos_tagger=None
def train():
    global  pos_tagger
    tagged_set = 'hindi.pos'
    word_set = indian.sents(tagged_set)
    count = 0
    for sen in word_set:
        count = count + 1
        sen = "".join([" "+i if not i.startswith("'") and i not in string.punctuation else i for i in sen]).strip()
    print ('Total sentences in the tagged file are',count)

    train_perc = .9

    train_rows = int(train_perc*count)
    test_rows = train_rows + 1

    print ('Sentences to be trained',train_rows, 'Sentences to be tested against',test_rows)

    data = indian.tagged_sents(tagged_set)
    train_data = data[:train_rows]
    test_data = data[test_rows:]


    pos_tagger = tnt.TnT()
    pos_tagger.train(train_data)
    pos_tagger.evaluate(test_data)



def get_result(sentence_to_be_tagged):
    #download()

    tokenized = nltk.word_tokenize(sentence_to_be_tagged)


    return(pos_tagger.tag(tokenized))

'''
def hindi_model():
    train_data = indian.tagged_sents('hindi.pos')
    print(len(train_data))
    tnt_pos_tagger = tnt.TnT()
    tnt_pos_tagger.train(train_data)
    return tnt_pos_tagger

text = "इराक के विदेश मंत्री ने अमरीका के उस प्रस्ताव का मजाक उड़ाया है , जिसमें अमरीका ने संयुक्त राष्ट्र के प्रतिबंधों को इराकी नागरिकों के लिए कम हानिकारक बनाने के लिए कहा है ।"

model = hindi_model()
new_tagged = (model.tag(nltk.word_tokenize(text)))
'''
