import streamlit as st
from PIL import Image
import pandas as pd
import pydeck as pdk
import numpy as np
import random

image = Image.open('images.jfif')
st.image(image, width=1000)

st.title("My First App")
st.caption("これは地域経済実践演習の練習アプリです")
st.subheader("入力事項")
st.write("以下の項目を入力してください")
st.markdown("# 練習")
st.markdown("## 練習中")

with st.form(key='info_form'):
    
    name = st.text_input('名前')
    address = st.text_input('住所')
    st.checkbox('banana')
    st.radio('お手持ちの携帯電話の会社', ('au', 'soufbank', 'docomo','その他'))
    st.text_input('その他の方はご入力ください')

    
    st.text_area('クレーム承ります！！！')
    
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'ようこそ。{address}にお住いの{name}さん、こんにちは！')
        
df = pd.read_csv('data.csv', index_col='月')
st.dataframe(df)
st.table(df)
st.line_chart(df)
st.bar_chart(df['2020年'])

chart_data = pd.DataFrame(
    np.random.randn(30, 2) / [3000, 3000] + [34.7979457494506, 135.2464190411745],
    columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=34.7979457494506,
        longitude=135.2464190411745,
        zoom=16,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=chart_data,
            get_position='[lon, lat]',
            radius=5,
            elevation_scale=4,
            elevation_range=[0, 10],
            pickable=True,
            extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position_data='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=6,
        ),
    ],
))