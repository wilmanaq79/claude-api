"""Clase 01 - inicio: Quickstart: tu primera llamada a Claude API.

Este archivo es el punto de partida de la clase. Está lleno de pistas y
TODOs para que el estudiante escriba el código durante la explicación.
"""

import os
from anthropic import Anthropic


MODEL = "claude-sonnet-4-6"



def requirw_api_key() -> str:
    """Requiere la clave de API de Anthropic desde la variable de entorno ANTHROPIC_API_KEY."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:

        raise RuntimeError("Define la variable de entorno ANTHROPIC_API_KEY  antes de ejecutar el script.")
    
    return api_key

    
def main() -> None:
    """Completa este ejercicio durante la clase.
    api_key = requirw_api_key()
    client = Anthropic(api_key=api_key)
    """
    client = Anthropic(api_key=requirw_api_key())
    message = client.messages.create(
        model=MODEL,
        max_tokens=300,
        system="Responde como un experto en algoritmia y programacion.",
        
       # messages=[
       #     {
       #         "role": "user",
       #         "content": "Dime los signo de asignacion.",
       #     }
       # ],
       messages = [
                    {"role": "user", "content": "Mi proyecto será un chabot para recetas."},
                    {"role": "assistant", "content": "Puedo ayudarte con ingredientes y pasos."},
                    {"role": "user", "content": "Recuerdame cuál era mi proyecto y sugiereme el primer Feature."},
        ],

    )

    for block in message.content:
        if block.type == "text":
            print(block.text)
    



if __name__ == "__main__":
    main()
