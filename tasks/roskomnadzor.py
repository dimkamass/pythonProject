alpha = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
         'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# word=input()
word = 'роскомнадзор'

stroka = f'{word} запретил букву'
for i in alpha:
    if i in stroka:
        print(stroka, i)
    stroka = stroka.replace(i, "")
    stroka = stroka.strip()
    if '  ' in stroka:
        stroka = stroka.replace('  ', ' ')
