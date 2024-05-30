import sys
import os
# app/some_module.py

def some_function():
    return 42  # Substitua pela lógica real da função

# Adicione o diretório raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
