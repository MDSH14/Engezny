# Engezny
***Engezny*** is a python package that quickly generates all of the possible charts from pandas DataFrame and save them to your local machine.
***Engezny*** is only supporting now the uniparameter visualization using the pie, bar and barh visualizations

## Installation
To install ***Engezny*** you can use the command line `pip intall Engezny` or `pip3 intall Engezny`

## Simple Use
The most simple format of using ***Engezny*** is as follow:
```
from Engezny import Engezny
import pandas as pd

Data = pd.read_csv("FileName.csv")
Egz = Engezny(Data)
Egz.visualise()
```

## Advanteges:
1. ***Engezny*** is totally supporting Arabic
2. ***Engezny*** handles the multiparameters co;umns and sperate them by the comma
3. The output charts are fully descriptive

## Visualize Parameters
1. start (int) default = 0
    - The start column index
2. end (int) default= -1
    - The end column index
3. location (str) default= 'Charts/'
    - The file location to save charts in
4. extention (str) default= 'jpg'
    - The extention of the created charts
