import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def check_document(document):
    validation = True
    required_fileds = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for field in required_fileds:
        if field + ':' not in document:
            validation = False
            break

    return validation


if __name__ == '__main__':

    file_name = 'zadanie 2 - plik wejsciowy.txt'
    file_path = os.path.join(BASE_DIR, file_name)

    with open(file_path, "r") as f:
        documents = f.read()

    documents = re.split(r'(?:\r?\n){2,}', documents)

    documents_ok = 0
    documents_nok = 0

    for document in documents:
        if check_document(document):
            documents_ok += 1
        else:
            documents_nok += 1

    print('In file exist {} documents whose is ok'.format(documents_ok))
