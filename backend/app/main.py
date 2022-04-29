from re import S
from fastapi import FastAPI
import pymysql
import sqlalchemy as db
from sqlalchemy import create_engine, null
import json
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.sql import select
from sqlalchemy import func 
import random

engine = db.create_engine('mysql+pymysql://georgelacerda:Z2VvcmdlbGFj@jobs.visie.com.br/georgelacerda',connect_args={'connect_timeout': 40}) 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/pessoas/{pessoa_id}")
def get_pessoa(pessoa_id):
    connection = engine.connect()
    metadata = db.MetaData()
    pessoas = db.Table('pessoas', metadata, autoload=True, autoload_with=engine)
    
    quer = connection.execute(select(pessoas).where(pessoas.c.id_pessoa ==pessoa_id )).fetchall()
    connection.invalidate()
    return quer

@app.get("/pessoas")
def get_pessoa():
    
    connection = engine.connect()
    metadata = db.MetaData()
    pessoas = db.Table('pessoas', metadata, autoload=True, autoload_with=engine)

   
    quer = connection.execute(select(pessoas)).fetchall()
    connection.invalidate()
    
    return quer

@app.post("/pessoas")
def criar_pessoa(nome :str,rg:str,cpf:str,data_nascimento,data_admissao):
    connection = engine.connect()
    metadata = db.MetaData()
    pessoas = db.Table('pessoas', metadata, autoload=True, autoload_with=engine)
    query = db.insert(pessoas)
    randomizar = random.randint(0, 10000)
    values_list = [{'id_pessoa':randomizar, 'nome':nome, "rg": rg, "cpf": cpf, "data_nascimento": data_nascimento, "data_admissao": data_admissao, "funcao":''}]
    ResultProxy = connection.execute(query,values_list)
    connection.invalidate()

    return {'nome':nome, "rg": rg, "cpf": cpf, "data_nascimento": data_nascimento, "data_admissao": data_admissao, "funcao":''}

@app.delete("/pessoas")
def deletar_pessoa(id_api : int):
    connection = engine.connect()
    metadata = db.MetaData()
    pessoas = db.Table('pessoas', metadata, autoload=True, autoload_with=engine)

    query = db.delete(pessoas)
    query = query.where(pessoas.columns.id_pessoa == id_api)
    results = connection.execute(query)
    connection.invalidate()
    return {"deletou": ""}

@app.put("/pessoas")
def alterar_pessoa(id_pessoa:int,nome:str,rg:str,cpf:str,data_nascimento:str,data_admissao:str,funcao:str):
    connection = engine.connect()
    metadata = db.MetaData()
    pessoas = db.Table('pessoas', metadata, autoload=True, autoload_with=engine)

    query = db.update(pessoas)
    query = query.where(pessoas.columns.id_pessoa == id_pessoa).values(funcao=funcao,nome=nome,cpf=cpf,data_nascimento = data_nascimento,data_admissao = data_admissao,rg = rg)
    results = connection.execute(query)
    connection.invalidate()

    return {"alterou": ""}

@app.get("/")
def read_root():
    return {"Hello": "World"}
