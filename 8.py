def solution(left, right):
    answer = 0
    O = []
    for i in range(left, right+1):
        V = []
        for j in range(1, i+1):
            if i % j == 0:
                V.append(j)
        if len(V) % 2 == 0:
            O.append(i)
        else:
            O.append(-i)
        answer = sum(O)        
    return answer


solution(13,17)  