from tkinter import *
root=Tk()
root.title("Dictionary")
root.geometry("600x400")
list_items=label(root)
item_no=label(root)

list1=(bottle,tiffen,chips,chocolate,napkin)
list_items=list1+str()

def random_number():
 item_no=random.randint(0,5)+str()
 item_no["text"]="put item number"+list_items+"in bag"
 
 btn = Button(root, text = "next item", command = random_number)
btn.place(relx = 0.5, rely =0.6, anchor = CENTER)

root.mainloop()