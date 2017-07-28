# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 13:55:02 2017
@author: dhurt

GOAL: Reproduce Aquion's Data Extraction Protocols with a Python Version
Begin with reading MACCOR standard data format, followed by MTI Data. 
(Include in sub-programs?)
"""

#import standard libraries
import numpy as np                             #in case of math
import scipy as sp                             #in case of science
import pandas as pd                            #in case of DATA
import matplotlib as mpl                       #in case of images
import matplotlib.pyplot as plt                #in case of plots
import os                                      #in case of files
#import csv                                     #in case of .txt files
#import struct                    #unpacking?

#Import special libraries
#import tkinter as tk                           #default python gui 
#from tkinter import filedialog                 #not sure if needed since have tkinter but simple

#ASSIGN HARD-CODED FILE PATHS HERE
Data2Sort = "C:\\Users\\dhurt\\Desktop\\Battery Testing\\Data to Sort\\" 
RawData =   "C:\\Users\\dhurt\\Desktop\\Battery Testing\\Raw Data\\" 
FmtData =   "C:\\Users\\dhurt\\Desktop\\Battery Testing\\Formatted Data\\" 

#Begin Script
#Initialize Strings?
Files = os.listdir(Data2Sort);
ZZ=len(Files)
Serials=[]


for YY in range(0,ZZ):
    #Get Serial Info from File Names
    j=0;
    Dat=""
    Loc=""
    Num=""
    Typ=""
    Tno=""
    TTy=""
    FName=""
    for i in range(0,len(Files[YY])):
        if Files[YY][i] == "_":
            j+=1;
        elif Files[YY][i] == " " or Files[YY][i] == ".":
            j=10; #This will shut down any loops that get to the end of the file
        elif j==0:
            Dat=Dat+(Files[YY][i])
        elif j==1:
            Loc=Loc+(Files[YY][i])
        elif j==2:
            Num=Num+(Files[YY][i])
        elif j==3:
            Tno=Tno+(Files[YY][i])
        elif j==4:
            TTy=TTy+(Files[YY][i])
##             
    #Fix some of the above, save serial
    Serials.append(Dat+Loc+Num)
    Typ=Num[4]
    Num=Num[0:4]
    if Dat[2]=="A":
        Dat="14"+Dat[0:2]+Dat[3:5]
    elif Dat[2]=="B":
        Dat="15"+Dat[0:2]+Dat[3:5]
    elif Dat[2]=="C":
        Dat="16"+Dat[0:2]+Dat[3:5]
    elif Dat[2]=="D":
        Dat="17"+Dat[0:2]+Dat[3:5]
    elif Dat[2]=="E":
        Dat="18"+Dat[0:2]+Dat[3:5]
      
def readFiles():        
    FName=(Data2Sort+Files[YY])
    data=open(FName)
    theData=pd.read_table(data, skiprows=2)
    
    
    
#    np.loadtxt(FName)
    
    
    
    
    
    
    
    
    