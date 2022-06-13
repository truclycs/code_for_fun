from pathlib import Path


file_predict = 'data/process_data/error_case/test_trainword.txt'
train_file = '/home/trucly/Documents/DATASET/HANDWRITTEN/completed/annotation/word/train_edited.txt'
target_file = '/home/trucly/Documents/DATASET/HANDWRITTEN/completed/annotation/word/train_edit.txt'


files = []
with open(file_predict, 'r') as f:
    lines = f.read()
    lines = lines.split('\n')
    for line in lines:
        file, gt, pre = line.split('\t')      
        file = file.split('/')[-1]
        files.append(file)
        
   
text = []     
with open(train_file, 'r') as f:
    lines = f.read()
    lines = lines.split('\n')
    for line in lines:
        file, val = line.split('\t')      
        if file in files:
            continue  
        else:
            text.append(line)
            
        
text = sorted(text)
# text_output = 'text_sorted.txt'
with open(target_file, 'w') as f:
    for t in text:
        f.write(t + '\n')