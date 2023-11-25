#Loacal Library
import Day1Package.Day1 as D1



txtpathD1 = "ahoj"

def main():
    toprint = D1.Day1a('E:/PythonProjects/AdventOfCode/Day1Package/Calories.xlsx')
    print(toprint.caloriescounter())
    print(toprint.caloriescounter()[1])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


