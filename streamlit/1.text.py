# streamlit, pandas 라이브러리 불러오기 
import streamlit as st
import pandas as pd

# header, subheader, text, caption 연습하기
st.title('Text elements')
st.caption('text 참고사이트: https://docs.streamlit.io/library/api-reference/text')
st.header('Header: 데이터 분석 표현')
st.subheader('Subheader: 스트림릿')
st.text('Text: this is the Streamlit')
st.caption('Caption: Streamlit은 2019년 하반기에 등장한 파이썬 기반의 웹어플리케이션 툴이다.')

# markdown 연습하기
st.markdown('# Markdown')
st.markdown('## Markdown')
st.markdown('### Markdown')

st.markdown('Markdown')
st.markdown('- Markdown')
# Latex & Code 연습하기
st.markdown('## Code & Latex')

st.code('x=2021')
st.latex(r''' a + ar + a r^2 + a r^3''')

# write 연습하기
st.title('write')
st.caption('참고사이트: https://docs.streamlit.io/library/api-reference/write-magic/st.write')
st.text('아래 딕셔너리를 판다스 데이터프레임으로 변경')
st.caption("{'이름': ['홍길동', '김사랑', '일지매', '이루리'],'수준': ['금', '동', '은', '은']}")

df = pd.DataFrame({'이름': ['홍길동', '김사랑', '일지매', '이루리'],'수준': ['금', '동', '은', '은']})
st.write('딕셔너리를 판다스의 데이터프레임으로 바꿔서:', df, '스트림릿의 write 함수로 표현.')

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run 파이썬파일명