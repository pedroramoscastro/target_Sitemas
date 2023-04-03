def inverte(s):
    if len(s) == 0:
        return s
    else:
        return inverte(s[1:]) + s[0]
 
 
s =str(input("Digite a palavra a ser invertida:"))
 
print("A string original é : ", end="")
print(s)
 
print("A string invertida é: ", end="")
print(inverte(s))