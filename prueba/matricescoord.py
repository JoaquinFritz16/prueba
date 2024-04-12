def NumeroPrimo(matrix1):
    divisor=2
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            if(matrix1[i][j])%divisor==0:
                divisor+=1
                return NoPrimo
    return Primo

def SumValues(matrix1):
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            if NumeroPrimo(matrix1[i][j]) == NoPrimo:
                return NoPrimo
            else:
                matrix1[i][j]+=matrix1[i][j]
matrix1=[[2,3, 10],[4,5,6],[7,8,9]]
Primo='Primo'
NoPrimo='NoPrimo'
NumeroPrimo(matrix1)
SumValues(matrix1)
