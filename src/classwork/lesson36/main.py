import psycopg2 as PyPG

connectBD = PyPG.connect(
    dbname = "Projects",
    user = "postgres",
    password = "zxcasd123",
    host = "localhost",
    port = 5432
)

cursor = connectBD.cursor()

query = (f"SELECT clients.client_id, clients.name, projects.project_id, "
         f"projects.title FROM projects	"
         f"LEFT JOIN clients ON projects.client_id = clients.client_id;")

cursor.execute(query)

table = cursor.fetchall()
for line in table:
    print(f"{line[0]} - {line[1]} - {line[2]} - {line[3]}")
    # print(f"{line[0]} - {line[1]} - {line[2]} - {line[3]} - {line[4]}")

def create_table(name_table, title_values):
    cursor = connectBD.cursor()
    query = f"CREATE TABLE {name_table} ({title_values});"
    cursor.execute(query)

table_create_values_title = ("id uuid DEFAULT gen_random_uuid(),"
                             "name text NOT NULL,"
                             "age int"
                             "PRIMARY KEY (id)")
name_table = "test_table"

cursor.close()
connectBD.close()