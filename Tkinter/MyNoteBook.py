# my notebook for saving notes when I reading PDF files
# Functions:
# 1. load FSCapture APP and save screenshot
# 2. piece note images togather
# 3. add beautiful notes to pictures or as a supplementry for the pictures
# 4. add notes stand alone 
# 5. push to google drives -- will do

######################################################################
# created by lingkangjie
# date: 2019-03-03
######################################################################

import subprocess
import PySimpleGUI as sg
import sys
import os
from datetime import datetime
from tkinter import messagebox,filedialog
from PIL import Image,ImageDraw,ImageFont
import img2pdf

# layout for GUI
def note_gui():

    #sg.ChangeLookAndFeel('Black')

    working_folder = os.getcwd()
    #name_val_paris = {'wp':working_folder,'time':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    name_val_paris = None
    wp_list,fp_list = save_config_env(working_folder,name_val_paris)
    wp = [i['wp'] for i in wp_list]
    fp = [i['fp'] for i in fp_list]
    doc_path = {}
    print(fp)

    # column layout for PDF reader
    col = [[sg.Text('D0',text_color='white',font=('Times',10),background_color='OliveDrab'),sg.Input(fp[0],font=('Times',12),key='__D0__',do_not_clear=True),sg.Button('open',font=('Times',10),button_color=('red','white')),sg.Button('Check Note')],
           [sg.Text('D1',text_color='white',font=('Times',10),background_color='OliveDrab'),sg.Input(fp[1],font=('Times',12),key='__D1__',do_not_clear=True),sg.Button('open',font=('Times',10),button_color=('red','white')),sg.Button('Check Note')],
           [sg.Text('D2',text_color='white',font=('Times',10),background_color='OliveDrab'),sg.Input(fp[2],font=('Times',12),key='__D2__',do_not_clear=True),sg.Button('open',font=('Times',10),button_color=('red','white')),sg.Button('Check Note')],
           [sg.Text('D3',text_color='white',font=('Times',10),background_color='OliveDrab'),sg.Input(fp[3],font=('Times',12),key='__D3__',do_not_clear=True),sg.Button('open',font=('Times',10),button_color=('red','white')),sg.Button('Check Note')],
           [sg.Text('D4',text_color='white',font=('Times',10),background_color='OliveDrab'),sg.Input(fp[4],font=('Times',12),key='__D4__',do_not_clear=True),sg.Button('open',font=('Times',10),button_color=('red','white')),sg.Button('Check Note')],
           [sg.Text('D5',text_color='white',font=('Times',10),background_color='OliveDrab'),sg.Input(fp[5],font=('Times',12),key='__D5__',do_not_clear=True),sg.Button('open',font=('Times',10),button_color=('red','white')),sg.Button('Check Note')],
           [sg.Text('D6',text_color='white',font=('Times',10),background_color='OliveDrab'),sg.Input(fp[6],font=('Times',12),key='__D6__',do_not_clear=True),sg.Button('open',font=('Times',10),button_color=('red','white')),sg.Button('Check Note')],
           [sg.Text('D7',text_color='white',font=('Times',10),background_color='OliveDrab'),sg.Input(fp[7],font=('Times',12),key='__D7__',do_not_clear=True),sg.Button('open',font=('Times',10),button_color=('red','white')),sg.Button('Check Note')],
           [sg.Text('D8',text_color='white',font=('Times',10),background_color='OliveDrab'),sg.Input(fp[8],font=('Times',12),key='__D8__',do_not_clear=True),sg.Button('open',font=('Times',10),button_color=('red','white')),sg.Button('Check Note')],
           [sg.Text('D9',text_color='white',font=('Times',10),background_color='OliveDrab'),sg.Input(fp[9],font=('Times',12),key='__D9__',do_not_clear=True),sg.Button('open',font=('Times',10),button_color=('red','white')),sg.Button('Check Note')]
           ]

    layout = [
        [sg.Text('ToolBoxes for Notes', size=(20, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
        [sg.Button('Open FSCapture',font=('Times',12),button_color=('black','lightgreen'))],
        [sg.InputCombo(wp,key='__WorkingFolder__',size=(40,1),enable_events=True),sg.Checkbox('Default Path',default=True,key='__DefaultPath__')],
        [sg.InputText('',key='__NewFolder__',do_not_clear=True),sg.Button('New Working Folder',font=('Times',12),button_color=('black','Orange'))],
        [sg.Text('Your notes here:',font=('Times',11))],
        [sg.Multiline('',font=('Times',14),text_color='Black',key='__notes__',do_not_clear=True)],
        [sg.Button('File Attached'),sg.Button('Note Done')],
        [sg.InputText('*.jpg',key='__imName__',font=('Times',12),do_not_clear=True),sg.Button('Merge All',font=('Times',12))],
        [sg.Button('To PDF',size=(6,None),font=('Times',12)),sg.Quit(button_color=('black','LightPink'),font=('Times',12))],
        [sg.Button('Open PDF Reader',size=(10,None),font=('Times',12))],
        [sg.Column(col,background_color='DarkSeaGreen')]
        ]

    window = sg.Window('Notes System', default_element_size=(50, 1), grab_anywhere=False,\
            keep_on_top=True).Layout(layout)

    while True:
        event, values = window.Read()
        print('the event is %s' %event)
        print(values)

        if event == 'New Working Folder':
            #folder_path = sg.PopupGetFolder('Please enter the folder you want to work')
            folder_path = filedialog.askdirectory(initialdir=os.getcwd())
            if folder_path is not None:
                window.FindElement('__NewFolder__').Update(value=folder_path)
                window.FindElement('__DefaultPath__').Update(value=False)
                working_folder = os.getcwd()
                name_val_paris = {}
                name_val_paris['wp'] = folder_path
                name_val_paris['time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                _, _ = save_config_env(working_folder,name_val_paris)

        if event == 'Open FSCapture':
            app_path = 'D:\\Program Files (x86)\\screenshot_green\\FSCapture.exe'
            subprocess.Popen([app_path])

        if event == 'Open PDF Reader':
            # if cancel, will return an empty string
            pdf_file_name = filedialog.askopenfilename(initialdir=os.getcwd(),\
                    filetype=(('PDF files','*.pdf'),('all files','*,*')))
            print('pdf_file_name:%s'%pdf_file_name)
            if pdf_file_name:
                subprocess.Popen(['D:\Program Files (x86)\Foxit Software\Foxit Reader\FoxitReader.exe',pdf_file_name])
                name_val_paris = {'fp':pdf_file_name,'time':datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 
                fp.append(pdf_file_name)
                _, _ = save_config_env(working_folder,name_val_paris)

                # update the document area
                fp_ = fp[::-1]
                for i in range(0,10):
                    e = '__D' + str(i) + '__'
                    fp__ = fp_[i]
                    (filepath,filenametmp) = os.path.split(fp__)
                    (filename,name_extension) = os.path.splitext(filenametmp)
                    doc_path[filenametmp] = filepath
                    print(doc_path)
                    window.FindElement(e).Update(value=filename)


        if event == '__WorkingFolder__' and values['__DefaultPath__'] == True:
            folder_path = values['__WorkingFolder__']
            print(folder_path)

        if event == 'File Attached':
            file_need_note = filedialog.askopenfilename(initialdir=folder_path,\
                    filetype=(('Image files','*.jpg'),('all files','*,*')))

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
            if values['__imName__'] == '*.jpg' or values['__imName__'] == '':
                messagebox.showwarning('ATTENTION','please input image name')
            else:
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
    font = ImageFont.truetype('../arial.ttf',size=36)
    draw_ = ImageDraw.Draw(new_im)
    (x,y) = (0,0)
    draw_.text((x,y),message,fill='rgb(0,0,0)',font=font)
    (filepath,filenametmp) = os.path.split(file_)
    (filename,name_extension) = os.path.splitext(filenametmp)
    filename = filepath + '//' + filename + '_note'+'.jpg'
    new_im.save(filename)

def save_config_env(working_folder,name_val_pairs):

    file_name = working_folder +'\\config.cfg'
    max_working_path = 5
    max_files_num = 10
    wp_list = []
    fp_list = []
    if os.path.exists(file_name):
        with open(file_name,'r') as f:
            v = f.read().split('\n')
            v = [x for x in v if len(x)>0]
            history = []
            if name_val_pairs is not None:
                history.append(name_val_pairs)
            for i in v:
                hist_dict = {}
                p, t = i.split('>>>')[0], i.split('>>>')[1]
                hist_dict[p.split('>>')[0]] = p.split('>>')[1]
                hist_dict[t.split('>>')[0]] = t.split('>>')[1]
                history.append(hist_dict)
            history_sorted = sorted(history,key=lambda k:k['time'],reverse=True) # sorted by descending

            # constraint the config items
            for i in history_sorted:
                if 'wp' in i.keys():
                    wp_list.append(i)
                if 'fp' in i.keys():
                    fp_list.append(i)
            if len(wp_list) > max_working_path:
                wp_list = wp_list[0:5]
            if len(fp_list) > max_files_num:
                fp_list = fp_list[0:10]

        # save all config to file
        with open(file_name,'w') as f:
            for i in wp_list+fp_list:
                k = list(i.keys())
                f.write(k[0] + '>>' + i[k[0]] + '>>>')
                f.write(k[1] + '>>' + i[k[1]] + '\n')
        print('ok')
    else:
        if name_val_pairs is not None:
            with open(file_name,'w') as f:
                k = list(name_val_pairs.keys())
                f.write(k[0] + '>>' + name_val_pairs[k[0]] + '>>>')
                f.write(k[1] + '>>' + name_val_pairs[k[1]] + '\n')

    return wp_list,fp_list

if __name__=='__main__':

    note_gui()
    #image_merge()
    #draw_text_to_image()
    #working_folder = os.getcwd()
    #t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #name_val_paris = {'wp':'d:\\tmp\\aa','time':t}
    #save_config_env(working_folder,name_val_paris)

