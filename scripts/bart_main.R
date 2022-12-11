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
y <- df$target

##generate Friedman data
set.seed(11)

##build BART regression model

##Build another BART regression model
bart_machine = bartMachine(X,y, num_trees = 200, num_burn_in = 500,
                           num_iterations_after_burn_in = 1000)

summary(bart_machine)
plot(bart_machine$y, bart_machine$residuals) ; abline(0,1)
