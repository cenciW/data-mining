import pandas as pd
import numpy as np
import os

# Load the data
df = pd.read_csv('0-Datasets/train.csv')

print(df.head(15))

# Imprime informações sobre dos dados
print("INFORMAÇÕES GERAIS DOS DADOS\n")
print(df.info())
print("\n")

#Imprime analise descritiva sobre os dados
print("ANALISE DESCRITIVA DOS DADOS\n")
print(df.describe())
print("\n")

#Imprime a quantidade de valores faltantes por coluna
print("VALORES FALTANTES POR COLUNA\n")
print(df.isnull().sum())
print("\n")





    

