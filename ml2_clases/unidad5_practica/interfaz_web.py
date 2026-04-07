"""
Interfaz web para el Asistente RAG TechCorp.
Bonus: implementación con Gradio para visualización en navegador.
Ejecutar después de haber realizado la ingesta con ingesta.py.
"""

import gradio as gr
from asistente import cargar_base_vectorial, crear_cadena_rag

# Cargar base vectorial y cadena RAG al arrancar
vectorstore = cargar_base_vectorial()
cadena, retriever = crear_cadena_rag(vectorstore)

def responder(pregunta, historial):
    """Genera respuesta y actualiza el historial del chat."""
    if not pregunta.strip():
        return "", historial

    # Obtener documentos recuperados para mostrar en debug
    docs = retriever.invoke(pregunta)
    fuentes = [doc.metadata.get("source", "desconocida").split("/")[-1] for doc in docs]
    info_fuentes = f"[Fuentes consultadas: {', '.join(set(fuentes))}]"

    # Generar respuesta
    respuesta = cadena.invoke(pregunta)
    respuesta_completa = f"{respuesta}\n\n{info_fuentes}"

    historial.append((pregunta, respuesta_completa))
    return "", historial

with gr.Blocks(title="Asistente TechCorp") as demo:
    gr.Markdown("# Asistente RAG - TechCorp")
    gr.Markdown("Consulta la documentación interna de la empresa: políticas de RRHH, procedimientos técnicos y más.")
    chatbot = gr.Chatbot(height=400)
    msg = gr.Textbox(
        placeholder="Escribe tu pregunta sobre la documentación de TechCorp...",
        label="Tu pregunta"
    )
    limpiar = gr.Button("Limpiar conversación")
    msg.submit(responder, [msg, chatbot], [msg, chatbot])
    limpiar.click(lambda: ([], ""), outputs=[chatbot, msg])

if __name__ == "__main__":
    demo.launch(share=False)
