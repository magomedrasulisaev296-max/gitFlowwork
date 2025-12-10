from src.utils import load_transactions
from src.files_loaders import read_csv_file, read_excel_file
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.project_1 import process_bank_search
from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card

def main():
    user_input = input('''Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
ввод:''')
    while True:
        if user_input == '1':
            print("выбранный файл для обработки: JSON-файл")
            dict_ = load_transactions("data/transactions.json")
            break
        elif user_input == '2':
            print("выбранный файл для обработки: CSV-файл")
            dict_ = read_csv_file("data/transactions.csv")
            break
        elif user_input == '3':
            print("выбранный файл для обработки: XLSX-файл")
            dict_ = read_excel_file("data/transactions_excel.xlsx")
            break
        else:
            user_input = input("проверьте ваш ввод он должен быть 1, 2 или 3. ввод:")
    while True:
        user_input = input('''Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
ввод:''').upper()
        if user_input in ('EXECUTED', 'CANCELED', 'PENDING'):
            dict_ = filter_by_state(dict_, user_input)
            print(f"Операции отфильтрованы по статусу {user_input}")
            break
        else:
            print(f"Статус операции {user_input} недоступен.")
    user_input = input('''Отсортировать операции по дате? Да/Нет
ввод:''').lower()
    if user_input == "да":
        while True:
            user_input = input('''Отсортировать по возрастанию или по убыванию?
ввод:''').lower()
            if user_input == "по возрастанию":
                dict_ = sort_by_date(dict_)
                break
            elif user_input == "по убыванию":
                dict_ = sort_by_date(dict_, reverse = False)
                break
            else:
                print("проверьте правильность написания условия 'по возрастанию' или 'по убыванию'")
    user_input = input('''Выводить только рублевые транзакции? Да/Нет
ввод:''').lower()
    if user_input == "да":
        dict_ = list((filter_by_currency(dict_, "RUB")))
    user_input = input('''Отфильтровать список транзакций по определенному слову в описании? Да/Нет
ввод:''').lower()
    if user_input == "да":
        user_input = input('''введи слово для фильтрации:''')
        dict_ = process_bank_search(dict_, user_input)
    print("Распечатываю итоговый список транзакций...")
    print(f'''
всего операций в выборке: {len(dict_)}''')
    for i in dict_:
        print(f'''{i["date"]} {i["description"]}
{i["from"]} -> {i["to"]}
сумма: {i["amount"]}{i["currency_code"]}''')

main()