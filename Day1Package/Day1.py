import pandas as pd
# Day1 Class
class Day1a:

    # init cfe
    def __init__(self,file_path):
        self.file_path = file_path

    # import content of .txt file
    def import_file(self):
        df = pd.read_excel(self.file_path, 'Sheet1', header= None)
        return df

    def caloriescounter(self):
        df = self.import_file()
        elfdict = {}
        elfnumb = 1
        calories = 0
        for i in range(len(df) - 1):
            try:
                value = int(df.at[i, 0])
                calories += value
            except ValueError:
                elfdict[elfnumb] = calories
                elfnumb += 1
                calories = 0
        maxcalelf = max(elfdict.items(), key=lambda x: x[1])
        return elfdict, maxcalelf




