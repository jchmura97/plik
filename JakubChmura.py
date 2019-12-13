print('Zadanie nr.1')

list_to_sort=[[3,2,3],[2,0,2],[3,0,1]]
print('lista przed sortowaniem: ',list_to_sort)

list_to_sort.sort(key=lambda x:(x[1],x[2]))
print('lista po sortowaniu: ',list_to_sort)


print('Zadanie nr.2')
password='informatyka'
attempts=5

while attempts>0:
    ans=input('Podaj hasło: ')
    if ans==password:
        print('Gratulacje! Udało się.')
        break
    else:
        continue
    attempts=attempts-1
    if attempts==0:
        print('Nie udało się odgadnąć hasła :(')


print('Zadanie nr.3')
from random import randint
a_list=[randint(0,3000) for element in range(1000000)]

import time 

start_time1=time.time()
if -1 in a_list:
        print('found')
print(time.time()-start_time1)
    

start_time2=time.time()
for num in a_list:
    if num==-1:
        print(num)
print(time.time()-start_time2)
    

start_time3=time.time()
if -1 not in a_list:
    pass
else:
    print('found')
print(time.time()-start_time3)

start_time4=time.time()
counter=len(a_list)-1
while counter>0:
    if a_list[counter]==-1:
        print(a_list[counter])
    counter=counter-counter
print(time.time()-start_time4)


print('Zadanie nr.4')

names=['Damian', 'Ola', 'Barbara', 'Robert', 'Zygmunt', 'Ewa']
let_array=[element[0] for element in names]

print(let_array)

