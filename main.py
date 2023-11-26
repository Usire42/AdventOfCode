#Loacal Library
import Day1Package.Day1 as d1



txtpathD1 = "ahoj"

def main():
    pathwayxls = 'E:/PythonProjects/AdventOfCode/Day1Package/Calories.xlsx'
    d1a_result = d1.Day1a(pathwayxls).caloriescounter()
    print(d1a_result[1])
    d1b_result = d1.Day1b(d1a_result[0]).sum_of_three_max_cal()
    print(d1b_result)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


