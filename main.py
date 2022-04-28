from re import S
from fastapi import FastAPI
import pymysql
import sqlalchemy as db
from sqlalchemy import create_engine
import json

engine = db.create_engine('mysql+pymysql://georgelacerda:Z2VvcmdlbGFj@jobs.visie.com.br/georgelacerda') 
connection = engine.connect()
metadata = db.MetaData()
pessoas = db.Table('pessoas', metadata, autoload=True, autoload_with=engine)



app = FastAPI()


@app.get("/pessoas")
def get_pessoa():
   
    quer = connection.execute(db.select([pessoas])).fetchall()
    return quer

@app.post("/pessoas")
def criar_pessoa(pessoa_id:int,nome :str,rg:str,cpf:str,data_nascimento,data_admissao):
    query = db.insert(pessoas)
    values_list = [{'id_pessoa': pessoa_id, 'nome':nome, "rg": rg, "cpf": cpf, "data_nascimento": data_nascimento, "data_admissao": data_admissao, "funcao":''}]
    ResultProxy = connection.execute(query,values_list)
    
    return {"Criou": ""}

@app.delete("/pessoas")
def deletar_pessoa(id_api : int):
    query = db.delete(pessoas)
    query = query.where(pessoas.columns.id_pessoa == id_api)
    results = connection.execute(query)
    return {"deletou": ""}

@app.put("/pessoas")
def alterar_pessoa(id_pessoa:int,funcao:str):
    query = db.update(pessoas)
    query = query.where(pessoas.columns.id_pessoa == id_pessoa).values(funcao=funcao)
    results = connection.execute(query)

    return {"alterou": ""}

@app.get("/")
def read_root():
    return {"Hello": "World"}
