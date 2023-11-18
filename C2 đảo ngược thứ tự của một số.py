n= int(input())

daoso= 0
while n != 0:
    chuso = n % 10
    daoso= daoso * 10 +  chuso  
    n //= 10
    
print(daoso)