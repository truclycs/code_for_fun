from torch.utils.data import dataset


val = 'dataset/vnondb/word/val.txt'
with open(val, 'r') as f:
    data = f.read().split('\n')
    for line in data:
        if 'ƒ' in line:
            print(line)