################
#Carré Victoria#
#########################################################################
# Le but de ce programme est de présenter une fenetre de dialogue        #
# permetant de coder ou décoder un message. Les trois styles d'encodages #
# pris en compt sont l'avocat, l'avocette et le cesar.                   #
#                                                                        #
# Pour décrypter un message cesar, l'application va renvoyer les dix     #
# décalages les plus plosible en fonction des dix lettres de             #
# l'alphabet les plus utilisé.                                           #
#                                                                        #
# Cette application utilise la bibliothèque tkinter permetant de créé    #
# des fenetres de dialogue en python. Si le programme ne fonctionne pas  #
# correctement c'est peut être par ce qu'elle n'est pas insallé.         #
##########################################################################

from tkinter import *

a=list('abcdefghijklmnopqrstuvwxyz')
A=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

root = Tk()
root.geometry('550x300')
root.minsize(670,300)
root.title('Cryptographie')
root.config(bg='light blue')

Label(root, text='Avocat, Avocette & Cesar', bg='light blue', font=('Courier New',23), cursor="star").grid(column=1, row=0, columnspan=2, padx=100, pady=10)
Label(root, text='formulaire de commande', bg='light blue', font=('Courier New',17), cursor="star").grid(column=1, row=1, columnspan=2, pady=5)
Label(root, text="Type de cryptage :",bg='light blue', font=('Courier New',13, 'underline')).grid(column=1, row=2, pady=10, padx=5)
Label(root, text="Type de methode :",bg='light blue', font=('Courier New',13, 'underline')).grid(column=2, row=2, pady=10, padx=5)

v = IntVar ()
Radiobutton (root, variable = v, value = 10, text="Avocat", bg='light blue').grid(column=1, row=4, sticky="w", padx=100)
Radiobutton (root, variable = v, value = 20, text="Avocette", bg='light blue').grid(column=1, row=5, sticky="w", padx=100)
Radiobutton (root, variable = v, value = 30, text="Cesar", bg='light blue').grid(column=1, row=6, sticky="w", padx=100)

w = IntVar ()
Radiobutton (root, variable = w, value = 10, text="Coder", bg='light blue').grid(column=2, row=4, sticky="w", padx=100)
Radiobutton (root, variable = w, value = 20, text="Décoder", bg='light blue').grid(column=2, row=5, sticky="w", padx=100)

def ok1 ():
    if v.get() == 10:
        if w.get() == 10:
            codeAvocat()
        elif w.get() == 20: 
           #decodeAvocat()
           print("plus d'actualité")
    elif v.get() == 20:
        if w.get() == 10:
            codeAvocette()
        elif w.get() == 20:
            #decodeAvocette()
            print("plus d'actualité")
    elif v.get() == 30:
        if w.get() == 10:
            codeCesar()
        elif w.get() == 20:
            decodeCesar()

def codeAvocat ():
    global e1, a, A, e3
    launch('Codage Avocat')

    def OKcodeAvocat ():
        newMessage = ''
        for i in e1.get('0.0','end-1c'):
            if i in a:
                newMessage += a[(a.index(i)+10)%26]
            elif i in A:
                newMessage += A[(A.index(i)+10)%26]
            else:
                newMessage += i
        return newMessage
        e3.delete("0.0", "end")
        e3.insert('0.0',newMessage)

    def OKdecodeAvocat ():
        newMessage = ''
        for i in e3.get('0.0','end-1c'):
            if i in a:
                newMessage += a[(a.index(i)-10)%26]
            elif i in A:
                newMessage += A[(A.index(i)-10)%26]
            else:
                newMessage += i
        return newMessage
        e1.delete("0.0", "end")
        e1.insert('0.0',newMessage)

    def convertir ():  # à refaire ici
        messageClair = e1.get('0.0','end-1c')
        messageCrypte = e3.get('0.0','end-1c')
        if messageClair == OKdecodeAvocat():
            None 
        print('en construction')

    Button(second, text='ok', command=OKcodeAvocat).grid(column=0, row=5, sticky='we', padx=150, pady=5)
    Button(second, text='ok', command=OKdecodeAvocat).grid(column=1, row=5, sticky='we', padx=150, pady=5)
    Button(second, text='convertir !', command=convertir).grid(column=0, row=6, sticky='we', padx=150, pady=5, columnspan=2)

def codeAvocette ():
    global a, A
    launch('Codage Avocette')

    def OKcodeAvocette ():
        newMessage = ''
        for i in e1.get('0.0','end-1c'):
            if i in a:
                newMessage += str(((a.index(i))+7)%33)+" "
            elif i in A:
                newMessage += str(((A.index(i))+7)%33)+" "
            else:
                newMessage += i
        e3.delete("0.0", "end")
        e3.insert('0.0',newMessage)

    def OKdecodeAvocette() :
        l2.grid_forget
        tableMessage = []
        newMessage = ''
        nb = ''
        n=list('0123456789')
        
        for i in range (len(e3.get('0.0','end-1c'))):
            if (e3.get('0.0','end-1c')[i] in n) == False :
                if nb == '':
                    None
                else:
                    tableMessage.append(int(nb))
                    nb = ''
            else:
                nb += e3.get('0.0','end')[i]
                if i == len(e3.get('0.0','end-1c'))-1:
                    tableMessage.append(int(nb))
        
        for i in range (len(tableMessage)):
            if (tableMessage[i]) > 32 or (tableMessage[i]) < 7:
                #second.geometry("410x400")
                newMessage = "Erreur : \nUn des nombres n'est pas \ncomvenable (>32 ou <7)"
                break
            else:
                newMessage += a[(tableMessage[i]-7)%32]

        e1.delete("0.0", "end")
        e1.insert('0.0',newMessage)

    Button(second, text='ok', command=OKcodeAvocette).grid(column=0, row=5, sticky='we', padx=150, pady=5)
    Button(second, text='ok', command=OKdecodeAvocette).grid(column=1, row=5, sticky='we', padx=150, pady=5)







def codeCesar ():
    global e1, a, A
    launch('Codage Cesar')
    labelTitre.grid(column=0, row=0, padx=70, pady=10)
    l1.grid(column=0, row=1, padx=30, pady=5)
    e1.grid(column=0, row=2, padx=30, pady=5)

    def OKcodeCesar ():
        newMessage = ''
        for i in e1.get('0.0','end-1c'):
            if i in a:
                newMessage += a[(a.index(i)+int(e2.get()))%26]
            elif i in A:
                newMessage += A[(A.index(i)+int(e2.get()))%26]
            else:
                newMessage += i

        second.geometry("420x420")

        Label(second, text='Votre message codé est : ', bg='light green', font=('Courier New',17)).grid(column=0, row=6)
        Label(second, text=newMessage, bg='light green', font=('Courier New',17)).grid(column=0, row=7)

    Label(second, text="nombre de décalage : ", bg='light green', font=('Courier New',17)).grid(column=0, row=3)

    x = IntVar()  
    e2 = Scale(second, variable = x, from_ = -26, to = 26 , orient = HORIZONTAL,) # bg='light green' 
    e2.grid(column=0, row=4)

    Button(second, text='ok', command=OKcodeCesar).grid(column=0, row=5, sticky='we', padx=150, pady=5)


def decodeCesar ():
    global e1, a, A
    launch('Décodage Cesar')
    labelTitre.grid(column=0, row=0, padx=70, pady=10)
    l1.grid(column=0, row=1, padx=30, pady=5)
    e1.grid(column=0, row=2, padx=30, pady=5)
    
    def OKdecodeCesar ():
        tableProbable = [a.index('e'),a.index('s'),a.index('a'),a.index('r'),a.index('t'),a.index('i'),a.index('n'),a.index('u'),a.index('l'),a.index('o')] # index dans la liste de l'alphabet des 10 lettre les plus utiliser en français
        second.geometry("420x570")
        oc=[] # occurence
        for j in range(26):
            oc=oc+[0]
        
        for i in e1.get('0.0','end-1c'):
            if i in a:
                oc[a.index(i)]=oc[a.index(i)]+1
            if i in A:
                oc[A.index(i)]=oc[A.index(i)]+1

        maxi=oc.index(max(oc)) #l'index de la lettre qui a la plus grande occurence

        Label(second, text='Propositions de décryptages : ', bg='light green', font=('Courier New',17)).grid(column=0, row=6)

        for j in tableProbable:
            newMessage = ''
            for i in e1.get('0.0','end-1c'):
                decalage = j-maxi
                if i in a:
                    newMessage += a[(a.index(i)+decalage)%26]
                elif i in A:
                    newMessage += A[(A.index(i)+decalage)%26]
                else:
                    newMessage += i
            Label(second, text=newMessage, bg='light green', font=('Courier New',17)).grid(column=0, row=(tableProbable.index(j))+7)
                

    Button(second, text='ok', command=OKdecodeCesar).grid(column=0, row=5, sticky='we', padx=150, pady=5)





def launch(titre):
    global second, e1, l1, labelTitre, l2, e3, l3
    second = Toplevel()
    second.title("Cryptographie")
    second.geometry("710x330")
    second.config(bg='light green')

    labelTitre = Label(second, text=titre, bg='light green', font=('Courier New',23), cursor="star")
    l1 = Label(second, text='Entrez votre message : ', bg='light green', font=('Courier New',17))
    #l2 = Label(second, text='Resultat : ', bg='light green', font=('Courier New',17))
    l2 = Label(second, text='massage en claire : ', bg='light green', font=('Courier New',17))
    l3 = Label(second, text='massage crypté : ', bg='light green', font=('Courier New',17))

    e1 = Text(second)
    e1.config (width = 30, height = 4)
    
    e3 = Text(second)
    e3.config (width = 30, height = 4)

    labelTitre.grid(column=0, row=0, padx=70, pady=10, columnspan=2)

    e1.grid(column=0, row=2, padx=30, pady=5) # zone de text pour entrer un message clair
    
    e3.grid(column=1, row=2, padx=30, pady=5) # zone de text pour entrer un message crypté

    l2.grid(column=0, row=1, padx=30, pady=5 )

    l3.grid(column=1, row=1, padx=30, pady=5 )

btn1 = Button(root, text='ok', command=ok1, cursor='pirate')
btn1.grid(column=1, row=7, sticky="we", columnspan=2, padx=250, pady=10)

root.mainloop()
