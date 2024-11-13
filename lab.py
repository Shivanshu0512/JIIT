#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np


# In[6]:


from sklearn.datasets import load_breast_cancer


# In[7]:


from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report






# In[17]:



data = load_breast_cancer()
X= pd.DataFrame(data.data, columns=data.feature_names)
y =data.target
print("First 10 rows of the dataset:")
print(X.head(10))


# In[12]:




print(X.describe())


# In[18]:


missing_values = X.isnull().sum()
print("Missing values in each column:")
print(missing_values[missing_values > 0])
print("Note: There are no missing values in this dataset")


# In[19]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


# In[20]:


scaler = StandardScaler()
X_train =scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)


# In[22]:


correlation_matrix = pd.DataFrame(X_train, columns=data.feature_names).corr()
print("Correlation matrix (displaying highly correlated features):")
highly_correlated_features = correlation_matrix[correlation_matrix.abs()>0.8]
print(highly_correlated_features)


# In[26]:


param_grid = {'n_neighbors': range(1,21)}
grid_search = GridSearchCV(KNeighborsClassifier(),param_grid,cv=5)
grid_search.fit(X_train,y_train)
best_k = grid_search.best_params_['n_neighbors']
print(f"Optimal k value selected: {best_k}")


# In[25]:


knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train, y_train)
y_pred= knn.predict(X_test)
conf_matrix =confusion_matrix(y_test, y_pred)
class_report =classification_report(y_test, y_pred)
print("Confusion Matrix")
print(conf_matrix)
print("Classification Report")
print(class_report)


# In[ ]:




