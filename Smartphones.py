import pickle
import pandas as pd
import streamlit as st


def recommend(smartphone):
    smartphone_index = smartphones[smartphones['model'] == smartphone].index[0]
    distances = similarity[smartphone_index]
    smartphones_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_smartphones = []
    for i in smartphones_list:
        recommended_smartphones.append(smartphones['tags'].iloc[i[0]])
    return recommended_smartphones


smartphone_dict = pickle.load(open('smartphone_dict.pkl', 'rb'))
smartphones = pd.DataFrame(smartphone_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("SmartPhone Recommender System")
Selected_smartphone = st.selectbox('Please select', smartphones['model'].values)

if st.button('Recommend'):
    recommendations = recommend(Selected_smartphone)
    for i in recommendations:
        st.write(i)