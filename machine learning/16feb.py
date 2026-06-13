"""
machine learning

first :-  feature engineering :-

1. feature cleaning
2. removing null values, filling null values etc
3. transforming feature, merging feature, making new feature

weight and height == BMI

second :-  feature scaling
types :- 1. minmax scaling 2. standard scaling

third :- feature encoding:- 
as everything cant be measured in numbers, can be measured in categoricl values like gender (female and male) but can be changed in 
number like (0 or 1) 

what is minmax scaling
it is a preprocessing technique in machine learning that scales numerical data to a fixed range. typically 0 to 1 by calculating
X(scaled)= (x-x(min))/(x(max)-X(min))

what is standard scaling
it is in the feature scaling technique which follows standard normal distribution and is used to standardize the vlaue. it transforms the data
so that the mean becomes 0 and standard deviation 1.
(x-mean)/standard deviation

what is feature encoding?
feature encoding means converting the categorical values into numbers so that it becomes easier for calculation.
it is of two types:- ordinal data (which has order) and nominal data (which has no order)

methods of feature encoding:- 

one hot encoding  (it make individual columns and put 1 for that corresponding thing and will give 0 to the rest of the columns.)
label encoding (reverse of one hot encoding) (it will give numbers to the category n cretes another columns.)

Classification:- means getting results in either true or false , male or female, right or wrong
regression:- means getting continuous results. like 0-10 or 10-20 or so on

confusion matrix :- 
True positive ( prediction is correct and actual value is also correct as well)
True Negative (prediction is wrong and actual value is also wrong as well)
False Positive (prediction is correct but the actual value was not correct) (predicted that the patient has cancer(and it was true,actually) but wasn't having cancer actually)
False negative (prediction is wrong but the actual value is correct) (predicted that the patient doesnt have cancer but it has cancer (actually) )

Bias:- underfitting (will get bias if the model is underfitting)
variance:- overfitting(means machine will even trained on those columns which doesnt makes any sense and will leads to predict the answers wrong , overally, overfitting)

underfitting:- means the machine is trained on low data. and will predict the answers wrong
overfitting:- means machine is trained on high data and even on lame columns and will results in wrong prediction as cuz of sensitive data trained it is on.



decision tree
it is a tree which divide further. and then it furtherly divide and so on. just to predict the result. 
if branches becomes more, the more will be the instability. 
pruning:- types (pre pruning and post pruning)

random forest :- basically it is a gooup of decision tree. and it doesnt needs scaling as well.

"""