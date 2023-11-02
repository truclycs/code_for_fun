from utils import load_yaml, abs_path


class Splitter:
    def __init__(self, dosage_info_path, field_drug, field_dosage, max_ratio=0.85):
        self.max_ratio = max_ratio
        self.field_drug = field_drug
        self.field_dosage = field_dosage
        dosage_infos = load_yaml(abs_path(dosage_info_path))
        self.value_dosage_forms = sorted(
            [dosage_forms for dosage_forms in dosage_infos.get('list_dosage_forms', [])],
            key=lambda x: -len(x))

    def LCS(self, X, Y):
        m, n = len(X), len(Y)
        L = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif X[i - 1] == Y[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + 1
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])

        index = L[m][n]
        lcs = [""] * (index + 1)
        lcs[index] = ""

        start = end = -1
        i = m
        j = n
        while i > 0 and j > 0:
            if X[i - 1] == Y[j - 1]:
                lcs[index - 1] = X[i - 1]
                i -= 1
                j -= 1
                index -= 1

                if end == -1:
                    end = i
                start = i

            elif L[i - 1][j] > L[i][j - 1]:
                i -= 1
            else:
                j -= 1

        return start, end, "".join(lcs)

    def search(self, predict):
        # If exist full
        for dosage_forms in self.value_dosage_forms:
            low_predict = predict.lower()
            low_dosage_form = dosage_forms.lower()
            start = low_predict.find(low_dosage_form)
            if start != -1:
                if start - 1 == 0 or predict[start - 1] == ' ':
                    if start + len(dosage_forms) == len(predict) or predict[start + len(dosage_forms)] in [' ', ',']:
                        return start, start + len(dosage_forms) - 1, dosage_forms, dosage_forms

        # Find Longest Common Subsequence
        for dosage_forms in self.value_dosage_forms:
            low_predict = predict.lower()
            low_dosage_form = dosage_forms.lower()

            # Check again
            start, end, common_str = self.LCS(low_predict, low_dosage_form)
            if len(common_str) / len(dosage_forms) > self.max_ratio:
                return start, end, predict[start: end + 1], dosage_forms

        return -1, -1, None, None

    def get_full_dosage_forms(self, start, end, predict):
        while start - 1 >= 0 and predict[start - 1].isalpha() and predict[start - 1] != " ":
            start -= 1

        while end + 1 <= len(predict) - 1 and not predict[end + 1].isdigit():
            end += 1

        return start, end, predict[start: end + 1]

    def split_name(self, predict):
        name = predict
        dosage_forms = None
        start, end, dosage_forms, dosage_forms_db = self.search(predict)

        if dosage_forms:
            start, end, dosage_forms = self.get_full_dosage_forms(
                start, end, predict)

        if dosage_forms is not None:
            name = predict[:start].strip()
            if any(map(str.isdigit, predict[end:])):
                name += predict[end:]
            # dosage_forms = predict[start: end + 1]
        else:
            name = predict

        # if dosage_forms:
            # dosage_forms = dosage_forms.strip(',')
        return name.strip(','), dosage_forms_db

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



predict_files = "drug_and_dosage.txt"


def test():
    predict = []
    with open(predict_files, "r") as f:
        predicts = f.read().split('\n')

    # predicts = ["Trileptal Oral suspension 60 mg/ml", "Voltaren Modified-release tablet 75 mg"]
    # predicts = ['Zykadia Capsule, hard 150 mg']
    # predicts = ['Nutriflex peri, solution for infusion']

    # predicts = ['- Exforge Fim-coated Tablet 10/160 mg']

    sn = Splitter(dosage_info_path='dosage_info.yaml',
                  field_drug=[],
                  field_dosage=[])
    
    for predict in predicts:
        name, dosage_forms = sn.split_name(predict)
        print("Original: ", predict)
        print("Name: ", name)
        print("Dosage forms: ", dosage_forms)
        print()

test()
