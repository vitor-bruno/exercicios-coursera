nfat = n = int(input('Digite o valor de n: '))
m = n - 1
while m > 0:
    nfat *= m
    m -= 1
if n == 0:
    nfat = 1
print(nfat)
