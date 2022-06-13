import time

from utils import load_yaml, abs_path


class Splitter:
    def __init__(self, dosage_info_path, field_drug, field_dosage, max_ratio=0.84, max_dist=2):
        self.max_dist = max_dist
        self.max_ratio = max_ratio
        self.field_drug = field_drug
        self.field_dosage = field_dosage
        dosage_infos = load_yaml(abs_path(dosage_info_path))
        self.value_dosage_forms = sorted(
            [dosage_forms for dosage_forms in dosage_infos.get('list_dosage_forms', [])],
            key=lambda x: -len(x))
        self.low_value_dosage = [dosage.lower() for dosage in dosage_infos.get('list_dosage_forms', [])]

    def longest_common_string(self, predict, dosage):
        len_predict, len_dosage = len(predict), len(dosage)
        L = [[0 for _ in range(len_dosage + 1)] for _ in range(len_predict + 1)]

        for i in range(len_predict + 1):
            for j in range(len_dosage + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif predict[i - 1] == dosage[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])

        lcs = ""
        result = ""
        distance = 0
        start = end = -1
        i = len_predict
        j = len_dosage
        while i > 0 and j > 0:
            if predict[i - 1] == dosage[j - 1]:
                lcs = predict[i - 1] + lcs
                i -= 1
                j -= 1
                if end == -1:
                    end = i
                start = i
                distance = 0
            elif L[i - 1][j] > L[i][j - 1]:
                i -= 1
                distance += 1
                if distance >= self.max_dist:
                    lcs = predict[i]
            else:
                j -= 1

            if len(lcs) > len(result):
                result = lcs

        return start, end, (result.strip()).strip(',')

    def search(self, predict):
        res = [-1, -1, "", ""]
        for dosage_forms in self.value_dosage_forms:
            low_predict, low_dosage_form = predict.lower(), dosage_forms.lower()
            start, end, common_str = self.longest_common_string(low_predict, low_dosage_form)
            if len(common_str) > len(res[3]) and len(common_str) / len(dosage_forms) > self.max_ratio:
                res = [start, end, dosage_forms, common_str]
                if common_str in self.low_value_dosage:
                    res[2] = common_str
        return res[:-1]

    def get_full_dosage_forms(self, start, end, predict):
        while start - 1 >= 0 and predict[start - 1].isalpha() and predict[start - 1] != " ":
            start -= 1
        while end + 1 <= len(predict) - 1 and not predict[end + 1].isdigit():
            end += 1
        return start, end

    def split_name(self, predict):
        name_drug = predict
        start, end, dosage_forms_db = self.search(predict)

        if dosage_forms_db:
            start, end, = self.get_full_dosage_forms(start, end, predict)
            name_drug = predict[:start].strip()
            if any(map(str.isdigit, predict[end:])):
                name_drug += predict[end:]

        return name_drug.strip(','), dosage_forms_db

    def __call__(self, matcher_result, **kwargs):
        recognized_text = ' '.join(matcher_result['matched_strs'])
        name_drug, dosage_forms = self.split_name(recognized_text)
        matcher_result['matched_strs'] = [
            {'class_name': self.field_drug,
             'matched_strs': [name_drug if name_drug is not None else ''],
             'idxs': matcher_result['idxs'] if name_drug is not None else []},
            {'class_name': self.field_dosage,
             'matched_strs': [dosage_forms if dosage_forms is not None else ''],
             'idxs': matcher_result['idxs'] if dosage_forms is not None else []}]
        return matcher_result


def test():
    predict_files = "test.txt"
    predict = []
    with open(predict_files, "r") as f:
        predicts = f.read().split('\n')

    # predicts = ["Trileptal Oral suspension 60 mg/ml"]
    # predicts = ["Voltaren Modified-release tablet 75 mg"]
    # predicts = ['abc injesions 76mg, ']
    # predicts = ['Zykadia Capsule, hard 150 mg']
    # predicts = ['Nutriflex peri, solution for infusion']
    # predicts = ['- Exforge Fim-coated Tablet 10/160 mg']
    # predicts = ['Eprex 2000 U solution for injection (pre-filled syringes']
    # predicts = ['Eprex 2000 U solution for injection']
    # # predicts = ['Recormon PS 2000 lU/0.3 ml prefilled syringes']
    # # predicts = ['Revolade Fiim-coated tablet 25 mg']
    # predicts = ['Durogesic Matrix 25 ng/h, transdermal pạtch Active ingredient(s)? a']
    # predicts = [' Gonal-f PEN 300 U.1./0.5 ml, Injektionslosung']
    # predicts = ['Antramups 20, Tabletten']
    # predicts = ['Sandimmun Neoral Capsule, soft 25 mg']
    # predicts = [' Rivoleve 500 mg film-coated tablet']
    # predicts = ['Exforge Filmn-coated tablet.5/80 mg']

    sn = Splitter(dosage_info_path='dosage_info.yaml',
                  field_drug=[],
                  field_dosage=[])

    since = time.time()
    for predict in predicts:
        name_drug, dosage_forms = sn.split_name(predict)
        print("ORIGINAL: ", predict)
        print("DRUG:     ", name_drug)
        print("DOSAGE:   ", dosage_forms)
        print()

    print("TIME", (time.time() - since) / len(predicts))


test()
