value_dosage_forms_file = "value_dosage_forms.txt"


class SplitDrugAndDosage:
    def __init__(self, value_dosage_forms_file="value_dosage_forms.txt", max_ratio=0.8):
        self.value_dosage_forms_file = value_dosage_forms_file      
        self.max_ratio = max_ratio  

        with open(value_dosage_forms_file, "r") as f:
            value_dosage_forms = f.read().split('\n')      
        
        self.value_dosage_forms = sorted(value_dosage_forms, key=lambda x: -len(x))
        self.low_value_dosage_forms = [dosage_forms.lower() for dosage_forms in self.value_dosage_forms]

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
        for dosage_forms in self.low_value_dosage_forms:
            low_predict = predict.lower()            
            start = low_predict.find(dosage_forms)           
            if  start != -1:
                return start, start + len(dosage_forms) - 1, dosage_forms    
        
        # Find Longest Common Subsequence      
        for dosage_forms in self.low_value_dosage_forms:
            low_predict = predict.lower()

            # Check again
            start, end, common_str = self.LCS(low_predict, dosage_forms)
            if len(common_str) / len(dosage_forms) > self.max_ratio:
                return start, end, predict[start : end + 1]                
            
        return -1, -1, None


    def get_full_dosage_forms(self, start, end, predict):        
        while start - 1 >= 0 and predict[start - 1].isalpha() and predict[start - 1] != " ":
            start -= 1
            
        while end + 1 <= len(predict) - 1 and not predict[end + 1].isdigit():
            end += 1
        
        return start, end, predict[start: end + 1]


    def split_name(self, predict):   
        name = predict
        dosage_forms = None 
        # if "," in predict:
        #     predict = re.compile("(?!\d)\,(?!\d)").split(predict)        
        #     name = predict[0].strip()
        #     predict = ", ".join(x.strip() for x in predict[1:])
            
        #     start, end, dosage_forms = self.search(predict)  
        #     if dosage_forms:      
        #         start, end, dosage_forms = self.get_full_dosage_forms(start, end, predict)
            
        #     before = predict[:start]
        #     after = predict[end:]
        #     if any(map(str.isdigit, after)):
        #         name += after   
                
        #     if not dosage_forms:
        #         start, end, dosage_forms = self.search(name)
        #         if dosage_forms:
        #             dosage_forms = name[start: end + 1]
        #             name = name[: start - 1]
                                    
        #         if predict:
        #             name += " " + predict
            
        # else:
        start, end, dosage_forms = self.search(predict) 
        
        if dosage_forms:
            start, end, dosage_forms = self.get_full_dosage_forms(start, end, predict)
        
        if dosage_forms is not None:      
            name = predict[:start].strip()
            if any(map(str.isdigit, predict[end:])):
                name += predict[end:]
            dosage_forms = predict[start : end + 1]
        else:
            name = predict
                
        if dosage_forms:
            dosage_forms = dosage_forms.strip(',')
        return name.strip(','), dosage_forms
                

predict_files = "drug_and_dosage.txt"
def test():
    predict = []
    with open(predict_files, "r") as f:
        predicts = f.read().split('\n')
    
    # predicts = ["Trileptal Oral suspension 60 mg/ml", "Voltaren Modified-release tablet 75 mg"]
    # predicts = ['Zykadia Capsule, hard 150 mg']
    # predicts = ['Nutriflex peri, solution for infusion']
    
    sn = SplitDrugAndDosage()
    for predict in predicts:
        name, dosage_forms = sn.split_name(predict)
        print("Original: ", predict)
        print("Name: ", name)
        print("Dosage forms: ", dosage_forms)
        print()

test()