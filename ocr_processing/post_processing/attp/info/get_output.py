from pathlib import Path
from natsort import natsorted
import json


input_path = "info/output"
output_path = "info"
reuslt_paths = natsorted(Path(input_path).glob('**/*.json'), key=lambda x: x.stem)


for result_path in reuslt_paths:
    f = open(result_path, "r")
    result = json.loads(f.read())

    value = ""
    if 'name_analyst_center' in result:
        value = result['name_analyst_center']

    if "name_analyst_center_normal" in result and result['name_analyst_center_normal'] != '':
        value = value + ' ' + result['name_analyst_center_normal']

    output = str(result_path) + '\t' + value + '\n'
    with open('output.txt', 'a') as file:
        file.write(output)
