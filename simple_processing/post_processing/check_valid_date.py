import re
import datetime


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
    return s


def extract_datetime(input_str: str, debug=False):
    str = no_accent_vietnamese(input_str).lower()
    str = re.sub(r'[^a-z0-9]', '', str)
    if debug:
        print(f"Input str: {input_str}\nStr: {str}")
    patterns = [
        # exactly full
        [r'.*ngay(\d{1,2})thang(\d{1,2})nam(\d{1,4}).*', r'\1/\2/\3'],
        # exactly but miss day/month/year
        [r'.*ngay(\d{1,2})thang(\d{1,2})nam.*', r'\1/\2/None'],
        [r'.*ngay(\d{1,2})thangnam(\d{1,4}).*', r'\1/None/\2'],
        [r'.*ngaythang(\d{1,2})nam(\d{1,4}).*', r'None/\1/\2'],
        # exactly but miss two field
        [r'.*ngaythangnam(\d{1,4}).*', r'None/None/\1'],
        [r'.*ngay(\d{1,2})thangnam.*', r'\1/None/None'],
        [r'.*ngaythang(\d{1,2})nam.*', r'None/\1/None'],
        # error one char per field [1]
        [r'.*(nga.|ng.y|n.ay|.gay)(\d{1,2})(than.|tha.g|th.ng|t.ang|.hang)(\d{1,2})(na.|n.m|.am)(\d{1,4}).*', r'\2/\4/\6'],
        # [1] but miss day/month/year
        [r'.*(nga.|ng.y|n.ay|.gay)(than.|tha.g|th.ng|t.ang|.hang)(\d{1,2})(na.|n.m|.am)(\d{1,4}).*', r'None/\3/\5'],
        [r'.*(nga.|ng.y|n.ay|.gay)(\d{1,2})(than.|tha.g|th.ng|t.ang|.hang)(na.|n.m|.am)(\d{1,4}).*', r'\2/None/\5'],
        [r'.*(nga.|ng.y|n.ay|.gay)(\d{1,2})(than.|tha.g|th.ng|t.ang|.hang)(\d{1,2})(na.|n.m|.am).*', r'\2/\4/None'],
    ]
    for pattern in patterns:
        if re.match(pattern[0], str) is not None:
            if debug:
                print('Match pattern:', pattern)
            return re.sub(pattern[0], pattern[1], str)
    return None


def check_valid(date_time: str):
    '''
    date_time: None/None/None
    '''
    is_valid = True
    if date_time is None:
        is_valid = False
    elif 'None' in date_time:
        is_valid = False
    else:
        try:
            day, month, year = date_time.split('/')
            datetime.date(int(year), int(month), int(day))
        except ValueError:
            is_valid = False
    return is_valid


# class CheckValidDate:
#     def __init__(self, date_input=None):
#         self.date_input = date_input        
    
#     def keep_numchar(self, string):
#         return ''.join(c for c in string if c.isdigit() or c.isalpha())

#     def get_date(self, date_input):
#         tmp = date_input[0]
#         for i in range(1, len(date_input)):
#             if date_input[i] == '.' and date_input[i - 1] == '.':
#                 continue
#             else:
#                 tmp += date_input[i]    
#         date_input = [self.keep_numchar(item) for item in (' '.join(tmp.split('.')).split())]
        
#         first_num = -1
#         last_num = -1
#         for i in range(len(date_input)):
#             if len(date_input[i]) > 5:
#                 if first_num == -1:
#                     first_num = i        
#                 last_num = i
#             elif date_input[i].isdecimal():
#                 if first_num == -1:
#                     first_num = i
#                 last_num = i                
#         date_input = date_input[first_num: last_num + 1] + ["end"]
        
#         num = ""
#         date = []
#         for item in date_input:
#             if item.isdecimal():
#                 num += item
#             else:
#                 date.append(num)
#                 num = ""                
#                 if len(item) <= 5:            
#                     date.append(item)
#                 else:
#                     split = re.findall('\d+|\D+', item)
#                     date += split          
                    
#         return date[:-1]

#     def split_date(self, date_input):   
#         date_input = self.get_date(date_input)
#         date_output = {"day": "",
#                        "month": "",
#                        "year": ""}             
        
#         idx = -1
#         for item in date_input[::-1]:
#             if item == "":
#                 continue
#             elif item.isdecimal():
#                 if len(item) == 4:
#                     date_output['year'] = item
#                     idx += 1
#                 elif idx == 1:
#                     date_output['month'] = item
#                 elif idx == 2:
#                     date_output['day'] = item
#             elif date_output["year"] != "":
#                 idx += 1
        
#         return date_output

#     def check_valid_date(self, date):
#         date = self.split_date(date)
#         is_valid = all(date.values())
#         if is_valid:
#             day, month, year = date['day'], date['month'], date['year']
#             try:
#                 datetime.date(int(year), int(month), int(day))
#                 is_valid = True
#             except ValueError:
#                 is_valid = False        
#         return is_valid, date
    
    
# if __name__ == '__main__':
#     tests = ['ng6y...1han7.0.2.nam .2018.',
#         "Hà nội ngay12tháng03năm2012",
#         "TP.HCM. ngày 12. tháng .03 năm 2012.",
#         "Hà nội ngày 12 tháng 03 năm 2012., được cấp theo",
#         "Giấy phép có hiệu lực từ ngày 12 tháng 03 năm 2012",
#         "Giấy phép có hiệu lực từ ngày 12 tháng 03 năm 2012, được cấp theo",
#         "Hà nội ngày 0.5... tháng 0.3 năm 2012",
#         "TP.HCM. ngày .2.1. tháng .03 năm 2012.",
#         "Hà nội ngày 12 tháng 03 năm 2012., được cấp theo",
#         "Giấy phép có hiệu lực từ ngày .. tháng 03 năm 2012",
#         "Giấy phép có hiệu lực từ ngày 12 tháng ... năm 2012, được cấp theo",
#         "Hà nội ngàv 0.5... tháno 0.3 năm 2012",
#         "TP.HCM. ngàv .2.1. tháno .03 năm 2012.",
#         "Hà nội ngàv 12 tháno 03 năm 2012., được cấp theo",
#         "Giấy phép có hiệu lực từ ngàv .. tháno 03 năm 2012",
#         "Giấy phép có hiệu lực từ ngàv 12 tháno ... năm 2012, được cấp theo",
#         "Giấy phép có hiệu lực từ ngàv 32 tháno ... năm 2012, được cấp theo",
#         "ngày 12 tháng 03 năm 2048 năm 21. Của bộ trường bộ y tế",
#         "ngay4thang4nam2021",
#         "ngay.27.thang.5.nam2021",
#         " ngay.27.thang5 nam 2021",
#         "ngay27thang 05nam2021.",
#         "ng4y27thang05 nam 2021"
#         ]
#     check = CheckValidDate()
#     for date in tests:
#         print(check.check_valid_date(date))      