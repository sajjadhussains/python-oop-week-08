from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

digits = load_digits()
# print(dir(digits))
# print(digits.data.ndim)
# plt.gray()
# for i in range(5):
#     plt.matshow(digits.images[i])
#     plt.show()
X=digits.data
Y=digits.target
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)
# print(X_train.shape)
# print(X_test.shape)
model=LogisticRegression()
model.fit(X_train,Y_train)

#manual spot testing 
# print('target value of the test:',digits.target[1700])
# result = model.predict([digits.data[1700]])
# print('test result:',result)

accuracy=model.score(X_test,Y_test)
# print('accuracy : ',accuracy)

Y_predicted=model.predict(X_test)
confusion = confusion_matrix(Y_test,Y_predicted)
# print(confusion)
ConfusionMatrixDisplay.from_estimator(model,X_test,Y_test)
plt.show()