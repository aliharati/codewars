# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    if ord(text[-1]) > 63 and ord(text[-1])<122:
        lst = text.split(' ')
        punct =''
    else:
        if text[-2] == " ":
            punct = " " + text[-1]
        else:
            punct = text[-1]
        lst = text[:-1].split(' ')
    
    _str = ' '.join([word[1:] + word[0] + 'ay' for word in lst if word !='' ]) + punct
    return _str