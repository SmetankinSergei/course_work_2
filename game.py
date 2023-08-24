from player import Player
from utils import load_random_word


def get_greeting_message(player, basic_word):
    """
    Создание приветственной строки
    """
    return f'''         Привет, {player.name}!
         Составьте 8 слов из слова {basic_word.main_word.upper()}
         Слова должны быть не короче 3 букв
         Чтобы закончить игру, угадайте все слова или напишите "stop"
         Поехали, ваше первое слово?\n--> '''


def end_game(player):
    """
    Метод конца игры
    """
    print(f'Игра завершена, вы угадали {len(player.player_words)} слов!')


def start_game(player, basic_word):
    """
    Метод игровой сессии
    """
    player_word = input(get_greeting_message(player, basic_word)).lower()
    while player_word != 'stop' and player.player_words_count() < 8:
        if len(player_word) < 3:
            print('слишком короткое слово')
        else:
            if basic_word.check_input_word(player_word):
                if player_word in player.player_words:
                    print('уже использовано')
                else:
                    player.add_word_in_player_words(player_word)
                    print('верно')
            else:
                print('неверно')
        if player.player_words_count() < 8:
            player_word = input('--> ').lower()
    end_game(player)


def prepare_to_game():
    """
    Метод подготовки к игре, получение имени игрока и случайного слова
    """
    start_game(Player(input('Введите имя игрока\n--> ')), load_random_word())


# старт программы
if __name__ == "__main__":
    prepare_to_game()
