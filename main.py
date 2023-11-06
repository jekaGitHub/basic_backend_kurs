from src.utils import load_data, get_mask_deposit, get_date_formatting, get_list_dictionary_by_key, \
    get_list_dictionaries_sorted

if __name__ == '__main__':
    # загрузка данных из файла operations.json
    data_list = load_data()

    # получение списка выполненных (EXECUTED) операций
    executed_operations_list = get_list_dictionary_by_key(data_list)
    #
    # фильтруем полученный список по дате (по убыванию)
    list_by_date = get_list_dictionaries_sorted(executed_operations_list)

    # забираем только последние 5 операций из списка операций
    list_five_operations = list_by_date[:5]

    # выводим необходимые данные построчно из сформированного списка операций
    for item in list_five_operations:
        print(f'{get_date_formatting(item["date"])} {item["description"]}')
        print(f'{get_mask_deposit(item.get("from", "Нет данных"))} -> {get_mask_deposit(item.get("to"))}')
        print(f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}')
        print("")
