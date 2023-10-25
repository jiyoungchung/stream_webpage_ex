# fastapi api 서버 (로 서빙)
# 광고 문구 작성 함수를 호출

import random
from fastapi import FastAPI
from pydantic import BaseModel

class AdGenerator:
    ''' 
    광고 문구 만드는 클래스
    '''
    def __init__(self):
        self.adjectives = ["신나는", "매혹적인", "혁신적인", "환상적인", "놀라운", "편안한"]
        self.actions = ["체험하세요", "사용해보세요", "즐기세요", "누려보세요", "놓치지 마세요", "구입해보세요"]

    def generate_ad(self, product):
        adjective  = random.choice(self.adjectives)
        action = random.choice(self.actions)
        ad_text = f"{adjective} {product}을(를) {action}!"
        return ad_text

# # 예시
# generator = AdGenerator()
# ad1 = generator.generate_ad("나이키 신발")

# fastapi
app = FastAPI()

class Product(BaseModel):
    product_name:str

@app.post("/create_ad_slogan")
def create_ad_slogan(product:Product):
    product_name = product.product_name               # Product에서 input을 받아서 product_name에 저장
    generator = AdGenerator()                         # 클래스 호출
    ad_slogan = generator.generate_ad(product_name)   # 광고 문구 호출
    return {"product_name": product_name, "ad_slogan": ad_slogan}