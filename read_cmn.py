import jieba
import nltk
from model import *

def read_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read()
    entokens = []
    cntokens = []
    tokenizer = nltk.tokenize.TreebankWordTokenizer()
    datasplits = data.split('\n')
    tokenized_dataset = [[token.lower() for token in tokenizer.tokenize(sentence.split('\t')[0])] for sentence in datasplits[:100]]
    vocabulary_en = list(set(list(word for sentence in tokenized_dataset for word in sentence)))
    tokenized_dataset_zh = [list(jieba.cut(sentence.split('\t')[1])) for sentence in datasplits[:100]]
    vocabulary_zh = list(set(list(word for sentence in tokenized_dataset_zh for word in sentence)))
    return vocabulary_zh, vocabulary_en, tokenized_dataset,tokenized_dataset_zh

def add_word(self, vocabularies):
    '''
    return a idx2word and a index to word mapping
    '''
    idx2word = []
    word2idx = {}
    for word in vocabularies:
        if word not in []:
            idx2word.append(word)
            word2idx[word] = len(self.idx2word) - 1
    return idx2word, word2idx

def sentencetoindex(tokenized_dataset, word2idex):
    ret = []
    for sentence in tokenized_dataset:
        to_be_append = []
        for word in sentence:
            to_be_append.append(word2idex[word])
        ret.append(to_be_append)
    return ret

if __name__ == "__main__":

    vocabulary_zh, vocabulary_en, tokenized_dataset,tokenized_dataset_zh = read_data('cmn.txt')
    vocab_size = 1500
    hidden_size = 512
    idx2word, word2idex = add_word(vocabulary_zh)
    idx2worden, word2idexen = add_word(vocabulary_en)

    #encoder = GRUEncoder(vocab_size, hidden_size, None)



# vocabulary_zh, vocabulary_en, tokenized_dataset,tokenized_dataset_zh = read_data('cmn.txt')
# print(vocabulary_zh)

