import numpy as np
from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt

md5 = pd.read_csv("VgSalesTrain.csv")
md6 = pd.read_csv("MarketingTrain.csv")

reg51 = linear_model.LinearRegression()
reg51.fit(md5[["Sports", "Platformer", "Racing", "Role-Playing", "Puzzle", "Misc", "Shooter", "Simulation", "Fighting", "Action", "Strategy", "Adventure","Nintendo","Ubisoft","Electronic Arts", "Activision","Sony Computer Entertainment", "Microsoft Game Studios", "Namco Bandai Games", "Konami Digital Entertainment", "THQ", "Sega", "Take-Two Interactive", "Capcom", "10TACLE Studios", "1C Company", "20th Century Fox Video Games","EU_Sales", "Other_Sales"]],md5.NA_Sales)
reg52 = linear_model.LinearRegression()
reg52.fit(md5[["Sports", "Platformer", "Racing", "Role-Playing", "Puzzle", "Misc", "Shooter", "Simulation", "Fighting", "Action", "Strategy", "Adventure","Nintendo","Ubisoft","Electronic Arts", "Activision","Sony Computer Entertainment", "Microsoft Game Studios", "Namco Bandai Games", "Konami Digital Entertainment", "THQ", "Sega", "Take-Two Interactive", "Capcom", "10TACLE Studios", "1C Company", "20th Century Fox Video Games", "NA_Sales",  "Other_Sales"]],md5.EU_Sales)
reg53 = linear_model.LinearRegression()
reg53.fit(md5[["Sports", "Platformer", "Racing", "Role-Playing", "Puzzle", "Misc", "Shooter", "Simulation", "Fighting", "Action", "Strategy", "Adventure","Nintendo","Ubisoft","Electronic Arts", "Activision","Sony Computer Entertainment", "Microsoft Game Studios", "Namco Bandai Games", "Konami Digital Entertainment", "THQ", "Sega", "Take-Two Interactive", "Capcom", "10TACLE Studios", "1C Company", "20th Century Fox Video Games", "NA_Sales",  "EU_Sales"]],md5.Other_Sales)
reg6 = linear_model.LinearRegression()
reg6.fit(md6[["TV","Radio","Social Media", "OrdInfluencers"]],md6.Sales)

a = int(input("Enter the model to be used; \n 5 = md5 - Advanced Video Game Sales Prediction \n 6 = md6 - Marketing Sales Prediction Programme"))

if a == 5:
    print("Enter the Genre the Game will be launched in: (1- for yes, 0 for no)") # " \n 1 = Sports \n 2 = Platformer \n 3 = Racing \n 4 = Role-Playing \n 5 = Puzzle \n 6 = Misc \n 7 = Shooter \n 8 = Simulation \n 9 = Fighting \n 10 = Action \n 11 = Strategy \n 12 = Adventure   "
    Sports = int(input("isSports?"))
    Platform = int(input("isPlatformer?"))
    Racing = int(input("isRacing?"))
    RolePlaying = int(input("isRoleplaying?"))
    Puzzle = int(input("isPuzzle?"))
    Misc = int(input("isMisc?"))
    Shooter = int(input("isShooter?"))
    Simulation = int(input("isSimulation?"))
    Fighting = int(input("isFighting?"))
    Action = int(input("isAction?"))
    Strategy = int(input("isStrategy?"))
    Adventure = int(input("isAdventure?"))
    print("Enter the publisher the game is published on: (1- for yes, 0 for no)")
    Nintendo = int(input("isNintendo?"))
    Ubisoft = int(input("isUbisoft"))
    ElectronicArts = int(input("isElectronic Arts?"))
    Activision = int(input("is Activision?"))
    SonyComputerEntertainment =int(input("isSony Computer Entertainment?"))
    MicrosoftGameStudios = int(input("isMicrosoft Game Studios?"))
    NamcoBandaiGmaes = int(input("is Namco Bandai Games ?"))
    KonamiDigitalEntertainment = int(input("is Konami Digital Entertainment ?"))
    thq = int(input("is THQ?"))
    Sega = int(input("is Sega?"))
    TakeTwoInteractive = int(input("is Take Two Interactive?"))
    Capcom = int(input("isCapcom?"))
    TenTacleStudios = int(input("is 10TACLE Studios?"))
    OneCCompany = int(input("is 1C Company?"))
    CenturyFoxVG = int(input("is 20th Century Fox Video Games?"))
    init = int(input("Hello! This is the VGSales model, I will help you forecast the sales of your game in a region based on how it has performed in other regions. \n Enter 1 for NA Prediction \n Enter 2 for EU Prediction \n Enter 3 for Prediction in APAC Prediction"))
    if init == 1:
        Eu = float(input("Enter your EU Sales"))
        #JP = float(input("Enter your JP Sales"))
        Apac = float (input("Enter your APAC Sales"))
        
        VGSalesF = reg51.predict([[Sports, Platform, Racing, RolePlaying, Puzzle, Misc, Shooter, Simulation, Fighting, Action, Strategy, Adventure, Nintendo, Ubisoft, ElectronicArts, Activision, SonyComputerEntertainment, MicrosoftGameStudios, NamcoBandaiGmaes, KonamiDigitalEntertainment, thq, Sega, TakeTwoInteractive, Capcom, TenTacleStudios, OneCCompany, CenturyFoxVG, Eu, Apac]])
        
        print("The Sales Forecast is ", VGSalesF, "(in millions)")
        plt.xlabel('NA Sales (in millions)')
        plt.ylabel('Global Sales (in millions)')
        plt.scatter(md5.Global_Sales, md5.NA_Sales, color='red',marker='+')
        plt.show()
        
    elif init == 2:
        Na = float(input("Enter your NA Sales"))
        #JP = float(input("Enter your JP Sales"))
        Apac = float (input("Enter your OTHER Sales"))
        
        VGSalesF = reg52.predict([[Sports, Platform, Racing, RolePlaying, Puzzle, Misc, Shooter, Simulation, Fighting, Action, Strategy, Adventure, Nintendo, Ubisoft, ElectronicArts, Activision, SonyComputerEntertainment, MicrosoftGameStudios, NamcoBandaiGmaes, KonamiDigitalEntertainment, thq, Sega, TakeTwoInteractive, Capcom, TenTacleStudios, OneCCompany, CenturyFoxVG,Na,Apac]])
        
        print("The Sales Forecast is ", VGSalesF, "(in millions)")
        plt.xlabel('EU Sales (in millions)')
        plt.ylabel('Global Sales (in millions)')
        plt.scatter(md5.Global_Sales, md5.EU_Sales, color='red',marker='+')
        plt.show()
    elif init == 3:
        Na = float(input("Enter your NA Sales"))
        #JP = float(input("Enter your JP Sales"))
        Eu = float (input("Enter your EU Sales"))
        
        VGSalesF = reg53.predict([[Sports, Platform, Racing, RolePlaying, Puzzle, Misc, Shooter, Simulation, Fighting, Action, Strategy, Adventure, Nintendo, Ubisoft, ElectronicArts, Activision, SonyComputerEntertainment, MicrosoftGameStudios, NamcoBandaiGmaes, KonamiDigitalEntertainment, thq, Sega, TakeTwoInteractive, Capcom, TenTacleStudios, OneCCompany, CenturyFoxVG, Na, Eu ]])
        
        print("The Sales Forecast is ", VGSalesF, "(in millions)")
        plt.xlabel('APAC Sales (in millions)')
        plt.ylabel('Global Sales (in millions)')
        plt.scatter(md5.Global_Sales, md5.Other_Sales, color='red',marker='+')
        plt.show()
    #VgSalesF = reg51.predict([[Sports, Platform, Racing, RolePlaying, Puzzle, Misc, Shooter, Simulation, Fighting, Action, Strategy, Adventure, Nintendo, Ubisoft, ElectronicArts, Activision, SonyComputerEntertainment, MicrosoftGameStudios, NamcoBandaiGmaes, KonamiDigitalEntertainment, thq, Sega, TakeTwoInteractive, Capcom, TenTacleStudios, OneCCompany, CenturyFoxVG]])
elif a == 6:
    Tv = float(input("Please tell your TV Promotions Budget (in millions $)"))
    Radio = float(input("Please tell your Radio Promotions Budget (in millions $)"))
    SocialMedia = float(input("Please tell your SocialMedia Promotions Budget (in millions $)"))
    ordval_1 = float(input("Please tell the influencer size that you are partnering with: \n Mega (>1Million Followers) - 4 \n Macro (100k-1Mil Followers) - 3 \n Micro (10k-100k Followers) - 2, \n Nano(<10k Followers) - 1 \n : "))
    sales = reg6.predict([[Tv,Radio,SocialMedia,ordval_1]])
    print("The Estimated Sales with this Marketing Plans are $", sales , "(in millions)")
    


    