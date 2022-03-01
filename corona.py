# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 07:25:35 2021

@author: ugrer
"""
import pandas as pd

csvfile = pd.read_csv('data.csv')

def question1():
    iso=list(csvfile["iso_code"])
    count=0
    for row in range(len(iso)-2):
        if(iso[row]!=iso[row+1]):
            count+=1
    return count

def question2():
    df=csvfile.groupby("location")["date"].min()
    temp=df.reset_index()
    temp=temp.sort_values('date')
    return temp.values[0]
        
def questions3_4_11_14to16(header,number):
    temp=csvfile.groupby("location")[header].max()
    dataframe=temp.reset_index()
    return pd.DataFrame({"q#"+number:list(dataframe[header])})

def questions5to10_12_13(header,number):
    

    #calculate mean and take countries
    df=csvfile.groupby("location")[header].mean()
    temp=df.reset_index()
    averages=list(temp[header])
    #calculate min
    df=csvfile.groupby("location")[header].min()
    temp=df.reset_index()
    mins=list(temp[header])
    #calculate max
    df=csvfile.groupby("location")[header].max()
    temp=df.reset_index()
    maxs=list(temp[header])
    #calculate variation
    #calculate var
    df=csvfile.groupby("location")[header].var()
    temp=df.reset_index()
    vars=list(temp[header])
    #make table
    table=pd.DataFrame({"q#"+number+"_min":mins, "q#"+number+"_max":maxs, "q#"+number+"_avg":averages,
                        "q#"+number+"_var":vars})
    #print table
    return table

def question17():
    headings=["location","population","median_age","aged_65_older","aged_70_older","extreme_poverty","cardiovasc_death_rate","diabetes_prevalence","female_smokers","male_smokers","handwashing_facilities","hospital_beds_per_thousand","life_expectancy","human_development_index"]
    dfs = pd.read_csv('data.csv', skipinitialspace=True, usecols=headings)   
    dfs=dfs.groupby("location")[headings[1:]].max()
    return dfs.reset_index()

def question18():
    data=[]
    df=csvfile.groupby("location")["reproduction_rate"].mean()
    temp=df.reset_index()
    table=pd.DataFrame({"countries":list(temp.location)})
    data.append(pd.DataFrame({"countries":list(temp.location)}))
    data.append(questions3_4_11_14to16("total_cases","3"))
    data.append(questions3_4_11_14to16("total_deaths","4"))
    data.append(questions5to10_12_13("reproduction_rate","5"))
    data.append(questions5to10_12_13("icu_patients","6"))
    data.append(questions5to10_12_13("hosp_patients","7"))
    data.append(questions5to10_12_13("weekly_icu_admissions","8"))
    data.append(questions5to10_12_13("weekly_hosp_admissions","9"))
    data.append(questions5to10_12_13("new_tests","10"))
    data.append(questions3_4_11_14to16("total_tests","11"))
    data.append(questions5to10_12_13("positive_rate","12"))
    data.append(questions5to10_12_13("tests_per_case","13"))
    data.append(questions3_4_11_14to16("people_vaccinated","14"))
    data.append(questions3_4_11_14to16("people_fully_vaccinated","15"))
    data.append(questions3_4_11_14to16("total_vaccinations","16"))
    temp=question17()
    del temp['location']
    data.append(temp)
    for i in range(1,16):
        table=table.join(data[i])
    
    table.to_csv("output.csv")  #creates output.csv file of question18
    return table

print("Question 1 :", question1())
print("Question 2: ",question2())
print("Other Questions:")
print(question18())