library("bartMachine")

# import heart disease data
df <- read.csv("heart_disease\\heart.csv")

# get the dimensions of our data
dim(df)

# build the train-and-test-set
# Specify the binary treatment variables
X <- data.frame(df$sex)
y = df$target 
x2 = df$chol 
x3 = df$thal

x = cbind(x1, x2, x3)

# build BART regression model
bart_machine = bartMachine(X,y)

# obtain the hypothesized effect of X on y
cov_importance_test(bart_machine, covariates = c(1))
