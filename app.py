from flask import Flask
import psutil
import os
import platform

APP = Flask(__name__)

print(psutil.cpu_percent(percpu=True))
print(psutil.virtual_memory().used / 1024 ** 2)
print(os.getpid())
print(platform.platform())

@APP.get('/')
def index():
    return """
        <a href="/info"><button>Info</button></a><br>
        <a href="/metricas"><button>Métricas</button></a>
    """
@APP.get('/info')
def informacoes():
    return """
        <a href="/"><button>Home</button></a><br>
        <a href="/metricas"><button>Métricas</button></a>
        <h1> Pedro Henrique Valente Favero</h1><br><h1> Davi Kazuhiro Natume </h1><br><h1> Lucas Antonio Pelanda </h1>"""


@APP.get('/metricas')
def metricas():
    nomes = "Pedro Henrique Valente Favero, Lucas Antonio Pelanda e Davi Kazuhiro Natume"
    pid = os.getpid()
    memoria_mb = psutil.virtual_memory().used / 1024 ** 2 
    cpu = psutil.cpu_percent()
    sistema_op = platform.platform()
    return {
        "integrantes": nomes,
        "pid": pid,
        "memoria_mb": round(memoria_mb, 2),
        "cpu_percent": cpu,
        "sistema_operacional": sistema_op
    }

if(__name__ ==" __main__"):
    APP.run(host="0.0.0.0", port=80)