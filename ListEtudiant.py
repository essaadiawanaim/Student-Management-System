from tkinter import *
from tkinter import ttk, messagebox
import pymysql
import mysql.connector
from pymysql import cursors

class Etudiant:
    def __init__(self,root):
        self.root = root
        self.root.title('liste des étudiants Inscries ')
        self.root.geometry('1920x1080+0+0')
        #self.root.configure(background='SkyBlue2')#108cff

        #Formulaire
        Gestion_Frame= Frame(self.root, bd=5, relief=GROOVE, bg="SkyBlue2")
        Gestion_Frame.place(x=40, y=100, width=400, height=500)

        #les variables
        self.id= StringVar()
        self.nom = StringVar()
        self.email = StringVar()
        self.sexe = StringVar()
        self.contact= StringVar()
        self.filiere= StringVar()
        self.ville = StringVar()

        self.recherch_par = StringVar()
        self.recherch = StringVar()

        gestion_title = Label(Gestion_Frame,text="Information de l'Etudiant",font=("times new roman",20,"bold"), bg="SkyBlue2")
        gestion_title.place(x=40, y=45)
        # ID Etudiant
        id = Label(Gestion_Frame, text="ID Etudiant",font=("times new roman",16), bg="SkyBlue2")
        id.place(x=20, y=100)
        id_txt=Entry(Gestion_Frame, textvariable=self.id,font=("times new roman",15), bg="white" )
        id_txt.place(x=150, y=100)
        #Nom Complet
        NomComplet = Label(Gestion_Frame, text="Nom Complet", font=("times new roman", 16), bg="SkyBlue2")
        NomComplet.place(x=20, y=150)
        nom_txt = Entry(Gestion_Frame, textvariable=self.nom ,font=("times new roman", 15), bg="white")
        nom_txt.place(x=150, y=150)
        #email
        email = Label(Gestion_Frame, text="Email", font=("times new roman", 16), bg="SkyBlue2")
        email.place(x=20, y=200)
        email_txt = Entry(Gestion_Frame, textvariable=self.email ,font=("times new roman", 15), bg="white")
        email_txt.place(x=150, y=200)
        #sexe
        sexe = Label(Gestion_Frame, text="Sexe", font=("times new roman", 16), bg="SkyBlue2")
        sexe.place(x=20, y=245)
        sexe_txt =ttk.Combobox(Gestion_Frame, textvariable=self.sexe ,font=("times new roman", 16), state="readonly")
        sexe_txt["values"]=("Homme", "Femme")
        sexe_txt.place(x=148,y=245, width=208)
        sexe_txt.current(0)
        #contact
        contact = Label(Gestion_Frame, text="Contact", font=("times new roman", 16), bg="SkyBlue2")
        contact.place(x=20, y=290)
        contact_txt = Entry(Gestion_Frame, textvariable=self.contact ,font=("times new roman", 15), bg="white")
        contact_txt.place(x=150, y=290)
        #filiére
        filiere = Label(Gestion_Frame, text="Filière", font=("times new roman", 16), bg="SkyBlue2")
        filiere.place(x=20, y=330)
        filiere_txt =ttk.Combobox(Gestion_Frame, textvariable=self.filiere ,font=("times new roman", 15), state="readonly")
        filiere_txt["values"]=('select','Cycle Préparatoire', 'Ingénierie des données','Génie Civil', 'Génie Informatique','Génie Mécanique','Génie de l’Eau et de l’Environnement')
        filiere_txt.place(x=150, y=330,width=208)
        filiere_txt.current(0)
        #Ville
        ville = Label(Gestion_Frame, text="Ville", font=("times new roman", 16), bg="SkyBlue2")
        ville.place(x=20, y=380)
        ville_txt = Entry(Gestion_Frame, textvariable=self.ville ,font=("times new roman", 15), bg="white")
        ville_txt.place(x=150, y=380)

        #Button Ajouter __________________________________________________________________________________
        btn_ajt = Button(Gestion_Frame, text="Ajouter", command=self.ajou_etudiant ,cursor="hand2",
                      font=("yu gothic ui", 13, "bold"), bg="white",
                      fg="black")
        btn_ajt.place(x=5, y=441, width=88)
        # Button Modifier _______________________________________________________________________________
        btn_mdf = Button(Gestion_Frame, text="Modifier", command=self.modifier,cursor="hand2",
                         font=("yu gothic ui", 13, "bold"), bg="white",fg="black")
        btn_mdf.place(x=100, y=441, width=88)
        # Button Supprimer __________________________________________________________________________________
        btn_spr = Button(Gestion_Frame, text="Supprimer", command=self.supprimer, cursor="hand2",
                         font=("yu gothic ui", 13, "bold"), bg="white", fg="black")
        btn_spr.place(x=200, y=441, width=89)
        # Button Réinitialiser ______________________________________________________________________________
        btn_rnt = Button(Gestion_Frame, text="Réinitialiser", command=self.reini ,cursor="hand2",
                         font=("yu gothic ui", 13, "bold"), bg="white",fg="black")
        btn_rnt.place(x=300, y=441, width=89)

        #----------------------------------------------------------------------------------------------------
        #La Rechercher
        #----------------------------------------------------------------------------------------------------
        Details_Frame = Frame(self.root, bd=5,relief=GROOVE, bg="SkyBlue2")
        Details_Frame.place(x=470, y=98, width=780, height=500)

        Affichage_resultat= Label(Details_Frame, text="Rechercher par ",font=("times new roman", 20), bg="SkyBlue2")
        Affichage_resultat.place(x=50, y=50)

        rech= ttk.Combobox(Details_Frame, textvariable=self.recherch_par ,font=("times new roman", 16), state="readonly")
        rech['values']=("select","id","nom", "contact")
        rech.place(x=228, y=60,width=120,height=29)
        rech.current(0)
        # ENtry  recherche
        rech_txt = Entry(Details_Frame, textvariable=self.recherch ,font=("times new roman", 13),bd=5,relief=GROOVE )
        rech_txt.place(x=355, y=60,width=170,height=33)
        #button recherche_____________________________________________________________
        btn_rech = Button(Details_Frame, text="Rechercher", command=self.rechercherInfo,
                         font=("yu gothic ui", 13, "bold"), bg="lightgrey", fg="black")
        btn_rech.place(x=540, y=60, width=95,height=29)
        # button afficher tous________________________________________________
        btn_afcht = Button(Details_Frame, text="Afficher Tous",command=self.afficherResultat,
                          font=("yu gothic ui", 13, "bold"), bg="lightgrey",fg="black")
        btn_afcht.place(x=645, y=60, width=120, height=29)

        # AFFICHAGE
        result_Frame = Frame(Details_Frame,bd=5,relief=GROOVE, bg="SkyBlue2")
        result_Frame.place(x=8, y=110,width=757,height=363)

        scroll_x= Scrollbar(result_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(result_Frame, orient=VERTICAL)
        self.tabl_resul= ttk.Treeview(result_Frame, columns=("id", "nom","email","sexe","contact","filiere","ville" ), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.tabl_resul.heading("id", text="ID Etudiant")
        self.tabl_resul.heading("nom", text="Nom Complet")
        self.tabl_resul.heading("email", text="Email")
        self.tabl_resul.heading("sexe", text="Sexe")
        self.tabl_resul.heading("contact", text="Contact")
        self.tabl_resul.heading("filiere", text="filière")
        self.tabl_resul.heading("ville", text="Ville")

        self.tabl_resul["show"]="headings"

        self.tabl_resul.column("id",width =88)
        self.tabl_resul.column("nom",width =100)
        self.tabl_resul.column("email", width=140)
        self.tabl_resul.column("sexe", width=80)
        self.tabl_resul.column("contact",width=100)
        self.tabl_resul.column("filiere", width=140)
        self.tabl_resul.column("ville", width=100)

        self.tabl_resul.pack()
        self.tabl_resul.bind("<ButtonRelease-1>",self.inforamtion)
        self.afficherResultat()

    def ajou_etudiant(self):
        if self.id.get()==""or self.nom.get()==""or self.email.get()=="":
            messagebox.showerror("Erreur", "vous n'avez pas rempli les champs obligatoires ",parent=self.root)
        else:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="enregistrer")
            cur = con.cursor()
            cur.execute("insert into inscritetudiant values(%s,%s,%s,%s,%s,%s,%s)",(self.id.get(), self.nom.get(),self.email.get(),self.sexe.get(),self.contact.get(),self.filiere.get(),self.ville.get()))
            con.commit()
            self.afficherResultat()
            self.reini()
            con.close()
            messagebox.showinfo("Succès"," Enregistrement Effectué")

    def afficherResultat(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="enregistrer")
        cur = con.cursor()
        cur.execute("select * from inscritetudiant")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.tabl_resul.delete(*self.tabl_resul.get_children())
            for row in rows:
                self.tabl_resul.insert("",END,values=row)
        con.commit()
        con.close()

    def reini(self):
        self.id.set("")
        self.nom.set("")
        self.email.set("")
        self.sexe.set("")
        self.contact.set("")
        self.filiere.set("")
        self.ville.set("")
  # fct pour recupérer les information si je voudrais le modifier
    def inforamtion(self, ev):
        cursors_row = self.tabl_resul.focus()
        contents = self.tabl_resul.item(cursors_row)
        row = contents["values"]
        self.id.set(row[0]),
        self.nom.set(row[1]),
        self.email.set(row[2]),
        self.sexe.set(row[3]),
        self.contact.set(row[4]),
        self.filiere.set(row[5]),
        self.ville.set(row[6]),

  #fct pour faire la modification d'une information(colomn) ou de tous les colonnes
    def modifier(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="enregistrer")
        cur = con.cursor()
        cur.execute("update inscritetudiant set nom=%s ,email=%s,sexe=%s,contact=%s,filiere=%s ,ville=%s  where id=%s", (self.nom.get(),self.email.get(),self.sexe.get(),self.contact.get(),self.filiere.get(),self.ville.get(),self.id.get()))
        con.commit()
        messagebox.showinfo("Succès", " Modification Effectué")
        self.afficherResultat()
        self.reini()
        con.close()

    def supprimer(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="enregistrer")
        cur = con.cursor()
        cur.execute("delete from inscritetudiant where id = %s", self.id.get())
        con.commit()
        self.afficherResultat()
        self.reini()
        con.close()

    def rechercherInfo(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="enregistrer")
            cur = con.cursor()
            cur.execute("SELECT * FROM inscritetudiant WHERE " + str(self.recherch_par.get()) + " LIKE '%" + str(self.recherch.get()) + "%'")
            rows = cur.fetchall()
            if len(rows)!=0:
                self.tabl_resul.delete(*self.tabl_resul.get_children())
                for row in rows:
                    self.tabl_resul.insert("", END, values=row)
            con.commit()
            con.close()
        except Exception as ex:
            messagebox.showerror("Erreur", f"Erreur dans la recherche des infos {str(ex)}", parent=self.root)
    def is_valid_email(self,email):
        """
        Vérifie si une adresse e-mail est valide en utilisant une expression régulière.
        Retourne True si l'adresse e-mail est valide, False sinon.
        """
        pattern = r'^[a-zA-Z0-9.]+@gmail\.com$'
        return re.match(pattern,email) is not None


root = Tk()
obj= Etudiant(root)
root.mainloop()
