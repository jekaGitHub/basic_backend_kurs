import pytest

from src.utils import (get_mask_number_card, get_mask_number_bill, get_list_dictionary_by_key,
                       get_list_dictionaries_sorted, get_mask_deposit, get_date_formatting)


@pytest.mark.parametrize("number, expected", [("1234567834627910", "1234 56** **** 7910"),
                                              ("9876990045613477", "9876 99** **** 3477"),
                                              ("0055678932216996", "0055 67** **** 6996"),
                                              ("", "Некорректный номер. Введите номер снова.")
                                              ])
def test_get_mask_number_card(number, expected):
    assert get_mask_number_card(number) == expected


@pytest.mark.parametrize("number, expected", [("12345678346279109845", "**9845"),
                                              ("56789876990045613477", "**3477"),
                                              ("65670055678932214321", "**4321"),
                                              ("", "Некорректный номер. Введите номер снова.")
                                              ])
def test_get_mask_number_bill(number, expected):
    assert get_mask_number_bill(number) == expected


@pytest.fixture
def list_dictionary():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def test_get_list_dictionary_by_key(list_dictionary):
    assert get_list_dictionary_by_key(list_dictionary) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


def test_get_list_dictionaries_sorted(list_dictionary):
    assert get_list_dictionaries_sorted(list_dictionary) == [{'id': 41428829, 'state': 'EXECUTED',
                                             'date': '2019-07-03T18:35:29.512364'},
                                            {'id': 615064591, 'state': 'CANCELED',
                                             'date': '2018-10-14T08:21:33.419441'},
                                            {'id': 594226727, 'state': 'CANCELED',
                                             'date': '2018-09-12T21:27:25.241689'},
                                            {'id': 939719570, 'state': 'EXECUTED',
                                             'date': '2018-06-30T02:08:58.425572'}]


@pytest.mark.parametrize("deposit, expected", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                               ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                                               ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                                               ("Счет 64686473678894779589", "Счет **9589")
                                               ])
def test_get_mask_deposit(deposit, expected):
    assert get_mask_deposit(deposit) == expected


