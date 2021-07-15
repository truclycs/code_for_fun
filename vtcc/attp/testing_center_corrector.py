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

        idx_lines = []
        if self.check_existence(s[len(s) - 1]):
            idx_lines = list(self.testing_center_words[s[len(s) - 1]])

        for i in range(len(s) - 1):
            if self.check_existence(s[i]):
                idx_lines += list(self.testing_center_words[s[i]])
            if self.check_existence(s[i] + s[i + 1]):
                idx_lines += list(self.testing_center_words[s[i] + s[i + 1]])

        if len(idx_lines) == 0:
            return s

        idx_lines, counts = np.unique(np.array(idx_lines), return_counts=True)
        indexes = idx_lines[counts == counts.max()]
        return indexes

    def get_result(self, indexes, s):
        if len(indexes) == 1:
            return self.testing_center_list[int(indexes)]
        else:
            return s

    def __call__(self, s):
        indexes = self.get_idx_line(s)
        result = self.get_result(indexes, s)
        return result


if __name__ == '__main__':
    with open("output.txt", "r") as f:
        output = f.read().split('\n')

    testcases = []
    for line in output:
        testcases.append(line.split('\t')[-1])

    corrector = TestingCenterCorrector(testing_center_list_path='testing_center_list.yaml',
                                       testting_center_words_path='testing_center_words.pkl')

    for testcase in testcases:
        if testcase:
            print('testcase', testcase)
            print('corrects', corrector(testcase))
            print()
