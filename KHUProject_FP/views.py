# -- coding: utf-8 --
"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, request,redirect
from KHUProject_FP import app
from werkzeug import secure_filename
import pymysql
import copy
import cv2
from keras.models import model_from_json

@app.route('/')
@app.route('/home')
def home(charset="euc-kr"):
    return render_template(
        'index2.html'
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/upload',methods=['GET','POST'])
def load_file():
    if request.method == 'POST':
        answerlist = ['세라마이딘 리퀴드', '엑스트라 페이스 오일','이드라 세럼','블루 쎄럼','보떼 이니샬','컨트롤에이 수딩 모이스처라이저','엑스트라 리페어 모이스춰 크림','르리프트 아이크림','세라마이딘 크림','이드라 뷰티 마이크로 버블 크림','2세대 시카페어 크림','리바이탈라이징 수프림+ 글로벌 안티에이징 파워 크림','6세대 갈색병 리페어 에센스','아이디얼리스트 포어 미니마이징 스킨 리휘니셔','마이크로 에센스 스킨 액티베이팅 트리트먼트 로션','하이드레셔니스트 모이스춰 크림','더마클리어 마이크로 폼','베이킹 파우더 모공 클렌징폼','닥터자르트 바이탈 하이드라 솔루션 바이옴','크레센트 화이트 풀 사이클 브라이트닝 UV 프로텍터 SPF 50/PA++++','원더포어 프레쉬너','수분가득 콜라겐 크림','리얼아트 클렌징 오일 모이스처','블루베리 리밸런싱세트','몬스터 미셀라 클렌징 워터','더 미니멈 선크림 SPF25 PA++ 40mL','그린티 밸런싱 로션 EX 160mL','제주 왕벚꽃 톤업 크림 50mL','순정 약산성 5.5 진정 토너','순정 약산성 6.5 휩 클렌저','미사 금설 유액 100ml','트루케어 논나노 논코메도 무기자차 선크림 SPF48 50mL','수퍼 오프 클렌징 오일 [블랙헤드 오프]']
        f = request.files['file']
        json_file = open("./model/model.json", "r")
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights("./model/model.h5")
        print("Loaded model from disk")
#        f.save(secure_filename(f.filename))
#        im = cv2.imread(f,mode='RGB')
#        json_file = open("./model/model.json", "r") 
#        loaded_model_json = json_file.read() 
#        json_file.close() 
#        loaded_model = model_from_json(loaded_model_json)
#        loaded_model.compile(loss="binary_crossentropy",optimizer="rmsprop",metrics=['accuracy'])
#        score= loaded_model.evaluate(X,Y,verbose=0)
#        print("%s : %.2f%%" % (loaded_model.metrics_names[1],score[1]*100))
        size=220,220
        new_img = Image.new("RGB", (220,220), "black")
        im = Image.open(f)
        im.thumbnail(size, Image.ANTIALIAS)
        load_img = im.load()
        load_newimg = new_img.load()
        i_offset = (220 - im.size[0]) / 2
        j_offset = (220 - im.size[1]) / 2
        for i in range(0, im.size[0]):
            for j in range(0, im.size[1]):
                load_newimg[i + i_offset,j + j_offset] = load_img[i,j]
        f=img_to_array(new_img)
        f=f.reshape(-1,f.shape[0],f.shape[1],f.shape[2])
        f/=255.
        pred=loaded_model.predict(f,verbose=2)
        pred_class=loaded_model.predict_classes(f,verbose=2)
        print(answerlist[int(pred_class)])
    return render_template('index2.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    return redirect('/choice')



# 디테일페이지
@app.route('/test/<id>', methods = ['POST', 'GET'])
def test(id):
    product_id = id

    conn = pymysql.connect(host="54.180.96.226", user="root", passwd="123123", db="KHUProject", charset="utf8")
    curs = conn.cursor()

    # 한글 뽑아내서 리스트화
    curs.execute("select product_ingredient from product where product_id = (%s)", (product_id))
    rows = [item[0] for item in curs.fetchall()]
    arr = rows[0].split(',')
    li = []
    # 각 리스트 변수별로 쿼리문 비교
    for i in range(len(arr)):
        temp = arr[i].strip()
        curs.execute(" select T.dictionary_name_ko, i.ingredient_scorenumber, i.ingredient_concerns_kr from ingredient i,  (SELECT dictionary_name_ko, dictionary_name_en from dictionary where dictionary_name_ko = (%s)) T where i.ingredient_name = T.dictionary_name_en ", (temp))
        rows = curs.fetchall()
        if rows:
            li.append(rows[0])

    # 평균 값
    avg = 0
    for i in li:
        if float(i[1]) >= 3.0:
            avg = 2
        if float(i[1]) >= 6.0:
            avg = 3
    # 위험순
    li_order = copy.deepcopy(li)
    li_order = sorted(li_order, key=lambda li_order: li_order[1])
    li_order.reverse()
    li_order = li_order[0:4]

    # 이름, 회사, 카테고리, 가격 추출
    curs.execute("select c.company_name, p.product_price, p.product_name, pd.productdesc_desc, p.product_company, pf.productfamily_name from product p, company c, productdesc pd, productfamily pf where p.product_company = c.company_id and p.product_name = pd.productdesc_name and pf.productfamily_id =p.product_productfamily and p.product_id = (%s)", (id))
    rows = curs.fetchall()[0]
    company = rows[0]
    price = rows[1]
    name = rows[2]
    desc = rows[3]
    company_id = rows[4]
    category = rows[5]

    pro_img_path = str(product_id)+".png"
    brand_img_path = company_id+".png"

    return render_template(
        'detail2.html',
        li = li,
        name = name,
        company = company,
        price = price,
        product_id = product_id,
        desc = desc,
        company_id = company_id,
        category = category,
        pro_img_path = pro_img_path,
        brand_img_path = brand_img_path,
        avg = avg,
        li_order = li_order
    )

# 인풋값을 위한 임시
@app.route('/input')
def input():
    return render_template('input.html')

    


# 상위 2개 화장품 선택
@app.route('/choice', methods = ['POST', 'GET'])
def choice():
    # name = request.form['name']
    name = "6세대 갈색병 리페어 에센스"
    conn = pymysql.connect(host="54.180.96.226", user="root", passwd="123123", db="KHUProject", charset="utf8")
    curs = conn.cursor()
    # 회사, 가격 추출
    curs.execute("select c.company_name, p.product_price, p.product_id from product p, company c where p.product_company = c.company_id and p.product_name = (%s)", (name))
    rows = curs.fetchall()[0]
    company = rows[0]
    price = rows[1]
    product_id = rows[2]

    pro_img_path = str(product_id)+".png"
   # pro_img_path = "12.png"
    return render_template('choice2.html',
                            name = name,
                            company = company,
                            price = price,
                            product_id = product_id,
                            pro_img_path = pro_img_path)
