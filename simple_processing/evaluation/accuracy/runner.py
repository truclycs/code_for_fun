import os
import sys
import argparse
from pathlib import Path
from natsort import natsorted

import utils

sys.path.append(os.environ['PWD'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--label-dir', default='scripts/data/output/labels/')
    parser.add_argument('--pred-dir', default='scripts/data/output/predictions/')
    parser.add_argument('--pattern', default='**/*.json')
    args = parser.parse_args()

    evaluator = utils.eval_config(config='accuracy/config.yaml')['doc_evaluator']

    pred_paths = natsorted(Path(args.pred_dir).glob(args.pattern), key=lambda x: x.stem)
    label_paths = natsorted(Path(args.label_dir).glob(args.pattern), key=lambda x: x.stem)
    evaluator(label_paths, pred_paths)
