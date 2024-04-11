import psycopg2
import loguru

DB_NAME = 'ComputerCompany'
USER_NAME = 'admin'
PASSWORD = 'admin'

def create_connection():
    with psycopg2.connect() as conn:
        pass

async def init_db():
    pass

if __name__ == '__main__':
    pass