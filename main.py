import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_file_button = sg.FilesBrowse("Choose: ")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input()
choose_dest_button = sg.FilesBrowse("Choose: ")

compress_button = sg.Button("Compress: ")

layout = [
    [label1, input1, choose_file_button],
    [label2, input2, choose_dest_button],
    [compress_button],
]

w = sg.Window("PFile Compressor", layout=layout)
w.read()
w.close()

