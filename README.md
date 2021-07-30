# Engezny
***Engezny*** is a python package that quickly generates all possible charts from your dataframe and save them for you as <b>JPG</b>, and engezny is only supporting now uniparameter visualization using the pie, bar and barh visualizations.

## Advanteges
1. Totally supports Arabic Language.
2. Handles multi-parameters columns and separates them by a comma.
3. The output charts are fully descriptive.

## Installation Guide
To install ***Engezny*** Package:
- Make sure python3 and pip is installed in your machine.
- Use the command line and type: `pip install Engezny` or `pip3 install Engezny`
- You can check if the package is installed by typing: `pip freeze | grep Engezny` or `pip3 freeze | grep Engezny`

## How to Use?
The most simple format of using ***Engezny*** is as follow:
```python
from Engezny import Engezny
import pandas as pd

Data = pd.read_csv("FileName.csv")
Egz = Engezny(Data)
Egz.visualise()
```

## Visualization Parameters
- The start column index: `start (int) default = 0`
    - Default Value: 0
- The end column index: `end (int) default= -1`
    - Default Value: -1
- The file location to save charts in: `location = 'Charts/'`
    - Default Value: 'Charts/' 
- The extention of the created charts: `extention = 'jpg'`
    - Default Value: 'jpg'
