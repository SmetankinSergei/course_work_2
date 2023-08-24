class BasicWord:
    def __init__(self, words_dict):
        self.main_word = words_dict['word']
        self.sub_words = words_dict['sub_words']

    def __repr__(self):
        """
        Решил не усложнять и вернуть имя класса и главное слово
        """
        return f'Basic word - {self.main_word}'

    def check_input_word(self, word):
        """
        Проверяем, если введённое слово в sub_words
        """
        return word in self.sub_words

    def sub_words_count(self):
        """
        По заданию этот метод должен быть, как я понял - для того, чтобы определить, сколько слов нужно угадать.
        Но в задании же на примере показано, что sub_words больше, чем требуется ответов, как можно догадаться,
        для того, чтобы дать игроку возможность пройти раунд, потому что под_слов может быть гораздо больше.
        Поэтому я оставил как в задании - 8
        """
        return len(self.sub_words)
