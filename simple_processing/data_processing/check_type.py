import json
import shutil
import argparse
from pathlib import Path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("data_dir", type=str)
    parser.add_argument("--image-patterns", type=str, nargs="+")
    parser.add_argument("--output-dir", type=str, default="output/")
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    output_dir = Path(args.output_dir)

    image_paths = []
    for image_pattern in args.image_patterns or ["**/*.png", "**/*.jpg", "**/*.jpeg"]:
        image_paths += list(data_dir.glob(image_pattern))

    path_pairs = [(path, path.with_suffix(".json")) for path in image_paths
                  if path.with_suffix(".json")]

    for image_path, label_path in path_pairs:
        with open(label_path) as f:
            data = json.load(f)

        copy_stamp_regions = list(filter(lambda x: x["label"] == "COPY_STAMP", data["shapes"]))
        if len(copy_stamp_regions):
            flags = dict(origin=False, verification=True, photo=False)
        else:
            flags = dict(origin=False, verification=False, photo=True)

        data["flags"] = flags

        output_path = output_dir.joinpath(image_path.relative_to(data_dir))
        if not output_path.parent.exists():
            output_path.parent.mkdir(parents=True)
        shutil.copy(image_path, output_path)
        with open(output_path.with_suffix(".json"), "w") as f:
            f.write(json.dumps(data, indent=4))