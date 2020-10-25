from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from threading import *



font = ('verdana', 20)
file_size = 0

#on complete callback function
def completedDownload(stream=None, file_path=None):
    print("download completed")
    showinfo('Message', 'File has been downloaded.')
    downloadBtn['text'] = 'Download Video'
    downloadBtn['state'] = 'active'
    urlField.delete(0, END)

#on progress callback function
def progressDownload(stream=None, chunk=None, bytes_remaining=None):
    percentage = (100 * ((file_size - bytes_remaining)/file_size))
    downloadBtn['text'] = '{:00.0f} % downloaded'.format(percentage)


#download function
def startDownload(url):
    global file_size
    path_to_save_video = askdirectory()
    if path_to_save_video is None:
        return
    try:
        yt = YouTube(url)
        st = yt.streams.first()

        yt.register_on_complete_callback(completedDownload)
        yt.register_on_progress_callback(progressDownload)

        file_size = st.filesize
        st.download(output_path=path_to_save_video)

    except Exception as e:
        print(e)
        print('Something went wrong!!!')

def btnClick():
    try:
        downloadBtn['text'] = 'Please wait....'
        downloadBtn['state'] = 'disabled'
        url=urlField.get()
        if url=='':
            return
        print(url)
        thread = Thread(target=startDownload, args=(url,))
        thread.start()

    except Exception as e:
         print(e)






# GUI config
root = Tk()
root.title('YouTube Downloader.')
root.iconbitmap('IMG/ico.ico')
root.geometry('500x600')

#main icon
file = PhotoImage(file='IMG/youtube.png')
headingIcon = Label(root, image=file)
headingIcon.pack(side = TOP, pady = 3)

#creating url field
urlField = Entry(root, font=font, justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10)
urlField.focus()

#download button
downloadBtn = Button(root, text='Download Video', font=font, relief='ridge', command=btnClick)
downloadBtn.pack(side=TOP, pady=20)

''''''
root.mainloop()