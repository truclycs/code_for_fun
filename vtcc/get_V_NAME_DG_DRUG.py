from pathlib import Path
from natsort import natsorted
import json


input_path = "/home/trucly/Documents/DATASET/VTCC/CPP/CPP_03062021"
output_path = "/home/trucly/Documents/PERSONAL/code_for_fun/vtcc"
label_paths = natsorted(Path(input_path).glob('**/*.json'), key=lambda x: x.stem)


for label_path in label_paths:
    f = open(label_path, "r")
    label = json.loads(f.read())        
    shapes = label["shapes"]
    for shape in shapes:
        if shape["label"] == "V_NAME_DG_DRUG":
            with open("value_V_NAME_DG_DRUG.txt", "a") as f:
                f.write(shape["value"] + '\n')
            print(shape["value"])
    