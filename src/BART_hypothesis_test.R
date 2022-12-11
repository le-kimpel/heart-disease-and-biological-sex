library("bartMachine")

# import heart disease data
df <- read.csv("heart_disease\\heart.csv")


# get the dimensions of our data
dim(df)

# build the train-and-test-set
# Specify the binary treatment variables
X <- data.frame(df$sex)
x1 = df$target 
x2 = df$chol 
x3 = df$thal
x4 = df$age
x5 = df$trestbps
x6 = df$cp

y = cbind(x1, x2, x3, x4, x5, x6)

##regression example

##build BART regression model

for(i in 0:len(y)){
  bart_machine = bartMachine(bartMachine(X,y[i], num_trees = 200, num_burn_in = 500,
                                         num_iterations_after_burn_in = 1000))
  cov_importance_test(bart_machine, covariates = c(1))
}
