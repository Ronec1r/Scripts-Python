segundos=int(input('Por favor, entre com o número de segundos que deseja converter: '))
minuto=segundos//60
d=segundos%60
hora=minuto//60
c=minuto%60
dia=hora//24
b=hora%24
print(dia,'dias,',b,'horas,',c,'minutos e',d,'segundos.')
