"""
encoding decoding:-

usually used to convert the text. 
it uses multiple lstm's
there are two terms :-

SOS :- start of statement 
EOS :- End of Statement

better than LSTM and RNN.

If the length of the sentence increases then the accuracy nmight change. so to check that, we use accuracy measure. 
like there is performance measure. the name of the accuracy measure is Blue Score.

in that, there, we use a graph, if the length increases, then the accuracy will becomes low.
longer the sentence, lesser the blue score. so this is the MAIN PROBLEM.

TO SOLVE THAT PROBLEM, WE USE ATTENTION MECHANISM:-

WE USUALLY PASS ONLY THE CONTEXT VECTOR BUT TO INCREASE THE ACCURACY MEASURE, WE WILL PASS THE CONTEXT AS WELL(SENTENCE).

"""