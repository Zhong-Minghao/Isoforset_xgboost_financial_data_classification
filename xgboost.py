import xgboost
import pandas as pd
# First XGBoost model for Pima Indians dataset
from xgboost import XGBClassifier 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# load data
dataset=pd.read_excel('D:/AnacondaSpyder/300313iso.xlsx').values
# split data into X and y
X = dataset[:,0:10]
Y = dataset[:,10]
X_pred = X[21881:42990,:]
yy = Y[21881:42990]
# split data into train and test sets
seed = 7
test_size = 0.33
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)
# fit model no training data
model = XGBClassifier()
model.fit(X_train, y_train)
# make predictions for test data
y_pred = model.predict(X_pred)
predictions = [round(value) for value in y_pred]
# evaluate predictions
accuracy = accuracy_score(y_pred, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))


data_V = pd.DataFrame(X_pred)
data_P = pd.DataFrame(predictions)
data_N = pd.DataFrame(yy)

data_V.columns=['申报价格/时间窗口成交均价','申报价格','调整后档位','申报量/时间窗口平均申报量','订单申报量','时间间隔','加权撤单量','成交率','撤单量','价格冲击']
data_P.columns=['异常值']
data_N.columns=['原异常值']

writer = pd.ExcelWriter('异常值表格xgboost300313.xlsx')
data_V.to_excel(writer,'A')
data_P.to_excel(writer,'B')
data_N.to_excel(writer,'C')
writer.save()