import time
from plyer import notification

def Lembrete(intervalo_lembrete=60):
    notification.notify(
        title = "Esta na hora de beber água 🧃",
        message = "Levanta, toma um ar e vai beber água",
        timeout = 5

    )
    time.sleep(intervalo_lembrete * 60)

Lembrete(60)