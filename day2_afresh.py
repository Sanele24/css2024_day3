#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 12:47:54 2024

@author: sanelecebekhulu
"""

#working with dates


import pandas as pd

df = pd.read_csv("/Users/sanelecebekhulu/Desktop/css2024_day2/time_series_data.csv")

df = pd.read_csv("/Users/sanelecebekhulu/Desktop/css2024_day2/time_series_data.csv", index_col = 0)

df['Date'] = pd.to_datetime(df['Date'])


df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')


df = pd.read_csv("/Users/sanelecebekhulu/Desktop/css2024_day2/iris.csv")

#print(df.columns)


col_names = df.columns.tolist()

print(col_names)

df["sepal_length_sq"] = df["sepal_length"]**2

#df2["sepal_length_sq"] = df["sepal_length"].apply(lambda x: x**2)


grouped = df.groupby("class")

mean_square_values = grouped['sepal_length_sq'].mean()

print(mean_square_values)

#Append & merge

df1 = pd.read_csv("/Users/sanelecebekhulu/Desktop/css2024_day2/person_split1.csv")

df2 = pd.read_csv("/Users/sanelecebekhulu/Desktop/css2024_day2/person_split2.csv")

df = pd.concat([df1, df2], ignore_index=True)

df1 = pd.read_csv("/Users/sanelecebekhulu/Desktop/css2024_day2/person_education.csv")

df2 = pd.read_csv("/Users/sanelecebekhulu/Desktop/css2024_day2/person_work.csv")

## inner join
df_merge = pd.merge(df1,df2,on='id')


print(df_merge)


df_merge = pd.merge(df1, df2, on='id', how='outer')


print(df_merge)

###Filtering



df = pd.read_csv("/Users/sanelecebekhulu/Desktop/css2024_day2/iris.csv")

print(df)

df["class"] = df["class"].str.replace("Iris-", "")

df = df[df["sepal_length"]>5]

df = df[df["class"]=="virginica"]



###LOAD
df.to_csv("pulsar.csv")
df.to_excel("pulsar.xlsx")
df.to_json("pulsar.json")








