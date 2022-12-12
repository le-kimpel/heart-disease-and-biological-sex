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

##regression example

##build BART regression model

'''
Ugly, but I chose to build several different BartMachines for each of the various categories.

bart_machine1 = bartMachine(X,x1, num_trees = 200, num_burn_in = 500,
                           num_iterations_after_burn_in = 1000)

cov_importance_test(bart_machine1, covariates = c(1))


bart_machine2 = bartMachine(X,x2, num_trees = 200, num_burn_in = 500,
                           num_iterations_after_burn_in = 1000)

cov_importance_test(bart_machine2, covariates = c(1))


bart_machine3 = bartMachine(X,x3, num_trees = 200, num_burn_in = 500,
                           num_iterations_after_burn_in = 1000)

cov_importance_test(bart_machine3, covariates = c(1))


bart_machine4 = bartMachine(X,x4, num_trees = 200, num_burn_in = 500,
                           num_iterations_after_burn_in = 1000)

cov_importance_test(bart_machine4, covariates = c(1))

bart_machine5 = bartMachine(X,x5, num_trees = 200, num_burn_in = 500,
                           num_iterations_after_burn_in = 1000)

cov_importance_test(bart_machine5, covariates = c(1))

bart_machine6 = bartMachine(X,x6, num_trees = 200, num_burn_in = 500,
                           num_iterations_after_burn_in = 1000)

cov_importance_test(bart_machine6, covariates = c(1))
'''
