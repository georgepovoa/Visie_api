import pymysql
import sqlalchemy as db
from sqlalchemy import create_engine

engine = db.create_engine('mysql+pymysql://georgelacerda:Z2VvcmdlbGFj@jobs.visie.com.br/georgelacerda') 
connection = engine.connect()
metadata = db.MetaData()
pessoas = db.Table('pessoas', metadata, autoload=True, autoload_with=engine)


# census = db.Table('census', metadata, autoload=True, autoload_with=engine)
# query = db.select([census]) 
# ResultProxy = connection.execute(query)
# ResultSet = ResultProxy.fetchall()
# ResultSet[:3]

# pessoas = db.Table('pessoas', metadata,
#               db.Column('id_pessoa', db.Integer()),
#               db.Column('nome', db.String(100), nullable=False),
#               db.Column('rg', db.String(100), nullable=False),
#               db.Column('cpf', db.String(100), nullable=False),
#               db.Column('data_nascimento', db.Date(), nullable=False),
#               db.Column('data_admissao', db.Date(), nullable=False),
#               db.Column('funcao', db.String(100), nullable=False),
              
#               )

# metadata.create_all(engine)

# query = db.insert(pessoas) 
# values_list = [{'id_pessoa': 0, 'nome': "Alberto Vieira", "rg": "25.507.105-2", "cpf": "168.637.122-53", "data_nascimento": "1997-07-01", "data_admissao": "2020-09-28", "funcao":'' }
# ,
# {"id_pessoa": 1, "nome": "Alexandre Teixeira", "rg": "79.474.888-8", "cpf": "877.733.889-89", "data_nascimento": "1982-08-16", "data_admissao": "2020-05-15", "funcao":'' }
# ,
# {"id_pessoa": 2, "nome": "Ana Carolina Souza", "rg": "52.565.667-8", "cpf": "766.370.920-96", "data_nascimento": "1982-03-19", "data_admissao": "2016-08-19", "funcao":'' }
# ,
# {"id_pessoa": 3, "nome": "Ana Paula Soares", "rg": "54.744.331-9", "cpf": "746.917.734-52", "data_nascimento": "1984-09-01", "data_admissao": "2019-08-25", "funcao":'' }
# ,
# {"id_pessoa": 4, "nome": "Antônio Siqueira", "rg": "81.669.888-5", "cpf": "695.991.412-45", "data_nascimento": "1990-07-26", "data_admissao": "2016-05-18", "funcao":'' }
# ,
# {"id_pessoa": 5, "nome": "Arthur Silva", "rg": "43.204.402-9", "cpf": "345.898.157-88", "data_nascimento": "1996-12-30", "data_admissao": "2016-04-28", "funcao":'' }
# ,
# {"id_pessoa": 6, "nome": "Bárbara Santos", "rg": "57.106.623-3", "cpf": "587.914.225-66", "data_nascimento": "2000-09-04", "data_admissao": "2018-11-17", "funcao":'' }
# ,
# {"id_pessoa": 7, "nome": "Beatriz Santana", "rg": "70.855.305-2", "cpf": "093.084.203-04", "data_nascimento": "1994-05-17", "data_admissao": "2018-03-05", "funcao":'' }
# ,
# {"id_pessoa": 8, "nome": "Caio Sampaio", "rg": "14.475.327-9", "cpf": "483.764.953-05", "data_nascimento": "1995-11-18", "data_admissao": "2020-06-03", "funcao":'' }
# ,
# {"id_pessoa": 9, "nome": "Carla Rodrigues", "rg": "62.692.082-5", "cpf": "566.412.961-13", "data_nascimento": "1996-08-04", "data_admissao": "2015-03-31", "funcao":'' }
# ,
# {"id_pessoa": 10, "nome": "Carlos Rocha", "rg": "23.782.125-5", "cpf": "053.166.034-60", "data_nascimento": "1983-07-07", "data_admissao": "2017-03-08", "funcao":'' }
# ,
# {"id_pessoa": 11, "nome": "Cauê Ribeiro", "rg": "33.548.790-1", "cpf": "491.145.149-15", "data_nascimento": "1981-01-27", "data_admissao": "2020-12-31", "funcao":'' }
# ,
# {"id_pessoa": 12, "nome": "Cláudia Reis", "rg": "54.435.082-9", "cpf": "511.020.782-80", "data_nascimento": "1986-08-04", "data_admissao": "2020-09-25", "funcao":'' }
# ,
# {"id_pessoa": 13, "nome": "Cláudio Ramos", "rg": "41.432.308-6", "cpf": "673.452.026-90", "data_nascimento": "1982-08-12", "data_admissao": "2019-11-01", "funcao":'' }
# ,
# {"id_pessoa": 14, "nome": "Daiane Pereira", "rg": "90.815.741-8", "cpf": "704.352.424-58", "data_nascimento": "2002-11-22", "data_admissao": "2017-06-15", "funcao":'' }
# ,
# {"id_pessoa": 15, "nome": "Diego Penha", "rg": "43.099.953-1", "cpf": "329.630.074-00", "data_nascimento": "1983-02-23", "data_admissao": "2017-12-01", "funcao":'' }
# ,
# {"id_pessoa": 16, "nome": "Eduardo Oliveira", "rg": "46.249.609-1", "cpf": "772.220.114-80", "data_nascimento": "2001-02-12", "data_admissao": "2020-05-10", "funcao":'' }
# ,
# {"id_pessoa": 17, "nome": "Eliana Nunes", "rg": "84.269.396-7", "cpf": "130.491.959-59", "data_nascimento": "1994-07-03", "data_admissao": "2018-01-16", "funcao":'' }
# ,
# {"id_pessoa": 18, "nome": "Enzo Nascimento", "rg": "68.986.227-4", "cpf": "356.759.355-25", "data_nascimento": "1989-05-05", "data_admissao": "2016-08-23", "funcao":'' }
# ,]

# ResultProxy = connection.execute(query,values_list)
print(connection.execute(db.select([pessoas])).fetchall())