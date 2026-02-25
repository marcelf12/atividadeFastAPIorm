from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base, Session

# Configuração do Banco de Dados SQLite
DATABASE_URL = "sqlite:///./banco.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelos (Tabelas)
class Perfil(Base):
    __tablename__ = "perfis"
    id = Column(Integer, primary_key=True, index=True)
    perfil_nome = Column(String)
    usuario = relationship("Usuario", back_populates="perfil", uselist=False)

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String, unique=True, index=True)
    senha = Column(String)
    id_perfil = Column(Integer, ForeignKey("perfis.id"))
    perfil = relationship("Perfil", back_populates="usuario")

# Cria as tabelas automaticamente
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Função para conectar ao banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para Criar Usuário + Perfil (Regra da Atividade)
@app.post("/usuarios/")
def criar_usuario(nome: str, email: str, senha: str, perfil_nome: str, db: Session = Depends(get_db)):
    if db.query(Usuario).filter(Usuario.email == email).first():
        raise HTTPException(status_code=400, detail="Email ja cadastrado")
    
    novo_perfil = Perfil(perfil_nome=perfil_nome)
    db.add(novo_perfil)
    db.commit()
    db.refresh(novo_perfil)
    
    novo_usuario = Usuario(nome=nome, email=email, senha=senha, id_perfil=novo_perfil.id)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return {"status": "sucesso", "usuario": novo_usuario}

# Rota para Listar Usuários com Perfil
@app.get("/usuarios/")
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

# Rota para Deletar Usuário (A barra vermelha!)
@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    # Busca o usuário pelo ID
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    
    # Se não encontrar, retorna erro 404
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    # Remove do banco e salva
    db.delete(usuario)
    db.commit()
    
    return {"status": "sucesso", "mensagem": f"Usuário {usuario_id} deletado"}