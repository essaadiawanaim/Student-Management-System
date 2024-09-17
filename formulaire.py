from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import *
from PIL import ImageTk, Image
import pymysql
import re   # pour

class Formulaire:
    def __init__(self, root):
        self.root =root
        self.root.title("Student Registration Form")
        self.root.geometry("1920x1080+0+0")
        self.root.configure(background='SkyBlue2')
        #============================================================================
        #champs du formulaire :
        #============================================================================
        frame1 = Frame(self.root, bg="#ffffff", width=1300, height=680)
        frame1.place(x=30, y=30)
        title= Label(frame1, text=" Formulaire d'inscription des étudiants ", font=('yu gothic ui', 23, "bold"), bg="white",
                             fg='black',
                             bd=5,
                             relief=FLAT)
        title.place(x=0, y=0, width=650)
        # =========== Frame : pour  les Détails personnels  ===========================
        cred_frame = LabelFrame(frame1, text="Détails personnels", bg="white", fg="#4f4e4d", height=300,
                                     width=950, borderwidth=2.4,
                                     font=("yu gothic ui", 13, "bold"))
        cred_frame.config(highlightbackground="red")
        cred_frame.place(x=100, y=100)


        #=============== Détails personnels  ===========================

        #------------------Prénom ------------------
        f_name_label = Label(cred_frame, text=" Prénom: ", bg="white", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold"))
        f_name_label.place(x=10, y=10)
        self.f_name_entry = Entry(self.root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                  font=("yu gothic ui semibold", 12))
        self.f_name_entry.place(x=234, y=167, width=260)  # trebuchet ms

        self.f_name_line = Canvas(self.root, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.f_name_line.place(x=230, y=189)

        # ---------------- Nom --------------------
        l_name_label = Label(cred_frame, text="Nom:", bg="white", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold"))
        l_name_label.place(x=380, y=10)

        self.l_name_entry = Entry(self.root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                  font=("yu gothic ui semibold", 12))
        self.l_name_entry.place(x=576, y=167, width=350)

        self.l_name_line = Canvas(self.root, width=350, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.l_name_line.place(x=570, y=189)
        # ---------------- CNE: --------------------
        cne_label = Label(cred_frame, text="CNE: ", bg="white", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold"))
        cne_label.place(x=20, y=50)

        self.cne_entry = Entry(self.root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                  font=("yu gothic ui semibold", 12))
        self.cne_entry.place(x=252, y=207, width=260)  # trebuchet ms

        self.cne_line = Canvas(self.root, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.cne_line.place(x=222, y=230)
        # ---------------- Date de naissance : --------------------
        dn_label = Label(cred_frame, text="Date de naissance: ", bg="white", fg="#4f4e4d",
                               font=("yu gothic ui", 13, "bold"))
        dn_label.place(x=380, y=50)
        self.dn_entry = DateEntry(self.root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                               font=("yu gothic ui semibold", 12), state="readonly",date_pattern="dd/mm/yy")
        self.dn_entry.place(x=680, y=207, width=255)  # trebuchet ms
        # ---------------- Filière : --------------------
        f_label = Label(cred_frame, text=" Filière : ",
                                         bg="white", fg="#4f4e4d", font=("yu gothic ui", 14, "bold"))
        f_label.place(x=10, y=100)

        self.f_label_combo = ttk.Combobox(self.root, font=('yu gothic ui semibold', 12, 'bold'),
                                                state='readonly',
                                                width=25)
        f_list = ['select','Cycle Préparatoire', 'Ingénierie des données','Génie Civil', 'Génie Informatique','Génie Mécanique','Génie de l’Eau et de l’Environnement']
        self.f_label_combo['values'] = f_list
        self.f_label_combo.place(x=230, y=260)
        self.f_label_combo.current(0)
        # ---------------- Sexe : --------------------

        sexe_label = Label(cred_frame, text="Genre:", bg="white", fg="#4f4e4d",
                                  font=("yu gothic ui", 13, "bold"))
        sexe_label.place(x=380, y=100)
        self.sexe_combo = ttk.Combobox(self.root, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                         width=35)
        sexe_list = ['Male', 'Female']
        self.sexe_combo['values'] =  sexe_list
        self.sexe_combo.place(x=580, y=258)

        # ---------------- Téléphone: --------------------
        tl_label = Label(cred_frame, text="Téléphone: ", bg="white", fg="#4f4e4d",
                              font=("yu gothic ui", 13, "bold"))
        tl_label.place(x=10, y=150)

        self.tl_entry = Entry(self.root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                   font=("yu gothic ui semibold", 12))
        self.tl_entry.place(x=242, y=308, width=260)  # trebuchet ms

        self.tl_line = Canvas(self.root, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.tl_line.place(x=230, y=330)
        # ---------------- Nationalité: --------------------
        country_label = Label(cred_frame, text="Nationalité: ", bg="white", fg="#4f4e4d",
                                   font=("yu gothic ui", 13, "bold"))
        country_label.place(x=380, y=150)

        self.country_entry = Entry(self.root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                   font=("yu gothic ui semibold", 12))
        self.country_entry.place(x=615, y=308, width=260)  # trebuchet ms

        self.country_line = Canvas(self.root, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.country_line.place(x=610, y=330)
        # # ---------------- Address : --------------------
        self.address_label = Label(cred_frame, text="Address: ", bg="white", fg="#4f4e4d",
                                   font=("yu gothic ui", 13, "bold"))
        self.address_label.place(x=10, y=200)

        self.address_entry = Entry(self.root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                   font=("yu gothic ui semibold", 12))
        self.address_entry.place(x=220, y=359, width=280)  # trebuchet ms

        self.address_line = Canvas(self.root, width=280, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.address_line.place(x=220, y=380)

        # ----------------  Année d'obtention BAC  : --------------------
        bac_label = Label(cred_frame, text="Année d'obtention BAC: ", bg="white", fg="#4f4e4d",
                         font=("yu gothic ui", 13, "bold"))
        bac_label.place(x=380, y=200)
        self.bac_entry = DateEntry(self.root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                  font=("yu gothic ui semibold", 12), state="readonly", date_pattern="dd/mm/yy")
        self.bac_entry.place(x=710, y=357, width=255)  # trebuchet ms

        # ======  frame : pour les détails du compte ===========================================

        frame_account = LabelFrame(frame1, text="détails du compte", bg="white", fg="#4f4e4d", height=190,
                                       width=950, borderwidth=2.4,
                                       font=("yu gothic ui", 13, "bold"))
        frame_account.config(highlightbackground="red")
        frame_account.place(x=100, y=410)
        # ______________________ email : ______________________________
        email_label = Label(frame_account, text="Email: ", bg="white", fg="#4f4e4d",
                                       font=("yu gothic ui", 13, "bold"))
        email_label.place(x=10, y=10)

        self.email_entry = Entry(self.root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                       font=("yu gothic ui semibold", 12))
        self.email_entry.place(x=215, y=477, width=260)  # trebuchet ms

        self.email_line = Canvas(self.root, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.email_line.place(x=215, y=500)
        # ______________________ Sélectionnez une Question : _________________________________________
        Question_label = Label(frame_account, text="Sélectionnez une Question : ", bg="white",
                                     fg="#4f4e4d", font=("yu gothic ui", 11, "bold"))
        Question_label.place(x=380, y=10)

        self.Question_combo = ttk.Combobox(self.root, font=('yu gothic ui semibold', 12, 'bold'), state='readonly',
                                            width=35)

        Question_list = ['select','Film préféré', 'Lieu de naissance', 'Meilleur ami','couleur préférée']
        self.Question_combo['values'] = Question_list
        self.Question_combo.place(x=720, y=476)
        self.Question_combo.current(0)
        # ============== mot de pass : ===================================================
        passwd_label = Label(frame_account, text=" mot de pass: ", bg="white", fg="#4f4e4d",
                                       font=("yu gothic ui", 13, "bold"))
        passwd_label.place(x=10, y=60)

        self.passwd_entry = Entry(self.root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                       font=("yu gothic ui semibold", 12))
        self.passwd_entry.place(x=265, y=525, width=260)  # trebuchet ms

        self.passwd_line = Canvas(self.root, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.passwd_line.place(x=259, y=549)
        # ============== la reponse : ==========================================
        rep_label= Label(frame_account, text="Répondre : ", bg="white",
                                     fg="#4f4e4d", font=("yu gothic ui", 13, "bold"))
        rep_label.place(x=450, y=55)
        self.rep_entry = Entry(self.root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                                  font=("yu gothic ui semibold", 12))

        self.rep_entry.place(x=680, y=525)
        self.rep_line = Canvas(self.root, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.rep_line.place(x=680, y=547)

        # ==============  confirmer mot de pass : ==================================================
        con_passwd_label = Label(frame_account, text=" Confirme password: ", bg="white", fg="#4f4e4d",
                             font=("yu gothic ui", 13, "bold"))
        con_passwd_label.place(x=0, y=110)
        self.con_passwd_entry = Entry(self.root, highlightthickness=0, relief=FLAT, bg="white", fg="#6b6a69",
                          font=("yu gothic ui semibold", 12))
        self.con_passwd_entry.place(x=295, y=576, width=260)  # trebuchet ms

        self.con_passwd_line = Canvas(self.root, width=260, height=1.5, bg="#bdb9b1", highlightthickness=0)
        self.con_passwd_line.place(x=289, y=598)

        # ======= les termes et condition =======================================================
        self.var_chech = IntVar()
        chk = Checkbutton(frame_account, variable=self.var_chech, onvalue=1, offvalue=0 ,text="j'accepte les conditions et les termes",
                          font=("yu gothic ui", 12, "bold"), bg="white", fg="black")

        chk.place(x=570, y= 115)
        self.chk_line = Canvas(self.root, width=290, height=1.5, bg="black", highlightthickness=0)
        self.chk_line.place(x=705, y=603)

        # ======  frame for rightImage  : ==================================================
        # ==================================================================================
        right_image_frame = LabelFrame(frame1, "",bg="white", fg="#4f4e4d", height=300,
        width=177, borderwidth=2.4,
        font=("yu gothic ui", 13, "bold"))
        right_image_frame.config(highlightbackground="red")
        right_image_frame.place(x=966, y=108)

        right_image = Image.open('images\\vector2.png')
        photo = ImageTk.PhotoImage(right_image)
        self.right_image_label = Label(self.root, image=photo, bg='white')
        self.right_image_label.image = photo
        self.right_image_label.place(x=966, y=93)

        # ==== les buttons de validation et de connection ==================================
        btn1 = Button(frame1, text="Enregistrer", cursor="hand2",command= self.enregistrer, font=("yu gothic ui", 14, "bold"), bg="SkyBlue2",
                      fg="black")
        btn1.place(x=1077, y=410, width=150)
        btn2 = Button(frame1, text="Connexion",command=self.fenetre_login,cursor="hand2", font=("yu gothic ui", 14, "bold"), bg="SkyBlue2",
                      fg="black")  # SteelBlue3
        btn2.place(x=1077, y=470, width=150)
        btn3 = Button(frame1, text="Exit", cursor="hand2", font=("yu gothic ui", 14, "bold"), bg="SkyBlue2", fg="black",
                      command=lambda: exit())
        btn3.place(x=1077, y=528, width=150)

    def enregistrer(self):
        if self.f_name_entry.get()=="" or self.l_name_entry.get()==""or self.Question_combo.get()==""or self.rep_entry.get()==""or self.passwd_entry.get()=="" or self.con_passwd_entry.get()=="" or self.email_entry.get()=="" or self.tl_entry.get()==""or self.sexe_combo.get()=="" or self.address_entry.get()=="" or self.bac_entry.get()==""or self.country_entry.get()=="" or self.cne_entry.get()=="" or self.dn_entry.get()=="" or self.f_label_combo.get()=="":
            messagebox.showerror("Erreur", " Remplir les champs vide",parent=self.root)
        elif self.passwd_entry.get()!= self.con_passwd_entry.get():
            messagebox.showerror("Erreur", "les mots de passe ne sont pas conforme ", parent=self.root)
        elif not self.is_valid_email(self.email_entry.get()):
                messagebox.showerror("Validation d'email", "L'adresse e-mail n'est pas valide.")
        elif self.var_chech.get()==0:
            messagebox.showerror("Erreur", "Veillez accepter les termes et conditions", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="",database="enregistrer")
                cur= con.cursor()
                cur.execute("select * from compte where email= %s", self.email_entry.get())
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror("Erreur", " Ce email existe déja", parent=self.root)
                else:
                    cur.execute("insert into compte (prenom, nom,cne, date_naissance,filiere, sexe,telephone,nationalite,address, annee_bac ,email, question, reponse, password) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.f_name_entry.get(),
                        self.l_name_entry.get(),
                        self.cne_entry.get(),
                        self.dn_entry.get(),
                        self.f_label_combo.get(),
                        self.sexe_combo.get(),
                        self.tl_entry.get(),
                        self.country_entry.get(),
                        self.address_entry.get(),
                        self.bac_entry.get(),
                        self.email_entry.get(),
                        self.Question_combo.get(),
                        self.rep_entry.get(),
                        self.passwd_entry.get()
                    ))
                    messagebox.showinfo("Success", " Vous avez faire l'enregistrement avec success (Votre compte a été crée)", parent=self.root)
                con.commit()
                self.reini()
                con.close()
            except Exception as es:
                messagebox.showerror("Erreur", f"Erreur de connexion{str(es)}", parent=self.root)
    def is_valid_email(self,email):
        """
        Vérifie si une adresse e-mail est valide en utilisant une expression régulière.
        Retourne True si l'adresse e-mail est valide, False sinon.
        """
        pattern = r'^[a-zA-Z0-9.]+@gmail\.com$'
        return re.match(pattern,email) is not None

    def reini(self):
        self.f_name_entry.delete(0,END)
        self.l_name_entry.delete(0,END)
        self.cne_entry.delete(0,END)
        self.dn_entry.delete(0,END)
        self.f_label_combo.delete(0,END)
        self.sexe_combo.delete(0,END)
        self.tl_entry.delete(0,END)
        self.country_entry.delete(0,END)
        self.address_entry.delete(0,END)
        self.bac_entry.delete(0,END)
        self.email_entry.delete(0,END)
        self.Question_combo.delete(0,END)
        self.rep_entry.delete(0,END)
        self.passwd_entry.delete(0,END)
        self.con_passwd_entry.delete(0, END)

        #connection à la page login --------------------------------------------------
    def fenetre_login(self):
        self.root.destroy()
        import login

root = Tk()
obj= Formulaire(root)
root.mainloop()