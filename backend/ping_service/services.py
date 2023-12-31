from ping3 import ping
from .models import AddressModel, PingModel
from django.conf import settings
from threading import Thread, Timer
import logging

log = logging.getLogger(__name__)

# Ping could be done like that. But I assume external dependencies are not banned,
# Thus not using such solution
# def ping(address:str) -> float:
#     from subprocess import check_output
#     from platform import system
#     from re import sub

#     if system() == 'Windows':
#         flag = '-n'
#     else:
#         flag = '-c'

#     command = "ping", flag, "1", address
#     raw_answer = str(check_output(command))

#     return float(sub(' ms.*', "", sub('^.*time=', "", raw_answer)))

def send_ping(address: AddressModel):
    response = ping(address.url, unit="ms", timeout=8)

    if response:
        log.info(f"Pinged {address.url} for {response} ms")

        ping_instance = PingModel.objects.create(
            value = response,
            address = address,
        )

    else:
        log.warning(f"{address.url} is unreachable")


# Usually threaded tasks are done via MQ like celery
def run_ping_fetcher():
    timer = Timer(settings.PING_TIMER, run_ping_fetcher)
    timer.setDaemon(True)
    timer.start()
    log.info("Pinging addresses")

    for i in AddressModel.objects.all():
        t = Thread(target=send_ping,args=[i])
        t.setDaemon(True)
        t.start()
