import sqlite3

def create_tables():
    conn = sqlite3.connect("nfce.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS empresa (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        cnpj TEXT,
        endereco TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        cpf TEXT,
        endereco TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produto (
        id INTEGER PRIMARY KEY,
        descricao TEXT,
        preco REAL,
        unidade TEXT
    )
    """)
    conn.commit()
    conn.close()

create_tables()
