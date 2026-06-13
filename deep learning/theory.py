"""
CNN techniques :- 
first technique is convolutional :- it extracts features from the image (formula = n(image size) - f(filter size)+1 )
second is pooling :- it removes the unwanted part and so also the size of data got reduced. it is of two types (max pooling and average pooling)

stride/step :- (n-f)/s+1
padding 


RNN :-
rnn is recurrent neural network  it is almost same like ann but it has a feature of storing data as it has memory and it is used for 
performing on sequential data.

gradient:- it means how much the error will change if the weights are being changed. 

rnn issues :-
vanishing gradient :- it is , when the gradients becomes extremely low during back propagation.
exploding gradient :- it is , when the gradients becomes extremely high during back propagation.
(and it is not only for rnn or some other nn , these both are the problem for every neural network.)

bptt :- it is a training method which we use in neural network-making so that it will check the gradients. it helps to check the gradients
and then there might be a chance of the issue which is vanishing or exploding gradients.

lstm :- long short term memory

"""