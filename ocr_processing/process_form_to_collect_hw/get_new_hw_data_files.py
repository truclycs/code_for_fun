data_address_dir = '/home/trucly/Documents/DATASET/hw_collect/original_text_for_hw/address/'
data_common_dir = '/home/trucly/Documents/DATASET/hw_collect/original_text_for_hw/common/'
data_company_name_dir = '/home/trucly/Documents/DATASET/hw_collect/original_text_for_hw/company_name/'
data_name_dir = '/home/trucly/Documents/DATASET/hw_collect/original_text_for_hw/name/'
data_name_card_dir = '/home/trucly/Documents/DATASET/hw_collect/original_text_for_hw/name_card/'

MIN_LEN_STRING = 3
MAX_LEN_STRING = 15


def get_data(data_path):
    with open(data_path, "r") as f:
        data = f.read()
    return data.split('\n')


def check_limit_string(s):
    s = s.split(' ')
    return MIN_LEN_STRING <= len(s) <= MAX_LEN_STRING


def create_new_file_data(data, filename):
    with open(filename, 'w') as f:
        for line in data:
            if check_limit_string(line):
                f.write(line + '\n')


if __name__ == '__main__':
    address = get_data(data_address_dir + 'add.txt')
    common = get_data(data_common_dir + 'common.txt')
    company_name = get_data(data_company_name_dir + 'comp.txt')
    name = get_data(data_name_dir + 'name.txt')
    name_card = get_data(data_name_card_dir + 'namecard.txt')

    create_new_file_data(address, data_address_dir + 'new_add.txt')
    create_new_file_data(common, data_common_dir + 'new_common.txt')
    create_new_file_data(company_name, data_company_name_dir + 'new_comp.txt')
    create_new_file_data(name, data_name_dir + 'new_name.txt')
    create_new_file_data(name_card, data_name_card_dir + 'new_namecard.txt')
