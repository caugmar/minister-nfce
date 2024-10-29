# build.py
from pybuilder.core import use_plugin, init, task
import os

use_plugin("python.core")

name = "my_project"
default_task = "build"

@init
def initialize(project):
    # Configurações de inicialização podem ser adicionadas aqui, se necessário
    pass

@task
def build(project):
    """Tarefa que executa o PyInstaller com main.spec"""
    os.system("pyinstaller main.spec")

@task
def clean(project):
    """Tarefa que remove os diretórios dist/, build/ e __pycache__"""
    os.system("rm -rf dist/ build/ __pycache__")
