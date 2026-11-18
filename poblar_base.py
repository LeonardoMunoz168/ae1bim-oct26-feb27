from datetime import date

from configuracion import session

from crear_base_entidades import (
    Clinica,
    Consultorio,
    Veterinario,
    HistoriaClinica
)

# =========================
# CLINICAS
# =========================

clinica_norte = Clinica(
    nombre="Clinica Norte",
    direccion="Av. Amazonas 100",
    veterinario_responsable="Ana Lopez"
)

clinica_centro = Clinica(
    nombre="Clinica Centro",
    direccion="Av. Quito 250",
    veterinario_responsable="Carlos Perez"
)

clinica_sur = Clinica(
    nombre="Clinica Sur",
    direccion="Av. Maldonado 780",
    veterinario_responsable="Maria Gomez"
)

# =========================
# CONSULTORIOS
# =========================

cirugia = Consultorio(
    nombre="Consultorio Cirugia",
    especialidad="Cirugia",
    clinica=clinica_norte
)

dermatologia = Consultorio(
    nombre="Consultorio Dermatologia",
    especialidad="Dermatologia",
    clinica=clinica_norte
)

medicina_general = Consultorio(
    nombre="Consultorio Medicina General",
    especialidad="Medicina General",
    clinica=clinica_centro
)

cardiologia = Consultorio(
    nombre="Consultorio Cardiologia",
    especialidad="Cardiologia",
    clinica=clinica_centro
)

traumatologia = Consultorio(
    nombre="Consultorio Traumatologia",
    especialidad="Traumatologia",
    clinica=clinica_sur
)

nutricion = Consultorio(
    nombre="Consultorio Nutricion",
    especialidad="Nutricion",
    clinica=clinica_sur
)

# =========================
# VETERINARIOS
# =========================

vet1 = Veterinario(
    nombres="Luis",
    apellidos="Garcia",
    correo="luis.garcia@veterinaria.com",
    licencia="LIC001",
    consultorio=cirugia
)

vet2 = Veterinario(
    nombres="Sofia",
    apellidos="Martinez",
    correo="sofia.martinez@veterinaria.com",
    licencia="LIC002",
    consultorio=cirugia
)

vet3 = Veterinario(
    nombres="Pedro",
    apellidos="Lopez",
    correo="pedro.lopez@veterinaria.com",
    licencia="LIC003",
    consultorio=dermatologia
)

vet4 = Veterinario(
    nombres="Laura",
    apellidos="Fernandez",
    correo="laura.fernandez@veterinaria.com",
    licencia="LIC004",
    consultorio=dermatologia
)

vet5 = Veterinario(
    nombres="Andres",
    apellidos="Castro",
    correo="andres.castro@veterinaria.com",
    licencia="LIC005",
    consultorio=medicina_general
)

vet6 = Veterinario(
    nombres="Daniela",
    apellidos="Rojas",
    correo="daniela.rojas@veterinaria.com",
    licencia="LIC006",
    consultorio=medicina_general
)

vet7 = Veterinario(
    nombres="Miguel",
    apellidos="Torres",
    correo="miguel.torres@veterinaria.com",
    licencia="LIC007",
    consultorio=cardiologia
)

vet8 = Veterinario(
    nombres="Valeria",
    apellidos="Mendoza",
    correo="valeria.mendoza@veterinaria.com",
    licencia="LIC008",
    consultorio=traumatologia
)

vet9 = Veterinario(
    nombres="Jorge",
    apellidos="Vera",
    correo="jorge.vera@veterinaria.com",
    licencia="LIC009",
    consultorio=nutricion
)

vet10 = Veterinario(
    nombres="Camila",
    apellidos="Salazar",
    correo="camila.salazar@veterinaria.com",
    licencia="LIC010",
    consultorio=nutricion
)

# =========================
# HISTORIAS CLINICAS
# =========================

historias = [

    HistoriaClinica(
        fecha_atencion=date(2026, 1, 10),
        diagnostico="Dermatitis",
        tratamiento="Shampoo medicado",
        mascota="Rocky",
        veterinario=vet3
    ),

    HistoriaClinica(
        fecha_atencion=date(2026, 1, 11),
        diagnostico="Otitis",
        tratamiento="Gotas antibioticas",
        mascota="Luna",
        veterinario=vet1
    ),

    HistoriaClinica(
        fecha_atencion=date(2026, 1, 12),
        diagnostico="Fractura",
        tratamiento="Inmovilizacion",
        mascota="Max",
        veterinario=vet8
    ),

    HistoriaClinica(
        fecha_atencion=date(2026, 1, 13),
        diagnostico="Vacunacion",
        tratamiento="Vacuna anual",
        mascota="Nala",
        veterinario=vet5
    ),

    HistoriaClinica(
        fecha_atencion=date(2026, 1, 14),
        diagnostico="Control General",
        tratamiento="Revision completa",
        mascota="Milo",
        veterinario=vet6
    ),

    HistoriaClinica(
        fecha_atencion=date(2026, 1, 15),
        diagnostico="Alergia",
        tratamiento="Antihistaminicos",
        mascota="Coco",
        veterinario=vet4
    ),

    HistoriaClinica(
        fecha_atencion=date(2026, 1, 16),
        diagnostico="Problema Cardiaco",
        tratamiento="Medicacion cardiaca",
        mascota="Toby",
        veterinario=vet7
    ),

    HistoriaClinica(
        fecha_atencion=date(2026, 1, 17),
        diagnostico="Desnutricion",
        tratamiento="Suplementacion",
        mascota="Simba",
        veterinario=vet9
    ),

    HistoriaClinica(
        fecha_atencion=date(2026, 1, 18),
        diagnostico="Dermatitis",
        tratamiento="Tratamiento topico",
        mascota="Luna",
        veterinario=vet3
    ),

    HistoriaClinica(
        fecha_atencion=date(2026, 1, 19),
        diagnostico="Control General",
        tratamiento="Observacion",
        mascota="Rocky",
        veterinario=vet5
    ),

    HistoriaClinica(
        fecha_atencion=date(2026, 1, 20),
        diagnostico="Otitis",
        tratamiento="Limpieza auditiva",
        mascota="Max",
        veterinario=vet1
    ),

    HistoriaClinica(
        fecha_atencion=date(2026, 1, 21),
        diagnostico="Alergia",
        tratamiento="Medicacion",
        mascota="Coco",
        veterinario=vet4
    ),

    HistoriaClinica(
        fecha_atencion=date(2026, 1, 22),
        diagnostico="Fractura",
        tratamiento="Yeso",
        mascota="Toby",
        veterinario=vet8
    ),

    HistoriaClinica(
        fecha_atencion=date(2026, 1, 23),
        diagnostico="Vacunacion",
        tratamiento="Refuerzo",
        mascota="Milo",
        veterinario=vet6
    ),

    HistoriaClinica(
        fecha_atencion=date(2026, 1, 24),
        diagnostico="Dermatitis",
        tratamiento="Medicacion",
        mascota="Simba",
        veterinario=vet3
    ),

    HistoriaClinica(
        fecha_atencion=date(2026, 1, 25),
        diagnostico="Control General",
        tratamiento="Chequeo",
        mascota="Nala",
        veterinario=vet5
    ),

    HistoriaClinica(
        fecha_atencion=date(2026, 1, 26),
        diagnostico="Otitis",
        tratamiento="Antibioticos",
        mascota="Rocky",
        veterinario=vet2
    ),

    HistoriaClinica(
        fecha_atencion=date(2026, 1, 27),
        diagnostico="Alergia",
        tratamiento="Control alimenticio",
        mascota="Luna",
        veterinario=vet10
    ),

    HistoriaClinica(
        fecha_atencion=date(2026, 1, 28),
        diagnostico="Desnutricion",
        tratamiento="Plan nutricional",
        mascota="Max",
        veterinario=vet9
    ),

    HistoriaClinica(
        fecha_atencion=date(2026, 1, 29),
        diagnostico="Control General",
        tratamiento="Revision periodica",
        mascota="Coco",
        veterinario=vet6
    )
]

# =========================
# GUARDAR EN BD
# =========================

session.add_all([
    clinica_norte,
    clinica_centro,
    clinica_sur
])

session.add_all(historias)

session.commit()

print("Datos cargados correctamente")