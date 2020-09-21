# -*- coding: utf-8 -*-
"""
Created on Tue May 19 21:29:59 2020

@author: Amaging Grace
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:43:03 2020

@author: Amaging Grace
"""

#importing modules
from tkinter import *
import tkinter.messagebox
import sqlite3
#-------------------------------------------------------------------------------
'''creating class for front end user interface'''
class product:
    def __init__(self,root):
        '''creating object instance of database class in product class and \
            connecting the objecct instance to connection function'''        
        objData = database()
        objData.connecting()
        
        self.root = root
        self.root.title('AMAZING COLLECTIONS STOCK')
        self.root.geometry('1325x690')
        self.root.config(bg='yellow')
        
        '''declareing variables as stringvars'''
        PName = StringVar()
        Colour = StringVar()
        Qty = StringVar()
        Size= StringVar()
        CostPrice = StringVar()
        SellPrice = StringVar()
        Expense = StringVar()
        newQty = StringVar()
        Pid = StringVar()
#-----------------------------------------------------------------------------#        
        '''creating functions for operation button and database\
            operation methode call'''
        def close():
            print('application: close methode called')
            close = tkinter.messagebox.askyesno('AMAZING COLLECTIONS STOCK',\
                        'Do you want to close the application')
            if close > 0:
                root.destroy()
                print('application: close methode finish\n')
                return
        
        #def clear():
           # print('application: close methode called')
            #self.entryPName.delete(0,1)
            #self.entryColour.delete(0,1)
            #self.entryQty.delete(0,1)
            #self.entrySize.delete(0,1)
            #self.entryCostPrice.delete(0,1)
            #self.entryExpense.delete(0,1)
            #self.entrySellPrice.delete(0,1)
            #self.entryPid.delete(0,1)
            #print('application: clear methode finish\n')
            #return
           
        def reset():
            print('application: reset methode called')
            self.entryPName.delete(0,END)
            self.entryColour.delete(0,END)
            self.entryQty.delete(0,END)
            self.entrySize.delete(0,END)
            self.entryCostPrice.delete(0,END)
            self.entryExpense.delete(0,END)
            self.entrySellPrice.delete(0,END)
            self.entryPid.delete(0,END)
            self.entryQty2.delete(0,END)
            print('application: reset methode finish\n')
            return
#----------------------------------------------------------------------------------#        
        '''referencing database functions with this fuctions to save\
            product details OR retrieve details in databae'''
#-------saving product ddetails on data base        
        def insertData():
            print('application: insert methode called')
            if (len(PName.get()) != 0):
                objData.insert(PName.get(),Colour.get(),Qty.get(),Size.get(),
                               CostPrice.get(),Expense.get(),SellPrice.get())
                productList.delete(0,END)
                productList.insert(END,(PName.get(),Colour.get(),Qty.get(),
                               Size.get(),CostPrice.get(),Expense.get(),SellPrice.get()))
            else:
                 tkinter.messagebox.askokcancel('AMAZING COLLECTIONS STOCK',\
                                                'You must provid the product name')
            print('application: insert methode finish\n')
            
        def showStock():
            print('application: showStock methode called')
            productList.delete(0,END)
            for row in objData.show():
                productList.insert(END,row,str(''))
            print('application: showStock methode finish\n')
            
        '''Using Event Driven Function'''
# --------using curselection  methode to query current selection and get the result-----        
        def showSelection(event):
            print('application: showSelection methode called')
            global result
            saerchClick = productList.curselection()[0] #return list index
            result = productList.get(saerchClick)
            #print(result)
            '''Assigning cursor event to all entry'''
            self.entryPid.delete(0,END)
            self.entryPid.insert(END,result[0])
            
            self.entryPName.delete(0,END)
            self.entryPName.insert(END,result[1])
            
            self.entryColour.delete(0,END)
            self.entryColour.insert(END,result[2])
            
            self.entryQty.delete(0,END)
            self.entryQty.insert(END,result[3])
            #print(result[3])
            self.entrySize.delete(0,END)
            self.entrySize.insert(END,result[4])
            
            self.entryCostPrice.delete(0,END)
            self.entryCostPrice.insert(END,result[5])
            
            self.entryExpense.delete(0,END)
            self.entryExpense.insert(END,result[6])
            
            self.entrySellPrice.delete(0,END)
            self.entrySellPrice.insert(END,result[7])
            
            self.entryQty2.delete(0,END)
            print('application: showSelection methode finished\n')    

        '''DELETING RECORD FROM DATA BASE BY SELECTIN DAIA FROM LISTBOX'''
        def deleteData():
            print('application: deletData methode called')
            if (len(PName.get()) != 0):
                objData.delete(result[0])
                reset()
                showStock()
            print('application: deletData methode finished\n')
        
        '''SEARCHING FOR DATABASE CONTENT USING ANY DETAIL IN DATA BASE'''    
        def searchData():
            print('application: searchData methode called')
            productList.delete(0,END)
            for row in objData.search(PName.get(),Colour.get(),Qty.get(),Size.get(),
                               CostPrice.get(),Expense.get(),SellPrice.get()):
                productList.insert(END,row,str(''))
            print('application: searchData methode finished\n')
            
        def updateDate():
            print('application:updateData methode called')
            
            if (len(PName.get()) != 0):
                objData.delete(result[0])
            if (len(PName.get()) != 0):
                num = int(result[3])
                Qtysum = num + int(newQty.get())
                objData.insert(PName.get(),Colour.get(),Qtysum,Size.get(),
                              CostPrice.get(),Expense.get(),SellPrice.get())
                productList.delete(0,END)
                productList.insert(END,(PName.get(),Colour.get(),Qty.get(),
                              Size.get(),CostPrice.get(),Expense.get(),SellPrice.get()))
            print('application:updateData methode finished\n')
        '''Creating different Frames GUI'''
#-------------------------------------------------------------------------------       
        mainFrame = Frame(self.root,bg='red')
        mainFrame.grid()
        
        headFrame = Frame(mainFrame,bg='white',bd=1,padx=45,pady=10,
                     relief=RIDGE)
        headFrame.pack(side=TOP)
        
        self.labelTitle = Label(headFrame,font=('arial',40,'bold'),fg='red',
                           text='AMAZING COLLECTIONS STOCK INVENTORY',bg='white')
        self.labelTitle.grid()
        
        operationFrame = Frame(mainFrame,bg='white',bd=2,width=1300,height=45,
                               padx=45,pady=10,relief=RIDGE)
        operationFrame.pack(side=BOTTOM)
        
        bodyFrame = Frame(mainFrame,bg='white',bd=2,width=1280,height=500,
                               padx=30,pady=20,relief=RIDGE)
        bodyFrame.pack(side=BOTTOM)
        '''creating frames containing label 'LabelFrame'''
         
        leftbodyFrame = LabelFrame(bodyFrame,bg='yellow',bd=2,width=600,height=280,
                               padx=20,pady=10,relief=RIDGE,
                               font=('arial',15,'bold'),text='Stock Items:')
        leftbodyFrame.pack(side=LEFT)
        
        rightbodyFrame = LabelFrame(bodyFrame,bg='yellow',bd=2,width=450,height=400,
                               padx=20,pady=10,relief=RIDGE,
                               font=('arial',15,'bold'),text='Stock Items Details:')
        rightbodyFrame.pack(side=RIGHT)
        
        ''' adding widget or coponents with their label'''
#------------------------------------------------------------------------------        
        #self.Pidlabel = Label(leftbodyFrame,bg='white',padx=2,fg='blue',
                               #font=('arial',15,'bold'),text='Product id:')
        #self.Pidlabel.grid(row=0,column=0,sticky=W)
        #self.entryPid = Entry(leftbodyFrame,bg='white',width=35,
                                #font=('arial',20,'bold'),textvariable=Pid)
        #self.entryPid.grid(row=0,column=1,sticky=W)
        
        
        self.PNamelabel = Label(leftbodyFrame,bg='white',padx=2,fg='blue',
                               font=('arial',15,'bold'),text='Product Name:')
        self.PNamelabel.grid(row=1,column=0,sticky=W)
        self.entryPName = Entry(leftbodyFrame,bg='white',width=35,
                                font=('arial',20,'bold'),textvariable=PName)
        self.entryPName.grid(row=1,column=1,sticky=W)
        
        
        self.Colourlabel = Label(leftbodyFrame,bg='white',padx=2,fg='blue',
                               font=('arial',15,'bold'),text='Product Colour:')
        self.Colourlabel.grid(row=2,column=0,sticky=W)
        self.entryColour = Entry(leftbodyFrame,bg='white',width=35,
                                font=('arial',20,'bold'),textvariable=Colour)
        self.entryColour.grid(row=2,column=1,sticky=W)
        
        
        self.Qtylabel = Label(leftbodyFrame,bg='white',padx=2,fg='blue',
                               font=('arial',15,'bold'),text='Product Quantity:')
        self.Qtylabel.grid(row=3,column=0,sticky=W)
        self.entryQty = Entry(leftbodyFrame,bg='white',width=35,
                                font=('arial',20,'bold'),textvariable=Qty)
        self.entryQty.grid(row=3,column=1,sticky=W)
        
        
        self.Sizelabel = Label(leftbodyFrame,bg='white',padx=2,fg='blue',
                               font=('arial',15,'bold'),text='Product Size:')
        self.Sizelabel.grid(row=4,column=0,sticky=W)
        self.entrySize = Entry(leftbodyFrame,bg='white',width=35,
                                font=('arial',20,'bold'),textvariable=Size)
        self.entrySize.grid(row=4,column=1,sticky=W)
        
        
        self.CostPricelabel = Label(leftbodyFrame,bg='white',padx=2,fg='blue',
                               font=('arial',15,'bold'),text='Cost Price:')
        self.CostPricelabel.grid(row=5,column=0,sticky=W)
        self.entryCostPrice = Entry(leftbodyFrame,bg='white',width=35,
                                font=('arial',20,'bold'),textvariable=CostPrice)
        self.entryCostPrice.grid(row=5,column=1,sticky=W)
        
        
        self.Expenselabel = Label(leftbodyFrame,bg='white',padx=2,fg='blue',
                               font=('arial',15,'bold'),text='Expense:')
        self.Expenselabel.grid(row=6,column=0,sticky=W)
        self.entryExpense = Entry(leftbodyFrame,bg='white',width=35,
                                font=('arial',20,'bold'),textvariable=Expense)
        self.entryExpense.grid(row=6,column=1,sticky=W)
        
        
        self.SellPricelabel = Label(leftbodyFrame,bg='white',padx=2,fg='blue',
                               font=('arial',15,'bold'),text='Selling Price:')
        self.SellPricelabel.grid(row=7,column=0,sticky=W)
        self.entrySellPrice = Entry(leftbodyFrame,bg='white',width=35,
                                font=('arial',20,'bold'),textvariable=SellPrice)
        self.entrySellPrice.grid(row=7,column=1,sticky=W)
        
        self.dommy2 = Label(leftbodyFrame,padx=2,bg='yellow')
        self.dommy2.grid(row=8,column=0,sticky=W)
        self.dommy2 = Label(leftbodyFrame,padx=2,bg='yellow')
        self.dommy2.grid(row=9,column=0,sticky=W)
        self.dommy2 = Label(leftbodyFrame,padx=2,bg='yellow')
        self.dommy2.grid(row=10,column=0,sticky=W)
        
        self.dommy2 = Label(rightbodyFrame,padx=2,bg='yellow')
        self.dommy2.grid(row=8,column=0,sticky=W)
        self.dommy2 = Label(rightbodyFrame,padx=2,bg='yellow')
        self.dommy2.grid(row=9,column=0,sticky=W)
        self.dommy2 = Label(rightbodyFrame,padx=2,bg='yellow')
        self.dommy2.grid(row=10,column=0,sticky=W)
        
        self.Pidlabel = Label(leftbodyFrame,bg='white',padx=2,fg='red',
                               font=('arial',15,'bold'),text='Product id:')
        self.Pidlabel.grid(row=11,column=0,sticky=W)
        self.entryPid = Entry(leftbodyFrame,bg='white',width=35,
                                font=('arial',20,'bold'),textvariable=Pid)
        self.entryPid.grid(row=11,column=1,sticky=W)
        
        self.Qty2label = Label(leftbodyFrame,bg='white',padx=2,fg='red',
                               font=('arial',15,'bold'),text='Additional Quantity:')
        self.Qty2label.grid(row=12,column=0,sticky=W)
        self.entryQty2 = Entry(leftbodyFrame,bg='white',width=35,
                                font=('arial',20,'bold'),textvariable=newQty)
        self.entryQty2.grid(row=12,column=1,sticky=W)
        
#-------------------------------------------------------------------------------        
        '''Adding Scroll Bar To listbox widget'''
        scroll = Scrollbar(rightbodyFrame)
        scroll.grid(row=0,column=1,sticky=NS)
        '''Creating a listbox and Adding listbox to scrollbar '''
        productList = Listbox(rightbodyFrame,width=40,height=16,
                              font=('arial',12,'bold'),yscrollcommand=scroll.set)
        productList.grid(row=0,column=0)
        '''setting the scrollbar command to vertical view of the listbox'''
        scroll.config(command=productList.yview) 
        '''Binding cursor Event and Handler methode Selection to listbox/productlist'''
        productList.bind('<<ListboxSelect>>',showSelection)
#-------------------------------------------------------------------------------#
        '''Adding Buttons to the Operation Frame'''
        self.btSave = Button(operationFrame,text='Save', font=('arial',15,'bold'),
                             height=1,width=10,bd=4,command=insertData)
        self.btSave.grid(row=0,column=0)
        
        self.btShowdata = Button(operationFrame,text='Show Data', font=('arial',15,'bold'),
                             height=1,width=10,bd=4,command=showStock)
        self.btShowdata.grid(row=0,column=1)
        
        #self.btClear = Button(operationFrame,text='Clear', font=('arial',15,'bold'),
                             #height=1,width=10,bd=4,command=clear)
        #self.btClear.grid(row=0,column=2)
        
        self.btDelete = Button(operationFrame,text='Delete', font=('arial',15,'bold'),
                             height=1,width=10,bd=4,command=deleteData)
        self.btDelete.grid(row=0,column=3)
        
        self.btSearch = Button(operationFrame,text='Search', font=('arial',15,'bold'),
                             height=1,width=10,bd=4,command=searchData)
        self.btSearch.grid(row=0,column=4)
        
        self.btUpdate = Button(operationFrame,text='Update', font=('arial',15,'bold'),
                             height=1,width=10,bd=4,command=updateDate)
        self.btUpdate.grid(row=0,column=5)
        
        self.btClose = Button(operationFrame,text='Close', font=('arial',15,'bold'),
                             height=1,width=10,bd=4,command=close)
        self.btClose.grid(row=0,column=6)
        
        self.btReset = Button(operationFrame,text='Reset', font=('arial',15,'bold'),
                             height=1,width=10,bd=4,command=reset)
        self.btReset.grid(row=0,column=7)
        '''End of Front End Graphic User interface section'''
#--------------------------------------------------------------------------------------#        
#Back End Data Base Operation
#ceating or connetion database
#creating cursor
#creating table
#updating database
class database():
    def connecting(self):
        print('Database: connection methode called')
        conn = sqlite3.connect('UPDATEINVENTORY.db')
        coso = conn.cursor()
        query ='CREATE TABLE IF NOT EXISTS mystockData(pid INTEGER PRIMARY KEY,name TEXT,\
            colour TEXT,quantity TEXT,size TEXT,costprice TEXT,expense TEXT,sellprice TEXT)'
        coso.execute(query)
        conn.commit()
        conn.close()
        print('Database: connection methode finished \n')
        
    def insert(self,name,colour,quantity,size,costprice,expense,sellprice):
        print('Database: insert methode called')
        conn = sqlite3.connect('UPDATEINVENTORY.db')
        coso = conn.cursor()
        query ='INSERT INTO mystockData VALUES(NULL,?,?,?,?,?,?,?)' 
            
        coso.execute(query,(name,colour,quantity,size,costprice,expense,sellprice))
        conn.commit()
        conn.close()
        print('Database: insert methode finished \n')
        
    def show(self):
        print('Database: show methode called')
        conn = sqlite3.connect('UPDATEINVENTORY.db')
        coso = conn.cursor()
        query ='SELECT * FROM mystockData'
        coso.execute(query)
        rows = coso.fetchall()
        conn.commit()
        conn.close()
        print('Database: show methode finished \n')
        return rows
    
    def delete(self,pid):
        print('Database: delete methode called')
        conn = sqlite3.connect('UPDATEINVENTORY.db')
        coso = conn.cursor()
        query ='DELETE FROM mystockData WHERE pid=?'
        coso.execute(query,[pid]) # add the str because of valueError because pid type is text
        conn.commit()
        conn.close()
        print('Database: delete methode finished \n')
        
    def search(self,name='',colour='',quantity='',size='',costprice='',\
               expense='',sellprice=''):
        print('Database: search methode called')
        conn = sqlite3.connect('UPDATEINVENTORY.db')
        coso = conn.cursor()
        query ='SELECT * FROM mystockData WHERE name=? or colour=?\
             or quantity=? or size=? or costprice=?  or expense=? or sellprice=?'
        coso.execute(query,(name,colour,quantity,size,costprice,expense,sellprice))
        rows = coso.fetchall()
        conn.commit()
        conn.close()
        print('Database: search methode finished \n')
        return rows
    
    def update(self,pid,name='',colour='',quantity='',size='',costprice='',\
               expense='',sellprice=''):
        print('Database: update methode called')
        conn = sqlite3.connect('UPDATEINVENTORY.db')
        coso = conn.cursor()
        query ='UPDATE mystockData SET name=?,colour=?,quantity=?,size=?,\
              costprice=?,expense=?,sellprice=? WHERE pid=?'
        coso.execute(query,(name,colour,quantity,size,costprice,expense,sellprice,pid))
        conn.commit()
        conn.close()
        print('Database: update methode finished \n')
        
        
    
        

        
if __name__ == '__main__':
    root = Tk()
    application = product(root)
    root.mainloop()
        
    