
import urllib.parse
import sqlalchemy
from dotenv import load_dotenv  
import os
 
load_dotenv()
USER = os.getenv('DB_USER')
PASSWORD = os.getenv('DB_PASSWORD')
HOST = os.getenv('DB_HOST')
PORT = os.getenv('DB_PORT')
DATABASE = os.getenv('DB_NAME')

PASSWORD_ESCAPADA= urllib.parse.quote_plus(PASSWORD) # como a minha senha tinha um "@" precisei escapar para funcionar na url 
connection_url = f'postgresql://{USER}:{PASSWORD_ESCAPADA}@{HOST}:{PORT}/{DATABASE}'
engine = sqlalchemy.create_engine(connection_url)
  
print("Engine criada com sucesso!")