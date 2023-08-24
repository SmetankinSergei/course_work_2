class Player:
    def __init__(self, name):
        self.name = name
        self.player_words = []

    def __repr__(self):
        """
        Вывожу имя класса и игрока
        """
        return f'Player - {self.name}'

    def player_words_count(self):
        """
        Подсчёт корректно введённых слов
        """
        return len(self.player_words)

    def add_word_in_player_words(self, word):
        """
        Добавление корректно введённого слова в список
        """
        if not self.check_word_usage(word):
            self.player_words.append(word)

    def check_word_usage(self, word):
        """
        Проверка - использовалось слово или нет
        """
        return word in self.player_words
