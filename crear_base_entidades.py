from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    ForeignKey
)

from sqlalchemy.orm import (
    declarative_base,
    relationship
)

from configuracion import engine

Base = declarative_base()


# =========================
# CLINICA
# =========================

class Clinica(Base):
    __tablename__ = "clinica"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(200), nullable=False)
    veterinario_responsable = Column(String(100), nullable=False)

    consultorios = relationship(
        "Consultorio",
        back_populates="clinica"
    )


# =========================
# CONSULTORIO
# =========================

class Consultorio(Base):
    __tablename__ = "consultorio"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    especialidad = Column(String(100), nullable=False)

    clinica_id = Column(
        Integer,
        ForeignKey("clinica.id"),
        nullable=False
    )

    clinica = relationship(
        "Clinica",
        back_populates="consultorios"
    )

    veterinarios = relationship(
        "Veterinario",
        back_populates="consultorio"
    )


# =========================
# VETERINARIO
# =========================

class Veterinario(Base):
    __tablename__ = "veterinario"

    id = Column(Integer, primary_key=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(120), nullable=False)
    licencia = Column(String(50), nullable=False)

    consultorio_id = Column(
        Integer,
        ForeignKey("consultorio.id"),
        nullable=False
    )

    consultorio = relationship(
        "Consultorio",
        back_populates="veterinarios"
    )

    historias_clinicas = relationship(
        "HistoriaClinica",
        back_populates="veterinario"
    )


# =========================
# HISTORIA CLINICA
# =========================

class HistoriaClinica(Base):
    __tablename__ = "historia_clinica"

    id = Column(Integer, primary_key=True)

    fecha_atencion = Column(Date, nullable=False)

    diagnostico = Column(
        String(200),
        nullable=False
    )

    tratamiento = Column(
        String(300),
        nullable=False
    )

    mascota = Column(
        String(100),
        nullable=False
    )

    veterinario_id = Column(
        Integer,
        ForeignKey("veterinario.id"),
        nullable=False
    )

    veterinario = relationship(
        "Veterinario",
        back_populates="historias_clinicas"
    )


# =========================
# CREAR TABLAS
# =========================

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Base de datos creada correctamente")