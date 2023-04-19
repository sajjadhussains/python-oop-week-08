import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data=pd.read_csv('HR_comma_sep.csv')
# print(data.size)
# step-1:missing data for any row any column
# print(data.isnull().values.any())
#step-2:check data types
# print(data.dtypes)
# step-3:check unique values
# print(data.Department.unique())
# print(data.salary.unique())

clean_up_values={
    'low':1,
    'medium':2,
    'high':3
}
data.replace(clean_up_values,inplace=True)
# print(data)
# step:4->get dummies for the department
dummies=pd.get_dummies(data.Department)
# print(dummies)
# merge dummies with orginal data
merged=pd.concat([data,dummies],axis='columns')
# print(merged)
# step-6:drop unnecessary data
final_data=merged.drop(['Department','technical'],axis='columns')
# print('Department' in list(final_data.columns))
# print(list(final_data.columns))

# step-7:plot data set to see the data relation
# plt.scatter(x=final_data.salary,y=final_data.left)
# plt.scatter(x=final_data.satisfaction_level,y=final_data.left)
# plt.scatter(x=final_data.time_spend_company,y=final_data.left)
# plt.show()
X=final_data.drop('left',axis='columns')
y=final_data.left
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
model=LogisticRegression()
model.fit(X_train,y_train)
accuracy=model.score(X_test,y_test)
print(accuracy)