import hashlib 
from simplecrypt import encrypt,decrypt
from tkinter import*
root = Tk()
root.geometry("1000x1000")
root.title("Used43254836458768543254253647586976854362514`3243546584323Times")

label = Label(root)

value = "!@#$%^&*(){[}]|\:;<,>?/*{][$$%%%"

def SHA256():
    result = hashlib.sha256(value.encode())
    print("53 48 41 32 35 36 20 65 6e 63 72 79 70 74 65 64 20 44 61 74 61",result.hexdigest())
    label['text'] = "53 48 41 32 35 36 20 65 6e 63 72 79 70 74 65 64 20 44 61 74 61" + result.hexdigest()


def MD5():
    result = hashlib.md5(value.encode())
    print("57 6f 77 20 79 6f 75 20 61 72 65 20 64 65 65 70 65 72 20 74 68 61 6e 20 65 76 65 72 20 69 6e 20 74 68 65 20 66 69 65 6c 64 20 6f 66 20 6e 6f 74 68 69 6e 67",result.hexdigest())
    label['text'] = "57 6f 77 20 79 6f 75 20 61 72 65 20 64 65 65 70 65 72 20 74 68 61 6e 20 65 76 65 72 20 69 6e 20 74 68 65 20 66 69 65 6c 64 20 6f 66 20 6e 6f 74 68 69 6e 67" + result.hexdigest()



btn = Button(root,text = "Unorganized Sha",command = SHA256)
btn2 = Button(root,text = "Unorganized MD5",command = MD5)
    
btn.pack()
btn2.pack()
label.pack()

root.mainloop()












































    
    
    
    
    
    
    
    
    
    
    