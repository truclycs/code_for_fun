# data_address_dir = '/home/trucly/Documents/DATASET/hw_collect/original_text_for_hw/address/new_add.txt'
# data_common_dir = '/home/trucly/Documents/DATASET/hw_collect/original_text_for_hw/common/new_common.txt'
# data_company_name_dir = '/home/trucly/Documents/DATASET/hw_collect/original_text_for_hw/company_name/new_comp.txt'
# data_name_dir = '/home/trucly/Documents/DATASET/hw_collect/original_text_for_hw/name/new_name.txt'
data_name_card_dir = '/home/trucly/Documents/DATASET/hw_collect/original_text_for_hw/name_card/new_namecard.txt'
output_dir = '/home/trucly/Documents/DATASET/hw_collect/text_files/'

START_IDX = 1000
MOD = 10


def get_data(data_path):
    with open(data_path, "r") as f:
        data = f.read()
    return data.split('\n')


# if __name__ == '__main__':
#     address = get_data(data_address_dir)
#     common = get_data(data_common_dir)
#     company_name = get_data(data_company_name_dir)
#     name = get_data(data_name_dir)
#     name_card = get_data(data_name_card_dir)

#     cnt = 0
#     textlines = []
#     for add, comm, comp, name, card in zip(address, common, company_name, name, name_card):
#         cnt += 1
#         textlines.append(add)
#         textlines.append(comm)
#         textlines.append(comp)
#         textlines.append(name)
#         textlines.append(card)

#         if cnt % 2 == 0:
#             file_path = output_dir + str('%04d' % (cnt // 2)) + '.txt'
#             with open(file_path, "w") as f:
#                 for textline in textlines:
#                     f.write(textline + '\n')
#             textlines = []

if __name__ == '__main__':
    name_card = get_data(data_name_card_dir)

    cnt = 0
    idx = START_IDX

    textlines = []
    for card in name_card:
        cnt += 1

        textlines.append(card)

        if cnt == MOD:
            file_path = output_dir + str('%04d' % idx) + '.txt'
            with open(file_path, "w") as f:
                for textline in textlines:
                    f.write(textline + '\n')
            textlines = []
            cnt = 0
            idx += 1
