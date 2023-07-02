def palindrom(word):
    palindrom_word = word[::-1]
    if word == palindrom_word:
        print(True)
    else:
        print(False)
palindrom('лепсспел')
palindrom('helloworld')