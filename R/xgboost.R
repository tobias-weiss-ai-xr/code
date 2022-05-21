# https://www.rpubs.com/dalekube/XGBoost-Iris-Classification-Example-in-R

# install.packages('xgboost')
library(xgboost)
data(iris)

# create integer labels
species = iris$Species
label = as.integer(iris$Species)-1
iris$Species = NULL

# train/test split
train.index = sample(nrow(iris),floor(0.6*nrow(iris)))
train.data = as.matrix(iris[train.index,])
train.label = label[train.index]
test.data = as.matrix(iris[-train.index,])
test.label = label[-train.index]

# XGBoost DMatrix format
xgb.train = xgb.DMatrix(data=train.data,label=train.label)
xgb.test = xgb.DMatrix(data=test.data,label=test.label)

# parameters
params = list(booster="gbtree", 
              eta=0.001, 
              max_depth=5, 
              gamma=3, 
              subsample=0.75,
              colsample_bytree=1, 
              objective="multi:softprob",
              eval_metric="mlogloss", 
              num_class=length(levels(species)))

# training 
xgb.model=xgb.train(
  params=params,
  data=xgb.train,
  nrounds=10000,
  nthreads=1,
  early_stopping_rounds=10,
  watchlist=list(val1=xgb.train,val2=xgb.test),
  verbose=0
)

# Results
xgb.model

# Predict outcomes with the test data
xgb.pred = predict(xgb.model,test.data,reshape=T)
xgb.pred = as.data.frame(xgb.pred)
colnames(xgb.pred) = levels(species)

