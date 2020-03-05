def int_to_roman(N:int) -> str:
    val = [1000, 900, 500, 400,100, 90, 50, 40, 10, 9, 5, 4, 1]
    rn = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    rns = ''
    i = 0
    while N > 0:
        for _ in range(N // val[i]):
            rns += rn[i]
            N -= val[i]
        i += 1
    return rns

def roman_to_int(S:str) -> int:
    rv = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}
    N = 0
    for i in rv:
        j = 0
        while j > -1:
            j = S.find(i,0,len(i))  # Шукаемо зліва послідовності
            if j>-1:
                #print(' Строка ',S,' найден символ ', i, ' позиция  ', j,' длина ',len(i))
                S = S[len(i):]  # Обрізаємо строку на символ числа
                N += rv[i]        
    return N

def roman_sum(first_number: str, second_number: str) -> str:
    
    return int_to_roman(roman_to_int(first_number)+roman_to_int(second_number))

X1 = 253
X2 = 747
S1 = int_to_roman(X1)
S2 = int_to_roman(X2)
XS = roman_sum(S1,S2)
print (" Сума ", X1," + ", X2," дорівнює ", X1 + X2)
print (" Сума ", S1," + ", S2," дорівнює ", XS)
print (" Перевірка: ",XS, " у десятковому вигляді повино дорівнювати ", roman_to_int(XS))
