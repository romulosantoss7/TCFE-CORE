# TCFE Core SDK

**Autor:** Rômulo Santos de Carvalho  
**Versão:** 1.0.0

Este pacote implementa o núcleo computacional da Teoria do Campo de Força Estrutural (TCFE), permitindo análise vetorial, diagnóstico estrutural, visualização e simulação de circuitos quânticos baseados nos parâmetros θ (intenção), μ (resistência) e σ (coesão/ruído).

---

## 📦 Instalação

Clone o repositório ou extraia o `.zip` e depois execute:

```bash
pip install .
```

---

## 🚀 Uso Rápido

```python
from tcfe_core import init_engine, plot_zona_omega

engine = init_engine(lente="psiquico")
print(engine.classificar_regime())
plot_zona_omega(engine)
```

---

## 🧠 Lentes Disponíveis

- `psiquico` — Psíquico (MindLens)
- `fisico` — Físico (MechLens)
- `organizacional` — Organizacional (OrgLens)
- `quantico` — Quântico (QbitLens)

---

## 🧪 Simulação Quântica (Qiskit)

```python
engine.simular()  # Simula localmente com Aer
```

Ou exporte tudo com:

```python
engine.exportar_tudo()
```

---

## 📁 Estrutura

```
tcfe_core/
├── engine.py            # Núcleo do cálculo TCFE
├── visual.py            # Plotagem de LF x ER
├── qiskit_integration.py # Geração e simulação de QASM
├── constants/
│   ├── calibracao.json
│   └── lentes.json
```

---

## 📃 Licença

MIT License
