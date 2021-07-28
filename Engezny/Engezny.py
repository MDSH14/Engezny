#!/usr/bin/env python
# coding: utf-8

# In[80]:


class Engezny:
    def __init__(self, DataFrame):
        self.DataFrame = DataFrame
        from bidi.algorithm import get_display
        import arabic_reshaper
        import matplotlib
        import matplotlib.pyplot as plt
        import pandas as pd
        import os
    
    def visualize(self, start= 0, end = -1, location = 'Charts/', extention = 'jpg'):
        if end == -1:
            end = len(list(self.DataFrame))
        Count = 1
        for item in list(self.DataFrame)[start:end]:
            Dict = dict()
            try:
                for i in self.DataFrame[item].dropna().index:
                    Words = str(self.DataFrame[item][i]).split(",")
                    for Word in Words:
                        Word = Word.split("[")[0].strip()
                        if Word in Dict.keys():
                            Dict[Word] += 1
                        else:
                            Dict[Word] = 1
            except:
                print(item)
                continue
            Dict = dict(sorted(Dict.items(), key=lambda item: item[1], reverse=True))


            Keys = list()
            for Key in Dict.keys():
                Keys.append(get_display(arabic_reshaper.reshape(str(Key))))
            Values = list(Dict.values())

            labels = []
            Tot = sum(Values)
            for i in Values:
                labels.append("{}/{} ({}%)".format(i, Tot, int((i/Tot)*100)))

            matplotlib.rcParams.update({'font.size': 50})
            f, ax = plt.subplots(figsize=(32, 32))

            if len(Keys) <= 5:
                for i in range(len(Keys)):
                    Keys[i] += " (" + labels[i].split()[0] + ")"

                plt.pie(Values, labels=["" for k in Keys], autopct="%.1f%%")
                plt.legend(loc = 'lower center', bbox_to_anchor=(0.25, -0.1, 0.5, 0.5), labels = Keys)

            elif len(Keys) < 8:
                for i, v in enumerate(labels):
                    ax.text(i-0.5, Values[i], str(v), fontsize=50)

                plt.bar(Keys, Values)
                plt.xticks(rotation = 90)

            else:
                Keys.reverse()
                Values.reverse()
                labels.reverse()
                if len(Keys) > 20:
                    for i, v in enumerate(labels[-20:]):
                        ax.text(Values[-20:][i], i, str(v), fontsize=50)
                    plt.barh(Keys[-20:], Values[-20:])
                else:
                    for i, v in enumerate(labels):
                        ax.text(Values[i], i, str(v), fontsize=50)
                    plt.barh(Keys, Values)

            plt.title(item.title(), fontsize=70)
            Title = '{}'.format(item).title()
            Title = ''.join(e for e in Title if e.isalnum())

            try:
                os.mkdir(location)
            except:
                pass
            plt.savefig('{}{}. {}.{}'.format(location, Count, Title, extention), bbox_inches='tight');
            plt.show()
            Count += 1
