def toList(string):   #парсим строку в массив целых чисел
    split_value = []
    number = ''
    for c in string:
        if c == '.':
            split_value.append(int(number))
            number = ''
        else:
            number += c
    if number:
        split_value.append(int(number))
    return split_value

def tooLongStr(str1, length):  #если длина одной строки больше длины другой, проверяем, на продолжается ли она одними нулями
    i = length-1               #например, в случе версий 12.3.0.14.0.0.0 и 12.3.0.14 версии будут идентичны
    while i<len(str1):
        if str1[i]!=0:
            return '.'.join(str(number) for number in str1)
        else: 
            if i<len(str1)-1:
                i+=1
                continue
            else:
                return "Версии идентичны"

def whoIsYounger(str1, str2):
    firstApp = toList(str1)
    secondApp = toList(str2)
    if len(firstApp)>len(secondApp):
        length = len(secondApp)
    else:
        length = len(firstApp)
    i = 0
    while i<length:
        if firstApp[i]==secondApp[i]:
            i+=1
            continue
        elif firstApp[i]>secondApp[i]:
            return str1
        else:
            return str2
    if len(firstApp)==len(secondApp):
        return "Версии идентичны"
    else:
        if len(firstApp)>len(secondApp):
            return tooLongStr(firstApp, length)
        else:
            return tooLongStr(secondApp, length)

firstApplication = input("Введите номер версии первого приложения: ")
secondApplication = input("Введите номер второго приложения: ")
print("Какая версия новее: ")
print(whoIsYounger(firstApplication, secondApplication))
                
        