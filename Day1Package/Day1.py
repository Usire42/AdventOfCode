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

    # create of dictionary with number of elf and sum of calories is holding
    def caloriescounter(self):
        df = self.import_file()
        elfdict = {}
        elfnumb = 1
        calories = 0
        # loop for adding calories to one elf and creane new record in dictionary
        for i in range(len(df) - 1):
            try:
                value = int(df.at[i, 0])
                calories += value
            except ValueError:
                elfdict[elfnumb] = calories
                elfnumb += 1
                calories = 0
        maxcalelf = max(elfdict.items(), key=lambda x: x[1])
        # return dictionary of elfs and elf with max calories
        return elfdict, maxcalelf

class Day1b:
    def __init__(self, elf_dictionary):
        self.elf_dictionary = elf_dictionary


    # sum of calories of 3 efls with max caloies
    def sum_of_three_max_cal(self):
        max_cla = 0
        sortdict = sorted(self.elf_dictionary.items(), key=lambda x: x[1], reverse=True)
        for i in range(3):
            max_cla += sortdict[i][1]
        return max_cla

