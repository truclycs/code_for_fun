import pickle
import numpy as np

from utils import no_accent_vietnamese, load_yaml, abs_path


class TestingCenterCorrector:
    def __init__(self, testing_center_list_path, testting_center_words_path):
        self.testing_center_list = load_yaml(abs_path(testing_center_list_path)).get('testing_center')
        testing_center_words_file = open(testting_center_words_path, "rb")
        self.testing_center_words = pickle.load(testing_center_words_file)

    def check_existence(self, word):
        return (word in self.testing_center_words)

    def get_idx_line(self, s):
        s = no_accent_vietnamese(s).lower().split(' ')

        if self.check_existence(s[len(s) - 1]):
            idx_lines = list(self.testing_center_words[s[len(s) - 1]])
        else:
            idx_lines = []

        for i in range(len(s) - 1):
            if self.check_existence(s[i]):
                idx_lines += list(self.testing_center_words[s[i]])
            if self.check_existence(s[i] + s[i + 1]):
                idx_lines += list(self.testing_center_words[s[i] + s[i + 1]])

        idx_lines, counts = np.unique(np.array(idx_lines), return_counts=True)
        indexes = idx_lines[counts == counts.max()]
        return indexes

    def get_result(self, indexes):
        if len(indexes) == 1:
            return self.testing_center_list[int(indexes)]
        else:
            pass

    def __call__(self, s):
        indexes = self.get_idx_line(s)
        result = self.get_result(indexes)
        return result


if __name__ == '__main__':
    testcases = ["TRUNG TÂM KIỂM NGHIỆM THUỐC - THỰC PHẨM VÀ NGHIÊN CỬU ỨNG DỤNG",
                 "TUV SUD Vieam Co., Ltd.",
                 ""]

    corrector = TestingCenterCorrector(testing_center_list_path='testing_center_list.yaml',
                                       testting_center_words_path='testing_center_words.pkl')

    for testcase in testcases:
        print(corrector(testcase))
