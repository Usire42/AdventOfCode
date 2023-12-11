#Loacal Library
import Day1Package.Day1 as d1
import Day2Package.day2 as d2

def path_convert(pathway):
    newpath = pathway.replace('\\', '/')
    return newpath

def main():
    #day1
    '''
    pathwayxls = 'E:/PythonProjects/AdventOfCode/Day1Package/Calories.xlsx'
    d1a_result = d1.Day1a(pathwayxls).caloriescounter()
    print(d1a_result[1])
    d1b_result = d1.Day1b(d1a_result[0]).sum_of_three_max_cal()
    print(d1b_result)
    '''

    #Day2
    path_to_file = path_convert("E:\PythonProjects\AdventOfCode\Day2Package\Strategy_input.txt")
    d2a_result = d2.Day2a(path_to_file).score_counter()
    print(d2a_result)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


