import json
import datetime


def load_data():
    with open("src/operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_mask_number_card(number: str) -> str:
    """ Возвращает маску номера карты в формате XXXX XX** **** XXXX

        :param number: номер карты
        :return: замаскированный номер карты
    """
    if len(number) != 16:
        # return 'Некорректный номер. Введите номер снова.'
        raise ValueError('Некорректный номер. Введите номер снова.')
    return number[:4] + " " + number[4:6] + "**" + " " + "****" + " " + number[-4:]


def get_mask_number_bill(number: str) -> str:
    """ Возвращает маску номера счёта в формате **XXXX

        :param number: номер счёта
        :return: замаскированный номер счёта
    """

    if len(number) != 20:
        # return 'Некорректный номер. Введите номер снова.'
        raise ValueError('Некорректный номер. Введите номер снова.')
    return "**" + number[-4:]


def get_mask_deposit(deposit: str) -> str:
    """ принимает на вход строку с информацией тип карты/счета и номер карты/счета
        возвращает эту строку с замаскированным номером карты/счета.

        :param deposit: строка с название карты/счета и номером карты/счета
        :return: строка с маскированным по правилу номером карты/счета
    """

    # список, полученный из строки, переданной в функцию
    deposit_list = deposit.strip().split()

    if deposit_list[0].startswith('Счет'):
        return deposit_list[0] + ' ' + get_mask_number_bill(deposit_list[1])
    elif len(deposit_list) == 2 and not deposit_list[0].startswith('Счет'):
        return deposit_list[0] + ' ' + get_mask_number_card(deposit_list[1])
    else:
        return deposit_list[0] + ' ' + deposit_list[1] + ' ' + get_mask_number_card(deposit_list[2])
    

def get_date_formatting(str_date: str) -> str:
    """ Функция преобразования строки с датой в строку формата дд.мм.гггг

        :param str_date: строка, содержащая дату
        :return: строка с датой в виде "дд.мм.гггг"
    """

    return datetime.datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S.%f').strftime('%d.%m.%Y')


def get_list_dictionary_by_key(list_dictionaries: list, state: str = 'EXECUTED') -> list:
    """
    Функция принимает на вход список словарей и значение для ключа "state" и возвращает список,
    содержащий только те словари, у которых ключ state содержит переданное в функцию значение.
    :param list_dictionaries: список словарей
    :param state: значение для ключа state, по умолчанию = EXECUTED
    :return: список словарей, содержащий ключ со значением аргумента state
    """
    result_list = [item for item in list_dictionaries if item["state"] == state]
    return result_list


def get_list_dictionaries_sorted(list_dictionaries: list, sort_order: bool = True) -> list:
    """
    Функция принимает на вход список словарей и возвращает новый список, в котором исходные словари отсортированы
    по убыванию даты (ключ date). Функция принимает два аргумента, второй необязательный задает порядок сортировки
    (убывание, возрастание)
    :param list_dictionaries: список словарей
    :param sort_order: порядок сортировки, по умолчанию = True
    :return: список отсортированных словарей
    """
    sorted_dictionaries = sorted(list_dictionaries, key=lambda dictionary: dictionary['date'], reverse=sort_order)
    return sorted_dictionaries
