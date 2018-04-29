from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import os


def newTemplate():
    #Clears the text box of previous text and adds the Add Break button to the UI.
    text.delete(0.0, END)
    breakButton = Button(window, text='Add Break', width=12, command=detectClick)
    breakButton.pack()


def detectClick():
    #Runs when the Add Break button is clicked and adds a click event handler.
    window.bind('<Button-1>', addBreak)


def addBreak(event):
    #Adds a break to the text box when the box is clicked after the Add Break button is clicked and then removes the event handler.
    text.insert(str(event.x) + '.' + str(event.y), '|-----|')
    window.unbind('<Button-1>')


def saveFile():
    #Allows the user to save the contents of the text box to be saved where the user selects from their file system and then clears the text box.
    newFile = asksaveasfile(mode='w', defaultextension='.txt')
    newText = text.get(0.0, END)
    try:
        newFile.write(newText.rstrip())
        text.delete(0.0, END)
    except:
        showerror(title='Failure', message='File failed to save.')


def setTemplate():
    #Adds an entry box for the user to insert the the name of the template they made and adds a save button for the template.
    templateName = Entry(window, width=75, bg='white')
    templateName.pack()
    saveButton = Button(window, text='Save', width=4, command=lambda: saveTemplate(templateName.get(), templateName, saveButton))
    saveButton.pack()


def saveTemplate(templateName, entry, button):
    #Creates a file in the template folder with the name they gave it along with a .tem extension and then removes the entry box and save button.
    if str(templateName) != '':
        templetCreate = open('./Templates/' + str(templateName) + '.tem', 'w')
        newTemplate = text.get(0.0, END)
        templetCreate.write(newTemplate)
        templetCreate.close()
        text.delete(0.0, END)
        entry.pack_forget()
        button.pack_forget()
    else:
        showerror(title='Failure', message='Template requires a name.')


def selectTemplate():
    #Goes through the templates folder and adds a button for each of the users saved templates.
    templateButtons = []
    for file in os.listdir('./Templates/'):
        if file.endswith('.tem'):
            templateButtons.append(Button(window, text=file[:-4], width=12, command=lambda file=file: openTemplate(file, templateButtons)))
    for i in templateButtons:
        i.pack()


def openTemplate(selTemp, templateButtons):
    #Opens the template selected by the user and then removes the buttons.
    template = open('./Templates/' + selTemp, 'r')
    templateText = template.read()
    text.delete(0.0, END)
    text.insert(0.0, templateText)
    template.close()
    for i in templateButtons:
        i.pack_forget()


window = Tk()
window.title('Right-Up tool')
window.configure(background='gray')

text = Text(window, width=75, height=6)
text.pack()

Button(window, text='New Template', width=12, command=newTemplate).pack()
Button(window, text='Open Template', width=12, command=selectTemplate).pack()
Button(window, text='Save File', width=12, command=saveFile).pack()
Button(window, text='Save Template', width=12, command=setTemplate).pack()
window.mainloop()