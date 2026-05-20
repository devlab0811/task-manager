import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Carrega variáveis do arquivo .env
load_dotenv()

# Lê a URL do banco
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL não encontrada no arquivo .env")

# Cria o engine do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Cria fábrica de sessões
SessionLocal = sessionmaker(
    autocommite=False,
    autoflush=False,
    bind=engine
)

# Dependência para usar nas rotas do FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()