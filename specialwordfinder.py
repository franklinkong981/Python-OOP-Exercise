"""SpecialWordFinder: Finds random words in a text file on a line that isn't blank NOR starts with a #."""
from random import randint
from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """
    This is a class that reads in a list of words from a text file (one word per line) and generates a list of the words in the file.
    HOWEVER, it does not read in any lines that start with a # nor does it read in blank lines.
    It prints how many words it read in from the file and also offers functionality to return a random word from the file.

    >>> special_word_finder = SpecialWordFinder("fruits_and_veggies.txt")
    6 words read

    >>> special_word_finder.random() in special_word_finder.word_list
    True

    >>> special_word_finder.random() in special_word_finder.word_list
    True

    >>> special_word_finder.random() in special_word_finder.word_list
    True

    """
    def __init__(self, path_to_file):
        """Initializes the SpecialWordFinder by calling the constructor of the WordFinder class. The only difference is that 
        when read_file is called, the SpecialWordFinder's read_file method will be called which makes some adjustments."""
        super().__init__(path_to_file)
    
    def read_file(self, path_to_file):
        """Opens the file at the relative path path_to_file and reads each line.
        IF the line isn't blank and it isn't a comment (doesn't start with '#') then it adds it to the word_list attribute."""
        file_reader = open(path_to_file, 'r')
        for line in file_reader:
            trimmed_line = line.strip()
            if trimmed_line and trimmed_line[0] != '#':
                self.word_list.append(trimmed_line)
        file_reader.close()
    