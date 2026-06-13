"""
Transformers :-

well, its a type of machine learning model which helps the computer to understand language n images as well.

even though we had rnn and lstm but they had a problem in which they read only 1 word at a time. so to remove that problem, we have transformers

transformer read the whole sentence at a time. it uses Attention

now attention is something, we it it uses a word to understand other word. like it compares. 
example :- "The cat didn't chase the mouse because it was not hungry"

now to understand what is "it" , it will read the whole sentence at once and starts comparing, after a while, it will get to know that cat is 
maximum-ly compared with "it" word. so this is how it works.

Self attention mechanism :- The self attention mechanism allows transformers to determine which words in a sentence are most relevant to each other. This is done using a scaled dot-product attention approach:

Each word in a sequence is mapped to three vectors:

Query (Q) :- means what exactly is our query or we want to ask. example :- what is "it"
Key (K) :- keys are the all possible answers. like it will compare with almost everything .
Value (V) :- gives the info after the keys.

Multi head attention :- Now in this, it uses multiple self attention layers. firstly dividing into query, key and value then answers.
                            almost the whole process is same like self attention. 

initially we take a sentence. "how are you doing"
tokenize the sentence.
"How" "are" "You" "doing"
perform word embedding
generate query , key and value vector
send the embedded data/vector to the multiple attention heads or to all the attention head.
each self attention head will perform attention function
each head will generate a certain value/array. 
concatenate all the output.
multiply the concatenated value with the learned weights.
the resultant value will be the final output. 


POSITIONAL ENCODING :-

by passing the sentences, our words might gets shuffled, so for that we use positional encoding. in which it will pass the numbers with 
the words of the sentences.

like example:- lion killed tiger. (lion(1) killed(2) tiger(3) .(4))
                tiger killed lion. (tiger(1) killed(2) lion(3) .(4) )

                as both the sentences have different meanings so our shuffling the words might lead to happens bad. so we use positions with
                each words.

 it is of two types which are:-

 sinusoidal positional encoding



 layer normalisation:- it is of two types which are :-
                        


"""