from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
class espaceEtudiant:
    def __init__(self,root):
        self.root = root
        self.root.title('espace Etudiant ')
        self.root.geometry('1920x1080+0+0')# 1366x768
        #-----------------------------------------------------------------------------------
        self.header = Frame(self.root, bg="#009df4")#, width=1300, height=680
        self.header.place(x=300, y=0, width=1070, height=60)
       #-------------------------------------------------------------------------------------
        logout_label = Label(self.header, text="Se déconnecter", bg='#009df4', fg="white",
                             font=("yu gothic ui", 14, "bold"))
        logout_label.place(x=755, y=15)

        logout_image = Image.open('images\\logout1.png')
        photo = ImageTk.PhotoImage(logout_image)
        self.logout_btn =Button(self.root, image=photo, bg='#009df4', command=lambda: exit())
        self.logout_btn.image = photo
        self.logout_btn.place(x=1200, y=0, width=50, height=60)
        # --------------- icon notifa
        nt_image = Image.open('images\\nt.png')
        photo = ImageTk.PhotoImage(nt_image)
        self.nt_btn = Label(self.root, image=photo, bg='#009df4')
        self.nt_btn.image = photo
        self.nt_btn.place(x=990, y=0 ,width=40, height=60)

        msg_image = Image.open('images\\msg.png')
        photo = ImageTk.PhotoImage(msg_image)
        self.msg_btn = Label(self.root, image=photo, bg='#009df4')
        self.msg_btn.image = photo
        self.msg_btn.place(x=937, y=0, width=50, height=60)

        srch_image = Image.open('images\\srch.png')
        photo = ImageTk.PhotoImage(srch_image)
        self.srch_btn = Label(self.root, image=photo, bg='#009df4')
        self.srch_btn.image = photo
        self.srch_btn.place(x=310, y=9)#width=220, height=60

        self.srch_entry = Entry(self.root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                 font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
        self.srch_entry.place(x=315, y=12,width=270, height=40)
        # ========================================================================
        # -------------   sideBar  ----------------------
        self.sidebar = Frame(self.root, bg='white')
        self.sidebar.place(x=0, y=0, width=300, height=750)
        # ----------------------BODY  -----------------
        self.heading = Label(self.root, text="tableau de bord", fg='#0064d3', bg="#eff5f6",
                             font=("yu gothic ui", 13, "bold"))
        self.heading.place(x=325, y=60)


       #----- ------------ side bar -------------------
        self.logo_image = Image.open('images\\iconUser.png')
        photo = ImageTk.PhotoImage(self.logo_image)
        self.logo = Label(self.sidebar, image=photo, bg='#ffffff')
        self.logo.image = photo
        self.logo.place(x=70, y=80)



        self.brandeName = Label(self.sidebar, text = 'Etudiant' , bg ='#ffffff',font=("", 15, "bold"))
        self.brandeName.place(x=89, y=208)



        # Accueil
        self.Accueil_image = Image.open('images\\ac.png')
        photo = ImageTk.PhotoImage(self.Accueil_image)
        self.Accueil = Label(self.sidebar, image=photo, bg='lightSteelBlue2')
        self.Accueil.image = photo
        self.Accueil.place(x=50, y=280)

        self.Accueil_txt = Button(self.sidebar, text='Accueil', bg='white', fg='black', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='lightSteelBlue2')
        self.Accueil_txt.place(x=110, y=287)

        # cours
        self.cours_image = Image.open('images\\cours.png')
        photo = ImageTk.PhotoImage(self.cours_image)
        self.cours = Label(self.sidebar, image=photo, bg='lightSteelBlue2')
        self.cours.image = photo
        self.cours.place(x=50, y=350)

        self.cours_txt = Button(self.sidebar, text='cours', bg='white', fg='black', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='lightSteelBlue2')
        self.cours_txt.place(x=110, y=359)

        # Bibliothèque
        self.Bibliotheque_image = Image.open('images\\Bibliotheque.png')
        photo = ImageTk.PhotoImage(self.Bibliotheque_image)
        self.Bibliotheque= Label(self.sidebar, image=photo, bg='lightSteelBlue2')
        self.Bibliotheque.image = photo
        self.Bibliotheque.place(x=50, y=418)

        self.Bibliotheque_txt = Button(self.sidebar, text='Bibliothèque', bg='white', fg='black', font=("", 13, "bold"), bd=0,
                                cursor='hand2', activebackground='lightSteelBlue2')
        self.Bibliotheque_txt.place(x=105, y=428)

        # Demande
        self.demande_image = Image.open('images\\demande.png')
        photo = ImageTk.PhotoImage(self.demande_image)
        self.demande = Label(self.sidebar, image=photo, bg='lightSteelBlue2')
        self.demande.image = photo
        self.demande.place(x=50, y=488)

        self.demande_txt = Button(self.sidebar, text='Demande', bg='white', fg='black', font=("", 13, "bold"),
                                       bd=0,
                                       cursor='hand2', activebackground='lightSteelBlue2')
        self.demande_txt.place(x=105, y=500)

        # settings
        self.settings_image = Image.open('images\\st.png')
        photo = ImageTk.PhotoImage(self.settings_image)
        self.settings = Label(self.sidebar, image=photo, bg='lightSteelBlue2')
        self.settings.image = photo
        self.settings.place(x=50, y=565)

        self.settings_txt = Button(self.sidebar, text='Parametres', bg='white', fg='black', font=("", 13, "bold"),
                                  bd=0,
                                  cursor='hand2', activebackground='lightSteelBlue2')
        self.settings_txt.place(x=105, y=580)

        # ------------------  Body frame 1 -----------------------------------
        self.bodyFrame1 = Frame(self.root, bg='lightgrey')
        self.bodyFrame1.place(x=328, y=90, width=1000, height=560)
        #images
        self.mg_image = Image.open('images\\cr.png')
        photo = ImageTk.PhotoImage(self.mg_image)
        self.mg = Label(self.bodyFrame1 , image=photo, bg='lightgrey')
        self.mg.image = photo
        self.mg.place(x=585, y=0)
        # ----------------- second img --------------------
        self.mg_image = Image.open('images\\tous.png')
        photo = ImageTk.PhotoImage(self.mg_image)
        self.mg = Label(self.bodyFrame1, image=photo, bg='lightgrey')
        self.mg.image = photo
        self.mg.place(x=-15, y=430)

        self.esp_image = Image.open('images\\esp.png')
        photo = ImageTk.PhotoImage(self.esp_image)
        self.esp= Label(self.bodyFrame1, image=photo, bg='lightgrey')
        self.esp.image = photo
        self.esp.place(x=30, y=15)


root = Tk()
obj= espaceEtudiant(root)
root.mainloop()

