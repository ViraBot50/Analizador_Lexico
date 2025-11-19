from clases.Automata import Automata
from clases.archivo import Archivo
v_objAutomata=Automata()
v_ctrlArchivos=Archivo()
v_cadeFinal=v_objAutomata.m_buscCorreos(v_ctrlArchivos.m_leerCorreos("input/correos.in"))
print(v_cadeFinal)
v_ctrlArchivos.m_geneOutput(v_cadeFinal)
