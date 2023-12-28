"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    """
    This is a class that reads in a list of words from a text file (one word per line) and generates a list of the words in the file.
    It prints how many words it read in from the file and also offers functionality to return a random word from the file.
    """
    def __init__(self, path_to_file):
        """Initializes the WordFinder instance. It reads each word in the file specified in the relative path to the file 
        and adds each word to the word_list attribute. It then prints out how many words it read."""
        self.word_list = []
        self.read_file(path_to_file)
        self.print_words_read()
    
    def read_file(self, path_to_file):
        """It reads in the words at the file specified by the relative path path_to_file and appends each of the words it reads into
        the word_list attribute."""
        file_reader = open(path_to_file, 'r')
        for line in file_reader:
            trimmed_line = line.strip()
            self.word_list.append(trimmed_line)
        file_reader.close()
    
    def print_words_read(self):
        """Prints out how many words were read in the file."""
        word_list_len = len(self.word_list)
        print(f"{word_list_len} words read")
    
    def random(self):
        """Selects a random word from the list of words it read in from the file and returns it."""
        random_index = randint(0, len(self.word_list) - 1)
        return self.word_list[random_index]
