import shutil
from pathlib import Path


file_predict = 'data/process_data/error_case/test_word_224.txt'
s_folder = Path('/home/trucly/Documents/DATASET/HANDWRITTEN/completed/vnondb/word')
e_folder = Path('/home/trucly/Documents/DATASET/HANDWRITTEN/completed/wrong_case_train_word')


text = []
with open(file_predict, 'r') as f:
    lines = f.read()
    lines = lines.split('\n')
    for line in lines:
        # print(line)
        file, gt, pre = line.split('\t')      
        file = file.split('/')[-1]
        
        if gt.lower() != pre.lower():        
            text.append(line)
            shutil.copy(s_folder.joinpath(file), e_folder.joinpath(file))
        
        
text = sorted(text)
text_output = 'text_sorted.txt'
with open(e_folder.joinpath(text_output), 'w') as f:
    for t in text:
        f.write(t + '\n')