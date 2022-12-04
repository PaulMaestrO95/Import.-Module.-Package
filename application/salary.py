import os
from random import randint

def calculate_salary():
    print('Необходимо выплатить 1000000 рублей')
    file_path = os.path.join(os.getcwd(), 'data.txt')
    with open(file_path, 'w', encoding='utf-8') as f:
        random_choice = randint(1, 15)
        f.write(f'Премию получит работник с номером {random_choice} ')