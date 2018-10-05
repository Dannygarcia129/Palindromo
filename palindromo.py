__author__ = 'Daniel Garcia Alonso'
def Palindromo(input):
    inputB = input
    input = input[::-1]

    noPalindrome = inputB + " no es palindromo"
    esPalindrome = inputB + " si es palindromo"

    if input[0]!= input[-1]:
        print (noPalindrome)
    else:
        print (esPalindrome)



print = (Palindromo('ya ay ya ay'))



