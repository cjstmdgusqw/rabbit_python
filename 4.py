a = 12345
b = list(str(a))
d = list(map(int,str(a)))[::-1] 

print(d)



def solution(num):
   num_reverse = list(map(int,str(num))) 
   return num_reverse

solution(12345)   