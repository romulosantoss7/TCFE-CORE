from .engine import TCFEngine
from .visual import plot_zona_omega
from .qiskit_integration import gerar_qasm, simular_qasm

__version__ = "1.0.0"
__author__ = "Rômulo Santos de Carvalho"

def init_engine(lente: str = "organizacional",
                phi: float = 0.8, psi: float = 0.9, theta_graus: float = 15,
                mu: float = 0.5, sigma: float = 0.6) -> TCFEngine:
    engine = TCFEngine(lente=lente)
    engine.set_vetores(phi, psi, theta_graus)
    engine.set_parametros(mu, sigma)
    engine.calcular_metricas()
    engine.descrever_lente()
    return engine
