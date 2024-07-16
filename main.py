from src.find_transactions import find_transactions
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.readers import read_transactions_from_csv, read_transactions_from_xlsx
from src.utils import read_transactions_from_json
from src.widget import get_data, mask_account_card


def main():
    greeting_to_user = '''Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
\nВыберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла'''
    input_user = input(f"{greeting_to_user}\n")

    while input_user not in ["1", "2", "3"]:
        print("\nВы ввели некорректный символ\nПопробуйте еще раз:")
        input_user = input()

    if input_user == "1":
        print("\nДля обработки выбран JSON-файл.")
        result = read_transactions_from_json("data/operations.json")  # Функция чтения json формата
    elif input_user == "2":
        print("\nДля обработки выбран CSV-файл.")
        result = read_transactions_from_csv("data/transactions.csv")  # Функция чтения csv формата
    elif input_user == "3":
        print("\nДля обработки выбран XLSX-файл.")
        result = read_transactions_from_xlsx("data/transactions_excel.xlsx")  # Функция чтения xlsx формата

    status_operation = '''\nВведите статус, по которому необходимо выполнить фильтрацию. 
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.'''
    input_user_state = input(f"{status_operation}\n").upper()

    while input_user_state not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"\nСтатус операции {input_user_state} недоступен.\n{status_operation}")
        input_user_state = input().upper()

    if input_user_state == "EXECUTED":
        print('\nОперации отфильтрованы по статусу "EXECUTED"')
    elif input_user_state == "CANCELED":
        print('\nОперации отфильтрованы по статусу "CANCELED"')
    elif input_user_state == "PENDING":
        print('\nОперации отфильтрованы по статусу "PENDING"')

    result = filter_by_state(result, input_user_state)  # Функция фильтрации операций по статусу "state"

    choice_data = '''\nОтсортировать операции по дате? Да/Нет'''
    input_user_data = input(f"{choice_data}\n").lower()
    while input_user_data not in ["да", "нет"]:
        print(f"\nВвели некорректный символ.\n Попробуйте еще раз:")
        input_user_data = input(f"{choice_data}\n").lower()

    else:
        if input_user_data == "да":
            next_choice_ascending = '''\nОтсортировать по возрастанию или по убыванию?'''
            input_user_ascending = input(f"{next_choice_ascending}\n").lower()

            while input_user_ascending not in ["по возрастанию", "по убыванию"]:
                print(f"\nВвели некорректную сортировку\n Попробуйте еще раз:")
                input_user_ascending = input(f"{next_choice_ascending}\n").lower()

            else:
                if input_user_ascending == "по убыванию":
                    result = sort_by_date(result)  # функция сортирует операции по дате (по убыванию)
                elif input_user_ascending == "по возрастанию":
                    result = sort_by_date(result, False)  # сортирует операции по дате (по возрастанию)

    choice_rub = '''\nВыводить только рублевые тразакции? Да/Нет'''
    input_user_rub = input(f"{choice_rub}\n").lower()
    while input_user_rub not in ["да", "нет"]:
        print(f"\nВвели некорректную сортировку\n Попробуйте еще раз:")
        input_user_rub = input(f"{choice_rub}\n").lower()

    if input_user_rub == "да":
        result = filter_by_currency(result, "RUB")  # Функция-генератор
        # фильтрует операции по "RUB" -> возвращает по одной транзакции

    choice_word = '''\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет'''
    input_user_word = input(f"{choice_word}\n").lower()
    while input_user_word not in ["да", "нет"]:
        print(f"\nВвели некорректную фильтрацию\n Попробуйте еще раз:")
        input_user_word = input(f"{choice_word}\n").lower()

    else:
        if input_user_word == "да":
            word_filter = input("\nВведите слово для поиска:\n")

            if input_user_rub == "да":
                list_result = [r for r in [*result]]
                result = find_transactions([*result], word_filter)  # функция фильтрует операции
                # по слову word_filter в описании операции
            else:
                result = find_transactions(result, word_filter)  # функция фильтрует операции
                # по слову word_filter в описании операции

    print("Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(result)}\n")

    if result is []:
        return "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
    else:
        for i in result:
            data = get_data(i["date"])
            description = i["description"]
            from_ = mask_account_card(i.get("from", ""))
            to_ = mask_account_card(i.get("to", ""))
            amount = i["operationAmount"]["amount"]
            name = i["operationAmount"]["currency"]["name"]

            print(f"{data} {description}\n{from_} -> {to_}\nСумма: {amount} {name}\n")
    return 'finish'


if __name__ == "__main__":
    main()
