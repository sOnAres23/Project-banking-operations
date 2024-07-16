from src.find_transactions import find_transactions
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.readers import read_transactions_from_csv, read_transactions_from_xlsx
from src.utils import read_transactions_from_json
from src.widget import get_data, mask_account_card


def main():
    greeting_to_user = '''������! ����� ���������� � ��������� ������ � ����������� ������������. 
\n�������� ����������� ����� ����:
1. �������� ���������� � ����������� �� JSON-�����
2. �������� ���������� � ����������� �� CSV-�����
3. �������� ���������� � ����������� �� XLSX-�����'''
    input_user = input(f"{greeting_to_user}\n")

    while input_user not in ["1", "2", "3"]:
        print("\n�� ����� ������������ ������\n���������� ��� ���:")
        input_user = input()

    if input_user == "1":
        print("\n��� ��������� ������ JSON-����.")
        result = read_transactions_from_json("data/operations.json")  # ������� ������ json �������
    elif input_user == "2":
        print("\n��� ��������� ������ CSV-����.")
        result = read_transactions_from_csv("data/transactions.csv")  # ������� ������ csv �������
    elif input_user == "3":
        print("\n��� ��������� ������ XLSX-����.")
        result = read_transactions_from_xlsx("data/transactions_excel.xlsx")  # ������� ������ xlsx �������

    status_operation = '''\n������� ������, �� �������� ���������� ��������� ����������. 
    ��������� ��� ���������� �������: EXECUTED, CANCELED, PENDING.'''
    input_user_state = input(f"{status_operation}\n").upper()

    while input_user_state not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"\n������ �������� {input_user_state} ����������.\n{status_operation}")
        input_user_state = input().upper()

    if input_user_state == "EXECUTED":
        print('\n�������� ������������� �� ������� "EXECUTED"')
    elif input_user_state == "CANCELED":
        print('\n�������� ������������� �� ������� "CANCELED"')
    elif input_user_state == "PENDING":
        print('\n�������� ������������� �� ������� "PENDING"')

    result = filter_by_state(result, input_user_state)  # ������� ���������� �������� �� ������� "state"

    choice_data = '''\n������������� �������� �� ����? ��/���'''
    input_user_data = input(f"{choice_data}\n").lower()
    while input_user_data not in ["��", "���"]:
        print(f"\n����� ������������ ������.\n ���������� ��� ���:")
        input_user_data = input(f"{choice_data}\n").lower()

    else:
        if input_user_data == "��":
            next_choice_ascending = '''\n������������� �� ����������� ��� �� ��������?'''
            input_user_ascending = input(f"{next_choice_ascending}\n").lower()

            while input_user_ascending not in ["�� �����������", "�� ��������"]:
                print(f"\n����� ������������ ����������\n ���������� ��� ���:")
                input_user_ascending = input(f"{next_choice_ascending}\n").lower()

            else:
                if input_user_ascending == "�� ��������":
                    result = sort_by_date(result)  # ������� ��������� �������� �� ���� (�� ��������)
                elif input_user_ascending == "�� �����������":
                    result = sort_by_date(result, False)  # ��������� �������� �� ���� (�� �����������)

    choice_rub = '''\n�������� ������ �������� ���������? ��/���'''
    input_user_rub = input(f"{choice_rub}\n").lower()
    while input_user_rub not in ["��", "���"]:
        print(f"\n����� ������������ ����������\n ���������� ��� ���:")
        input_user_rub = input(f"{choice_rub}\n").lower()

    if input_user_rub == "��":
        result = filter_by_currency(result, "RUB")  # �������-���������
        # ��������� �������� �� "RUB" -> ���������� �� ����� ����������

    choice_word = '''\n������������� ������ ���������� �� ������������� ����� � ��������? ��/���'''
    input_user_word = input(f"{choice_word}\n").lower()
    while input_user_word not in ["��", "���"]:
        print(f"\n����� ������������ ����������\n ���������� ��� ���:")
        input_user_word = input(f"{choice_word}\n").lower()

    else:
        if input_user_word == "��":
            word_filter = input("\n������� ����� ��� ������:\n")

            if input_user_rub == "��":
                list_result = [r for r in [*result]]
                result = find_transactions([*result], word_filter)  # ������� ��������� ��������
                # �� ����� word_filter � �������� ��������
            else:
                result = find_transactions(result, word_filter)  # ������� ��������� ��������
                # �� ����� word_filter � �������� ��������

    print("������������ �������� ������ ����������...\n")
    print(f"����� ���������� �������� � �������: {len(result)}\n")

    if result is []:
        return "�� ������� �� ����� ����������, ���������� ��� ���� ������� ����������"
    else:
        for i in result:
            data = get_data(i["date"])
            description = i["description"]
            from_ = mask_account_card(i.get("from", ""))
            to_ = mask_account_card(i.get("to", ""))
            amount = i["operationAmount"]["amount"]
            name = i["operationAmount"]["currency"]["name"]

            print(f"{data} {description}\n{from_} -> {to_}\n�����: {amount} {name}\n")
    return 'finish'


if __name__ == "__main__":
    main()
