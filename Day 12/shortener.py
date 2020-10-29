from tkinter import *
import pyshorteners
import clipboard
  


root = Tk()

#set default size of the window
root.geometry("400x200")

#app title  
root.title("URL Shortener")

#not resizable window
root.resizable(False, False)

#url field
url_input = Entry(root, font=("Helvetica", "16"))
url_input.grid(row=2, column=2, pady=6)


#label shortend url
str_url = StringVar(root)

shortend_url = Label(root, textvariable=str_url, font=("Helvetica", "16"), 
fg="#fff", bg="#1abc9c")
shortend_url.grid(row=6, column=2, pady=6)


#short url function
def short_url():
    try:
        s = pyshorteners.Shortener()
        url = url_input.get()
        final_result = s.tinyurl.short(url)
        str_url.set(final_result)
        url_input.delete(0, END) #clear input
    except:
        str_url.set("Enter the URL!!")  



#click button
click_btn = Button(root, text="Short Url", padx=8, pady=4, bg="#cc2e2e", 
fg="#fff", font=("Helvetica", "16"), activebackground="#16a085", command=short_url)
click_btn.grid(row=4, column=2, pady=6)


#copy url function
def copy_short_url():
    try:
        clipboard.copy(str_url.get())
        print("URL copied successfully!!")
    except:
        str_url.set("OOPS! Something went wrong.")



#copy button
copy_btn = Button(root, text="copy", bg="#2e4bcc", fg="#fff", 
font=("Helvetica", "16"), command=copy_short_url)
copy_btn.grid(row=4, column=3, pady=6, padx=10)



root.mainloop() 