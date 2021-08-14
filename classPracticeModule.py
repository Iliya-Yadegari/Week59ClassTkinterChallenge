from tkinter import *

class BankCustomer:
    bankName = 'Barclays' ##static attributes, class object attributes
    num = 0

    def __init__(self,name,age,balance):
        self.name = name #dynamics attributes
        self.age = age #dynamics attributes
        self.balance = balance #dynamics attributes

        BankCustomer.num += 1

    def info(self):
        print(f'{self.name}\n{self.age}\n{self.balance}')

    def choice(self,num,amount_e,w):
        if num == 1:
            self.balance += int(amount_e)

        if num == 2:
            self.balance -= int(amount_e)
            
        res_lbl = Label(w,text = self.balance).grid(row = 4,column = 0,padx = 10,pady = 10)