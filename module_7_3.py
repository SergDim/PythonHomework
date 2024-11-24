
class WordsFinder:

    def __init__(self, *args):
        self.files = args

    def get_all_words(self):

        def replace(line):
            new_line = line.replace(",", " ")
            new_line = new_line.replace(".", " ")
            new_line = new_line.replace(":", " ")
            new_line = new_line.replace(";", " ")
            new_line = new_line.replace("?", " ")
            new_line = new_line.replace("!", " ")
            new_line = new_line.replace("=", " ")
            new_line = new_line.replace(" -", "  ")
            new_line = new_line.replace("\n", " ")
            return new_line.strip(" ")

        all_words = {}
        for file_name in self.files:
            list_worlds = []
            with open(file_name, mode = 'tr', encoding='utf-8') as file:
                for line in file:
                    list_worlds.extend(replace(line.lower()).split(' '))
            all_words.update({file_name : list_worlds})
        return all_words

    def find(self, word):
        find_words = {}
        w = word.lower()
        for key,value in self.get_all_words().items():
            for i in range(len(value)):
                if value[i] == w:
                    find_words.update({key : i+1})
                    break
        return find_words

    def count(self, word):
        count_words = {}
        w = word.lower()
        for key,value in self.get_all_words().items():
            count_words.update({key : value.count(w)})
        return count_words

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
