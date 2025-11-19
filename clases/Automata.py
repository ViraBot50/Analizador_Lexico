from warnings import catch_warnings

from clases.archivo import Archivo

class Automata:
    a_estaInicial=""
    a_estaFinal=""
    a_matriz={}
    def __init__(self):
        self.a_estaInicial="q0"
        self.a_estaFinal="q7"
        self.a_matriz=Archivo().m_cargMatrTransicion("input/matriz.xlsx")


    def m_buscCorreos(self,p_cadena):
        v_respuesta=""
        v_estaActual=self.a_estaInicial
        v_cadeActual=""
        v_posicion=0
        v_caraActual=""
        while v_estaActual!=self.a_estaFinal and v_posicion<len(p_cadena):
            v_caraActual=p_cadena[v_posicion]
            v_cadeActual+=v_caraActual
            #print(v_caraActual)
            if v_caraActual==" " :
                if v_estaActual=="q6":
                    v_respuesta+=v_cadeActual+"\n"
                v_cadeActual=""
                v_caraActual="espacio"

            else :
                if v_caraActual=="$" :
                    if v_estaActual=="q6":
                        v_respuesta+=v_cadeActual+"\n"

            #print(v_estaActual)

            v_estaActual=self.a_matriz[v_estaActual][v_caraActual]
            v_posicion+=1

        return v_respuesta.strip()