/Users/yun/PrivateSpace/Noonde-Script/docs/mayi.txtimport jieba.posseg as pseg
import codecs
from gensim import corpora, models, similarities

stop_words = '/Users/yun/PrivateSpace/Noonde-Script/docs/stop_words.txt'
stopwords = codecs.open(stop_words, 'r', encoding = 'utf-8').readline()
stopwords = [ w.strip() for w in stopwords]

stop_flag = ['x', 'c', 'u','d', 'p', 't', 'uj', 'm', 'f', 'r']


def tokenization(filename):
    result = []
    with open(filename, 'r') as f:
        text    =   f.read()
        words   =   pseg.cut(text)
    for word, flag in words:
        if flag not in stop_flag and word not in stopwords:
            result.append(word)
    return result


##选取两篇相同房源的内容， 选择一个不一样的内容
filenames = ['/Users/yun/PrivateSpace/Noonde-Script/docs/agoda.txt',
            '/Users/yun/PrivateSpace/Noonde-Script/docs/booking.txt',
            '/Users/yun/PrivateSpace/Noonde-Script/docs/ctrip.txt'
            ]

##建立词袋模型  Bag-of-words  描述文档中单词出现的文本的一种表示形式
corpus = []
for each in filenames:
    corpus.append(tokenization(each))

print(len(corpus))

dictionary   =   corpora.Dictionary(corpus)
print(dictionary)

doc_vectors = [dictionary.doc2bow(text) for text in corpus]
print(len(doc_vectors))
print(doc_vectors)

tfidf = models.TfidfModel(doc_vectors)
tfidf_vectors = tfidf[doc_vectors]

print(len(tfidf_vectors))
print(len(tfidf_vectors[0]))


query = tokenization('/Users/yun/PrivateSpace/Noonde-Script/docs/tem.txt')
query_bow = dictionary.doc2bow(query)

print(len(query_bow))
print(query_bow)

lsi = models.LsiModel(tfidf_vectors, id2word=dictionary, num_topics=2)

lsi.print_topics(2)

lsi_vector = lsi[tfidf_vectors]
for vec in lsi_vector:
    print(vec)
