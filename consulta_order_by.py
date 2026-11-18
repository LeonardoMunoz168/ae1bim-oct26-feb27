from configuracion import session
from crear_base_entidades import Veterinario

veterinarios = session.query(
    Veterinario
).order_by(
    Veterinario.apellidos
).all()

print("\nVETERINARIOS ORDENADOS POR APELLIDO\n")

for veterinario in veterinarios:
    print(
        veterinario.apellidos,
        veterinario.nombres
    )