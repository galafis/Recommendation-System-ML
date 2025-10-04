import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

class RecommendationSystem:
    def __init__(self, data_path='data/movies.csv'):
        self.data_path = data_path
        self.df = None
        self.tfidf_matrix = None
        self.cosine_sim = None

    def load_data(self):
        try:
            self.df = pd.read_csv(self.data_path)
            print("Dados carregados com sucesso.")
        except FileNotFoundError:
            print(f"Erro: O arquivo {self.data_path} não foi encontrado.")
            self.df = pd.DataFrame()

    def preprocess_data(self):
        if self.df.empty:
            print("Nenhum dado para pré-processar.")
            return
        
        # Exemplo de pré-processamento: combinar colunas para TF-IDF
        self.df['combined_features'] = self.df['genres'].fillna('') + ' ' + self.df['plot_keywords'].fillna('')
        print("Dados pré-processados.")

    def train_model(self):
        if self.df.empty or 'combined_features' not in self.df.columns:
            print("Nenhum dado ou features combinadas para treinar o modelo.")
            return

        tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = tfidf.fit_transform(self.df['combined_features'])
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)
        print("Modelo treinado com sucesso.")

    def recommend_movies(self, title, num_recommendations=10):
        if self.df.empty or self.cosine_sim is None:
            print("Sistema de recomendação não está pronto. Carregue os dados e treine o modelo primeiro.")
            return []

        if title not in self.df['title'].values:
            print(f"Filme '{title}' não encontrado na base de dados.")
            return []

        idx = self.df[self.df['title'] == title].index[0]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:num_recommendations+1] # Exclui o próprio filme

        movie_indices = [i[0] for i in sim_scores]
        return self.df['title'].iloc[movie_indices].tolist()

if __name__ == "__main__":
    # Exemplo de uso
    recommender = RecommendationSystem()
    recommender.load_data()
    recommender.preprocess_data()
    recommender.train_model()

    if not recommender.df.empty:
        # Adicionar alguns dados de exemplo para teste
        if 'title' not in recommender.df.columns or 'genres' not in recommender.df.columns or 'plot_keywords' not in recommender.df.columns:
            print("Adicionando dados de exemplo para teste.")
            example_data = {
                'title': ['The Dark Knight', 'Interstellar', 'Inception', 'Toy Story', 'Avatar'],
                'genres': ['Action|Crime|Drama', 'Adventure|Drama|Sci-Fi', 'Action|Adventure|Sci-Fi|Thriller', 'Animation|Adventure|Comedy', 'Action|Adventure|Fantasy|Sci-Fi'],
                'plot_keywords': ['superhero|crime|gotham', 'space|travel|future', 'dream|heist|subconscious', 'toys|adventure|friendship', 'alien|planet|future']
            }
            recommender.df = pd.DataFrame(example_data)
            recommender.preprocess_data() # Re-preprocess with new data
            recommender.train_model() # Re-train with new data

        recommendations = recommender.recommend_movies('The Dark Knight')
        print(f"Recomendações para 'The Dark Knight': {recommendations}")

        recommendations_interstellar = recommender.recommend_movies('Interstellar')
        print(f"Recomendações para 'Interstellar': {recommendations_interstellar}")
    else:
        print("Não foi possível executar o exemplo de uso devido à falta de dados.")

