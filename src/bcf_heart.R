library("bcf")

# import heart disease data
df <- read.csv("heart_disease\\heart.csv")

# n
n = nrow(df)
set.seed(1)

# get the dimensions of our data
dim(df)

# treatment variable
z = df$sex

# response variable(s)
x1 = df$target 
x2 = df$chol 
x3 = df$thal

x = cbind(x1, x2, x3)

# estimate pi
pihat = pnorm(q)

# create targeted selection
q = -1*(x[,1]>(x[,2])) + 1*(x[,1]<(x[,2]))

# tau is the true (homogeneous) treatment effect
tau = (0.5*(x[,3] > -3/4) + 0.25*(x[,3] > 0) + 0.25*(x[,3]>3/4))

# generate the response using q, tau and z
mu = (q + tau*z)

# set the noise level relative to the expected mean function of Y
sigma = diff(range(q + tau*pi))/8

# draw the response variable with additive error!
y = mu + sigma*rnorm(n)

bcf_fit = bcf(y, z, x, x, pihat, nburn=2000, nsim=2000)

# Get posterior of treatment effects
tau_post = bcf_fit$tau
tauhat = colMeans(tau_post)
plot(tau, tauhat); abline(0,1)
