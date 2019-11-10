#onp.lo - All Rights Reserved.
#Build Release 1.0

def identify(t): #identyfikacja argumentow i typu
    if(t=='¬' or t=="NOT" or t=='~'): #negacja
        return [int(1), 'negation'] 
    elif(t=='AND' or t=='&' or t=='∧'): #koniunkcja
        return [int(2), 'operator']
    elif(t=='OR' or t=='|' or t=='∨'): #alternatywa
        return [int(2), 'operator'] 
    elif(t=='IMPLIES' or t=='→'): #implikacja
        return [int(2), 'operator']
    elif(t=='IFF' or t=='↔'): #rownowaznosc
        return [int(2), 'operator']
    elif(t=='XOR' or t=='⊕'): #alternatywa wykluczajaca
        return [int(2), 'operator']
    elif(t=='FORALL' or t=='∀'): #kwantyfikator uniwersalny
        return [int(2), 'quantifier']
    elif(t=='EXISTS' or t=='∃'): #kwantyfikator egzystencjalny
        return [int(2), 'quantifier']
    elif(ord(t[0])>=97 and ord(t[0])<=101): #stala
        return [int(0), 'value']
    elif(ord(t[0])>=65 and ord(t[0])<=90): #zmienna
        return [int(0), 'value']
    elif(ord(t[0])>=102 and ord(t[0])<=110 and t[1]=='/'): #funkcja
        return [int(t[2]), 'pf']
    elif(ord(t[0])>=112 and ord(t[0])<=122 and t[1]=='/'): #predykat
        return [int(t[2]), 'pf']
    else: #cos nie tak
        return [int(-1), '']

def translate(postfix, rstring=''): #interpretacja znak po znaku (rek.)
    if(len(postfix)==0):
        return rstring 
    else:
        char = postfix.pop() #'stos', hehe.
        assign = identify(char)
        args = assign[0]
        typeOf = assign[1]
        if(args==0): #zwraca wyraz wolny
            rstring+=char
            return rstring
        else:
            order = []
            if(typeOf=='pf'): #formatowanie funkcji lub predykatu
                char = char[0]
                tmp = char+'('
                for i in range(args):
                    order.append(translate(postfix, rstring)) #wywolanie rekurencyjne
                    order[i]+=', '
            elif(typeOf=='operator'): #formatowanie operatorów
                tmp = '('
                order.append(translate(postfix, rstring)+' ')
                order.append(translate(postfix, rstring)+' '+char+' ')
            else:
                tmp = '('+char+' '
                for i in range(args):
                    order.append(translate(postfix, rstring)) #wywolanie rekurencyjne
                    order[i]+=' '
            for i in range(len(order)-1, -1, -1):
                tmp+=order[i] #odwracanie kolejnosci argumentow
            if(typeOf=='pf'):
                tmp=tmp[:-2]+')'
            else:
                tmp=tmp[:-1]+')'
            rstring+=tmp
            return rstring #zwrot tworu

while(True):
    print(translate(input().split())) #input zgodny z wytycznymi
