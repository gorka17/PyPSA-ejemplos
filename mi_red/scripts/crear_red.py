import pypsa
import os

# Crear la red
network = pypsa.Network()

# Añadir tres buses a la red
for i in range(3):
    network.add("Bus", f"Bus{i}", v_nom=20.0)

# Añadir líneas en anillo (con resistencia r=0)
network.add("Line", "Line0", bus0="Bus0", bus1="Bus1", x=0.1, r=0)
network.add("Line", "Line1", bus0="Bus1", bus1="Bus2", x=0.1, r=0)
network.add("Line", "Line2", bus0="Bus2", bus1="Bus0", x=0.1, r=0)

# Generador solar en bus 0: control="PV" para controlar tensión, potencia activa fija
network.add("Generator", "Gen_Solar", bus="Bus0", p_set=100, control="PV", marginal_cost=0)

# Carga en bus 1
network.add("Load", "Load1", bus="Bus1", p_set=100)

# Asegurarse que existe carpeta outputs para guardar resultados
os.makedirs("outputs", exist_ok=True)

# Resolver flujo de potencia 
network.pf()  

# Guardar la red resuelta
network.export_to_netcdf("outputs/red_resuelta.nc")