import os
import xlsxwriter


class BaseReport:
    def __init__(self, output_dir=''):
        self.output_dir = output_dir

    def add_worksheet(self, *args, **kwargs):
        pass

    def append_header(self, *args, **kwargs):
        pass

    def append_data(self, *args, **kwargs):
        pass

    def save(self, data, file_name):
        output_path = os.path.join(self.output_dir, file_name + ".xlsx")
        workbook = xlsxwriter.Workbook(output_path)
        worksheet = self.add_worksheet(workbook=workbook)
        self.append_data(data=data, workbook=workbook, worksheet=worksheet)
        workbook.close()
        return output_path
