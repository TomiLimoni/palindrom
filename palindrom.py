def palindrom(word):
    return word == word[::-1]
print(palindrom(input('Введите строку: ')))