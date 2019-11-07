#onp.lo - All Rights Reserved.
import sys
for postfix in sys.stdin: #nieskonczona petla 
    postfix = postfix.strip().split() 
    for i in range(len(postfix)-1, -1, -1): #odczytywanie wyrazow postfixa od konca
        
        #todo: bufor operacji/przestrzen  nazw/interpretacja (rekurencja?)
        
        
