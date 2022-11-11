from ast import NotIn
import pandas as pd
import os
import numpy as np
from pprint import pprint


def milking(request_json):
    try:
        response = {}
        df = pd.read_csv(r"C:\Users\satishkumar.s\Downloads\final-Pincode-and-mcc-code-main\final-Pincode-and-mcc-code-main\Haptik_Pincode-and-MCC-code-main\Haptik_Pincode-and-MCC-code-main\Milkrare-Haptik-copy\factory\Haptikdata.csv",encoding='latin-1')
        #url = "https://github.com/wazsee/Haptik_Pincode-and-MCC-code/blob/main/Milkrare-Haptik%20-%20Copy/factory/Haptikdata.csv?raw=true"
        #df = pd.read_csv(url)
        

        
        response_values = df.loc[(df['PinCode']==request_json['PinCode'])] 
        response_values = df.loc[(df['MccCode']==request_json['MccCode'])]
        print(df.head())
                ################################################################

        # if [request_json["PinCode"]]not in df.values:
        #     response["Pincode is False"]
        # elif str(request_json["PinCode"]).zfill(6) and str(request_json["MCCcode"]) in df.values:
        #     response["True"]
        # else:
        #     response["False"]


        
        #PinCode = ['516309']
        #B=['356']
        
        #pd.concat([s1, s2])
        
        c=str(request_json["PinCode"]) + str(request_json["MccCode"])
        print(c)
        if c in df.values:
            #response["PinCode and MCC code Exists"]
            response['RegionName'] = response_values['RegionName'].values[0]
        else:
            response["PinCode and MCC code Does not Exists"]
            

        # if str(request_json["PinCode_MCCcode"])in df.values:
        #     response["True"]
        # else:
        #     response["False"]


                
        return response
    except Exception as e:
        return str(e)
    
