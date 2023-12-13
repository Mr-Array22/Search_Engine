import nltk
from nltk import word_tokenize
from nltk.stem import PorterStemmer
import re



class Tokenization:

    def __init__(self):
        self.query=[]

    def tokenization(self,query):
         tokens = word_tokenize(query)
         filteredTokens = [word.lower() for word in tokens]
         return filteredTokens

    def tokenizationn(query):
         tokens = word_tokenize(query)
         filteredTokens = [word.lower() for word in tokens]
         return filteredTokens

    def stemming(self, tokens):
        ps = PorterStemmer()
        stemmed_tokens = [ps.stem(token) for token in tokens]
        return stemmed_tokens



    def get_p_index_with_stemming(docslist):
            index = {}
            ps = PorterStemmer()

            for doc in docslist:
                with open(doc) as f:
                    text = f.read()

                tokens = word_tokenize(text)

                for i in range(len(tokens)):
                    stemmed_token = ps.stem(tokens[i])

                    if stemmed_token not in index.keys():
                        index[stemmed_token] = [[], {}]
                        index[stemmed_token][0] = 1
                        index[stemmed_token][1][doc] = []
                        index[stemmed_token][1][doc].append(i + 1)
                    else:
                        word_map = index[stemmed_token][1]
                        if doc not in word_map.keys():
                            index[stemmed_token][0] += 1
                            word_map[doc] = []
                            word_map[doc].append(i + 1)
                            index[stemmed_token][1] = word_map
            return index


        
    
    def retrieve_list(word,index):

        ans = []
        if word in  index.keys():
            ans =  index[word]
        else:
            print('Term : {} not present in dictionary'.format(word))
        return ans



    def check(res,post):
        listt=list(res[1].keys())
        keys=list(post[1].keys())
        s= [[],{}]
        for i in range(len(keys)):
            if(keys[i] in listt):

                for j in range(len(post[1][keys[i]])):
                    c=0
                    for k in range(len(res[1][keys[i]])):

                       if(post[1][keys[i]][j]==(res[1][keys[i]][k]+1)) :
                           a = post[1][keys[i]]
                           s[1][keys[i]] = a
                           c=1
                           break
                       else:
                           k+=1
                    if(c==1):
                        break
                    else:
                        j+=1
        res=s
        return s

    
    
    def process_query(query,index):
        b = Tokenization
        res= []
        test=[]
        query = query.lower()
        text = b.tokenizationn(query)
        stemmer = PorterStemmer()
        text = [stemmer.stem(word) for word in text]    
        if(len(text)==1):
           post= b.retrieve_list(text[0], index)
           if(post==[]):
               return res
           else:
               return list(post[1].keys())
        else:
            for i in range(len(text)):
                if(i==0):
                    post = b.retrieve_list(text[0], index)
                    if (post==[]):
                        return res
                    else:
                        res = post
                else:
                    post=b.retrieve_list(text[i],index)
                    if (post==[]):
                        return []
                    else:
                       test= b.check(res, post)
                    res=test
        return list(res[1].keys())
    





