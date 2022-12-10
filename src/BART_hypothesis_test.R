library("bartMachine")

# import heart disease data
df <- read.csv("heart_disease\\heart.csv")

# get the dimensions of our data
dim(df)

# build the train-and-test-set
# Specify the binary treatment variables
z <- df$sex
x1 = df$target 
x2 = df$chol 
x3 = df$thal

x = cbind(x1, x2, x3)
X = data.frame(x)

# build BART regression model
bart_machine = bartMachine(X,z)

# obtain the hypothesized effect of X on y
cov_importance_test(bart_machine, covariates = c(1))
