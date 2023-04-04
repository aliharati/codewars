# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case). 
# The next words should be always capitalized.

def to_camel_case(text):
    text = text.replace('_','-')
    word_list = text.split('-')
    for i in range(1,len(word_list)):
        try:
            word_list[i] = word_list[i][0].upper() + word_list[i][1:]
        except:
            break;
    return ''.join(word_list)