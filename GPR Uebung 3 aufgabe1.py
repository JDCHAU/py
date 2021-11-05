__author__ = "S1317331,Jiadong Zhou"
#GPR Aufgabe 1
# a // 2 = b      rest = c
# a = b recursive rest = d ... until b == 1 (condition) 
#binary digit[b,c,d] (reverse) 
"""
Pseudocode
Algo:
number <- Input()
a = int(number)
b initial
Store_List initial
if <a == 0>:
    Store_List[0]
else:
    Store_List[] # empty list
while<>:
    a // 2 = b  b quotient
    a % 2 = c   c is rest, append to the list
    a <- b      recursive
    if<a == 1>:
        should end and 1 ist the last elemnt in list
    else:
        do nothing 
reverse list
print
"""   
number = input("input a number\n")
a = int(number)    
b = 0
Store_List = [0] if a==0 else []
while a // 2 >= 1:
    b = a // 2 
    c = a % 2 
    Store_List.append(c)
    a = b
    if a == 1:
        Store_List.append(1)
        Store_List.reverse()   
    else:
        pass
print(Store_List[::])
