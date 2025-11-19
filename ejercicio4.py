import csv

# Diccionario donde guardamos los datos de cada equipo
equipos = {}

def crear_equipo(nombre):
    return {
        "puntos": 0,
        "goles_favor": 0,
        "goles_contra": 0,
        "tarjetas": 0,
        "directos": {}
    }

# --- 1. LEER CSV ---
archivo = "season-2425.csv"   

with open(archivo, "r", encoding="utf-8") as f:
    lector = csv.DictReader(f)

    for fila in lector:
        local = fila["HomeTeam"]
        visitante = fila["AwayTeam"]
        gl = int(fila["FTHG"])
        gv = int(fila["FTAG"])

        # Tarjetas si existen
        try:
            tl = int(fila.get("HomeYellow", 0))
            tv = int(fila.get("AwayYellow", 0))
        except:
            tl = 0
            tv = 0

        # Crear equipos si no existen todavía
        if local not in equipos:
            equipos[local] = crear_equipo(local)
        if visitante not in equipos:
            equipos[visitante] = crear_equipo(visitante)

        # Actualizar goles
        equipos[local]["goles_favor"] += gl
        equipos[local]["goles_contra"] += gv
        equipos[visitante]["goles_favor"] += gv
        equipos[visitante]["goles_contra"] += gl

        # Actualizar tarjetas
        equipos[local]["tarjetas"] += tl
        equipos[visitante]["tarjetas"] += tv

        # Guardar enfrentamientos directos
        equipos[local]["directos"].setdefault(visitante, 0)
        equipos[visitante]["directos"].setdefault(local, 0)
        equipos[local]["directos"][visitante] += (gl - gv)
        equipos[visitante]["directos"][local] += (gv - gl)

        # Asignar puntos
        if gl > gv:
            equipos[local]["puntos"] += 3
        elif gv > gl:
            equipos[visitante]["puntos"] += 3
        else:
            equipos[local]["puntos"] += 1
            equipos[visitante]["puntos"] += 1


# --- 2. IMPRIMIR GOLES A FAVOR ---
print("=== GOLES A FAVOR ===")
for eq, datos in equipos.items():
    print(eq, "→", datos["goles_favor"], "goles")


# --- 3. ORDENAR CLASIFICACIÓN ---

def criterios(equipo):
    datos = equipos[equipo]
    return (
        datos["puntos"],
        datos["goles_favor"] - datos["goles_contra"],
        datos["goles_favor"],
        -datos["tarjetas"]
    )

clasificacion = sorted(equipos.keys(), key=criterios, reverse=True)

# --- 4. MOSTRAR CLASIFICACIÓN ---
print("\n=== CLASIFICACIÓN FINAL ===")
pos = 1
for eq in clasificacion:
    d = equipos[eq]
    print(pos, "-", eq, "| Pts:", d["puntos"], "| GF:", d["goles_favor"],
          "| GC:", d["goles_contra"], "| Tarjetas:", d["tarjetas"])
    pos += 1
