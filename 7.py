# 일단 이진법으로 변환하는법 알기
n = 30
b = bin(n)[2:]
c = list(map(int, str(b)))


arr = [9 ,20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

A = []
for i in range(0,5):
    V = []
    a = bin(arr[i])[2:].zfill(5)
    b = bin(arr2[i])[2:].zfill(5)
    # print(a)
    
    a_list = list(map(int, str(a)))
    b_list = list(map(int, str(b)))
    

    for j in range(0,5):
            
        if a_list[j] + b_list[j] >= 1:
            V.append('#')
        else:
            V.append('')
    result = ''.join(map(str, V))
    A.append(result)
print(A)
        

        