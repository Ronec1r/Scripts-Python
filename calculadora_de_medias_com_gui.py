import PySimpleGUI as sg
layout=[[sg.Text('Calculadora de médias!!\n')],[sg.Text('Digite a primeira nota:')],
        [sg.Input()],[sg.Text('Digite a segunda nota:')],[sg.Input()],
        [sg.Submit()], [sg.Cancel()]]
window=sg.Window('Window Title',layout)
event, values=window.read()
window.close()
if (event==sg.WIN_CLOSED) or (event=='Cancel'):
    breakpoint
elif (values[0]=='') or (values[1]==''):
    sg.popup('Pelo menos uma das notas não foi digitada!!')
else:
    nota_1=int(values[0])
    nota_2=int(values[1])
    media=(nota_1+nota_2)/2
    sg.popup('A média foi igual a:',media) 



