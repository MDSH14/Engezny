from bidi.algorithm import get_display
import arabic_reshaper
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import os
class Engezny:
    def __init__(self, DataFrame):
        self.DataFrame = DataFrame
    
    def labelcolor(self, colors):
        rgb = [tuple(int(item.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)) for item in color]
        return ["white" if (0.2126*item[0] + 0.7152*item[1] + 0.0722*item[2]) < 128 else "black" for item in rgb]
    
    def value_counts(self, Data, multi_sep=None, single_sep=None):
        if multi_sep == None and single_sep == None:
            return dict(Data.value_counts())
        Dict = dict()
        try:
            for i in Data.dropna().index:
                Words = str(Data).split(multi_sep)
                for Word in Words:
                    Word = Word.split(single_sep)[0].strip()
                    if Word in Dict.keys():
                        Dict[Word] += 1
                    else:
                        Dict[Word] = 1
        except:
            return "Error"
        return dict(sorted(Dict.items(), key=lambda item: item[1], reverse=True))
    
    
    def save(self, location, Count, extention, item):
        Title = '{}'.format(item).title()
        Title = ''.join(e for e in Title if e.isalnum())
        try:
            os.mkdir(location)
        except:
            pass
        plt.savefig('{}{}. {}.{}'.format(location, Count, Title, extention), bbox_inches='tight', transparent=True);
        
    
    def visualize(self,
                  start= 0,
                  end = None,
                  location = 'Charts/',
                  extention = 'jpg',
                  colors = None,
                  save=True,
                  multi_sep=None,
                  single_sep=None,
                  figsize=(15, 15),
                  base = 'total_values',
                  other= False):
        Count = 1
        for item in list(self.DataFrame)[start:end]:
            Dict = self.value_counts(self.DataFrame[item], multi_sep, single_sep)
            if Dict == "Error":
                continue
            
            if other:
                if len(Dict) > 5:
                    Tot = sum(Dict.values())
                    Dict = dict(list(Dict.items())[:4])
                    Dict['Other'] = Tot - sum(Dict.values())

            Keys = list()
            for Key in Dict.keys():
                Keys.append(get_display(arabic_reshaper.reshape(str(Key))))
            Values = list(Dict.values())

            labels = []
            if not other:
                if base == 'total_values':
                    Tot = sum(Values)
                elif base == "data_base":
                    Tot = len(self.DataFrame)
                elif base == "column_base":
                    Tot = len(self.DataFrame[item].dropna())
                else:
                    raise ValueError('Unknown base !')
                
            for i in Values:
                labels.append("{}/{} ({}%)".format(i, Tot, int((i/Tot)*100)))

            matplotlib.rcParams.update({'font.size': 25})
            f, ax = plt.subplots(figsize=figsize)

            if len(Keys) <= 5 and base == 'total_values':
                for i in range(len(Keys)):
                    Keys[i] += " (" + labels[i].split()[0] + ")"

                _, _, autotexts = plt.pie(Values, labels=["" for k in Keys], autopct="%.1f%%", colors=colors)
                for color, autotext in zip(self.labelcolor(colors), autotexts):
                    autotext.set_color(color)
                plt.legend(loc = 'lower center', bbox_to_anchor=(0.25, -0.1, 0.5, 0.5), labels = Keys)

            elif len(Keys) < 8:
                for i, v in enumerate(labels):
                    ax.text(i-0.5, Values[i], str(v), fontsize=25)

                plt.bar(Keys, Values, color=colors[0])
                plt.xticks(rotation = 90)

            else:
                Keys.reverse()
                Values.reverse()
                labels.reverse()
                if len(Keys) > 20:
                    for i, v in enumerate(labels[-20:]):
                        ax.text(Values[-20:][i], i, str(v), fontsize=25)
                    plt.barh(Keys[-20:], Values[-20:], color=colors[0])
                else:
                    for i, v in enumerate(labels):
                        ax.text(Values[i], i, str(v), fontsize=25)
                    plt.barh(Keys, Values, color=colors[0])

            plt.title(get_display(arabic_reshaper.reshape(item.title())), fontsize=35)
            if save:
                self.save(location, Count, extention, item)
            plt.show()
            Count += 1
