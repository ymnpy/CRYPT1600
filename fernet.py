from cryptography.fernet import Fernet
import tkinter as tk
import tkinter.font as font
from tkinter import filedialog, messagebox
from tkinter import messagebox

def encrypt():
    key_text.config(state="normal") #key toggle
    #text=str.encode(text_entry.get("1.0","end-1c"))
    text=text_entry.get("1.0","end-1c")
    text=text.encode('utf-8')
    key=Fernet.generate_key()
    f=Fernet(key)
    cipher=f.encrypt(text)

    key_text.insert("1.0",key)
    text_entry.delete("1.0", "end")
    text_entry.insert("1.0",cipher)
    key_text.config(state="disabled") #key toggle

def decrypt():
    key_text.config(state="normal") #key toggle
    cipher=text_entry.get("1.0","end-1c")
    key=key_text.get("1.0","end-1c")

    try:
        f=Fernet(key)
        text=f.decrypt(cipher)
        text=text.decode('utf-8')
    except ValueError:
        key_text.delete("1.0","end")
        key_text.insert("1.0","wrong key!")
        return None
    
    #key_text.insert("1.0",key)
    text_entry.delete("1.0", "end")
    text_entry.insert("1.0", text)
    key_text.config(state="disabled") #key toggle

def pop_up():
    popup=tk.Toplevel(app)
    popup.title("Warning")
    popup.geometry("400x200")

    label=tk.Label(popup,text="yo",font=("Arial",14))
    label.pack(pady=20)

    close_btn=tk.Button(popup,text="close", command=popup.destroy)
    close_btn.pack(pady=10)

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


if __name__=="__main__": 
    # Initialize the GUI
    app = tk.Tk()
    app.title("CRYPT1600")
    app.geometry("450x600")
    app.configure(bg="black")  # Set background color to gray
    app.resizable(False,False)
    center_window(app)

    font1 = font.Font(family="Consolas", size=10)
    font2 = font.Font(family="Consolas", size=11, weight="bold")
    font3 = font.Font(family="Consolas", size=11)

    # File selection label and entry
    """ file_label = tk.Button(app, text="Select File :", command=browse_file, width=15,font=font1, bg="#444", fg="#00FF00")
    file_label.place(x=20, y=20)  # Adjust x and y as needed """

    # Retrieve the button's height
    #button_height = file_label.winfo_reqheight()

    text_label = tk.Label(app, text="write your text below:", bg="black", fg="#00FF00", 
                        width=22, font=font3,justify="left")
    text_label.place(x=20,y=20)

    # new window for text input
    text_frame = tk.Frame(app)
    text_frame.place(x=20, y=50, width=405, height=420)

    # filling that new window with input and scrollbar
    text_entry = tk.Text(text_frame, wrap="word", width=40, bd=2, relief="sunken", 
                        bg="black", fg="#00FF00")
    text_entry.pack(side="left", expand=True, fill="both")
    scrollbar = tk.Scrollbar(text_frame, orient="vertical",command=text_entry.yview)
    scrollbar.pack(side="right", fill="y")

    # make scrollbar appear/disappear
    text_entry.config(yscrollcommand=scrollbar.set)

    #key section
    key_label = tk.Label(app, text="key:", bg="black", fg="#00FF00", 
                        width=5, font=font3,justify="left")
    key_label.place(x=16,y=490)
    key_text=tk.Text(app, height=1, width=45,bg="black",fg="#00FF00", bd=0,font=("Consolas",8))
    #key_text.insert("1.0","what is this")
    key_text.place(x=60,y=496)

    encrypt_btn = tk.Button(app, text="ENCRYPT", width=23, height=1, font=font2, bg="#444", 
                            fg="#00FF00",command=encrypt)
    encrypt_btn.place(x=235, y=540)
    decrypt_btn = tk.Button(app, text="DECRYPT", width=23, height=1, font=font2, bg="#444", 
                            fg="#00FF00", command=decrypt)
    decrypt_btn.place(x=20, y=540)

    app.mainloop()
