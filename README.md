# Recommendation System ML

Sistema de recomendacao de filmes baseado em conteudo usando TF-IDF e similaridade de cosseno.

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB.svg)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4-F7931E.svg)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[English](#english) | [Portugues](#portugues)

---

## Portugues

### Visao Geral

Sistema simples de recomendacao de filmes baseado em conteudo. Dado o titulo de um filme, encontra filmes similares com base na sobreposicao de generos e palavras-chave usando vetorizacao TF-IDF e similaridade de cosseno.

O dataset incluido contem apenas 5 filmes de exemplo. Substitua `data/movies.csv` por seus proprios dados para uso real.

### Arquitetura

```mermaid
graph LR
    A[movies.csv] --> B[Preprocessamento]
    B -->|genres + plot_keywords| C[TF-IDF Vectorizer]
    C --> D[Matriz de Similaridade - Cosseno]
    D --> E[Top-N Recomendacoes]
```

### Funcionalidades

- **Vetorizacao TF-IDF** — converte texto de generos e palavras-chave em vetores numericos
- **Similaridade de cosseno** — calcula similaridade entre todos os pares de filmes
- **Recomendacoes top-N** — retorna os N filmes mais similares ao titulo informado

### Como Executar

```bash
# Instalar dependencias
pip install -r requirements.txt

# Executar
python src/recommendation_system.py
```

### Exemplo de Saida

```
Top 5 recommendations for 'The Dark Knight':
1. The Dark Knight Rises (Score: 0.82)
2. Batman Begins (Score: 0.71)
...
```

### Estrutura do Projeto

```
Recommendation-System-ML/
├── data/
│   └── movies.csv                   # Dataset (5 filmes de exemplo)
├── src/
│   ├── __init__.py
│   └── recommendation_system.py     # Modulo principal (~85 linhas)
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

### Tecnologias

| Tecnologia | Uso |
|------------|-----|
| Python | Linguagem principal |
| pandas | Carregamento e manipulacao de dados |
| scikit-learn | TF-IDF e similaridade de cosseno |

### Limitacoes

- Dataset de exemplo com apenas 5 filmes
- Sem avaliacao de metricas (nao ha teste de precisao/recall)
- Sem API ou interface web
- Sem testes automatizados

---

## English

### Overview

Simple content-based movie recommendation system. Given a movie title, finds similar movies based on genre and plot keyword overlap using TF-IDF vectorization and cosine similarity.

The included dataset contains only 5 sample movies. Replace `data/movies.csv` with your own data for real use.

### Architecture

```mermaid
graph LR
    A[movies.csv] --> B[Preprocessing]
    B -->|genres + plot_keywords| C[TF-IDF Vectorizer]
    C --> D[Cosine Similarity Matrix]
    D --> E[Top-N Recommendations]
```

### Features

- **TF-IDF vectorization** — converts genre and keyword text into numerical vectors
- **Cosine similarity** — computes similarity between all movie pairs
- **Top-N recommendations** — returns the N most similar movies to the given title

### How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run
python src/recommendation_system.py
```

### Project Structure

```
Recommendation-System-ML/
├── data/
│   └── movies.csv                   # Dataset (5 sample movies)
├── src/
│   ├── __init__.py
│   └── recommendation_system.py     # Main module (~85 lines)
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

### Technologies

| Technology | Usage |
|------------|-------|
| Python | Core language |
| pandas | Data loading and manipulation |
| scikit-learn | TF-IDF and cosine similarity |

### Limitations

- Sample dataset with only 5 movies
- No evaluation metrics (no precision/recall testing)
- No API or web interface
- No automated tests

---

**Autor / Author:** Gabriel Demetrios Lafis
- GitHub: [@galafis](https://github.com/galafis)
- LinkedIn: [Gabriel Demetrios Lafis](https://linkedin.com/in/gabriel-demetrios-lafis)
