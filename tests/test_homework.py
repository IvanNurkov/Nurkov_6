import pytest
from main import city_of_russia, max_tv, unique_id, creat_folder

FIXTERE_1 = [
    ([{'visit1': ['Москва', 'Россия']}, {'visit2': ['Дели', 'Индия']}],
     [{'visit1': ['Москва', 'Россия']}]),
    ([{'visit1': ['Москва', 'Россия']}, {'visit2': ['Санкт - Петербург', 'Россия']}],
     [{'visit1': ['Москва', 'Россия']}, {'visit2': ['Санкт - Петербург', 'Россия']}]),
    ([{'visit1': ['Vladymir', 'Россия']}, {'visit2': ['Берлин', 'Германия']}], [{'visit1': ['Vladymir', 'Россия']}])
]

FIXTERE_2 = [
    ({'vk': 4, 'google': 6, 'yahoo': 4}, 'google'),
    ({'isq': 8, 'git': 5, 'instagram': 6}, 'isq')
]

FIXTERE_3 = [
    ({'user1': [213, 213, 213, 15, 213], 'user2': [54, 54, 119, 119, 119]}, [213, 15, 54, 119]),
    ({'user1': [1, 3, 3, 54], 'user2': [1, 1, 1, 1]}, [1, 3, 54]),
    ({'user1': [-4, 85, 9], 'user2': [5, 10, 17]}, [-4, 85, 9, 5, 10, 17])

]

FIXTERE_4 = [
    ('Папка1', 201),
    ('Папка на задание', 409)
]

@pytest.mark.parametrize('geo_log, result', FIXTERE_1)
def test_city_of_russia(geo_log, result):
    res = city_of_russia(geo_log)
    assert res == result

@pytest.mark.parametrize('stats, result', FIXTERE_2)
def test_max_tv(stats, result):
    res = max_tv(stats)
    assert res == result

@pytest.mark.parametrize('ids, result', FIXTERE_3)
def test_unique_id(ids, result):
    res = unique_id(ids)
    assert set(res).issubset(result) and set(result).issubset(res)

@pytest.mark.parametrize('name_of_folder, status', FIXTERE_4)
def test_create_folder(name_of_folder, status):
    result = creat_folder(name_of_folder)
    assert result == status