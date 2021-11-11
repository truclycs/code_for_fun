input_dir = ''
output = ''
text_file = ''


with open(text_file, 'r') as f:
    files = f.read().split('\n')


for file in files:
    filename = ".".join(file.split('.')[:-1]) + '.txt'
    with open(filename, 'r') as f:
        label = f.read()

    with open(output, 'a') as f:
        f.write(filename + '\t' + label + '\n')
