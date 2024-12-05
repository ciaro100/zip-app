import FreeSimpleGUI as sg
from functions import make_zip

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_file_button = sg.FilesBrowse("Choose: ", key="files")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_dest_button = sg.FolderBrowse("Choose: ", key="folder")

compress_button = sg.Button("Compress: ")
output_label = sg.Text(key="output", text_color="black")

layout = [
    [label1, input1, choose_file_button],
    [label2, input2, choose_dest_button],
    [compress_button,output_label],
]

w = sg.Window("PyFile Compressor", layout=layout)
while True:
    try:
        event, values = w.read()
        filepaths = values["files"].split(";")
        folder = values["folder"]
        make_zip(filepaths, folder)
    except AttributeError:
        sg.popup("Restart program and enter some files!")
        break
    match values:
        case "Compress":
            w["output"].update(value="Compression Completed! ")
        case sg.WIN_CLOSED:
            break

w.close()

