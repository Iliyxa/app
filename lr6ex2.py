
def _split(string, deliter):
    mas = []
    word = ""
    s = spaces(string)
    for i in range(len(s)):
        if s[i] == deliter:
            mas += [word]
            word = ""
        elif s[i] not in ('.,' + deliter):
            word += s[i]
    if len(word) > 0:
        mas += [word]
    return mas
list_ = split_(string)
count = 0
for el in list_:
    if len(el) !=  0;
    count +=1
    print (f'Количество слов в данном тексте {count}')

def spaces(string): 
    i = 0
    while string[i] in (" "): 
         i +=1
    no_spaces = ''
    for j in range(i,len(string)):
        no_spaces += string[j]

    return no_spaces

while True:
    try:    
        text = input('Введите текст -> ')
        if len(spaces(text)) == 0:
            raise ValueError
        break
    except ValueError:
        print('Введенна пустая строка')
print(_split(text, " "))
print (f'Количество слов в данном тексте {len(_split(text, " "))}')
