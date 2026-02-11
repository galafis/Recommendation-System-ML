# Recommendation-System-ML

![Hero Image](assets/hero_image.png)



## 🇧🇷 Sistema de Recomendação com Machine Learning

Este repositório apresenta um **Sistema de Recomendação** desenvolvido utilizando técnicas de **Machine Learning**. O objetivo é fornecer recomendações personalizadas de itens (como filmes, produtos, etc.) com base nas preferências do usuário e nas características dos itens. A implementação utiliza algoritmos de similaridade de conteúdo para gerar sugestões relevantes.

### 🚀 Funcionalidades

*   **Carregamento de Dados**: Suporte para carregar dados de arquivos CSV.
*   **Pré-processamento de Dados**: Limpeza e preparação dos dados para análise.
*   **Treinamento do Modelo**: Utiliza `TfidfVectorizer` e `cosine_similarity` para construir o modelo de recomendação.
*   **Geração de Recomendações**: Retorna uma lista de itens recomendados com base em um item de entrada.

### 🛠️ Tecnologias Utilizadas

*   **Python**: Linguagem de programação principal.
*   **Pandas**: Manipulação e análise de dados.
*   **scikit-learn**: Ferramentas para Machine Learning, incluindo `TfidfVectorizer` e `cosine_similarity`.

### ⚙️ Instalação e Uso

Para configurar e executar o projeto localmente, siga os passos abaixo:

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/galafis/Recommendation-System-ML.git
    cd Recommendation-System-ML
    ```

2.  **Crie um ambiente virtual (opcional, mas recomendado):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o sistema de recomendação:**

    ```bash
    python3 src/recommendation_system.py
    ```

    O script `recommendation_system.py` contém um exemplo de uso que carrega dados de `data/movies.csv`, treina o modelo e gera recomendações para filmes específicos.

### 📂 Estrutura do Projeto

```
Recommendation-System-ML/
├── data/
│   └── movies.csv          # Conjunto de dados de exemplo (filmes)
├── src/
│   └── recommendation_system.py # Lógica principal do sistema de recomendação
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo
```

### 📊 Conjunto de Dados

O arquivo `data/movies.csv` é um conjunto de dados de exemplo contendo informações sobre filmes, incluindo título, gêneros e palavras-chave do enredo. Este dataset é utilizado para demonstrar a funcionalidade do sistema de recomendação.

---

## 🇬🇧 Recommendation System with Machine Learning

This repository presents a **Recommendation System** developed using **Machine Learning** techniques. The goal is to provide personalized recommendations for items (such as movies, products, etc.) based on user preferences and item characteristics. The implementation uses content-based similarity algorithms to generate relevant suggestions.

### 🚀 Features

*   **Data Loading**: Supports loading data from CSV files.
*   **Data Preprocessing**: Cleans and prepares data for analysis.
*   **Model Training**: Uses `TfidfVectorizer` and `cosine_similarity` to build the recommendation model.
*   **Recommendation Generation**: Returns a list of recommended items based on an input item.

### 🛠️ Technologies Used

*   **Python**: Main programming language.
*   **Pandas**: Data manipulation and analysis.
*   **scikit-learn**: Machine Learning tools, including `TfidfVectorizer` and `cosine_similarity`.

### ⚙️ Installation and Usage

To set up and run the project locally, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/galafis/Recommendation-System-ML.git
    cd Recommendation-System-ML
    ```

2.  **Create a virtual environment (optional, but recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the recommendation system:**

    ```bash
    python3 src/recommendation_system.py
    ```

    The `recommendation_system.py` script includes an example of use that loads data from `data/movies.csv`, trains the model, and generates recommendations for specific movies.

### 📂 Project Structure

```
Recommendation-System-ML/
├── data/
│   └── movies.csv          # Example dataset (movies)
├── src/
│   └── recommendation_system.py # Main recommendation system logic
├── requirements.txt        # Project dependencies
└── README.md               # This file
```

### 📊 Dataset

The `data/movies.csv` file is an example dataset containing movie information, including title, genres, and plot keywords. This dataset is used to demonstrate the functionality of the recommendation system.

