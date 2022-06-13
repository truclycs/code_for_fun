import datetime

from .base import BaseReport
from .verify import Verification


class GeneralReport(BaseReport):
    workbook = None
    worksheet = None
    freeze_panel_row = 1
    freeze_panel_col = 1
    is_verification = 0
    header_format = {
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#366092',
        'color': '#ffffff'
    }
    leftside_format = {
        'bold': 1,
        'border': 1,
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#538DD5',
        'color': '#ffffff'
    }
    data_format = {
        'file_name': {'header': 'file_name', 'size': 30, 'index': 0, 'type': 'str'},
        'field_name': {'header': 'field_name', 'size': 20, 'index': 1, 'type': 'str'},
        'type': {'header': 'type', 'size': 10, 'index': 2, 'type': 'str'},
        'ocr': {'header': 'AI_OCR', 'size': 30, 'index': 3, 'type': 'str'},
        'label': {'header': 'LABEL', 'size': 30, 'index': 4, 'type': 'str'},
    }
    default_col_height = 50

    def __init__(self, output_dir=None, is_appending_date=False, is_appending_img=True):
        super().__init__()
        if output_dir:
            self.output_dir = output_dir

        self.cur_datetime = ''
        if is_appending_date:
            self.cur_datetime = datetime.datetime.now().strftime("%Y%m%d")
        self.is_appending_img = is_appending_img

    def add_worksheet(self, workbook, sheet_name="report"):
        worksheet = None
        if workbook:
            worksheet = workbook.add_worksheet(name=sheet_name)
        return worksheet

    def append_header(self, workbook=None, worksheet=None):
        # Freeze table
        worksheet.freeze_panes(self.freeze_panel_row, self.freeze_panel_col)
        general_format = workbook.add_format()
        general_format.set_text_wrap(True)
        worksheet.set_default_row(self.default_col_height)
        cell_format = workbook.add_format(self.header_format)

        for key, item in self.data_format.items():
            worksheet.set_column(item['index'], item['index'], item['size'])
            worksheet.write(0, item['index'], item['header'], cell_format)

    def append_data(self, workbook=None, worksheet=None, data=[]):
        if worksheet:
            self.append_header(workbook, worksheet)
            # Set data to row
            for index, item in enumerate(data):
                for key_name in item.keys():
                    if key_name in self.data_format.keys():
                        if self.data_format[key_name]['index'] in [0]:
                            cell_format = workbook.add_format(self.leftside_format)
                        else:
                            cell_format = None

                        worksheet.write_string(
                            index + 1, self.data_format[key_name]['index'],
                            str(item[key_name]), cell_format
                        )

    def verify(self, excel_file, attributes=('file_name', 'field_name'), is_strip=False, is_normalize=False):
        verification = Verification()
        output_file = excel_file.replace('.xlsx', '_verified.xlsx')
        verification.run(excel_file, output_file, attributes=attributes, strip=is_strip, normalize=is_normalize)

    def save(self, data, file_name: str):
        file_name = f'{self.cur_datetime}_{file_name}'
        excel_file = super().save(data, file_name)
        if self.is_verification:
            self.verify(excel_file)
        return excel_file
