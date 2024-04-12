import csv

MARKS_FILE_csv = 'marks2.csv'
ID_SUBJECTS_FILE_csv = 'id_subjects.csv'

def output_subject(subject):
    with open(ID_SUBJECTS_FILE_csv, 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([2, subject])
        # if not is_subject_in_lst(subject):
        #     file.write(f'{get_last_subject_id()+1}: {subject}\n')

def is_subject_in_lst(subject):
    return subject in lst_subject()

def lst_subject():
    return list(dct_subjects_with_id().keys())

def dct_subjects_with_id():
    with open(ID_SUBJECTS_FILE_csv, 'r', encoding='utf-8', newline='') as file:
        return dict(list(csv.reader(file, delimiter=','))[1:])

def get_last_subject_id():
    with open(ID_SUBJECTS_FILE_csv, 'r', encoding='utf-8', newline='') as file:
        rows = list(csv.reader(file))
        print(rows)
        if len(rows) == 1:
            pass

get_last_subject_id()

