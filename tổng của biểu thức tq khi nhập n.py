
n=0
sa=0
sb=1
n=int(input())
for x in range(1,n+1):
    sa+=x**2
print(f'{sa:.3f}')

for y in range(1,n+1):
    sb+=1/(y*(y+1))
print(f'{sb:.3f}')