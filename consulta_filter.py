from configuracion import session
from crear_base_entidades import Veterinario

veterinarios = session.query(
    Veterinario
).filter(
    Veterinario.consultorio_id == 1
).all()

print("\nVETERINARIOS DEL CONSULTORIO 1\n")

for veterinario in veterinarios:
    print(
        veterinario.nombres,
        veterinario.apellidos
    )