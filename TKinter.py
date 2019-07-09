
# coding: utf-8

# In[1]:

from tkinter import *

window = Tk()
labelWindow = Label(window, text = 'Hello World')
labelWindow.pack()
window.mainloop()


# In[2]:

#Window and form/display
window = Tk()

ftop = Frame(window)
ftop.pack(side = TOP)
fbot = Frame(window)
fbot.pack(side = BOTTOM)

tLabel = Label(ftop, text='top label')
tlabel1 = Label(ftop, text='new l')
bLabel = Label(fbot, text='bottom label')

tLabel.pack(side=RIGHT)
tlabel1.pack(side=LEFT)
bLabel.pack(side = RIGHT)

window.mainloop()


# In[5]:

#click
wn = Tk()

def buttonClick(x):
    print(x)

btn = Button(wn, bd = 50, bg = 'red', fg = 'white', text = 'Hello', padx = 50, pady = 80, command=buttonClick('clicked'))
btn.place(x=100,y=100)

window.mainloop()


# In[11]:

## Entry
wn = Tk()

def PrintValue():
    print (userWrote.get())

userWrote = StringVar()
userWrote.trace('w', lambda name, index, mode: PrintValue())

e = Entry(wn, bd=10, bg='black',fg='white', textvariable=userWrote)
e.pack()

window.mainloop()



# In[12]:

#Entry

window = Tk()

def printValue():
    print(userWrote.get())

userWrote=StringVar()
userWrote.trace('w', lambda name, index, mode: printValue())
e = Entry(window, bd = 10, bg='green', fg='black', textvariable=userWrote)
e.pack()

window.mainloop()


# In[20]:

import kivy




# In[21]:

class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

x = person('Aman', 'Aktar')
x. printname()


# In[22]:

class student(person):
    pass

y = student('Sadia', 'Aman')
y.printname()


# In[25]:

class personalInfo:
    def __init__(self, fname, lname, age, address, occupation):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.address = address
        self.occupation = occupation
    
    def printPersonalInfo(self):
        print(self.fname, self.lname, self.age, self.address, self.occupation)


# In[28]:

class newEmploye(personalInfo):
    pass

emp1 = newEmploye('Akt', 'Aman,', 32,',' 'Palmdale, CA,', 'Engineer')

emp1.printPersonalInfo()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



