#onp.lo - All Rights Reserved.
#Build RC

import sys

def identify(t): #identyfikacja argumentow
    if(t=='¬' or t=="NOT" or t=='~'): #negacja
        return int(1)
    elif(t=='AND' or t=='&' or t=='∧'): #koniunkcja
        return int(2)
    elif(t=='OR' or t=='|' or t=='∨'): #alternatywa
        return int(2)
    elif(t=='IMPLIES' or t=='→'): #implikacja
        return int(2)
    elif(t=='IFF' or t=='↔'): #rownowaznosc
        return int(2)
    elif(t=='XOR' or t=='⊕'): #alternatywa wykluczajaca
        return int(2)
    elif(t=='FORALL' or t=='∀'): #kwantyfikator uniwersalny
        return int(2)
    elif(t=='EXISTS' or t=='∃'): #kwantyfikator egzystencjalny
        return int(2)
    elif(ord(t[0])>=97 and ord(t[0])<=101): #stala
        return int(0)
    elif(ord(t[0])>=65 and ord(t[0])<=90): #zmienna
        return int(0)
    elif(ord(t[0])>=102 and ord(t[0])<=110 and t[1]=='/'): #funkcja
        return int(t[2])
    elif(ord(t[0])>=112 and ord(t[0])<=122 and t[1]=='/'): #predykat
        return int(t[2])
    else: #cos nie tak
        return int(-1)

def translate(postfix, rstring=''): #interpretacja znak po znaku (rek.)
    if(len(postfix)==0):
        return rstring 
    else:
        char = postfix.pop() #'stos', hehe.
        args = identify(char)
        if(args==0): #zwraca wyraz wolny
            rstring+=char
            return rstring
        else:
            isFunction = False #inne formatowanie gdy p/f
            if(len(char)>1):
                if(char[1]=='/'): #usuwanie nadmiaru znakow
                    char = char[0]
                    isFunction = True
            order = []
            if(isFunction): 
                tmp = char+'('
            else:
                tmp = '('+char+' '
            for i in range(args):
                order.append(translate(postfix, rstring)) #wywolanie rekurencyjne
                if(isFunction):
                    order[i]+=', '
                else:
                    order[i]+=' '
            for i in range(len(order)-1, -1, -1):
                tmp+=order[i] #odwracanie kolejnosci argumentow
            if(isFunction):
                tmp=tmp[:-2]+')'
            else:
                tmp=tmp[:-1]+')'
            rstring+=tmp
            return rstring #zwrot tworu


tmp = input("Wprowadz wyrażenie: ") #tymczasowy kod do debugowania
tmp = tmp.split()
print("Postać infiksowa: ")
print(translate(tmp))

#for postfix in sys.stdin: 
#    print(translate(input().split())) #input zgodny z wytycznymi
