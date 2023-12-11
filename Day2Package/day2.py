
class Day2a:
    def __init__(self, file_path):
        self.file_path = file_path

    # counting scoce
    def score_counter(self):
        score = 0
        r_p_s_dict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
        with open(self.file_path, 'r') as txt_file:
            score = self.ansver_logic_update(txt_file, r_p_s_dict, score)
        return score

    def ansver_logic(self, txt_file, r_p_s_dict, score):
        for txt_line in txt_file:
            txt_line = txt_line[0:3].replace(' ', '').upper()
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

    def ansver_logic_update(self, txt_file, r_p_s_dict, score):
        for txt_line in txt_file:
            txt_line = txt_line[0:3].replace(' ', '').upper()
            match txt_line[-1]:
                case 'Z':
                    score += 6 + ((r_p_s_dict[txt_line[0]] % 3) + 1)
                case 'Y':
                    score += 3 + r_p_s_dict[txt_line[0]]
                case 'X':
                    f = lambda x: x - 1 if (x > 1) else 3
                    score += f(r_p_s_dict[txt_line[0]])
        return score