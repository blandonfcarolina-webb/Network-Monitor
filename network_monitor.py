import subprocess
from datetime import datetime
import csv
import os
import time

DISP = [
    {"nombre": "Router", "ip": "192.168.1.1"},
    {"nombre": "Mi PC", "ip": "192.168.1.2"},
    {"nombre": "Dispositivo1", "ip": "192.168.1.3"},
    {"nombre": "Dispositivo2", "ip": "192.168.1.4"}]

Intervalo_s = 60

def ping(ip):
    result = subprocess.run(["ping", "-n", "1", "-w", "1000", ip],
            capture_output=True, text=True)
    if "TTL=" in result.stdout:
        for part in result.stdout.split():
            if part.startswith("tiempo=") or part.startswith("time="):
                ms = part.split("=")[1].replace("ms", "").strip()
                return "UP", float(ms)
        return "UP", None
    else:
        return "DOWN", None


if not os.path.exists("Datos.CSV"):  ##crea el archivo
    with open("Datos.CSV", mode="w", newline="") as f: 
        writer = csv.writer(f)
        writer.writerow(["timestamp", "nombre", "ip", "estado", "tiempo_ms"])


print(f"[*] Monitoreando {len(DISP)} dispositivos cada {Intervalo_s}s - Para detener Ctrl+C") 

while True:
    with open("Datos.CSV", mode="a", newline="") as f: ##escribe sobre el archivo existente y conserva los datos
        writer = csv.writer(f)
        for ips in DISP:
            estado, t_respuesta = ping(ips["ip"])
            timestamp = datetime.now()
            rt = f"{t_respuesta}ms" if t_respuesta else "N/A" 
            print(f"[{timestamp}] {ips['nombre']} ({ips['ip']}) - {estado} | {rt}]")
            writer.writerow([timestamp, ips["nombre"], ips["ip"], estado, t_respuesta])
    print(f"--- Próxima revisión en {Intervalo_s}s --- \n")
    time.sleep(Intervalo_s)

    

