import  sys
arr = []
arr = map(int,raw_input().strip().split(' '))

for i in xrange(len(arr)-2):
        lista =  map(int,raw_input().strip().split(' '))
        for j in xrange(len(arr)):
                arr[i] += lista[j]
print arr
