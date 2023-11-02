import re
import json
import wget
import argparse
from pathlib import Path


def no_accent_vietnamese(s):
    s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
    s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
    s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
    s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
    s = re.sub(r'[ìíịỉĩ]', 'i', s)
    s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
    s = re.sub(r'[ùúụủũưừứựửữ]', 'u', s)
    s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
    s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
    s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
    s = re.sub(r'[Đ]', 'D', s)
    s = re.sub(r'[đ]', 'd', s)
    s = re.sub(r'[-]', ' ', s)
    return s


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='List the content of a folder')
    parser.add_argument('--file-path', metavar='name_file', type=str, help='the path to list')
    parser.add_argument('--output-dir', type=str)
    parser.add_argument('--separator', default='#', help='Using specific separator to split each information parts of data')
    parser.add_argument('--merge-file', action='store_true', help='True: merge all in each sub folder into folder \
                                                                   False: divide folder into many sub folders')
    parser.add_argument('--remove-parent', action='store_true', help='True: move parent of file, just keep file name for metadata of json \
                                                                      False: remain current name of file path for metadata of json')
    parser.add_argument('--splited-field', help='using value of field to save json, image file based on data type')
    parser.add_argument('--web-site', type=str, default="http://tagging-ocr.vtcc.ai/")
    args = parser.parse_args()

    output_dir = Path(args.output_dir) if args.output_dir else Path(args.file_path).parent

    folder = output_dir.joinpath(Path(args.file_path).stem)
    if not folder.exists():
        folder.mkdir(parents=True)

    with open(file=args.file_path, mode='r', encoding='utf-8') as f:
        data_infos = f.readlines()

    saved_file, failed_file = 0, 0

    for data_info in data_infos:
        file_id, _, url_path, json_data = data_info.split(args.separator)  # split info of line into many infos

        sub_folder = folder.joinpath(file_id) if not args.merge_file else folder
        if not sub_folder.exists():
            sub_folder.mkdir(parents=True)

        image_path = sub_folder.joinpath(Path(url_path).name)
        label_path = sub_folder.joinpath(Path(url_path).stem).with_suffix('.json')
        if args.web_site not in url_path:
            url_path = args.web_site + url_path

        if (not label_path.exists()) or (not image_path.exists()):
            try:
                json_data = json.loads(json_data)  # convert json_data with string type to json_data with dictionary type

                if args.splited_field:
                    value_field = 'OTHERS'
                    for shape in json_data['shapes']:
                        if shape['label'] == args.splited_field:
                            value_field = no_accent_vietnamese(shape.get('value', value_field))
                            break
                    splited_sub_folder = sub_folder.joinpath(value_field)
                    if not splited_sub_folder.exists():
                        splited_sub_folder.mkdir(parents=True)
                    image_path = splited_sub_folder.joinpath(image_path.name)
                    label_path = splited_sub_folder.joinpath(label_path.name)

                if args.remove_parent:
                    json_data['imagePath'] = Path(json_data['imagePath']).name if len(json_data.get('imagePath', '')) != 0 else image_path.name

                wget.download(str(url_path), str(image_path))  # download image file from url path and then save to image_path
                with open(file=str(label_path), mode='w', encoding='utf-8') as fp:  # save data of json file to label_path
                    json.dump(json_data, fp, ensure_ascii=False, indent=4)

                saved_file += 1

            except Exception as e:
                print(f'\n ERROR: {e}')
                failed_file += 1

    print('\n', '*' * 50)
    print(f' Total files needed to download:{len(data_infos)}')
    print(f' Number of downloaded files: {saved_file} file')
    print(f' Number of failed files: {failed_file} file')
