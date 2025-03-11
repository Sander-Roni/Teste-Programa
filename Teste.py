import speech_recognition as service  #Usar Futuramente!
from tkinter import * # Tkinter Base
import tkinter as tk
from tkinter import messagebox # Message Box o Classico
from PIL import Image,ImageTk
import sqlite3 as conector #Sqlite 3 Sendo importado como Biblioteca
import random # Biblioteca para gerar numeros aleatorios
import time    # Biblioteca de tempo 
import webview    # Biblioteca concatenada ao tkinter que associa o google a ele


class App:
    def __init__(self):
        # Metodo Construtor
        pass

    def JanelaBase(self):
        
        """" Imagens e Widgets Janela Principal """
        self.intf = tk.Tk()
        self.icon = tk.PhotoImage(file="/Users/Anuli/Desktop/PROJETOS GIT/Meu Icone.png")
        self.intf.resizable(False,False)
        self.intf.title("Insistrus Corporation")
        self.intf.geometry("500x500")
        self.intfBack = Image.open(r"C://Users//Anuli//Desktop//Projetos GIT//telainicial.png")
        self.loadSc = ImageTk.PhotoImage(self.intfBack)
        self.ScPrinc = tk.Label(self.intf, image= self.loadSc)
        self.ScPrinc.place(relheight=1,relwidth=1)
        self.IButtonMage = Image.open(r"C://Users//Anuli//Desktop//Projetos GIT//Buton.png")
        self.ButtonImage = ImageTk.PhotoImage(self.IButtonMage)
        self.InteractButton = tk.Button(self.intf, image = self.ButtonImage, border= False, borderwidth= False, command= self.Funcao1)
        self.InteractButton.pack(padx=0,pady=230)
        self.intf.iconphoto(False,self.icon)
        self.intf.mainloop()
        
    """
    ______Implementação de Apagar dados______
    
    def ApagarTudo(self):            
        try:
            self.conexao = conector.connect("BancoUtilizavel")
            self.executar_tabela = self.conexao.cursor()
            self.comando = '''DELETE FROM CadastrarUsuario'''
            self.executar_tabela.execute(self.comando)
            self.conexao.commit()
            print("Banco Criado com Sucesso")
        except conector.DatabaseError as ex:
            print("Erro ao Conectar com o Banco de Dados", ex)
        finally:
            if self.conexao:
                self.conexao.close()
        

    """

    def Funcao1(self):
        self.intf.destroy()
        self.Tela_de_Cadastro()

    """Criação do Banco de Dados"""

    def CriarBanco(self):
        try:
            self.conexao = conector.connect("BancoUtilizavel")
            self.executar_tabela = self.conexao.cursor()
            self.comando = '''
                CREATE TABLE IF NOT EXISTS CadastrarUsuario(
                        id int (1) primary key,
                        nome varchar(255),
                        email varchar(255) UNIQUE,
                        senha varchar(255),
                        telefone varchar(255) UNIQUE,
                        cep varchar(255),
                        UF varchar(255) 
                        );     
                                '''

            self.executar_tabela.execute(self.comando)
            self.conexao.commit()
            print("Banco Criado com Sucesso")
        except conector.DatabaseError as ex:
            print("Erro ao Conectar com o Banco de Dados", ex)
        finally:
            if self.conexao:
                self.conexao.close()

    """Cadastrar Principal"""
    
    def Tela_de_Cadastro(self):
        self.conexion = conector.connect("BancoUtilizavel")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("SELECT * FROM CadastrarUsuario")
        self.dados = self.cursor.fetchall()
        for i in self.dados:
            print(i)
        self.conexion.close()
        self.panelCads = Tk()
        self.icon = tk.PhotoImage(file="/Users/Anuli/Desktop/PROJETOS GIT/Meu Icone.png")
        self.panelCads.resizable(False,False)
        self.panelCads.geometry("500x500")
        self.panelCads.title("Insistrus Corporation - Register")
        self.JanelaInteract = Image.open("/Users/Anuli/Desktop/Projetos GIT/ImagTela.jpg")
        self.JanRun = ImageTk.PhotoImage(self.JanelaInteract)
        self.JanPrinc = Label(self.panelCads,image = self.JanRun)
        self.JanPrinc.place(relheight=1, relwidth=1)
        self.NewJanela = Image.open("/Users/Anuli/Desktop/Projetos GIT/DownLoadImage.png")
        self.AddJan = ImageTk.PhotoImage(self.NewJanela)
        self.openJan = Label(self.JanPrinc, image = self.AddJan)
        self.openJan.place(x=100,y=100,height=300,width=300)
        self.Titulo = Label(self.openJan,text="Crie sua Conta",fg="white",bg="#2c4e78", font= ("Arial",12))
        self.Titulo.place(x=100,y=10)
        self.Nome = Label(self.openJan,text="Nome",fg="white",bg="#2c4e78")
        self.Nome.place(x=40,y=50)
        self.entrywid1 = Entry(self.openJan)
        self.entrywid1.place(x=85,y=50)
        self.Email = Label(self.openJan,text="Email",fg="white",bg="#2c4e78")
        self.Email.place(x=40,y=80)
        self.entrywid2 = Entry(self.openJan,width=25)
        self.entrywid2.place(x=85,y=80)
        self.Senha = tk.Label(self.openJan,text="Senha",fg="white",bg="#2c4e78")
        self.Senha.place(x=40,y=110)
        self.entrywid3 = Entry(self.openJan,show="*")
        self.entrywid3.place(x=85,y=110)
        self.Telefone = Label(self.openJan,text="Telefone",fg="white",bg="#2c4e78")
        self.Telefone.place(x=40,y=140)
        self.entrywid4 = Entry(self.openJan)
        self.entrywid4.place(x=95,y=140)
        self.Cep = Label(self.openJan,text="Cep",fg="white",bg="#2c4e78")
        self.Cep.place(x=40,y=170)
        self.entrywid5 = Entry(self.openJan)
        self.entrywid5.place(x=85,y=170)
        self.Uf = Label(self.openJan,text="UF",fg="white",bg="#2c4e78")
        self.Uf.place(x=40,y=200)
        self.entrywid6 = Entry(self.openJan)
        self.entrywid6.place(x=85,y=200)
        self.BtCadastrar = Button(self.openJan,fg="white",text="Cadastrar",bg="#169c87",borderwidth=False,command=self.Funcao2,border=0)
        self.BtCadastrar.place(x=120,y=230)
        self.BtEntrarConta = Button(self.openJan,fg="white",text="Entrar com Conta",bg="#2c4e78",borderwidth=False,command=self.Conta_JaRegistrada,border=0)
        self.BtEntrarConta.place(x=100,y=255)
        self.panelCads.iconphoto(False,self.icon)
        self.panelCads.mainloop()

    def Funcao2(self):
        self.Cadastrar()
        self.Conta_JaRegistrada()

    """Dados Inseridos/ Não Inseridos"""
    
    def Cadastrar(self):
        nome_completo = self.entrywid1.get().strip()
        primeiro_nome = nome_completo.split()[0] if nome_completo else ""
        nome = self.entrywid1.get()
        email = self.entrywid2.get()
        senha = self.entrywid3.get()
        telefone = self.entrywid4.get()
        cep = self.entrywid5.get()
        uf = self.entrywid6.get()
        
        if not primeiro_nome and not email and not senha and not telefone and not cep and not uf:
                messagebox.showinfo("Dados não Inseridos","Preencha todos os campos")
                return
        try:
            self.conexao = conector.connect("BancoUtilizavel")
            self.executar_table = self.conexao.cursor()
            self.comando = '''
                INSERT INTO CadastrarUsuario (nome,email,senha,telefone,cep,UF) VALUES (?,?,?,?,?,?)
                '''
            self.executar_table.execute(self.comando, (primeiro_nome,email,senha,telefone,cep,uf))
            self.conexao.commit()
            messagebox.showinfo("Sucesso!","Cadastrado com Sucesso!")

        except conector as erro:
            print("erro:", erro)
        finally:
            if self.conexao:
                self.conexao.close()

    """Confirmação de Conta"""
    
    def Conta_JaRegistrada(self):
        #Aqui vai pra Confirmação
        self.panelCads.destroy()
        self.Interface_Secund = tk.Tk()
        self.icon = tk.PhotoImage(file="/Users/Anuli/Desktop/PROJETOS GIT/Meu Icone.png") 
        self.Interface_Secund.resizable(False,False)
        self.Interface_Secund.title("Insistrus Corporation - Login")
        self.LoadingImage = Image.open("/Users/Anuli/Desktop/Projetos GIT/ImagTela.jpg")
        self.ChargeImage = ImageTk.PhotoImage(self.LoadingImage)
        self.Janela_otherScreen = Label(self.Interface_Secund,image=self.ChargeImage)
        self.Janela_otherScreen.place(relheight=1,relwidth=1)
        self.Interface_Secund.geometry("500x500")
        self.CargarIMG = Image.open("/Users/Anuli/Desktop/Projetos GIT/DownLoadImage.png")
        self.FunctIMG = ImageTk.PhotoImage(self.CargarIMG)
        self.SobJanela = Label(self.Janela_otherScreen,image=self.FunctIMG)
        self.ContaRegistr_Janela = Label(self.Interface_Secund,text="Entrar Com a Conta",fg="white",bg="#2c4e78", font= ("Arial",12))
        self.ContaRegistr_Janela.place(x=180,y=180)
        self.TkLabel1 = Label(self.SobJanela,text="Email",fg="white",bg="#2c4e78")
        self.TkLabel1.place(x=20,y=70)
        self.TkLabelGet1 = Entry(self.SobJanela,width=25)
        self.TkLabelGet1.place(x=60,y=70)
        self.TkLabel1 = Label(self.SobJanela,text="Senha",fg="white",bg="#2c4e78")
        self.TkLabel1.place(x=35,y=100)
        self.TkLabelGet2 = Entry(self.SobJanela,show="*")
        self.TkLabelGet2.place(width=85,x=80,y=100)
        self.TkLabelButton1 = Button(self.SobJanela,text="Entrar com Conta",bg="#169c87",fg="white",border=False,borderwidth=False,command=self.DadosLogados)
        self.TkLabelButton1.place(x=80,y=150)
        self.TkLabelButton2 = Button(self.SobJanela,text="Não possui Conta?",bg="#2c4e78",fg="white",border=False,borderwidth=False,command=self.Funcao3)
        self.TkLabelButton2.place(x=75,y=180)
        self.TkLabelButton3 = Button(self.SobJanela,text="Esqueceu a Senha?",bg="#2c4e78",fg="white",border=False,borderwidth=False,command=self.Esqueceu_Senha)
        self.TkLabelButton3.place(x=75,y=210)
        self.SobJanela.place(x=120,y=150,height=240,width=250)
        self.Interface_Secund.iconphoto(False,self.icon)
        self.Interface_Secund.mainloop()

    def Funcao3(self):
        #Solução:
        #Destroi a Janela do Metodo [Conta Registrada] para não Haver
        # Duplicatas nas Imagens (Motivo do Erro de PyImage que acredito ocorrer)
        # e Não Causa erro de Itens já Destruidos (caso use a Tela Anterior) 
        self.Interface_Secund.destroy()
        self.Tela_de_Cadastro()
    
    def Funcao4(self):
        
        self.Esqueceu_Senha()

    

        #Uma possivel boa Ideia para Contornar a Situação é Criar uma Nova Tela
    
    """MessageBox de Aviso!"""
    
    def DadosLogados(self):
        email1 = self.TkLabelGet1.get()
        senha2 = self.TkLabelGet2.get()
        if not email1 or not senha2:
            messagebox.showwarning("Aviso!","alguns dados não foram inseridos")
            return 
        try:
            self.conexao = conector.connect("BancoUtilizavel")
            self.newCursor = self.conexao.cursor()
            self.newCursor.execute("SELECT * FROM  CadastrarUsuario WHERE email = ?",(email1,))
            self.RecuperarDado = self.newCursor.fetchone()
            #Recuperação do Email
            if self.RecuperarDado:
                DadoEmail,DadoNome,DadoSenha,DadoTelefone,DadoCep,DadoUF = self.RecuperarDado[1],self.RecuperarDado[2],self.RecuperarDado[3],self.RecuperarDado[4],self.RecuperarDado[5],self.RecuperarDado[5]
                if senha2 == DadoSenha:
                    messagebox.showinfo("Bem Vindo",f"Seja Bem Vindo(a) {DadoEmail}")
                    self.Interface_Secund.destroy()
                    dado_nome = self.RecuperarDado[1]
                    self.Confirmacao(dado_nome)

                else:
                    messagebox.showwarning("Aviso","Senha não Encontrado")
            else:
                messagebox.showwarning("Aviso","Usuario não Encontrado")
        except conector.Error as Erro:
            messagebox.showinfo("Aviso","Ocorreu um erro ao tentar acessar o Banco de Dados",Erro)
        finally:
            if self.conexao:
                self.conexao.close()
    

    """Tela de Esqueceu Senha"""

    def Esqueceu_Senha(self):
        #Aqui vai pra Confirmação
        self.Interface_Secund.destroy() 
        self.Janela_ = tk.Tk()
        self.Janela_.geometry("500x500")
        self.Janela_.resizable(False,False)
        self.Janela_.title("Insistrus Corporation - Forgot Password")
        self.icon = tk.PhotoImage(file="/Users/Anuli/Desktop/Projetos GIT/Meu Icone.png")
        self.Charge_Label = Image.open("/Users/Anuli/Desktop/Projetos GIT/ImagTela.jpg")
        self.Janela_LD = ImageTk.PhotoImage(self.Charge_Label)
        self.Janela_Animada = tk.Label(self.Janela_,image=self.Janela_LD)
        self.Janela_Animada.place(relwidth=1,relheight=1)
        self.InChargeLabel = Image.open("/Users/Anuli/Desktop/Projetos GIT/DownLoadImage.png")
        self.InChargeFix = ImageTk.PhotoImage(self.InChargeLabel)
        self.CreateLabel = tk.Label(self.Janela_Animada,image=self.InChargeFix)
        self.CreateLabel.place(x=120,y=150,height=220,width=250)
        self.ContaRegistr_Janela_ = Label(self.CreateLabel,text="Esqueci minha Senha",fg="white",bg="#2c4e78", font= ("Arial",12))
        self.ContaRegistr_Janela_.place(x=50,y=20)
        self.TkLabel1_ = Label(self.CreateLabel,text="Email",fg="white",bg="#2c4e78")
        self.TkLabel1_.place(x=30,y=60)
        self.TkLabelGet1_ = Entry(self.CreateLabel)
        self.TkLabelGet1_.place(x=70,y=60,height=20,width=150)
        self.TkLabel2_ = Label(self.CreateLabel,text="Nova Senha",fg="white",bg="#2c4e78")
        self.TkLabel2_.place(x=40,y=90)
        self.TkLabelGet2_ = Entry(self.CreateLabel,show="*")
        self.TkLabelGet2_.place(height=20,width=100,x=120,y=90)
        self.TkLabel3_ = Label(self.CreateLabel,text="Confirme a Senha",fg="white",bg="#2c4e78")
        self.TkLabel3_.place(x=20,y=120)
        self.TkLabelGet3_ = Entry(self.CreateLabel,show="*")
        self.TkLabelGet3_.place(height=20,width=100,x=120,y=120)
        self.TkLabelButton_ = Button(self.CreateLabel,text="Entrar",bg="#169c87",fg="white",border=False,borderwidth=False,command=self.Dados_Logados_2)
        self.TkLabelButton_.place(x=100,y=150)
        self.Janela_.iconphoto(False,self.icon)
        self.Janela_.mainloop()

    def Dados_Logados_2(self):
        
        """UPDATE """
        
        dado_email = self.TkLabelGet1_.get()
        dado_senha = self.TkLabelGet2_.get()
        dado_confirmacao_senha = self.TkLabelGet3_.get()
        if not dado_email or not dado_senha or not dado_confirmacao_senha:
            messagebox.showinfo("Preencha os Campos","Alguns Dados não Foram Preenchidos")
            return
        if dado_senha != dado_confirmacao_senha:
            messagebox.showinfo("Erro","As Senhas Não Coincidem")
            return 
        try:
            self.conexao = conector.connect("BancoUtilizavel")
            self.executarTabela = self.conexao.cursor()
            self.executarTabela.execute("SELECT * FROM CadastrarUsuario WHERE email = ?", (dado_email,))
            user = self.executarTabela.fetchone()
            if user:
                """Arrumado"""
                self.Janela_.destroy()
                self.RecuperarDado = user
                dado_nome = self.RecuperarDado[1]
                self.executarTabela.execute("UPDATE CadastrarUsuario SET senha = ? WHERE email = ?",(dado_senha,dado_email))
                self.conexao.commit()
                messagebox.showinfo("Sucesso","Senha Atualizada com Sucesso!")
                self.Confirmacao(dado_nome)
            else:
                messagebox.showwarning("Erro","E-mail não encontrado.")
        except conector.Error as erro:
            messagebox.showerror("Erro",f"ocorreu um erro {erro}")
        finally:
            if self.conexao:
                self.conexao.close()
        

    def Confirmacao(self,dado_nome):
        """Confirmação de Duas Etapas, Tela de Colocar o Código Gerado"""

        self.Interface_central = tk.Tk()
        self.Interface_central.resizable(False,False)
        self.icon = tk.PhotoImage(file="/Users/Anuli/Desktop/Projetos GIT/Meu Icone.png") 
        self.Interface_central.geometry("500x500")
        self.Interface_central.title("Insistrus Corporation - Validation")
        self.Interface_Imagem = Image.open("/Users/Anuli/Desktop/Projetos GIT/ImagTela.jpg")
        self.Interface_CarregImagem = ImageTk.PhotoImage(self.Interface_Imagem)
        self.LabelFace = tk.Label(self.Interface_central,image=self.Interface_CarregImagem)
        self.LabelFace.place(relheight=1,relwidth=1)
        self.InterfaceConfirmLabel = Image.open("/Users/Anuli/Desktop/Projetos GIT/DownLoadImage.png")
        self.InterfaceConfirmLabel2 = ImageTk.PhotoImage(self.InterfaceConfirmLabel)
        self.Interface_Space = tk.Label(self.Interface_central,image=self.InterfaceConfirmLabel2)
        self.Interface_Space.place(x=100,y=100,height=300,width=300)
        self.Label_Codigo = tk.Label(self.Interface_Space,text="Codigo de Verificação",bg="#2c4e78",fg="white",font= ("Arial",12))
        self.Label_Codigo.place(x=70,y=40)
        self.Label_Titulo1 = tk.Label(self.Interface_Space,text="Codigo:",bg="#2c4e78",fg="white")
        self.Label_Titulo1.place(x=70,y=70)
        self.Entrada_Titulo1 = tk.Entry(self.Interface_Space,fg="black",show="*")
        self.Entrada_Titulo1.place(height=20,width=50,x=120,y=70)
        self.Button_code = tk.Button(self.Interface_Space,text="Verificar",bg="#2c4e78",fg="white",border=False,borderwidth=False,command=lambda:self.Validacao(dado_nome))
        self.Button_code.place(height=30,width=50,x=120,y=100)
        self.gerar_outro = tk.Button(self.Interface_Space,text="Gerar Código",bg="#2c4e78",fg="white",border=False,borderwidth=False,command=self.Gerar)
        self.gerar_outro.place(height=30,width=80,x=100,y=140)
        self.Interface_central.iconphoto(False,self.icon)
        self.Interface_central.mainloop()   

    def Gerar(self):

        """Gera o Código de Validação """

        self.gerar_outro.config(state=tk.DISABLED)
        self.Interface_Space.after(15000,self.reativar_botao)
        self.gerar_codigo = None 
        self.hora_enviada = None
        self.gerar_codigo = random.randint(10000,99999)
        self.hora_enviada = time.time()
        messagebox.showinfo("Código Enviado",f"o Código enviado é: {self.gerar_codigo}")

    def reativar_botao(self):
        self.gerar_outro.config(state=tk.NORMAL)
        

    def Validacao(self,dado_nome):
        """ Aqui tem a Segunda Etapa"""
        validacao_usuario = self.Entrada_Titulo1.get()
        if validacao_usuario == str(self.gerar_codigo):
            validade_do_codigo = time.time() - self.hora_enviada
            if validade_do_codigo <= 20:
                messagebox.showinfo("Sucesso","Login realizado com Sucesso!")
                self.Interface_central.destroy()
                self.Janela_Principal(dado_nome)
            else:
                messagebox.showinfo("Expirado","O Código foi Expirado. Tente de Novo")
        else:
            messagebox.showinfo("Erro","Código de Verificação Incorreto") 



    def Janela_Principal(self,dado_nome):
        self.Janela_Personalizada = tk.Tk()
        self.icon = tk.PhotoImage(file="/Users/Anuli/Desktop/Projetos GIT/Meu Icone.png")
        self.Janela_Personalizada.geometry("500x500")
        self.Janela_Personalizada.title("Insistrus Corporation - Principal Label")
        self.Janela_Personalizada.resizable(True,True)
        self.LoadImage1 = Image.open("/Users/Anuli/Desktop/Projetos GIT/AnotherTelaInicial.png")
        self.RegisterImage1 = ImageTk.PhotoImage(self.LoadImage1)
        self.Roupa_Primaria = tk.Label(self.Janela_Personalizada,image=self.RegisterImage1)
        self.Roupa_Primaria.place(relwidth=1,relheight=1)  
        self.LoadLoginImage = Image.open("/Users/Anuli/Desktop/Projetos GIT/Login icon.png")
        self.LoadLoginBase = ImageTk.PhotoImage(self.LoadLoginImage)
        self.User = tk.Label(self.Roupa_Primaria,text=f"{dado_nome}",bg="#1f1f1f",fg="white")  
        self.User.place(x=380,y=95)
        self.LabelLogin = tk.Button(self.Roupa_Primaria,image=self.LoadLoginBase,command=lambda:self.Configurações(dado_nome))
        self.LabelLogin.place(x=420,y=95)
        self.EdgeChargeImg = Image.open("/Users/Anuli/Desktop/Projetos GIT/Google Logo2.png")
        self.EdgeImgLoad = ImageTk.PhotoImage(self.EdgeChargeImg)
        self.EdgeButton = tk.Button(self.Roupa_Primaria,image=self.EdgeImgLoad,bg="#1f1f1f",border=None,borderwidth=None,command=self.Abrir_Navegador)
        self.EdgeButton.place(x=60,y=110,width=120,height=120)
        self.TextItem1 = tk.Label(self.Roupa_Primaria,text="Google",bg="#1f1f1f",fg="white")
        self.TextItem1.place(x=90,y=200,width=60,height=30)
        self.TextItemF = tk.Label(self.Roupa_Primaria,text="...Meus Aplicativos...",bg="#1f1f1f",fg="aqua")
        self.TextItemF.place(x=200,y=375)
        self.Janela_Personalizada.iconphoto(False,self.icon)
        self.Janela_Personalizada.mainloop()

    """Mudar a Logo do Navegador"""
    def Configurações(self,dado_nome):
        self.Janela_Personalizada.destroy()
        dado_nome = self.RecuperarDado[1]
        self.Configurar_ = tk.Tk()
        self.Configurar_.title("Tela de Configuração")
        self.Configurar_.geometry("500x500")
        self.Configurar_.resizable(False,False)
        self.LoadLabel = Image.open("C:/Users/Anuli/Desktop/Projetos GIT/Imagem Inicial.jpg")
        self.OpenLabel = ImageTk.PhotoImage(self.LoadLabel)
        self.CLabel = tk.Label(self.Configurar_,image = self.OpenLabel)
        self.CLabel.place(relheight=1,relwidth=1)
        self.NewLabel = tk.Label(self.CLabel,text=f"Bem Vindo {dado_nome}")
        self.NewLabel.place(x=100,y=100)
        self.BackButton = tk.Button(self.CLabel,text="voltar",command=lambda:self.Back(dado_nome))
        self.BackButton.place(x=90,y=4)
        self.Configurar_.mainloop()
        
    def Alterar_Dados(self,dado_nome):
        pass

    def Back(self,dado_nome):
        dado_nome = self.RecuperarDado[1]
        self.Configurar_.destroy()
        self.Janela_Principal(dado_nome)

    def Abrir_Navegador(self):
        dado_nome = self.RecuperarDado[1]
        self.Janela_Personalizada.destroy()
        webview.create_window("Google","https://www.google.com")
        webview.start()
        self.Janela_Principal(dado_nome)


# O Sistema aqui dava pra ter feito usado Herança


out = App()
out.JanelaBase()
