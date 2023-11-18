def nhap_du_lieu():
    n=int(input('so nguyen n:'))
    return n
def boi_so_n(n):
    for i in range(1,11):
        print(f'boi so cua n voi {i:>02} la: {n*i}')
n=nhap_du_lieu()
boi_so_n(n)
print('het')