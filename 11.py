import pickle
import streamlit as st
import pandas as pd
import os
import numpy as np
import altair as alt
import base64

#membuka file sav
model = pickle.load(open('model_prediksi_harga_mobil.sav', 'rb'))

        
@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No": 1, "Yes": 2}
    for key, value in feature_dict.items():
        if val == key:
            return value
def get_value(val, my_dict):
    for key, value in my_dict.items():
        if val == key:
            return value
        
#membuat sidebar
app_mode = st.sidebar.selectbox(
    'Select Page', ['Home', 'Highway-mpg', 'curbweight', 'horsepower','price prediction'])

#sidebar untuk home
if app_mode=='Home':
    st.title('Prediksi Harga Mobil')

    st.image('car.jpg')

    st.header("Dataset")

    df1 = pd.read_csv('CarPrice.csv')
    st.dataframe(df1)

# sidebar untuk highway-mpg
elif app_mode == 'Highway-mpg':
    st.write('Dataset')
    df1 = pd.read_csv('CarPrice.csv')
    st.dataframe(df1)
    st.write("Grafik Highway-mpg")
    chart_highwaympg = pd.DataFrame(df1, columns=["highwaympg"])
    st.line_chart(chart_highwaympg)
    st.bar_chart(chart_highwaympg)
    st.area_chart(chart_highwaympg)
# sidebar untuk curbweight
elif app_mode=='curbweight':
    st.write('Dataset')
    df1 = pd.read_csv('CarPrice.csv')
    st.dataframe(df1)
    st.write("Grafik curbweight")
    chart_curbweight = pd.DataFrame(df1, columns=["curbweight"])
    st.line_chart(chart_curbweight)
    st.bar_chart(chart_curbweight)
    st.area_chart(chart_curbweight)

#sidebar untuk horsepower
elif app_mode == 'horsepower':
    st.write('Dataset')
    df1 = pd.read_csv('CarPrice.csv')
    st.dataframe(df1)
    st.write("Grafik horsepower")
    chart_horsepower = pd.DataFrame(df1, columns=["horsepower"])
    st.line_chart(chart_horsepower)
    st.bar_chart(chart_horsepower)
    st.area_chart(chart_horsepower)

#sidebar untuk input price
elif app_mode == 'price prediction':
    st.write('Dataset')
    df1 = pd.read_csv('CarPrice.csv')
    st.dataframe(df1)
    highwaympg = st.number_input('Highway-mpg', 0, 10000000)
    curbweight = st.number_input('Curbweight', 0, 10000000)
    horsepower = st.number_input('Horsepower', 0, 10000000)

    #button untuk prediksi
    if st.button('Prediksi'):
        car_prediction = model.predict([[highwaympg, curbweight, horsepower]])

        harga_mobil_str = np.array(car_prediction)
        harga_mobil_float = float(harga_mobil_str[0])

        harga_mobil_formatted = "{:,.2f}".format(harga_mobil_float)
        st.markdown(f'Harga Mobil: $ {harga_mobil_formatted}')
