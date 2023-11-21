
def _split(string, deliter):
    mas = []
    word = ""
    s = spaces(string)
    for i in range(len(s)):
        if s[i] == deliter:
            mas += [word]
            word = ""
        elif s[i] not in ('.,'+ deliter):
            word += s[i]
    if len(word) > 0:
        mas += [word]
    return mas

def spaces(string): #Функция удаления пробелов перед строкой
    i = 0
    while string[i] in (" "): # изменяем i-й элемент до того момента пока не встретим символ
            i +=1
    no_spaces = ''
    for j in range(i,len(string)): #создаём новую строку без пробелов
        no_spaces += string[j]

    return no_spaces

while True:
    try:    
        text = input('Введите текст -> ')
        if len(spaces(text)) == 0:
            raise SyntaxError
        break
    except:
        print('Введенна пустая строка')
print(_split(text, " "))
print (f'Количество слов в данном тексте {len(_split(text, " "))}')
