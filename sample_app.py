import streamlit as st

st.title("this is a text")
st.write("this is a text")

# """
# # This is title
# ## This is subtitle

# - first
# - second
# - Third
# """ 

# # input box: 텍스트 노출
# text = st.text_input("text_input")
# st.write(text)

# # check box
# selected = st.checkbox("개인정보 사용에 동의하시겠습니까?")
# if selected:
#     st.success("동의했습니다.")

# # select box
# market = st.selectbox("시장",("코스닥","코스피","나스닥"))
# st.write(f"selected market: {market}")

# options = st.multiselect("종목",
#                ["네이버","카카오","삼성전자","현대자동차"])
# st.write(', '.join(options))

# # metric
# st.metric(label="네이버", value="200000 원", delta="-1000 원")

