""" if input word is palindrome
        :return this word

    if input word isnt palindrome but if will change two near letters and it will be palindrome
        -:return modified word

    else: return 'can't change'

"""


def PalindromeSwapper(strParam):
    if strParam == strParam[::-1]:
        return strParam[::-1]
    else:
        for i in range(len(strParam) - 1):
            list_of_elem = list(strParam)
            list_of_elem[i], list_of_elem[i + 1] = list_of_elem[i + 1], list_of_elem[i]
            new_line = ''
            for j in list_of_elem:
                new_line += j
            if new_line == new_line[::-1]:
                return new_line

    return 'cant change'


# keep this function call here
print(PalindromeSwapper(input()))
