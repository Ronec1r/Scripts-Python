import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED
from math import sqrt
layout=[[sg.Text('Calculadora de raízes de segundo grau!!\n')], [sg.Text('Digite o valor de a:')],
        [sg.Input()],[sg.Text('Digite o valor de b:')],[sg.Input()],[sg.Text('Digite o valor de c:')],
        [sg.Input()],[sg.Submit()],[sg.Cancel()]]
window=sg.Window('Window Title',layout)
event, values=window.read()
window.close()

if (event=='Cancel') or (event==sg.WIN_CLOSED):
    breakpoint
elif (values[0]=='') or (values[1]=='') or (values[2]==''):
    sg.popup('É necessário o preenchimento de todos valores!!')
else:
    a=float(values[0])
    b=float(values[1])
    c=float(values[2])
    delta=b**2-4*a*c
    if (delta<0):
        sg.popup('A equação não possui raízes reais!!')
    elif (delta>0):
        x1=(-b+sqrt(delta))/(2*a)
        x2=(-b-sqrt(delta))/(2*a)
        sg.popup('As raízes foram',x1,'e',x2,'!!')
    else:
        x=(-b+sqrt(delta))/(2*a)
        sg.popup('A raiz foi',x,'!!')


