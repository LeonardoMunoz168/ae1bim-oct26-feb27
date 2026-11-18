from configuracion import session
from crear_base_entidades import Clinica

clinicas = session.query(Clinica).all()

print("\nCLINICAS Y NUMERO DE HISTORIAS CLINICAS\n")

for clinica in clinicas:

    total_historias = 0

    for consultorio in clinica.consultorios:
        for veterinario in consultorio.veterinarios:
            total_historias += len(veterinario.historias_clinicas)

    print(
        f"{clinica.nombre} -> {total_historias} historias clinicas"
    )