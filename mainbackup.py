import numpy as np
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.model_selection import train_test_split
#md1 = pd.read_csv("PCOSTrain.csv")
md2 = pd.read_csv("VgSalesTrain.csv")
md3 = pd.read_csv("HousesTrain.csv")
md4 = pd.read_csv("PCOSTrain.csv")
#md4 = pd.read_csv("SalesTrain.csv")    

#reg1 = linear_model.LinearRegression()
#reg1.fit(md1[["Age", "Weight", "Height", "BG", "Pulse", "RR", "Hb", "Cycle", "CycleL", "MaStatus", "HCG1", "HCG2", "FSH", "LH", "Hip", "Waist", "TSH", "AMH", "PRL", "VITD3", "PRG", "RBS", "WeightG", "WeightL", ]],md1.PCOS)

reg2 = linear_model.LinearRegression()
reg2.fit(md2[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]],md2.Global_Sales)

reg21 = linear_model.LinearRegression()
reg21.fit(md2[[ "EU_Sales", "Other_Sales"]],md2.NA_Sales)
reg22 = linear_model.LinearRegression()
reg22.fit(md2[["NA_Sales",  "Other_Sales"]],md2.EU_Sales)
#reg23 = linear_model.LinearRegression()
#reg23.fit(md2[["NA_Sales", "EU_Sales", "Other_Sales"]],md2.JP_Sales)
reg24 = linear_model.LinearRegression()
reg24.fit(md2[["NA_Sales", "EU_Sales"]],md2.Other_Sales)

reg3 = linear_model.LinearRegression()
reg3.fit(md3[["Area", "BHK", "Bathroom", "Age"]],md3.Price)

reg4 = LogisticRegression()
reg4.fit(md4[["hcgI","hcgII","amh"]],md4.pcos)

a = int(input("Please tell us what model would you like to use \n 1 = md1 - Sales Prediction \n 2 = md2 - Video Game Sales Prediciton \n 3 = md3 - Housing Prices Prediction (in Lucknow) \n 4 = md4 - PCOS Syndrome Diagnosis \n "))

if a == 3:
    ar = float(input("Enter the Area of House (in sqft): "))
    bh = float(input("Enter the Number of Bedrooms + Hall + Kitchen in your house (BHk): "))
    bah = float(input("Enter the Number of Bathrooms in your House: "))
    ag = float(input("Enter the Age of your House: "))
    
    prf = reg3.predict([[ar , bh , bah , ag]])
    print("Your House is worth ", prf, "rupees (in lacs)")
    #print(reg3.coef_)
    #print(reg3.intercept_)
    #X = md3.iloc[:, :-1].values
    #y = md3.iloc[:, 1].values
    
    #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=5, random_state=0)
    #y_pred = reg3.predict(X_test)
    plt.xlabel('area (sqft)')
    plt.ylabel('price (Rs. In Lacs)')
    plt.scatter(md3.Area, md3.Price, color='red',marker='+')
    #plt.scatter(X_train, y_train,color='g')
    #plt.plot(X_test, y_pred,color='k')


    plt.show()
elif a == 2:
    init = int(input("Hello! This is the VGSales model, I will help you forecast the sales of your game in a region based on how it has performed in other regions. \n Enter 1 for NA Prediction \n Enter 2 for EU Prediction \n Enter 3 for Prediction in APAC Prediction"))
    if init == 1:
        Eu = float(input("Enter your EU Sales"))
        #JP = float(input("Enter your JP Sales"))
        Apac = float (input("Enter your APAC Sales"))
        
        VGSalesF = reg21.predict([[Eu , Apac]])
        
        print("The Sales Forecast is ", VGSalesF, "(in millions)")
        plt.xlabel('NA Sales (in millions)')
        plt.ylabel('Global Sales (in millions)')
        plt.scatter(md2.Global_Sales, md2.NA_Sales, color='red',marker='+')
        plt.show()
        
    elif init == 2:
        Na = float(input("Enter your NA Sales"))
        #JP = float(input("Enter your JP Sales"))
        Apac = float (input("Enter your OTHER Sales"))
        
        VGSalesF = reg22.predict([[Na , Apac]])
        
        print("The Sales Forecast is ", VGSalesF, "(in millions)")
        plt.xlabel('EU Sales (in millions)')
        plt.ylabel('Global Sales (in millions)')
        plt.scatter(md2.Global_Sales, md2.EU_Sales, color='red',marker='+')
        plt.show()
    elif init == 3:
        Na = float(input("Enter your NA Sales"))
        #JP = float(input("Enter your JP Sales"))
        Eu = float (input("Enter your EU Sales"))
        
        VGSalesF = reg24.predict([[Na, Eu]])
        
        print("The Sales Forecast is ", VGSalesF, "(in millions)")
        plt.xlabel('APAC Sales (in millions)')
        plt.ylabel('Global Sales (in millions)')
        plt.scatter(md2.Global_Sales, md2.Other_Sales, color='red',marker='+')
        plt.show()
    
elif a == 4:
    hcgI = int(input("Please enter the test results of 'I beta-HCG' in (mIU/mL) format."))
    hcgII = int(input("Please enter the test results of 'II beta-HCG' in (mIU/mL) format."))
    amh = int(input("Please enter the test results of 'AMH' in (ng/mL) format."))
    
    pcos = reg4.predict([[hcgI,hcgII,amh]])
    plt.xlabel('I-HCG Results (in millions)')
    plt.ylabel('PCOS Diagnosis (in millions)')
    plt.scatter(md4.pcos,md4.hcgI,color='red',marker='+')
    #plt.show()
    plt.xlabel('II-HCG Results (in millions)')
    plt.ylabel('PCOS Diagnosis (in millions)')
    plt.scatter(md4.pcos, md4.hcgII, color='red',marker='+')
    #plt.show()
    plt.xlabel('AMH Results (in millions)')
    plt.ylabel('PCOS Diagnosis (in millions)')
    plt.scatter(md4.pcos, md4.amh, color='red',marker='+')
    #plt.show()
    if hcgI > 100:
        pcosI = 1
    else:
        pcosI = 0
    print(pcosI)
    print(reg4.intercept_)
    print(reg4.coef_)
    if pcosI > 1:
        print("The patient is diagnosed with this disease.")
    else:
        print("The patient is not diagnosed with this disease.")
            
else:
    print("Out of Service")
    
    

