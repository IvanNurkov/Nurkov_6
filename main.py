import requests


def city_of_russia(geo_logs):
    result_list = []
    for visit in geo_logs:
        if 'Россия' in list(visit.values())[0]:
            result_list.append(visit)
    return result_list

def unique_id(ids):
    new_id = []
    for id in ids.values():
        for id_1 in id:
            new_id.append(id_1)
            un_id = set(new_id)
            un_id_list = list(un_id)
    return un_id_list

def max_tv(stats):
    namber = max(stats.values())
    for name, vol in stats.items():
        if vol == namber:
            return name

def test1():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]

    city_of_russia(geo_logs)

    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    unique_id(ids)

    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

    max_tv(stats)


def creat_folder(name_of_folder):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    token = ''
    params = {'path': name_of_folder, 'overwrite': 'True'}
    headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(token)}
    result_ = requests.put(url, headers=headers, params=params)
    status = result_.status_code
    return status




if __name__ == '__main__':
    test1()
    name_of_folder = 'Папка на задание'
    result = creat_folder(name_of_folder)
