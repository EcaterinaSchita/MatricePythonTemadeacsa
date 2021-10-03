A = [[1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]]
print('Suma primului rand este', sum(A[0]))
print('Suma randului doi este', sum(A[1]))    
print('Suma randului trei este', sum(A[2]))
print('Suma randului patru este', sum(A[3])) 
print('Suma randului cinci este', sum(A[5]))
coloana1=0
coloana2=0
coloana3=0
coloana4=0
coloana5=0
for i in A:
    coloana1+=i[0]
    coloana2+=i[1]
    coloana3+=i[2]
    coloana4+=i[3]
    coloana5+=i[4]
print('Suma primei coloane este', coloana1)
print('Suma coloanei doi este', coloana2)    
print('Suma coloanei trei este', coloana3)
print('Suma coloanei patru este', coloana4) 
print('Suma coloanei cinci este', coloana5)   
d= A[0][0]+A[1][1]+ A[2][2]+A[3][3]+A[4][4]
d1= A[0][4]+A[1][3]+ A[2][2]+A[3][1]+A[4][0]
print('Suma diagonalei principale este', d)
print('Suma diaonalei secundare este', d1)
