
class Day2a:
    def __init__(self, file_path):
        self.file_path = file_path

    # counting scoce
    def score_counter(self):
        r_p_s_dict = {'X' : 1, 'Y' : 2, 'Z' : 3}
        my_win_cond = {'AY': 6, 'BZ': 6, 'CX': 6, 'AX': 3, 'BY': 3, 'CZ': 3}
        score = 0
        # open txt file
        with open(self.file_path,'r') as txt_file:
            # remo
            for txt_line in txt_file:
                txt_line = txt_line[0:3].replace(' ', '').upper()
                if txt_line.isalpha():
                    score += r_p_s_dict[txt_line[-1]]
                    if txt_line in list(my_win_cond):
                        score += my_win_cond[txt_line]
                else:
                    pass
        return score

