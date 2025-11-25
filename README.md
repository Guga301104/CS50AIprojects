# 📘 CS50AI – Projetos do Curso (Harvard)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Harvard](https://img.shields.io/badge/Harvard-CS50AI-A51C30?style=flat-square&logo=harvard)

Este repositório contém minhas implementações, soluções e anotações referentes ao curso **CS50’s Introduction to Artificial Intelligence with Python**, oferecido pela Harvard University.

O curso aborda fundamentos de IA moderna — busca, lógica, probabilidade, otimização, aprendizado de máquina, redes neurais, NLP e mecanismos de atenção — sempre com projetos práticos.

---

## 🧠 Conteúdos e Projetos

### 📍 projects0 — Search
**Foco:** Algoritmos de busca (DFS, BFS, A*, Minimax).
- **Project0 — Degrees:** Descoberta de graus de separação entre atores (busca em largura).
- **Project0b — Tic-Tac-Toe:** IA perfeita para Jogo da Velha utilizando Minimax.

### 📍 projects1 — Knowledge
**Foco:** Lógica proposicional e inferência.
- **Project1 — Knights:** Resolução de quebra-cabeças lógicos usando proposições.
- **Project1b — Minesweeper:** IA para jogar Campo Minado usando inferência lógica.

### 📍 projects2 — Uncertainty
**Foco:** Probabilidade e Redes Bayesianas.
- **Project2 — PageRank:** Implementação do algoritmo de ranqueamento do Google.
- **Project2b — Heredity:** Inferência de probabilidade em genética.

### 📍 projects3 — Optimization
**Foco:** Problemas de Satisfação de Restrições (CSP).
- **Project3 — Crossword:** Solucionador de palavras cruzadas que respeita restrições de estrutura e vocabulário.

### 📍 projects4 — Learning
**Foco:** Machine Learning Supervisionado e por Reforço.
- **Project4 — Shopping:** Predição de comportamento de compra de usuários (k-NN).
- **Project4b — Nim:** IA que aprende a jogar Nim sozinha via Q-Learning.

### 📍 projects5 — Neural Networks
**Foco:** Redes Neurais e TensorFlow.
- **Project5 — Traffic:** Rede neural convolucional (CNN) para reconhecimento de placas de trânsito.

### 📍 projects6 — Language
**Foco:** Processamento de Linguagem Natural (NLP) e Transformers.
- **Project6 — Parser:** Análise sintática de frases em inglês (Context-Free Grammar).
- **Project6b — Attention:** Implementação de mecanismos de atenção (BERT).

---

## 🗂 Estrutura do Repositório

```text
/
├── projects0/
│   ├── degrees/
│   └── tictactoe/
│
├── projects1/
│   ├── knights/
│   └── minesweeper/
│
├── projects2/
│   ├── pagerank/
│   └── heredity/
│
├── projects3/
│   └── crossword/
│
├── projects4/
│   ├── shopping/
│   └── nim/
│
├── projects5/
│   └── traffic/
│
├── projects6/
│   ├── parser/
│   └── attention/
│
└── README.md
```

## 📦 Dependências Principais
Como este repositório agrupa vários projetos, as dependências variam. As principais bibliotecas utilizadas no curso são:
* pygame (para Tic-Tac-Toe, Minesweeper, etc.)
* scikit-learn (para Shopping)
* tensorflow (para Traffic e Attention)
* nltk (para Parser)
* Pillow (para processamento de imagens)

Caso não haja um requirements.txt na pasta específica, você pode instalar as bibliotecas manualmente conforme a necessidade do script.

## 🚀 Como Executar
Cada pasta contém instruções específicas dos projetos. De modo geral, o fluxo é:

Navegue até a pasta do projeto:

Bash
```
cd projectsX/nome_do_projeto
```
Instale as dependências: Verifique se há um arquivo requirements.txt na pasta. Se houver:

Bash
```
pip install -r requirements.txt
```
Caso contrário, instale a biblioteca necessária manualmente (ex: pip install pygame).
Execute o script principal: Geralmente o comando segue este formato (verifique o enunciado de cada projeto):

Bash
```
python3 nome_do_arquivo.py [argumentos]
```

## 🎓 Sobre o Curso
CS50’s Introduction to Artificial Intelligence with Python > Harvard University

[Link Oficial do Curso](https://cs50.harvard.edu/ai/)

Um dos cursos mais completos sobre IA moderna, combinando teoria rigorosa, matemática e prática em projetos que simulam problemas do mundo real.

👤 Autor
Gustavo Gontijo

Repositório destinado a registrar minha evolução e estudos em Inteligência Artificial.