# import heart disease data
df <- read.csv("heart_disease\\heart.csv")
library(caret)
library(bartMachine)
# get the dimensions of our data
dim(df)

# build the train-and-test-set
n = nrow(df)
# Specify the binary treatment variables
x <- data.frame(df$sex)

# Specify the effects
x1 = df$target 
x2 = df$chol 
x3 = df$thal
x4 = df$trestbps
x5 = df$age

X = data.frame(cbind(x1, x2, x3, x4, x5))

z = makeModelMatrixFromDataFrame(X)

##generate Friedman data
set.seed(11)

##build BART regression model

##Build another BART regression model
bart_machine = bartMachine(x,z, num_trees = 200, num_burn_in = 500,
                           num_iterations_after_burn_in = 1000)

summary(bart_machine)
plot(bart_machine$y, bart_machine$residuals) ; abline(0,1)
