import pyodbc

SERVER = "servername\test"
DATABASE = "WebApp"
USERNAME = "usernme"
PASSWORD = "password"

connectionString = f'DRIVER={{SQL SERVER}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
conn = pyodbc.connect(connectionString)

cursor = conn.cursor()
cursor.execute("SELECT Word FROM tWords")

records = cursor.fetchall()

for r in records:
    rec = []
    for col in r:
        rec.append(col)
    print(rec)
