# convert Excel datasheets with emails to csv
# import numpy as np
import pandas as pd
import os.path


# import csv
from PyQt5.QtWidgets import QMessageBox


def convert_bd(file):
    for i in file:

        name = i.rpartition('/')[2]  # prepare a proper name for the output file
        name = name[:name.find(".") + 0]
        duplicate_name = i.rpartition('/')[0]
        duplicate_name += i.rpartition('/')[1]

        sheets = pd.ExcelFile(i)  # get sheets' names
        sheet_names = sheets.sheet_names
        lists_amount = len(sheet_names)
        flag = 0

        while flag <= lists_amount:  # check each sheet of the file one by one
            check = pd.read_excel(i, sheet_names[flag])
            cols = check.columns.values  # get column names
            cur_sheet_name = sheet_names[flag]

            needed_col = []
            for col_val in cols:  # if there is no column name for email's row, saves the first email
                col_val = str(col_val)
                if "@" in col_val:
                    needed_col.append(col_val)

            check_values = check.values.tolist()
            tmp_mails = []
            mails = []

            for lst in check_values:  # i just wanted separate lists
                tmp_mails.extend(lst)

            for elem in tmp_mails:  # get all the emails from the current sheet
                elem = str(elem)
                if "@" in elem:
                    mails.append(elem)

            mails_frame = pd.DataFrame(mails)  # save emails as a frame of pandas data

            try:
                if mails_frame.empty and not needed_col:
                    print(f'{cur_sheet_name} is empty!')
                    pass
                else:
                    if os.path.isfile(f'{duplicate_name}{cur_sheet_name}.csv'):  # if there is a file with the same name
                        print("there is a duplicate")
                        print(duplicate_name)
                        mails_frame.to_csv(f'{duplicate_name}{name}{cur_sheet_name}.csv', header='email', index=None)

                        fix = pd.read_csv(f'{name}{cur_sheet_name}.csv')
                        new_header = ['email']
                        fix.to_csv(f'{name}{cur_sheet_name}.csv', index=False, header=new_header)
                        print(f'successfully written from {cur_sheet_name}')

                        if needed_col:  # if there was an email in column's name - adds it to the end of csv
                            print("fix for a duplicate needed")
                            mails.append(''.join(needed_col))
                            mails_frame = pd.DataFrame(mails)
                            mails_frame.to_csv(f'{name}{cur_sheet_name}.csv', header='email', index=None)
                            fix = pd.read_csv(f'{name}{cur_sheet_name}.csv')
                            new_header = ['email']
                            fix.to_csv(f'{name}{cur_sheet_name}.csv', index=False, header=new_header)
                            print(f'successfully fixed {cur_sheet_name}')

                    if not os.path.isfile(f'{duplicate_name}{cur_sheet_name}.csv'):
                        print("there is no duplicate")
                        mails_frame.to_csv(f'{duplicate_name}{cur_sheet_name}.csv', header='email', index=None)
                        fix = pd.read_csv(f'{duplicate_name}{cur_sheet_name}.csv')

                        new_header = ['e-mail']
                        fix.to_csv(f'{duplicate_name}{cur_sheet_name}.csv', index=False, header=new_header)
                        print(f'successfully written from {cur_sheet_name}')

                        if needed_col:  # if there was an email in column's name - adds it to the end of csv
                            print('needed fix')
                            mails.append(''.join(needed_col))
                            mails_frame = pd.DataFrame(mails)
                            mails_frame.to_csv(f'{duplicate_name}{cur_sheet_name}.csv', header='email', index=None)
                            fix = pd.read_csv(f'{duplicate_name}{cur_sheet_name}.csv')
                            new_header = ['email']
                            fix.to_csv(f'{duplicate_name}{cur_sheet_name}.csv', index=False, header=new_header)
                            print(f'successfully fixed {cur_sheet_name}')


            except:
                if needed_col:  # if there was an email in column's name - adds it to the end of csv
                    print('needed fix in except')
                    mails.append(''.join(needed_col))
                    mails_frame = pd.DataFrame(mails)
                    mails_frame.to_csv(f'{duplicate_name}{cur_sheet_name}.csv', header='email', index=None)
                    fix = pd.read_csv(f'{duplicate_name}{cur_sheet_name}.csv')
                    new_header = ['email']
                    fix.to_csv(f'{duplicate_name}{cur_sheet_name}.csv', index=False, header=new_header)

                else:
                    print(f"there are no emails on sheet {cur_sheet_name}, or another error")
                pass
            flag += 1
            if flag == lists_amount:
                return True


if __name__ == '__main__':
    convert_bd()
