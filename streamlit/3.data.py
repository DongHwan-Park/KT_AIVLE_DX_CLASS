# streamlit, pandas 라이브러리 불러오기 
import streamlit as st
import pandas as pd
st.title('Unit 3. Data display elements')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/data')

st.header('# 1. Metric')
st.metric(label = "Temperature", value = '30.5 C', delta = '2.5 C')
st.metric(label = "Temperature", value = '28 C', delta = '-2.5 C')

st.header('# 2. columns')
col1, col2, col3 = st.columns(3)
col1.metric('기온', '30.5 C', '2.5 C')
col2.metric('풍속', '9 mph', '-8%')
col3.metric('습도', '86 %', '4%')

st.header('# 3. Dataframe')
st.caption('10개 행  기준 스크롤, 열 크기조정, 열 정렬, 테이블  확대')

# 파일 위치- https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv
path = 'https://raw.githubusercontent.com/huhshin/streamlit/master/data_titanic.csv'
titanic = pd.read_csv(path)
st.dataframe(titanic)


st.header('# 4. Table')
st.caption('Table - 고정 형태의 테이블')

st.table(titanic)


# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\3.data.py