import sqlalchemy
from sqlalchemy.orm import sessionmaker
from pprint import pprint
from ClassesModelo import Login, Projetos, Funcionarios


engine = sqlalchemy.create_engine('sqlite:///empresa', echo = True)
class BD(Login):
    sqlalchemy.__version__

    def __init__(self):
        
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()
        Login.metadata.create_all(engine)
        Projetos.metadata.create_all(engine)

    #----------------------------------------- CRUD na tabela login-----------------------------------------
    def cria_user(self, nome, email, cpf, senha):
        p1 = Login( Nome = nome, 
                        Email = email, 
                        Cpf = cpf, 
                        Senha = senha)
        try:
            self.session.add(p1)
            self.session.commit()
            self.session.close()
        except sqlalchemy.exc.IntegrityError:
            return 'erro, usuario ja existe'
    
    def deleta_user(self, idd):
        user = self.session.query(Login).filter_by(id= idd)
        self.session.delete(user)
        self.session.commit()
        self.session.close()

    def edita_nome_user(self, idd, nome):
        querry = self.session.query(Login).filter_by(id = idd).first()
        querry.Nome = nome
        self.session.dirty
        self.session.commit()
        self.session.close()

    def redefinir_senha(self, email, senha):
        querry = self.session.query(Login).filter_by(Email = email).first()
        try:
            querry.Senha = senha
            self.session.dirty
            self.session.commit()
            self.session.close()
        except AttributeError:
            return 'email invalido'

    def ver_tabelaLogin(self):
        querry = []
        for res in self.session.query(Login).all():
            querry.append(res.__dict__)
        return querry

    def recuperar_senha(self, email):
        querry = self.session.query(Login).filter(Login.Email == email).first()
        try:
            self.session.close()
            return querry.Email
        except AttributeError:
            return False

    def verifica_login(self, email, senha):
        querry = self.session.query(Login).filter(Login.Email == email and Login.Senha == senha).first()
        if querry == None:
            self.session.close()
            return False
        else:
            self.session.close()
            return querry.id

        


    #----------------------------------------- CRUD na tabela projetos--------------------------------------
    
    def cria_projetos(self, nome, descricao, inicio_Projeto, final_prjeto, conclusao_projeto):
        p1 = Projetos( 
        nome = nome, 
        descricao = descricao,
        inicio_Projeto = inicio_Projeto, 
        final_prjeto = final_prjeto,
        conclusao_projeto = conclusao_projeto)
        try:
            self.session.add(p1)
            self.session.commit()
            self.session.close()
        except sqlalchemy.exc.IntegrityError:
            return 'erro, projeto ja existe'

    def edita_projeto(self, idd, nome , descricao, inicio, final ):
        querry = self.session.query(Projetos).filter_by(id = idd).first()
        querry.nome = nome
        querry.descricao = descricao
        querry.inicio_Projeto = inicio
        querry.final_prjeto = final
        self.session.dirty
        self.session.commit()
        self.session.close()

    def edita_andamento(self, idd, conclusao ):
        querry = self.session.query(Projetos).filter_by(id = idd).first()
        querry.conclusao_projeto = conclusao
        self.session.dirty
        self.session.commit()
        self.session.close()

    def deleta_projetos(self, idd):
        projeto = self.session.query(Projetos).filter_by(id= idd).first()
        self.session.delete(projeto)
        self.session.commit()
        self.session.close()
        
    def ver_tabelaProjetos(self):
        querry = []
        for res in self.session.query(Projetos).all():
            querry.append(res.__dict__)
        for i in range(len(querry)):
            lista = querry[i]
            del lista['_sa_instance_state']
        self.session.close()
        return querry

    #----------------------------------------- CRUD na tabela funcionarios-----------------------------------
     
    def cria_funcionario(self, nome, cargo, cpf, telefone):
        p1 = Funcionarios( Nome = nome, 
                        Cargo = cargo, 
                        Cpf = cpf, 
                        Telefone = telefone)
        try:
            self.session.add(p1)
            self.session.commit()
            self.session.close()
        except sqlalchemy.exc.IntegrityError:
            return 'erro, usuario ja existe'
    
    def deleta_funcionario(self, idd):
        funcionario = self.session.query(Funcionarios).filter_by(id= idd)
        self.session.delete(funcionario)
        self.session.commit()
        self.session.close()
        
        
    def ver_tabelaFuncionarios(self):
        querry = []
        for res in self.session.query(Funcionarios).all():
            querry.append(res.__dict__)
        for i in range(len(querry)):
            lista = querry[i]
            del lista['_sa_instance_state']
        self.session.close()
        return querry
    

