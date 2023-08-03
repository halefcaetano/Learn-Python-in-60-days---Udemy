import PySimpleGUI as py


label1 = py.Text("Enter feet: ")
input1 = py.Input()

label2 = py.Text("Enter inches: ")
input2 = py.Input()

button = py.Button("Convert")

window = py.Window("Convertor", layout=[[label1, input1], [label2, input2], [button]])

window.read()
window.close()