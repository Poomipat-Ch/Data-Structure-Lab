n = [int(i) for i in input('Enter Your List : ').split()]
 
sum = []
li = []
if len(n) < 3:
   print("Array Input Length Must More Than 2")
else:
   for i in n: 
           for j in n:
               if i < j:   
                   for k in n:
                       if j < k:   
                           if i + j + k == 0 and  [i,j,k] not in sum and [j,i,k] not in sum and [k,j,i] not in sum and [k,i,j] not in sum and  [j,k,i] not in sum and  [i,k,j] not in sum:
                               sum.append([i,j,k])
   print(sum)

