def palindrom(word):
    palindrom_word = word[::-1]
    return word == palindrom_word
print(palindrom('лепсспел'))
print(palindrom('helloworld'))
