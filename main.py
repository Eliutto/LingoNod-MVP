"""
-------------------------------------------------------------------------
PROYECTO: LingoNod MVP (ACA 3)
DESCRIPCIÓN: Sistema de traducción comercial con FastAPI y Web Speech API.
AUTORES: 
    - Jhonny Alberto Cotrina Buitrago
    - Gerson Eliut Torrado Guerrero
FECHA: Enero 2026
-------------------------------------------------------------------------
"""
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles # <--- NUEVO IMPORT
# CAMBIO: Usamos deep_translator que es más estable
from deep_translator import GoogleTranslator
from datetime import datetime
import traceback



app = FastAPI()

# --- ESTA ES LA LÍNEA MÁGICA PARA EL LOGO ---
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Historial en memoria
historial_traducciones = []

class TranslationRequest(BaseModel):
    text: str
    source_lang: str
    target_lang: str

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/translate")
async def translate_text(request: TranslationRequest):
    print(f"📥 Recibido: {request.text} ({request.source_lang} -> {request.target_lang})")
    
    try:
        # Ajuste de códigos de idioma para deep_translator
        # (El navegador envía 'en-US', pero el traductor quiere 'en')
        src_code = request.source_lang.split('-')[0] # toma 'en' de 'en-US'
        tgt_code = request.target_lang.split('-')[0] # toma 'es' de 'es-ES'

        # TRADUCCIÓN CON LA NUEVA LIBRERÍA
        translator = GoogleTranslator(source=src_code, target=tgt_code)
        translated_text = translator.translate(request.text)
        
        print(f"✅ Éxito: {translated_text}")

        # Guardar reporte
        registro = {
            "hora": datetime.now().strftime("%H:%M:%S"),
            "original": request.text,
            "traduccion": translated_text,
            "idioma_origen": src_code,
            "idioma_destino": tgt_code
        }
        historial_traducciones.append(registro)
        
        return {"original": request.text, "translated": translated_text}

    except Exception as e:
        print(f"❌ ERROR CRÍTICO: {str(e)}")
        traceback.print_exc()
        # Aquí enviamos el error al frontend para que no diga "undefined"
        return JSONResponse(status_code=500, content={"message": str(e)})

@app.get("/api/reporte")
def get_reporte():
    return historial_traducciones

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
