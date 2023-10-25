import streamlit as st
import requests


# 페이지 기본 설명
st.set_page_config( 
    page_icon='💡',                         # 이모티콘 넣을 수 있는 곳
    page_title='광고문구 작성 서비스',      # 페이지 제목
)
st.title("광고문구 작성 서비스")

# backend
generate_ad_slogan_url = "http://localhost:8000/create_ad_slogan"

# back 쪽에서 input으로 받아야 될 것들 만들기 (나는 제품이름만)
product_name = st.text_input("제품 이름")

# 내용을 받아서 back 쪽으로 전달
if st.button("광고 문구 생성"):
    try:
        response = requests.post(generate_ad_slogan_url,
                                json={"product_name":product_name})
        
        ad_slogan = response.json()['ad_slogan']
        st.success(ad_slogan)

    except:
        st.error("예상치 못한 에러가 발생했습니다")