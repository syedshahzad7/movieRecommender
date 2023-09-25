import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies =[]
        for i in movies_list:
            recommended_movies.append(movies.iloc[i[0]].title)
        return recommended_movies

movies_dict = pickle.load(open('static/movies_all.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('static/similarity.pkl','rb'))

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2022/02/21/06/11/tablet-7025855_1280.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()



original_title = '<h6 style="font-family:Courier; color:white; font-size: 40px;">MOVIE RECOMMENDER GENERATOR</h6>'
st.markdown(original_title, unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    'Choose The Movie For Recommendation',movies['title'].values)


if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)