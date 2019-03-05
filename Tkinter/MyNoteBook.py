# my notebook for saving notes when I reading PDF files
# Functions:
# 1. load FSCapture APP and save screenshot
# 2. piece pictures togather
# 3. add beautiful notes to pictures or as a supplementry for the pictures
# 4. add notes 
# 5. push to google drives

######################################################################
# created by lingkangjie
# date: 2019-03-03
######################################################################

import subprocess
import PySimpleGUI as sg
import sys
import os
from tkinter import messagebox
from PIL import Image,ImageDraw,ImageFont
import img2pdf

# layout for GUI
def note_gui():

    sg.ChangeLookAndFeel('White')
    #sg.ChangeLookAndFeel('Black')

    layout = [
        [sg.Text('ToolBoxes for Notes', size=(20, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
        [sg.Button('Open FSCapture',font=('Times',12),button_color=('black','lightgreen')),sg.Button('Working Folder',font=('Times',12),button_color=('black','Orange'))],
        [sg.Text('Your notes here:',font=('Times',11))],
        [sg.Multiline('',font=('Times',14),text_color='Black',key='__notes__')],
        [sg.Button('File Attached'),sg.Button('Note Done')],
        [sg.InputText('*.jpg',key='__imName__',font=('Times',12)),sg.Button('Merge All',font=('Times',12))],
        [sg.Button('To PDF',size=(6,None),font=('Times',12)),sg.Quit(button_color=('black','LightPink'),font=('Times',12))]
        ]

    window = sg.Window('Notes System', default_element_size=(40, 1), grab_anywhere=False,\
            keep_on_top=True).Layout(layout)

    while True:
        event, values = window.Read()
        if event == 'Working Folder':
            folder_path = sg.PopupGetFolder('Please enter the folder you want to work')
            print(folder_path)
        if event == 'Open FSCapture':
            app_path = 'F:\\Program Files (x86)\\screenshot_green\\FSCapture.exe'
            subprocess.Popen([app_path])
        if event == 'File Attached':
            file_need_note = sg.PopupGetFile('Please enter the file you want to attach')
        if event == 'Note Done':
            print(values['__notes__'])
            draw_text_to_image(values['__notes__'],file_=file_need_note)
        if event == 'Merge All':
            if values['__imName__'] == '*.jpg' or values['__imName__'] == '':
                messagebox.showwarning('ATTENTION','please input image name')
            else:
                save_image_path = folder_path + '//' + values['__imName__'] + '.jpg'
                image_merge(save_image_path)
        if event == 'To PDF':
            pdf_bytes = img2pdf.convert(save_image_path)
            (filepath,filenametmp) = os.path.split(save_image_path)
            (filename,name_extension) = os.path.splitext(filenametmp)
            pdf_name = filepath + '//' + filename + '.pdf'
            with open(pdf_name,'wb') as f:
                f.write(pdf_bytes)
        if event is None or event == 'Quit':
            break

def image_merge(save_image_path):

    (filepath,filename) = os.path.split(save_image_path)
    filelist = []
    for filename in os.listdir(filepath):
        filelist.append(os.path.join(filepath,filename))

    images = map(Image.open,filelist)
    widths, heights = zip(*(i.size for i in images))
    max_width = max(widths)
    total_height = sum(heights)
    new_im = Image.new('RGB',(max_width,total_height),(255,255,255))
    color_bar = Image.new('RGB',(max_width,5),(55,100,225))

    images = map(Image.open,filelist)
    y_offset = 0
    for im in images:
        new_im.paste(im,(0,y_offset))
        y_offset += im.size[1]
        new_im.paste(color_bar,(0,y_offset))
        y_offset += 5

    new_im.save(save_image_path)

def draw_text_to_image(message,file_):

    size_scale = 30
    width,_ = Image.open(file_).size
    height = len(message.split('\n')) * size_scale
    new_im = Image.new('RGB',(width,height),(255,255,255))
    font = ImageFont.truetype('../arial.ttf',size=35)
    draw_ = ImageDraw.Draw(new_im)
    (x,y) = (0,0)
    draw_.text((x,y),message,fill='rgb(0,0,0)',font=font)
    (filepath,filenametmp) = os.path.split(file_)
    (filename,name_extension) = os.path.splitext(filenametmp)
    filename = filepath + '//' + filename + '_note'+'.jpg'
    new_im.save(filename)


if __name__=='__main__':

    note_gui()
    #image_merge()
    #draw_text_to_image()

