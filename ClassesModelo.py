from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Login(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key= True)
    Nome = Column(String(50))
    Email = Column(String(30))
    Cpf = Column(Integer, unique= True)
    Senha = Column(String(500))

    def __repr__(self):
        return f"<Login(id = {self.id}, Nome = {self.Nome}, Email = {self.Email}, Cpf = {self.Cpf}, Senha = {self.Senha})>"


class Projetos(Base):
    __tablename__ = 'projetos'
    id =Column(Integer, primary_key= True)
    nome =Column(String(50), )
    descricao =Column(String(500))
    inicio_Projeto =Column(String(12))
    final_prjeto =Column(String(12))
    conclusao_projeto =Column(Integer)
    def __repr__(self):
        return f"<Projetos(id = {self.id}, nome = {self.nome}, descricao = {self.descricao}, inicio_Projeto = {self.inicio_Projeto}, final_projeto = {self.final_prjeto}, conclusao_projeto = {self.conclusao_projeto})>"

class Funcionarios(Base):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key= True)
    Nome = Column(String(50))
    Cargo = Column(String(25))
    Cpf = Column(Integer, unique= True)
    Telefone = Column(Integer)
    def __repr__(self):
        return f"<Login(id = {self.id}, Nome = {self.Nome}, Email = {self.Cargo}, Cpf = {self.Cpf}, Telefone = {self.Telefone})>"
