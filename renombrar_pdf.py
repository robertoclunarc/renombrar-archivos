import os
import openpyxl
import shutil
from PyPDF2 import PdfReader

# Ruta de la carpeta con los archivos PDF
carpeta_pdf = r"C:\Users\rober\OneDrive\Escritorio\arc2023\individuales"

def extraer_info_desde_pdf(ruta_pdf):
    with open(ruta_pdf, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        # Puedes personalizar la lógica para extraer información específica del PDF aquí
        # En este ejemplo, se extrae el texto de la primera página
        texto_pdf = pdf_reader.pages[0].extract_text()
        palabras = texto_pdf.split()
        nombre = None
        ccosto = palabras[31]
        cedula = None
        print("Arreglo:")
        print(palabras[30], palabras[31], palabras[32])
        print(palabras[33], palabras[34], palabras[35])
        print(palabras[36], palabras[37], palabras[38])
        print(palabras[39], palabras[40], palabras[41])
        print(palabras[42], palabras[43], palabras[44])
        print(palabras[45], palabras[46], palabras[47])
        print(palabras[48], palabras[49], palabras[50])
        for i in range(len(palabras)):
            if palabras[i] == "Apellidos" and i < len(palabras) - 1:
                nombre = f"{palabras[i + 5]} {palabras[i + 6]} {palabras[i + 7]}"
                cedula = palabras[i + 4]
               
        return nombre, ccosto, cedula

def renombrar_archivos_desde_pdf(carpeta_pdf):
    # Lista de archivos en la carpeta PDF
    archivos_pdf = [f for f in os.listdir(carpeta_pdf) if f.endswith(".pdf")]

    # Verificar que haya suficientes archivos PDF
    if len(archivos_pdf) == 0:
        print("No hay archivos PDF en la carpeta especificada.")
        return
    indice = 0
    # Iterar sobre los archivos PDF y renombrarlos
    for archivo_pdf in archivos_pdf:
        ruta_pdf = os.path.join(carpeta_pdf, archivo_pdf)
        indice = indice + 1
        print("Renombrando Archivo Nro: ", indice)
        # Extraer información desde el PDF
        nombre, ccosto, cedula = extraer_info_desde_pdf(ruta_pdf)
        # Construir el nuevo nombre
        nuevo_nombre = f"{cedula}{nombre}_{ccosto}.pdf"

        # Ruta completa de los archivos
        ruta_nueva = os.path.join(carpeta_pdf, nuevo_nombre)

        # Renombrar el archivo
        try:
            os.rename(ruta_pdf, ruta_nueva)
            print(f"Archivo renombrado: {ruta_pdf} -> {ruta_nueva}")
        except Exception as e:
            print(f"Error al renombrar el archivo {ruta_pdf}: {e}")

# Llamar a la función
renombrar_archivos_desde_pdf(carpeta_pdf)
