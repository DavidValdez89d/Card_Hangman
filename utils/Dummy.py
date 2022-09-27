word = ['d','a','v','i','d']
word_str = "".join(word)
used_letters = {'a','d'}
word_list = [letter if letter in used_letters else '_' for letter in "".join(word)]
print('Hangman: ', ' '.join(word_list))
print(word_str)