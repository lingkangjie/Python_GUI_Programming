# my notebook for saving notes when I reading PDF files
# Functions:
# 1. load FSCapture APP and save screenshot
# 2. piece note images togather
# 3. add beautiful notes to pictures or as a supplementry for the pictures
# 4. add notes stand alone 
# 5. save reading history
# 6. open PDF reader
# 7. rereading papers or notes
# 8. push to google drives -- will do

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
def note_gui(working_folder,wp,fp,doc_path,fp_name,folder_path):

    working_file_name = fp_name[0]

    sg.ChangeLookAndFeel('Black')

    # column layout for PDF reader
    col = [[sg.Text('D0',text_color='white',font=('Consolas',10),background_color='OliveDrab'),sg.Input(fp_name[0],text_color='#b58900',background_color='#073642',font=('Consolas',12),key='__D0__',do_not_clear=True),sg.Button('R0',font=('Consolas',10),button_color=('white','#007339')),sg.Button('Note0',button_color=('white','gold4'))],
           [sg.Text('D1',text_color='white',font=('Consolas',10),background_color='OliveDrab'),sg.Input(fp_name[1],text_color='#b58900',background_color='#073642',font=('Consolas',12),key='__D1__',do_not_clear=True),sg.Button('R1',font=('Consolas',10),button_color=('white','#007339')),sg.Button('Note1',button_color=('white','gold4'))],
           [sg.Text('D2',text_color='white',font=('Consolas',10),background_color='OliveDrab'),sg.Input(fp_name[2],text_color='#b58900',background_color='#073642',font=('Consolas',12),key='__D2__',do_not_clear=True),sg.Button('R2',font=('Consolas',10),button_color=('white','#007339')),sg.Button('Note2',button_color=('white','gold4'))],
           [sg.Text('D3',text_color='white',font=('Consolas',10),background_color='OliveDrab'),sg.Input(fp_name[3],text_color='#b58900',background_color='#073642',font=('Consolas',12),key='__D3__',do_not_clear=True),sg.Button('R3',font=('Consolas',10),button_color=('white','#007339')),sg.Button('Note3',button_color=('white','gold4'))],
           [sg.Text('D4',text_color='white',font=('Consolas',10),background_color='OliveDrab'),sg.Input(fp_name[4],text_color='#b58900',background_color='#073642',font=('Consolas',12),key='__D4__',do_not_clear=True),sg.Button('R4',font=('Consolas',10),button_color=('white','#007339')),sg.Button('Note4',button_color=('white','gold4'))],
           [sg.Text('D5',text_color='white',font=('Consolas',10),background_color='OliveDrab'),sg.Input(fp_name[5],text_color='#b58900',background_color='#073642',font=('Consolas',12),key='__D5__',do_not_clear=True),sg.Button('R5',font=('Consolas',10),button_color=('white','#007339')),sg.Button('Note5',button_color=('white','gold4'))],
           [sg.Text('D6',text_color='white',font=('Consolas',10),background_color='OliveDrab'),sg.Input(fp_name[6],text_color='#b58900',background_color='#073642',font=('Consolas',12),key='__D6__',do_not_clear=True),sg.Button('R6',font=('Consolas',10),button_color=('white','#007339')),sg.Button('Note6',button_color=('white','gold4'))],
           [sg.Text('D7',text_color='white',font=('Consolas',10),background_color='OliveDrab'),sg.Input(fp_name[7],text_color='#b58900',background_color='#073642',font=('Consolas',12),key='__D7__',do_not_clear=True),sg.Button('R7',font=('Consolas',10),button_color=('white','#007339')),sg.Button('Note7',button_color=('white','gold4'))],
           [sg.Text('D8',text_color='white',font=('Consolas',10),background_color='OliveDrab'),sg.Input(fp_name[8],text_color='#b58900',background_color='#073642',font=('Consolas',12),key='__D8__',do_not_clear=True),sg.Button('R8',font=('Consolas',10),button_color=('white','#007339')),sg.Button('Note8',button_color=('white','gold4'))],
           [sg.Text('D9',text_color='white',font=('Consolas',10),background_color='OliveDrab'),sg.Input(fp_name[9],text_color='#b58900',background_color='#073642',font=('Consolas',12),key='__D9__',do_not_clear=True),sg.Button('R9',font=('Consolas',10),button_color=('white','#007339')),sg.Button('Note9',button_color=('white','gold4'))]
           ]

    layout = [
        [sg.Text('Paper Reading Systems', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
        [sg.Button('Open FSCapture',font=('Consolas',12),button_color=('white','#007339')),sg.Quit(button_color=('white','firebrick4'),font=('Consolas',12))],
        [sg.InputCombo(wp,key='__WorkingFolder__',text_color='#dc322f',background_color='#002b36',size=(40,1),font=('Consolas',12),enable_events=True),sg.Checkbox('Default Path',default=True,font=('Consolas',12),key='__DefaultPath__')],
        [sg.InputText('',key='__NewFolder__',text_color='#dc322f',background_color='#002b36',font=('Consolas',12),do_not_clear=True),sg.Button('New Working Folder',font=('Consolas',12),button_color=('white','DarkOrange4'))],
        
        [sg.InputText('',key='__LastedImage__',text_color='#dc322f',background_color='#002b36',font=('Consolas',12),do_not_clear=True),sg.Checkbox('Lasted image',font=('Consolas',12),default=True,key='__DefaultLastedImage__')],
        [sg.Text('Your notes here:',font=('Consolas',12))],
        [sg.Multiline('',font=('Consolas',14),text_color='#268bd2',size=(60,1),background_color='#002b36',key='__notes__',do_not_clear=True)],
        [sg.Button('File Attached',font=('Consolas',12),button_color=('white','#001480')),sg.Button('Clear and Reflesh',font=('Consolas',12),button_color=('white','red3')),sg.Button('Noting Done',font=('Consolas',12),button_color=('white','#007339'))],
        [sg.InputText('',key='__imName__',font=('Consolas',12),do_not_clear=True),sg.Button('Merge All',button_color=('white','#007339'),font=('Consolas',12)),sg.Button('To PDF',size=(6,None),font=('Consolas',12),button_color=('white','#007339'))],
        [sg.Button('Open PDF Reader',button_color=('white','red3'),font=('Consolas',12))],
        [sg.Column(col,background_color='grey12')]
        ]

    window = sg.Window('Notes System', default_element_size=(50, 1), grab_anywhere=False,\
            keep_on_top=False).Layout(layout)

    # update the defualt image fold status
    filelist = []
    for filename in os.listdir(folder_path+'\\notes\\'):
        if filename[-3:] == 'jpg':
            filelist.append(filename)
    filelist = [s for s in filelist if '_NOTES' not in s]
    file_list_sorted = sorted(filelist,reverse=True)
    if file_list_sorted:
        window.FindElement('__LastedImage__').Update(value=file_list_sorted[0])
        file_need_note = folder_path + '\\notes\\' + file_list_sorted[0]

    while True:
        event, values = window.Read()
        #print('the event is %s' %event)
        #print(values)


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
            try:
                app_path = 'D:\\Program Files (x86)\\screenshot_green\\FSCapture.exe'
            except:
                app_path = 'F:\\Program Files (x86)\\screenshot_green\\FSCapture.exe'
            subprocess.Popen([app_path])

        if event == 'Open PDF Reader':
            # if cancel, will return an empty string
            pdf_file_name = filedialog.askopenfilename(initialdir=os.getcwd(),\
                    filetype=(('PDF files','*.pdf'),('all files','*,*')))
            if pdf_file_name:
                try:
                    subprocess.Popen(['D:\Program Files (x86)\Foxit Software\Foxit Reader\FoxitReader.exe',pdf_file_name])
                except:
                    subprocess.Popen(['F:\Program Files\Foxit Reader\Foxit Reader.exe',pdf_file_name])
                name_val_paris = {'fp':pdf_file_name,'time':datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 
                if pdf_file_name in fp:
                    fp.remove(pdf_file_name)
                else:
                    _, _ = save_config_env(working_folder,name_val_paris)
                fp.insert(0,pdf_file_name)

                # update the document area
                for i,fp__ in enumerate(fp[:10]):
                    if fp__:
                        e = '__D' + str(i) + '__'
                        (filepath,filenametmp) = os.path.split(fp__)
                        (filename,name_extension) = os.path.splitext(filenametmp)
                        doc_path[filename] = filepath
                        window.FindElement(e).Update(value=filename)

                # update image name area
                _, filenametmp = os.path.split(pdf_file_name)
                working_file_name  = filenametmp[:-4]
                window.FindElement('__imName__').Update(value=working_file_name+'_NOTES')

                # make a dir to save the corresponding notes
                if not os.path.exists(working_folder + '/notes/' + working_file_name):
                    os.makedirs(working_folder + '/notes/' + working_file_name)


        if event == '__WorkingFolder__' and values['__DefaultPath__'] == True:
            folder_path = values['__WorkingFolder__']

        if event == 'File Attached':
            file_need_note = filedialog.askopenfilename(initialdir=folder_path,\
                    filetype=(('Image files','*.jpg'),('all files','*,*')))
            window.FindElement('__DefaultLastedImage__').Update(value=False)
            (_, filenametmp) = os.path.split(file_need_note)
            window.FindElement('__LastedImage__').Update(value=filenametmp)

        if event == 'Noting Done':
            draw_text_to_image(values['__notes__'],file_=file_need_note)

        if event == 'Clear and Reflesh':
            # update the defualt image fold status
            filelist = []
            for filename in os.listdir(folder_path+'//notes//'+working_file_name):
                if filename[-3:] == 'jpg':
                    filelist.append(filename)
            filelist = [s for s in filelist if '_note' not in s]
            file_list_sorted = sorted(filelist,reverse=True)
            if file_list_sorted:
                file_need_note = folder_path + '//notes//' + working_file_name + '//' + file_list_sorted[0]
                window.FindElement('__LastedImage__').Update(value=file_list_sorted[0])
                window.FindElement('__notes__').Update(value='')

        if event == 'Merge All':
            if not values['__imName__']:
                messagebox.showwarning('ATTENTION','please input image name')
            else:
                save_image_path = folder_path + '\\notes\\' + working_file_name + '\\' + working_file_name + '.jpg'
                image_merge(save_image_path)

        if event == 'To PDF':
            if values['__imName__'] == '*.jpg' or values['__imName__'] == '':
                messagebox.showwarning('ATTENTION','please input image name')
            else:
                pdf_bytes = img2pdf.convert(save_image_path)
                (filepath,filenametmp) = os.path.split(save_image_path)
                (filename,name_extension) = os.path.splitext(filenametmp)
                pdf_name = filepath + '//' + filename + '_NOTES.pdf'
                with open(pdf_name,'wb') as f:
                    f.write(pdf_bytes)

        if event[0] == 'R':
            working_file_name = values['__D'+event[1]+'__']
            fpath = doc_path[working_file_name] + '//' + working_file_name + '.pdf'
            if fpath:
                if os.path.exists(fpath):
                    try:
                        subprocess.Popen(['F:\Program Files\Foxit Reader\Foxit Reader.exe',fpath])
                    except:
                        subprocess.Popen(['D:\Program Files (x86)\Foxit Software\Foxit Reader\FoxitReader.exe',fpath])
                else:
                    messagebox.showerror('ERROR','file does not exist')

            # update image name area
            window.FindElement('__imName__').Update(value=working_file_name+'_NOTES')
            
            # make a dir to save the corresponding notes
            if not os.path.exists(working_folder + '/notes/' + working_file_name):
                os.makedirs(working_folder + '/notes/' + working_file_name)

        if event[:-1] == 'Note':
            fname = values['__D'+event[-1]+'__']
            working_file_name = fname
            fpath = folder_path+'\\notes\\' + working_file_name + '\\' + working_file_name +'_NOTES.pdf'
            if fpath:
                if os.path.exists(fpath):
                    try:
                        subprocess.Popen(['F:\Program Files\Foxit Reader\Foxit Reader.exe',fpath])
                    except:
                        subprocess.Popen(['D:\Program Files (x86)\Foxit Software\Foxit Reader\FoxitReader.exe',fpath])
                else:
                    messagebox.showerror('ERROR','file does not exist')

        if event is None or event == 'Quit':
            break

def image_merge(save_image_path):

    (filepath,filename) = os.path.split(save_image_path)
    filelist = []
    for filename in os.listdir(filepath):
        filelist.append(os.path.join(filepath,filename))

    if filelist:
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
    else:
        if name_val_pairs is not None:
            with open(file_name,'w') as f:
                k = list(name_val_pairs.keys())
                f.write(k[0] + '>>' + name_val_pairs[k[0]] + '>>>')
                f.write(k[1] + '>>' + name_val_pairs[k[1]] + '\n')

    return wp_list,fp_list

def screenshot():
    pass

if __name__=='__main__':

    # env beginning and setting
    if not os.path.exists('./notes'):
        os.makedirs('./notes')
    if not os.path.exists('config.cfg'):
        with open('config.cfg','w') as f:
            f.write('wp'+'>>' + '>>>' + 'time' + '>>' + '\n')
    # default working path
    folder_path = os.getcwd()
    working_folder = os.getcwd()

    wp_list,fp_list = save_config_env(os.getcwd(),None)
    wp = [i['wp'] for i in wp_list]
    fp = [i['fp'] for i in fp_list]
    if len(fp)<10:
        for i in range(0,10-len(fp)):
            fp.append('')

    doc_path = {}
    fp_name = []
    for fp_ in fp:
        (filepath,filenametmp) = os.path.split(fp_)
        (filename,_) = os.path.splitext(filenametmp)
        fp_name.append(filename)
        doc_path[filename] = filepath


    note_gui(working_folder,wp,fp,doc_path,fp_name,folder_path)

