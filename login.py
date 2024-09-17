from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image  #pip install pillow
import pymysql

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title('Login Page')
        self.root.geometry('1166x718')#1500x780+230+250
        self.root.configure(background='SkyBlue2')#108cff

        # ============background Image ===================
        bg_frame = Image.open('images\\background1.png')
        photo = ImageTk.PhotoImage(bg_frame)
        self.bg_panel = Label(self.root, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')

        # ============= login frame ================
        lgn_frame = Frame(self.root, bg='black', width=950, height=570)
        lgn_frame.place(x=100, y=60)

        title= Label(lgn_frame, text='BIENVENUE', font=('yu gothic ui', 25, 'bold'), bg='#040405', fg='white',
                             bd=5,
                             relief=FLAT)
        title.place(x=80, y=30, width=300, height=30)

        # ============ Left Side Image ================================================
        # ========================================================================
        side_image = Image.open('images\\vector.png')
        photo = ImageTk.PhotoImage(side_image)
        self.side_image_label = Label(self.root, image=photo, bg='black')
        self.side_image_label.image = photo
        self.side_image_label.place(x=99, y=120)
        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
        sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(sign_in_image)
        self.sign_in_image_label = Label(self.root, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=720, y=180)
        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        sign_in_label = Label(lgn_frame, text="Se connecter", bg="#040405", fg="white",
                                   font=("yu gothic ui", 17, "bold"))
        sign_in_label.place(x=630, y=240)
        # ============================== Username ==========================
        email_entry_label = Label(lgn_frame, text="nom d'utilisateur", bg='black', font=('yu gothic ui', 13, 'bold'),
                                    fg='#4f4e4d')
        email_entry_label.place(x=530, y=284)
        self.email_entry = Entry(self.root, highlightthickness=0, relief=FLAT, bg="black", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"), insertbackground='#6b6a69')
        self.email_entry.place(x=658, y=377, width=270)
        self.username_line = Canvas(self.root, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=635, y=400)
        # ===== Username icon =========
        username_icon = Image.open('images\\username_icon.png')
        photo = ImageTk.PhotoImage(username_icon)
        self.username_icon_label = Label(self.root, image=photo, bg='#040405')
        self.username_icon_label.image = photo
        self.username_icon_label.place(x=632, y=372)

        # ========================================================================
        # ============================Password====================================
        # ========================================================================
        password_label = Label(lgn_frame, text="le mot de passe", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        password_label.place(x=532, y=353)

        self.passwd_entry = Entry(self.root, highlightthickness=0, relief=FLAT, bg="black", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*", insertbackground='#6b6a69')
        self.passwd_entry.place(x=660, y=440, width=244)

        self.password_line = Canvas(self.root, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=635, y=465)
        # ======== Password icon ================
        password_icon = Image.open('images\\password_icon.png')
        photo = ImageTk.PhotoImage(password_icon)
        self.password_icon_label = Label(self.root, image=photo, bg='#040405')
        self.password_icon_label.image = photo
        self.password_icon_label.place(x=634, y=437)
        # ========================================================================
        # ============================login button================================
        # ========================================================================
        lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(lgn_button)
        lgn_button_label = Label(lgn_frame, image=photo, bg='#040405')
        lgn_button_label.image = photo
        lgn_button_label.place(x=540, y=420)  #text='LOGIN',
        self.login = Button(self.root, text='Connection', command=self.connexion,font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white')
        self.login.place(x=660, y=490)


        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================
        self.forgot_button = Button(self.root, text="Mot de pass oublié ?",command=self.passwd_oublier_fenetre
                                    ,font=("yu gothic ui", 13, "bold underline"),fg="white", relief=FLAT,
                                    activebackground="#040405", borderwidth=0, background="#040405", cursor="hand2")
        self.forgot_button.place(x=720, y=535)

        # =========== Sign Up ==================================================
        sign_label = Label(lgn_frame, text="Pas de compte encore?", font=("yu gothic ui", 11, "bold"),
                                relief=FLAT, borderwidth=0, background="black", fg='white')
        sign_label.place(x=509, y=520)

        self.signup_img = ImageTk.PhotoImage(file='images\\register.png')#98a65d
        self.signup_button_label = Button(self.root, image=self.signup_img, command=self.fenetre_formulaire, bg='#98a65d', cursor="hand2",
                                          borderwidth=0, background="black", activebackground="#040405")#040405
        self.signup_button_label.place(x=770, y=575, width=111, height=35)

        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')
        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.root, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=915, y=445)

    def show(self):
        self.hide_button = Button(self.root, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=915, y=445)
        self.passwd_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.root, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=915, y=445)
        self.passwd_entry.config(show='*')
    def connexion(self):
        if self.email_entry.get()=="" or self.passwd_entry.get()=="":
            messagebox.showerror("Erreur", " Veillez saisir l'Email et le mot de passe", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="",database="enregistrer")
                cur = con.cursor()
                cur.execute("select * from compte where email=%s and password=%s",(self.email_entry.get(),self.passwd_entry.get()))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Erreur", "Invalide L'E-mail ou password", parent=self.root)
                else:
                    messagebox.showinfo("Success", "Bienvenu")
                    self.root.destroy()
                    # -------connexion à la page espaceEtudiant -------------------------------------------------------------
                    import espaceEtudiant
                    con.close()
            except Exception as ex:
                messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}", parent=self.root)

    def passwd_oublier_fenetre(self):
        if self.email_entry.get()=="":
            messagebox.showerror("Erreur", " Veillez donner un email valide ", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="enregistrer")
                cur = con.cursor()
                cur.execute("select * from compte where email=%s",self.email_entry.get())
                row= cur.fetchone()
                if row == None:
                    messagebox.showerror("Erreur", "Invalide Email, veillez entrer un mail valide ", parent=self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Mot de pass oublié")
                    self.root2.config(bg="white")
                    self.root2.geometry("500x800+300+250")
                    self.root2.focus_force()
                    self.root2.grab_set()

                    title= Label(self.root2, text="Mot de pass oublié", font=("algerian", 20,"bold"),bg="SkyBlue2", fg="black")
                    title.pack(side=TOP, fill=X)

                    #====================================
                    # Question
                    #==============================
                    Question_label = Label(self.root2, text="Sélectionnez une Question : ", bg="white",
                                           fg="#4f4e4d", font=("yu gothic ui", 11, "bold"))
                    Question_label.place(x=100, y=75)
                    self.Question_combo = ttk.Combobox(self.root2, font=('yu gothic ui semibold', 12, 'bold'),
                                                       state='readonly',width=35)
                    Question_list = ['select','Film préféré', 'Lieu de naissance', 'Meilleur ami', 'couleur préférée']
                    self.Question_combo['values'] = Question_list
                    self.Question_combo.place(x=100, y=110)
                    self.Question_combo.current(0)
                    #======================
                    # repondre
                    #==================
                    rep_label = Label(self.root2, text="Répondre : ", bg="white",
                                      fg="black", font=("yu gothic ui", 13, "bold"))
                    rep_label.place(x=100, y=195)
                    self.rep_entry = Entry(self.root2, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                           font=("yu gothic ui semibold", 12))

                    self.rep_entry.place(x=200, y=217)
                    self.rep_line = Canvas(self.root2, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
                    self.rep_line.place(x=190, y=240)
                    #================
                    # changer le mot de pass
                    #==================
                    nouvpass = Label(self.root2, text="Nouveau mot de pass : ", bg="white",
                                      fg="black", font=("yu gothic ui", 13, "bold"))
                    nouvpass.place(x=100, y=270)
                    self.nouvpass_entry = Entry(self.root2, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                           font=("yu gothic ui semibold", 12))

                    self.nouvpass_entry.place(x=220, y=298)
                    self.nouvpass_line = Canvas(self.root2, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
                    self.nouvpass_line.place(x=200, y=320)
                    #------------------
                    # Button de changer le mot de pass
                    #-----------------
                    changer_btn = Button(self.root2, text="Modifier", command=self.passwd_oublier, cursor="hand2", font=("algerian", 16,"bold"), bg="SkyBlue2", fg="black")
                    changer_btn.place(x=160, y=350, width=150)
            except Exception as ex:
                messagebox.showerror("Erreur", f"Erreur de connexion{str(ex)}", parent=self.root)

    def passwd_oublier(self):
        if self.Question_combo.get()=="" or self.rep_entry.get()=="" or self.nouvpass_entry.get()=="":
            messagebox.showerror("Erreur", " Remplir les champs", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="enregistrer")
                cur = con.cursor()
                cur.execute("select * from compte where email=%s and question=%s and reponse=%s ",(self.email_entry.get(), self.Question_combo.get(),self.rep_entry.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Erreur", "Vous n'avez pas bien répondu à la question séléctionné ",parent=self.root2)
                else:
                    cur.execute("update compte set password=%s where email=%s",(self.nouvpass_entry.get(),self.email_entry.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Vous avez modifié votre mot de passe avec Succès ",parent=self.root2)
                    self.rein()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Erreur", f"Erreur de connexion{str(es)}", parent=self.root2)

    def rein(self):
        self.Question_combo.current(0)
        self.rep_entry.delete(0,END)
        self.nouvpass_entry.delete(0,END)


    # connection à la page formulaire -----------------------------------------------------
    def fenetre_formulaire(self):
        self.root.destroy()
        import formulaire
root = Tk()
obj= Login(root)
root.mainloop()
