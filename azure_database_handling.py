"""
Relevant packages necessary for appropriate execution of the following script:
    ODBC driver for windows
    pyodbc package for python (for working and establishing connection with azure SQL database.)
    python-dotenv for python (for reading environment variables)
"""

import pyodbc
from dotenv import load_dotenv
from os import getenv
load_dotenv()
environment_variables_dictionary = {
"AZURE_SQL_DATABASE_CONNECTION_STRING":getenv("AZURE_SQL_DATABASE_CONNECTION_STRING"),
"SERVER_ADMIN_LOGIN" : getenv("SERVER_ADMIN_LOGIN"),
"SERVER_ADMIN_PASSWORD" : getenv("SERVER_ADMIN_PASSWORD")
}
connection_string = environment_variables_dictionary["AZURE_SQL_DATABASE_CONNECTION_STRING"]
print(connection_string)
connection_object = pyodbc.connect(connection_string)
cursor = connection_object.cursor()

print(dir(connection_object))
user_registration_table_creation = """
CREATE TABLE USER_DATA
(Username VARCHAR(255),
Email_address VARCHAR(255),
Password VARCHAR(255));
"""

inserting_sample_value = """
INSERT INTO USER_DATA (Username, Email_address, Password) VALUES
('again','again@gmail.com','again123'),
('lemim','nlime@yahoo.com','lemon');
"""
fetch_data = """
select * from USER_DATA;
"""

"""
execution of sql queries to perform CRUD operations upon the azure SQL Database;
"""
# cursor.execute(user_registration_table_creation)
cursor.execute(inserting_sample_value)
cursor.execute(fetch_data)
rows = cursor.fetchall()
print(rows)
cursor.commit()


