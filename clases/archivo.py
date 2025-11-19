import pandas as pd

class Archivo:
    def m_geneOutput(self,p_texto):
        with open("output/correosEncontrados.txt", "w", encoding="utf-8") as v_archivo:
            v_archivo.write(p_texto)
            print("Archivo generado correctamente")


    def m_leerCorreos(self,p_direCorreos):
        v_respuesta=""
        with open(p_direCorreos, "r", encoding="utf-8") as v_archivo:
            for linea in v_archivo.readlines():
                v_respuesta+=linea.strip()+" "
        return v_respuesta.strip()

    def m_cargMatrTransicion(self, ruta_excel):
        # Leer todo el Excel como texto
        df = pd.read_excel(ruta_excel, dtype=str)

        simbolos = list(df.columns[1:])

        matriz = {}
        for _, fila in df.iterrows():
            estado = str(fila["Estado"]).strip()
            matriz[estado] = {}
            for simbolo in simbolos:
                destino = str(fila[simbolo]).strip() if pd.notna(fila[simbolo]) else None
                if destino:
                    matriz[estado][str(simbolo).strip()] = destino

        return matriz