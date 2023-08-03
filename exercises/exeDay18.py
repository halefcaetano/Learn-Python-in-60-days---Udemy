import PySimpleGUI as py

py.theme("Black")
label1 = py.Text("Enter feet: ")
input1 = py.Input()

label2 = py.Text("Enter inches: ")
input2 = py.Input()

button = py.Button("Convert")

output_label = py.Text(key='output')

exit = py.Button("Exit")

window = py.Window("Convertor", layout=[[label1, input1], [label2, input2], [button], [output_label, exit]])

while True:
    event, values = window.read()
    feet = float(values[0])
    inches = float(values[1])
    total1 = feet * 0.3048
    total2 = inches * 0.0254
    total = total1 + total2
    final = "%.2f" % total
    window['output'].update(value=f"{final} m")
    match event:
        case "Exit":
            break


window.close()