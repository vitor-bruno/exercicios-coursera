s = int(input('Por favor, entre com o número de segundos que deseja converter: '))
a = s // 86400
b = (s % 86400) // 3600
c = (s % 3600) // 60
d = s % 60
print(f'{a} dias, {b} horas, {c} minutos e {d} segundos.')