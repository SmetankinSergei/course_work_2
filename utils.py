import requests
from random import randint
from basic_word import BasicWord


def load_random_word():
    """
    Получение случайного слова
    """
    data = get_game_data()
    game_data = get_game_data()[randint(0, len(data) - 1)]
    return BasicWord(game_data)


def get_game_data():
    """
    Получение данных для игры
    """
    return requests.get('https://www.jsonkeeper.com/b/JY14').json()
