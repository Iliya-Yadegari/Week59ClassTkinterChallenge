import classPracticeModule as cpm
from tkinter import *

window = Tk()
window.title('ATM')

r = IntVar()

amount_lbl = Label(window,text = 'Choose your amount').grid(row = 0,column = 0,padx = 10,pady = 10)
amount_ent = Entry(window)

Radiobutton(window,text = 'Depoist',variable = r,value = 1).grid(row = 1, column = 0, padx = 10, pady = 10)
Radiobutton(window,text = 'Withdrawn',variable = r,value = 2).grid(row = 2, column = 0, padx = 10, pady = 10)

submit_btn = Button(window,text = 'Submit',width = 20,height = 3,command = lambda: tom.choice(r.get(),amount_ent.get(),window)).grid(row = 3,column = 0,padx = 10,pady = 10)

amount_ent.grid(row = 0,column = 1,padx = 10,pady = 10)

tom = cpm.BankCustomer('Tom Smith',32,3000)
sarah = cpm.BankCustomer('Sarah White',46,300)

window.mainloop()