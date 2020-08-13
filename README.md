# Hwabun

## Hwabun 소개

![슬라이드1](https://user-images.githubusercontent.com/35910177/83611141-86f6a580-a5bb-11ea-88bc-f4664efc7ad7.PNG)



한국데이터산업진흥원에서 주관한 청년인재 프로젝트중 제가 진행했던 프로젝트인 Hwabun(이하 화분)입니다.

화분은 웹사이트이며, 웹사이트의 기능으로는 화장품 사진을 업로드하면 해당 상품이 어떤 상품인지를 알기 위해 머신러닝 기법중 하나인 CNN을 통하여 상품을 인식한 후, 해당 상품의 상세정보들을 알려주는 사이트입니다.



## 프로젝트 정보

- 프로젝트 기간 : 2019.8.16 ~ 8.30

- 프로젝트 인원 : 7명

- 프로젝트 기술요소(아키텍쳐)

![슬라이드12](https://user-images.githubusercontent.com/35910177/83612621-9aa30b80-a5bd-11ea-908f-732774603b97.PNG)


1. 사용자가 핸드폰으로 카메라로 사진을 촬영한 후, 안드로이드 앱을 통해서 사진업로드

2. CNN을 통하여 해당 사진이 어떤 상품인지 이미지 분석을 진행한 후, 제품을 찾아내면 DB를 통하여 해당 제품의 정보 등 화면 표시 기능



![슬라이드13](https://user-images.githubusercontent.com/35910177/83612644-a55da080-a5bd-11ea-84ea-2b86a6f1707b.PNG)

실제로 구현한 기술 목록

- Web : Flask

- Deep Learning : Keras, AWS SageMaker
(AWS SageMaker를 통하여 해당 서비스에 필요한 모델을 생성하였습니다.)

- DB : MySQL

- Data : BeautifulSoup, Selenium, Metplotlib, OpenCV, Pandas, Numpy 


## 프로젝트 PPT

[여기에 다 있습니다.](https://github.com/includesorrow/Hwabun/files/4721964/python.6.MSG.pptx)


## 프로젝트 중 직접구현한 내용

### 1. 크롤링

![슬라이드21](https://user-images.githubusercontent.com/35910177/83615697-df30a600-a5c1-11ea-8d9b-1c60b2e8b65b.PNG)

- 데이터를 확보하기 위해 인스타그램 크롤링 작업 및 Google 이미지 크롤링 작업을 진행하였습니다.

### 2. 전처리 작업

![슬라이드23](https://user-images.githubusercontent.com/35910177/83615774-f66f9380-a5c1-11ea-927d-6e00ad7a148a.PNG)

- OpenCV를 이용하여 크롤링한 이미지의 얼굴이 존재하는지에 대한 작업을 진행하였습니다.

- 얼굴이 나오는 사진이 있으면 해당 이미지를 전처리를 하기 위해 활용하였습니다.

![슬라이드29](https://user-images.githubusercontent.com/35910177/83616483-dd1b1700-a5c2-11ea-9ab7-a56b372d9732.PNG)

- 데이터의 수가 매우 부족하여 Crop, Rotation을 통해 이미지를 늘리는 작업을 진행하였습니다.

### 3. 화장품 데이터 DB작업

![슬라이드14](https://user-images.githubusercontent.com/35910177/83616274-94635e00-a5c2-11ea-984e-853e76604188.PNG)

- 화장품들의 데이터들을 DB화 작업을 하여 웹사이트에서 쉽게 데이터를 추출할 수 있게 작업하였습니다.

### 4. CNN 모델링 작업

![슬라이드30](https://user-images.githubusercontent.com/35910177/83616551-f4f29b00-a5c2-11ea-802f-d260efe0f106.PNG)

![슬라이드32](https://user-images.githubusercontent.com/35910177/83616681-194e7780-a5c3-11ea-8850-a6e09cb398f7.PNG)

- 업로드된 화장품 사진을 인식하기 위해 CNN모델을 생성 및 튜닝하는 작업을 진행하였습니다.

### 5. 웹페이지 작업

- 웹페이지에 CNN을 통한 모델링 작업을 한 결과물을 서버에 적용시켜, 사진을 업로드 하였을 때 화장품들의 연관성을 %로 수치화하여 View화 하였습니다.


## 프로젝트 결과

### 웹페이지 구현

![슬라이드35](https://user-images.githubusercontent.com/35910177/83616930-5dda1300-a5c3-11ea-8ffa-8f07694d09ed.PNG)

- 웹페이지에 해당 상품을 업로드하면, 화장품의 유사도에 따라 2가지의 추천목록을 보여주어 유저가 선택할 수 있게 하였습니다.

![슬라이드36](https://user-images.githubusercontent.com/35910177/83617011-764a2d80-a5c3-11ea-8857-779e7c991aa4.PNG)

- 해당 상품을 클릭하면 기본적인 화장품의 정보가 나옵니다.

- 전체 성분을 클릭하면 해당 상품의 DB를 불러와 웹페이지에 보여주도록 페이지를 구현하였습니다.

### 모델링

![슬라이드30](https://user-images.githubusercontent.com/35910177/83617213-bc9f8c80-a5c3-11ea-9736-76ca03530e21.PNG)

![슬라이드31](https://user-images.githubusercontent.com/35910177/83617216-bc9f8c80-a5c3-11ea-99ed-e22ef717bc79.PNG)

- Flip + Rotation을 진행한 모델 및 Flip + Crop을 진행한 모델 2개를 가지고 진행

- 또한 Convolution과 Fully Connected Layer를 조정하면서 Average Accuracy를 높이기 위해 진행하였고, 결국 Flip + Crop 설정 및 6 Conv, 5fc가 가장 높은 정확도가 나옴

- 해당 모델의 과적합 여부를 확인하기 위해 그래프를 표시하는 작업을 진행하였고 Val의 그래프를 통해 과적합이 아닌걸 판단해서 진행하였음.

![슬라이드32](https://user-images.githubusercontent.com/35910177/83617209-bb6e5f80-a5c3-11ea-8bf6-283da845b6c0.PNG)

- 하지만 여기서 정확도를 더 높이기 위해 추가 작업을 진행하였음

- VGG-16을 통해 정확도를 더 높일 수 있다고 판단하여 진행하였고, 기존보다 높은 정확도인 0.979의 정확도가 나타남.


