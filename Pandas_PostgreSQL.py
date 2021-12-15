'''
Link de estudo: https://www.youtube.com/watch?v=mF3c6jy5YRU
'''

print("Importamos a nossas bibliotecas:")
import pandas as pd
from sqlalchemy import create_engine

# Meu Usuário é: postgres
# Senha:  senhaEddy
engine = create_engine("postgresql://postgres:MINHASENHA#@localhost:5432/pruebas")

df = pd.DataFrame([
    ["messi", "messi@argentina.com", "barcelona"],
    ["c ronaldo", "cr7@rm.com", "el bicho"],
    ["neymar", "neymar@empresa.com", "12345"],
    ["mbappe", "mbappe@francia.com", "67890"],
    ["lewandowski", "robert@bayern.com", "1234567890"]
],
    columns=["user", "email", "password"])
print(df)
print("")
# Agora vamos a mandar estes Dados desta tabela criada aqui acima, para o Postgresql.
# users --> Nome da minha tabela lá no Postgresql.
df.to_sql("users", con=engine, if_exists="replace")

print("Agora fazemos uma consulta, assim: ")
query1 = engine.execute("SELECT * FROM users").fetchall() # Ver o porque não trouxe as querys
print(query1)

# Aqui vamos a adicionar mais Dados:
df2 = pd.DataFrame([
    ["Kevin De Bruyne", "kevin@gmail.com", "mipassword"],
    ["Virgil van Dijk", "van@hotmail.com", "nuevacontrasena"],
    ["Sadio Mane", "mane@outlook.com", "1234567890"]
],
    columns=["user", "email", "password"])
print(df2)

print("")
df2.to_sql("users", con=engine, if_exists="append")

print("Fazemos outra consulta e de outra maneira: ")
query2 = pd.read_sql("SELECT * FROM users", engine)
print(query2)

