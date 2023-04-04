# Your task is to sort a given string. Each word in the string will contain a single number. 
# This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. 
# The words in the input String will only contain valid consecutive numbers.


def order(sentence):
    word_list = sentence.split(' ');
    new_string = []
    for i in range(1, len(word_list)+1):
        for word in word_list:
            if str(i) in word:
                new_string.append(word)
    
    return " ".join(new_string)