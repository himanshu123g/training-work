"""
NLP :- natural language processing



for encoding in the nlp: 
we use bag of words :- consider as there are multiple docs and what it does is, it will firstly pick all the unique words, then it will do 
                        a table and then put the exact count of that particular word is repeated. and it keeps track of each doc, like how
                        much time that word is repeated in a particular doc. and then will check that same word if it is repeated in another
                        doc.

tf-idf :- (term frequency ( it calculates the number of times the word is repeated by total words. )-inverse document frequency( it calculates the number of documents in which that word is repeated. ))

        TF :- tf counts the total number of times that particular word is repeated and then it will divide that count of word with the 
        total number of word in that document.

        IDF:- there is a formula in this:- total documents divided by N number of docs containing that word.

        then both gets multiplied.
        so the numbers which are higher will be considered as common words means they are repaeated in most of the docs
        where as the words which has the lower count will be considered as rare words. 

        

word embedding :- it is used to convert the dense word into numerical as computer only understand nums.

    tokens (a single word inside any document will be considered as a token)
    corpus(all the document will be considered as a corpus)
    span (some part of a document/sentence will be considered as a span)
    document(a single sentence will be considered as a document)

"""