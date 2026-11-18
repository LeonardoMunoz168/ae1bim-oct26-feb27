from sqlalchemy import and_

from configuracion import session
from crear_base_entidades import HistoriaClinica

historias = session.query(
    HistoriaClinica
).filter(
    and_(
        HistoriaClinica.mascota == "Rocky",
        HistoriaClinica.diagnostico == "Dermatitis"
    )
).all()

print("\nHISTORIAS DE ROCKY CON DERMATITIS\n")

for historia in historias:
    print(
        historia.mascota,
        "-",
        historia.diagnostico,
        "-",
        historia.tratamiento
    )