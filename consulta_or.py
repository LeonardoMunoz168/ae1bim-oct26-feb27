from sqlalchemy import or_

from configuracion import session
from crear_base_entidades import HistoriaClinica

historias = session.query(
    HistoriaClinica
).filter(
    or_(
        HistoriaClinica.mascota == "Rocky",
        HistoriaClinica.mascota == "Luna"
    )
).all()

print("\nHISTORIAS DE ROCKY O LUNA\n")

for historia in historias:
    print(
        historia.mascota,
        "-",
        historia.diagnostico
    )