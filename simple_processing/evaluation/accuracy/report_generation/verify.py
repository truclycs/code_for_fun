import torch
import string
import unicodedata
import numpy as np
import pandas as pd
import editdistance as ed


AI_OCR = 'AI_OCR'
LABEL = 'LABEL'
COMMON_ATTRIBUTES = ('file_name', 'field_name')

TRUE_OR_FALSE = 'true_or_false'
OCR_LETTERS = 'OCR letters'
NUMBER_OF_LETTERS = 'Number of letters'
CORRECT_LETTERS = 'Correct letters'

COMMON_COLUMN = (TRUE_OR_FALSE, OCR_LETTERS)
EXPECTED_COLUMN = {'FL': (NUMBER_OF_LETTERS, CORRECT_LETTERS, *COMMON_COLUMN)}
ALL_OUTPUT_COLUMNS = (NUMBER_OF_LETTERS, CORRECT_LETTERS, *COMMON_COLUMN)


class Verification:
    def __init__(self):
        self.strip = False
        self.normalize = False

    def _preprocess_value(self, string):
        if self.normalize:
            string = unicodedata.normalize('NFKC', string)

        if self.strip:
            string = string.strip()

        return string

    def _compare_gt_and_pred(self, df):
        predict = self._preprocess_value(str(df[self.AI_OCR]))
        target = self._preprocess_value(str(df[self.label]))

        distance = torch.tensor(ed.distance(predict, target))
        char_correct = len(target) - distance

        return len(target), char_correct, predict == target, len(predict)

    def _set_color_false_field(self, writer, sheet_name, df_field, df):
        workbook = writer.book
        worksheet = writer.sheets[sheet_name]
        tmp = string.ascii_uppercase[df.columns.get_loc('true_or_false')]
        worksheet.conditional_format(f'{tmp}1:{tmp}{len(df_field) + 1}',
                                     {'type': 'text',
                                      'criteria': 'containing',
                                      'value': 'F',
                                      'format': workbook.add_format({'bg_color': 'red'})})

    def _accuract_pivot(self, dftable, index='type'):
        if index in dftable.columns:
            # count total field for each data_type
            df_total_field = pd.pivot_table(dftable,
                                            index=index,
                                            values=NUMBER_OF_LETTERS,
                                            aggfunc=len
                                            ).rename(index=str, columns={NUMBER_OF_LETTERS: 'Total field'})
            if df_total_field.empty:
                df_total_field.insert(loc=0, column='Total field', value=0)
            # count total true field for each data_type
            df_crr_field = pd.pivot_table(dftable,
                                          index=index,
                                          values='true_or_false',
                                          aggfunc=lambda x: sum(x == 'T')
                                          ).rename(index=str, columns={TRUE_OR_FALSE: 'Correct field'})
            if df_crr_field.empty:
                df_crr_field.insert(loc=0, column='Correct field', value=0)
            # count total (correct) letter for each data_type
            df_letters = pd.pivot_table(dftable,
                                        index=index,
                                        values=[NUMBER_OF_LETTERS, CORRECT_LETTERS, OCR_LETTERS],
                                        aggfunc=np.sum
                                        ).rename(index=str,
                                                 columns={
                                                     NUMBER_OF_LETTERS: 'Total CA letters',
                                                     OCR_LETTERS: 'Total OCR letters'
                                                 })

            df_all = pd.concat((df_total_field, df_crr_field, df_letters), axis=1)

            df_all['Accuracy by field (%)'] = round((df_all['Correct field'] / df_all['Total field']) * 100, 2)

            df_all['Accuracy by letter (%)'] = round(
                df_all[CORRECT_LETTERS] / (df_all['Total CA letters'] + df_all['Total OCR letters']) * 200, 2)

            return df_all

        else:
            return None

    def run(self, file_input, file_output, ocr=AI_OCR, ca=LABEL,
            attributes=COMMON_ATTRIBUTES, strip=False, normalize=False):
        self.AI_OCR = ocr
        self.label = ca
        self.strip = strip
        self.normalize = normalize

        df = pd.read_excel(file_input, converters={self.AI_OCR: str, self.label: str, **{_: str for _ in attributes}})
        df.fillna('', inplace=True)
        df1 = df.loc[:, attributes]

        if self.AI_OCR in df.columns:
            df1[self.AI_OCR] = df[self.AI_OCR]
            df1[self.label] = df[self.label]
            if strip:
                df1[self.AI_OCR] = df1[self.AI_OCR].apply(lambda x: x.strip())
            for i, column in enumerate(zip(*df1.apply(self._compare_gt_and_pred, axis=1))):
                df1[ALL_OUTPUT_COLUMNS[i]] = column

        writer = pd.ExcelWriter(file_output, engine='xlsxwriter')

        if self.AI_OCR in df.columns:
            col_idx = df.columns.get_loc(self.label) + 1
            for i, column in enumerate(EXPECTED_COLUMN["FL"]):
                df.insert(loc=col_idx + i, column=column, value=df1[column])
            df.to_excel(writer, sheet_name='result', index=False)

            for attribute in attributes:
                df[attribute] = df1[attribute]

            self._set_color_false_field(writer, 'result', df[TRUE_OR_FALSE], df)

            for attribute in attributes:
                res = self._accuract_pivot(df, attribute)
                if res is not None:
                    res.to_excel(writer, sheet_name='accuracy_by_' + attribute.replace(' ', '_'))
        writer.save()
        return True, None
