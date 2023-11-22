
def spaces(string): #Функция удаления пробелов перед строкой
    i = 0
    while string[i] in (" "): # изменяем i-й элемент до того момента пока не встретим символ
            i +=1
    no_spaces = ''
    for j in range(i,len(string)): #создаём новую строку без пробелов
        no_spaces += string[j]
    print(no_spaces)
    return no_spaces

while True:
    try:    
        text = input('Введите текст -> ')
        if len(spaces(text)) == 0:#если у нас строка без пробелов равна нулю то следовательно пустая
            raise SyntaxError
        break
    except:
        print('Введенна пустая строка')

numbers = '0123456789'

count_alf = 0
count_numbers = 0
for i in range(len(text)):
    if text[i] not in numbers:
        count_alf += 1
    elif text[i] in numbers:
        count_numbers += 1
if count_numbers > count_alf:
    print('В данном тексте больше цифр чем букв')
elif count_alf == count_numbers:
    print('В данном тексте количесво цифр и букв равно')
else:
    print('В данном тексте больше букв чем цифр')
