#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 12:25:24 2021

@author: prem
"""

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

dataset = pd.read_csv('data.csv')
x = dataset.iloc[:,0] 
y = dataset.iloc[:,1]

n = np.size(x) 
s_x = np.sum(x)
s_y = np.sum(y)
s_x2 = np.sum(x*x)
s_xy = np.sum(x*y)

slope = (n*s_xy - s_x*s_y) / (n*s_x2 - s_x*s_x)

m_x = np.mean(x)
m_y = np.mean(y)
 
intercept = m_y - slope*m_x 

print("y = ",slope,"* x + ",intercept) 

hours = 8
risk_score = intercept + slope*hours

print("Risk Score for ",hours," hours = ",risk_score)  

plt.scatter(x, y,marker = "o") 
y_pred = intercept + slope*x 
plt.plot(x, y_pred,c = 'g') 
plt.xlabel('x') 
plt.ylabel('y') 
plt.show() 


x = dataset.iloc[:,:-1]
y = dataset.iloc[:,1] 


from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x,y)
acc = lr.score(x,y)*100
print("Accuracy = ",acc)

print("y = ",lr.coef_[0],"* x + ",lr.intercept_)

hours = [[8]]
risk_score = lr.predict(hours)
print("Risk Score for ",hours[0][0]," hours = ",risk_score[0])

plt.scatter(x, y,marker = "o") 
y_pred =  lr.predict(x)
plt.plot(x, y_pred,c = 'g') 
plt.xlabel('x') 
plt.ylabel('y') 
plt.show() 
