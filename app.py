import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from styles import load_css

# ---------------------------- 
# Streamlit Page Config - THIS MUST BE FIRST!
# ---------------------------- 
st.set_page_config(page_title="Bollywood Movie Recommender", page_icon="🎬", layout="centered")

# ---------------------------- 
# Load External CSS 
# ---------------------------- 
st.markdown(load_css(), unsafe_allow_html=True)

# ---------------------------- 
# Load and preprocess dataset 
# ---------------------------- 
@st.cache_data
def load_data():
    df = pd.read_csv('BollywoodMovies.csv')
    df.columns = df.columns.str.strip().str.lower()

    df.rename(columns={
        'movie name': 'title',
        'genre': 'genre',
        'lead star': 'actors',
        'director': 'director'
    }, inplace=True)

    required_columns = ['title', 'genre', 'actors', 'director']
    for col in required_columns:
        if col not in df.columns:
            st.error(f"Missing column in dataset: {col}")
            return None

    for col in required_columns:
        df[col] = df[col].fillna('')

    df['combined_features'] = df['genre'] + ' ' + df['actors'] + ' ' + df['director']
    return df

@st.cache_resource
def train_knn(df, n_neighbors=6):
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['combined_features'])

    knn_model = NearestNeighbors(metric='cosine', algorithm='brute')
    knn_model.fit(tfidf_matrix)

    return knn_model, tfidf_matrix

def recommend_movies_knn(movie_title, df, knn_model, tfidf_matrix, n_recommendations=5):
    if movie_title not in df['title'].values:
        return None

    movie_idx = df[df['title'] == movie_title].index[0]
    movie_vector = tfidf_matrix[movie_idx]

    distances, indices = knn_model.kneighbors(movie_vector, n_neighbors=n_recommendations + 1)

    recommended_movies = []
    for i in range(1, len(indices[0])):
        idx = indices[0][i]
        recommended_movies.append({
            'title': df.iloc[idx]['title'],
            'genre': df.iloc[idx]['genre'],
            'actors': df.iloc[idx]['actors'],
            'director': df.iloc[idx]['director'],
            'distance': distances[0][i]
        })

    return recommended_movies

# ---------------------------- 
# Render Movie Card 
# ---------------------------- 
def render_movie_card(rec):
    st.markdown(f"""
        <div class="movie-card">
            <div class="movie-title">{rec['title']}</div>
            <div class="movie-info">🎭 Genre: {rec['genre']}</div>
            <div class="movie-info">🎬 Actors: {rec['actors']}</div>
            <div class="movie-info">🎥 Director: {rec['director']}</div>
            <div class="similarity-score">🔍 Similarity Score: {rec['distance']:.4f}</div>
        </div>
    """, unsafe_allow_html=True)

# ---------------------------- 
# Streamlit Web App Interface 
# ---------------------------- 
def main():
    # Header block after CSS is loaded
    st.markdown("""
        <div class="header-container">
            <h1 class="main-title">🎬 Bollywood Movie Recommender</h1>
            <p class="subtitle">✨ Discover movies similar to your favorite!</p>
        </div>
    """, unsafe_allow_html=True)

    df = load_data()
    if df is None:
        return

    knn_model, tfidf_matrix = train_knn(df)

    movie_list = df['title'].sort_values().unique()
    selected_movie = st.selectbox("Select a movie you like:", movie_list)

    if 'recommendations' not in st.session_state:
        st.session_state['recommendations'] = []
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 1

    recommendations_per_page = 5

    if st.button("Get Recommendations"):
        recommendations = recommend_movies_knn(selected_movie, df, knn_model, tfidf_matrix, n_recommendations=20)
        if recommendations:
            st.session_state['recommendations'] = recommendations
            st.session_state['current_page'] = 1
        else:
            st.session_state['recommendations'] = []
            st.warning(f"No recommendations found for {selected_movie}.")

    recommendations = st.session_state['recommendations']

    if recommendations:
        st.success(f"Recommendations similar to **{selected_movie}**:")

        # Wrap the cards in a container
        st.markdown("<div class='recommendations-container'>", unsafe_allow_html=True)

        total_recommendations = len(recommendations)
        total_pages = (total_recommendations + recommendations_per_page - 1) // recommendations_per_page
        current_page = st.session_state['current_page']

        start_idx = (current_page - 1) * recommendations_per_page
        end_idx = start_idx + recommendations_per_page
        paginated_recommendations = recommendations[start_idx:end_idx]

        for rec in paginated_recommendations:
            render_movie_card(rec)

        st.markdown("</div>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])

        with col1:
            if current_page > 1:
                if st.button("⬅️ Previous"):
                    st.session_state['current_page'] -= 1
                    st.rerun()

        with col3:
            if current_page < total_pages:
                if st.button("Next ➡️"):
                    st.session_state['current_page'] += 1
                    st.rerun()

        with col2:
            st.markdown(f"<div class='page-info'>Page {current_page} of {total_pages}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()