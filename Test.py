
import re

def import_txt(path_txt):
    r_p_s_dict = {'A': 1, 'B': 2, 'C': 3,'X': 1, 'Y': 2, 'Z': 3}
    score = 0
    with open(path_txt,'r') as txt_file:
        score = ansver_logic(txt_file, r_p_s_dict, score)
    print(score)

def ansver_logic(txt_file,r_p_s_dict,score):
    for txt_line in txt_file:
        txt_line = txt_line[0:3].replace(' ','').upper()
        if txt_line[0:3].isalpha():
            score += r_p_s_dict[txt_line[-1]]
            if r_p_s_dict[txt_line[0]] == r_p_s_dict[txt_line[-1]]:
                score += 3
            elif ((r_p_s_dict[txt_line[0]] % 3) + 1) == r_p_s_dict[txt_line[-1]]:
                score += 6
            else:
                pass
        else:
            pass
    return score



def ansver_logic_update(txt_file, r_p_s_dict, score):
    for txt_line in txt_file:
        txt_line = txt_line[0:3].replace(' ','').upper()
        match txt_line[-1]:
            case 'Z':
                score += 6 + ((r_p_s_dict[txt_line[0]] % 3) + 1)
            case 'Y':
                score += 3 + r_p_s_dict[txt_line[0]]
            case 'X':
                f = lambda x: x - 1 if (x > 1) else 3
                score += f(r_p_s_dict[txt_line[0]])
    return score


def win_condition(txt_line, score, r_p_s_dict):
    score += 6 + ((r_p_s_dict[txt_line[0]] + 1) % 3)

    return  score


def win_condition2(numb, score):
    f = lambda x: x - 1 if (x > 1) else 3
    score += f(numb)
    return score





#print(win_condition2(1,0))
testfce = import_txt('E:/PythonProjects/AdventOfCode/Day2Package/Strategy_test.txt')








