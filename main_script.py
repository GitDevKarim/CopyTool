import PySimpleGUI as sg
import processor as srcControl

sg.theme('DarkAmber')

layout = [
    [sg.Text('A tool that organizes your files into folders based on their extension')],

    [sg.Text('Source Folder Path: ', size=(15, 0)),
     sg.InputText(key="src"), sg.FolderBrowse()],

    [sg.Text('Destination Folder Path: ', size=(15, 0)),
     sg.InputText(key="dest"), sg.FolderBrowse()],

    [sg.Button('Copy'),
     sg.Button('Cancel')]
]

window = sg.Window('Copy Tool', layout)
while True:
    event, values = window.read()  # type: ignore
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == 'Copy':
        src = window['src'].get()
        dest = window['dest'].get()

        srcControl.init(src, dest)

window.close()
