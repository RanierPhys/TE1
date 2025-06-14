# 📡 Simulações de Campos Elétricos Relativísticos (TE1)

**Projeto teórico-computacional** desenvolvido por [Ranier Menote](https://github.com/RanierPhys) para visualizar linhas de campo elétrico de partículas carregadas em movimento acelerado, com aplicações em física de aceleradores e eletrodinâmica clássica.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.8%2B-yellowgreen)


<p align="center">
  <img src="figures/uniform_acceleration/72.png" width="45%">
  <img src="figures/synchtrotron/sincro.png" width="45%">
</p>

## 📌 Recursos Principais
- ✅ Simulações completas de 5 cenários físicos:
  - Movimento uniformemente acelerado
  - Desaceleração relativística
  - Oscilador harmônico
  - Radiação Wiggler
  - Movimento circular (síncrotron)
- ✅ Visualização científica com `matplotlib` e `numpy`
- ✅ Artigo PDF com fundamentação teórica completa
- ✅ Código modular e documentado para reprodução

## 🛠️ Tecnologias Utilizadas
| Área          | Ferramentas |
|---------------|------------|
| **Linguagem** | Python 3.8+ |
| **Bibliotecas**| `numpy`, `matplotlib`, `scipy` |
| **Física**    | Eletrodinâmica relativística, tempo retardado, formalismo covariante |
| **Métodos**   | Solução numérica de EDOs, visualização vetorial |

## 🚀 Como Executar
```bash
# 1. Clone o repositório
git clone https://github.com/RanierPhys/TE1.git
cd TE1

# 2. Instale as dependências (recomendado: ambiente virtual)
pip install -r requirements.txt

# 3. Execute qualquer simulação:
python simulations/uniform_acceleration.py  # Movimento acelerado
python simulations/synchrotron.py           # Síncrotron


📂 Estrutura do Projeto

TE1/
├── paper/
│   └── Campo_Elétrico_Relativístico.pdf   # Artigo completo
├── simulations/
│   ├── uniform_acceleration.py           # Caso 1: Eq. 11
│   ├── uniform_deceleration.py           # Caso 2: Eq. 19-20
│   ├── oscillator.py                     # Caso 3: Eq. 21-22
│   ├── wiggler.py                        # Caso 4: Eq. 33
│   └── synchrotron.py                    # Caso 5: Eq. 43
└── figures/
    ├── uniform_acceleration/             # Figuras 1-2 do artigo
    ├── synchrotron/                      # Figura 6
    └── ...
                                # Parâmetros de simulação

📄 Documentação Teórica
O artigo em paper/Campo_Elétrico_Relativístico.pdf contém:

Dedução das equações de campo (Seção 2)

Soluções analíticas para cada caso físico

Análise dos resultados (Figuras 1-6)

Email: ranier_m@hotmail.com

LinkedIn: www.linkedin.com/in/ranier-menote-lemes-silva-b57755275

GitHub: RanierPhys


Palavras Chave:
Python científico, otimização numérica, visualização vetorial,
Eletrodinâmica relativística, formalismo covariante, Validação teórico-computacional, 
interpretação física, tempo retardado
