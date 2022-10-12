"""L'esercizio è mirato a prendere confidenza con l’integrazione di Python e MySQL.
Dato il database fornito in input riportare le interrogazioni svolte nell’esercizio precedente
all’interno di funzioni Python e inoltre implementare una funzione di inserimento
e cancellazione in una tabella a propria scelta."""
import mysql.connector

def connection_database( user, password, host, database):
    try:
        conn = mysql.connector.connect(user = user, password =password, host = host, database = database)
        return conn
    except mysql.connector.errors.databaseError as db_error:
        print(db_error.msg)
        sys.exit()

def close_connection(connection):
    connection.close()

connection_database ('root', '', '127.0.0.1', 'discografia')

""" cursor = connection_database.cursor
AttributeError: 'function' object has no attribute 'cursor'"""

def insert_autore(name,title):
    cursor = connection_database.cursor
    query = "INSERT INTO autore(nome,TitoloCanzone) VALUES(%s,%s);"
    values = (name, title)
    cursor.execute(query,values)
    result = cursor.fetchall()
    return result


insert_autore('name1','title1')
insert_autore('name2','title2')
insert_autore('name3','title3')
insert_autore('name4','title4')
insert_autore('name5','title5')


def delete_autore(name, title):
    cursor = connection_database.cursor
    query = "DELETE FROM autore(nome,TitoloCanzone) WHERE values(%s,%s);"
    values = (name, title)
    cursor.execute(query, values)
    result = cursor.fetchall()
    return result

delete_autore('name1','title1')
delete_autore('name2','title2')
delete_autore('name3','title3')
delete_autore('name4','title4')
delete_autore('name5','title5')

def insert_query(query_statment):
    cursor = connection_database.cursor
    query = query_statment
    query_statment = None
    cursor.execute(query, values)
    result = cursor.fetchall()
    return result
    print(result)

str1 = "select NomeCantante from CANTANTE join ESECUZIONE on CANTANTE.CodiceReg=ESECUZIONE.CodiceReg join AUTORE on ESECUZIONE.TitoloCanz=AUTORE.TitoloCanzone where Nome=NomeCantante and Nome like ‘d%’"

str2 = "select TitoloAlbum from DISCO join CONTIENE on DISCO.NroSerie=CONTIENE.NroSerieDisco join ESECUZIONE on CONTIENE.CodiceReg=ESECUZIONE.CodiceReg where ESECUZIONE.anno is NULL"

str3 = "select distinct NomeCantante from CANTANTE where NomeC not in ( select S1.NomeCantante from CANTANTE as S1 where CodiceReg not in ( select CodiceReg from CANTANTE S2 where S2.NomeCantante <> S1.NomeCantante ) )"

str4 = " select NomeCantante from CANTANTE where NomeCantante not in ( select S1.NomeCantante from CANTANTE as S1 join ESECUZIONE on CodiceReg=S1.CodiceReg join CANTANTE as S2 on CodiceReg=S2.CodiceReg)  where S1.NomeCantante<> S2.NomeCantante "

insert_query(str1)
insert_query(str2)
insert_query(str3)
insert_query(str4)

close_connection()