#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 14:22:28 2021

@author: prem
"""

import pandas as pd
import matplotlib.pyplot as plt

#reading Dataset
dataset=pd.read_csv("data.csv")
x=dataset.iloc[:,1:5]
y = dataset.iloc[:,5]

from sklearn.preprocessing import LabelEncoder 
le = LabelEncoder()
x = x.apply(le.fit_transform)

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
dt.fit(x,y)

y_pred=dt.predict([[2,1,0,0]])
print("Prediction:", y_pred[0])

from sklearn import tree
fig = plt.figure(figsize=(25,20))
tree.plot_tree(dt)