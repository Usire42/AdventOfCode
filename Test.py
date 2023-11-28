
import re
def import_txt(path_txt):
    r_p_s_dict = {'X': 1, 'Y': 2, 'Z': 3}
    my_win_cond ={'AY': 6, 'BZ': 6, 'CX': 6, 'AX': 3, 'BY': 3, 'CZ': 3 }
    score = 0
    with open(path_txt,'r') as txt_file:
        for txt_line in txt_file:
            txt_line = txt_line[0:3].replace(' ','').upper()
            if txt_line[0:3].isalpha():
                score += r_p_s_dict[txt_line[-1]]
                if txt_line in list(my_win_cond):
                    score += my_win_cond[txt_line]
            else:
                print("ont an alpha")
    print(score)







testfce = import_txt('E:/PythonProjects/AdventOfCode/Day2Package/Strategy_test.txt')








