# Engezny
***Engezny*** is a python package that quickly generates all possible charts from your dataframe and save them for you, and engezny is only supporting now uniparameter visualization using the pie, bar and barh visualizations.

## New release features:
1. Full control with colors used in charts.
2. Arabic issues solved.
4. Base of data control.
5. Issues solved with saving charts.
6. New list of options which make your customization easier (Check them in parameters).

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
Egz.visualize()
```

## Visualization Parameters
- `start (int) default = 0`: The first column to start with index
- `end (int) default = None`: The final column to end with index
- `location (str) default ='Charts/'`: The file location to save charts in. The package creates the file if not exsist
- `extention (str) default = 'jpg'`: The extention of the created charts
- `colors (list) default = None`: A list of colors HEX codes to use in charts
- `save (bool) default = True`: The save option to save generated charts to the local machine
- `multi_sep (str) default = None`: the separator delimiter for multiselection columns
- `single_sep (str) default = None`: A delimiter to split single values with
- `figsize (tuple) default = (15, 15)`: The figure size of charts
- `base (str) default = 'total_values'`: The base to use in charts. Makes a difference with multiselection columns and has three available options:
    - `'total_values'`: Uses the sum of total values as a base
    - `'data_base'`: Uses the total number of rows in data as a base
    - `'column_base'`: Uses the count of non-null cells in the column as a base
- `other (bool) default = False` The other option takes only the top 4 values and combine the rest in and other value
