# 🐭미퀴마우스ver2.0🖱️
<span style="color:red"> Calculus Quiz solving program</span> **미**분적분학 **퀴**즈를 대신 풀어주는 프로그램 (a.k.a  Micqui Mouse)  
#OCR #mathocr 
> ver2.0인 이유? ~~만들다가 하도 실패해서 리뉴얼 버전인 것처럼 작성~~


## 📋Table of content
* [연구의 필요성](#연구의-필요성)
* [설치 및 진행](#설치-및-진행)
* [전략 및 단계별 수행과정](#전략-및-단계별-수행과정)
* [아쉬운 부분](#아쉬운-부분)
* [추후 필요한 연구](#추후-필요한-연구)
* [Reference](#Reference)
* [License](#License)



|Task|Date|
|---|---|
|수식 이미지 받아와 latex 포맷의 텍스트로 변환하고 문제의 답을 도출하는 문제|2022.11.1~2022.12.11|

# 실행과정:  
step1의 '관심영역 수동 드래그 후 google colab pyocr변환코드 환경에 자동업로드 크롤링.py' 실행 ->(물론 크롤링과 업로드까지 성공적으로 수행하려면, chromedriver.exe를 비롯해 우회법을 따라야 함. 귀찮을 경우,
https://colab.research.google.com/drive/1FJFH7UWQjfSuCFTDeEsvnuXI1-P3kC3O#scrollTo=CBdcWZBtCYCZ  사이트로 접속, 드래그 해 저장된 crop이미지를 업로드. LaTeX 수식을 얻을 수 있음.) -> step3의 '계산 및 출력.py'를 실행. colab환경에 붙여넣을 수 있지만, 보기 좋도록 따로 분리함. 원할 경우 붙여넣을 수 있음.(물론 이 경우엔 Latex_equation을 순차적으로 받아오도록 변수설정을 해줘야 함.) 만약 필자처럼 vscode에서 바로 수행하는 경우, OCR에서 예시로 뽑아온 문제 4번의 LaTeX 수식이 풀린 후 문제지 화면에 출력되도록 설정해둠.(물론 실행할 때 지정글꼴 폴더도 함께 열어야 잘 출력됨.)

## 연구의 필요성

지난 1학기, 미분적분학 튜터로 활동. 본인이 생각해도 직접 계산해서 풀기에는 빡센 문제들을 출제함. 특별히 1학기 퀴즈 중 7차 미적 퀴즈는 평균 점수가 낮은 편에 속했음. 적분 연산 과정이지만, 계산하기 어려운 초월함수를 피적분함수로 설정했기 때문. 이러한 복잡한 연산이 들어가는 문제를 사진찍은 후 자동으로 풀게 해 정답을 확인할 수 있는 프로그램이 있으면 좋겠다고 생각. 튜터 입장에서도 문제를 출제하고 답을 재빠르게 확인하기 위한 용도로 사용 가능하고, 온라인으로 퀴즈를 보게 된 학생의 경우(코로나에 확진 된 학생은 온라인으로 응시했음.) 직접 문제를 풀지 않고 프로그램을 이용해 정답을 구한 뒤 마치 태블릿을 이용해 푼 것처럼 답을 필기체로 출력하는 방식으로 이용가능.~~개꿀~~   

기존의 '콴*', 'mathp**'등의 앱이 있지만, 필기체 형식으로 답안지에 출력하는 것까지는 지원하지 않음. 이 기회에 직접 프로그램을 구현해보고 싶어짐. 아울러 해당 연구의 목적은 프로그램 구동에 국한되지 않음. 본 연구를 통해 컴퓨터 상에서 문제를 캡처해 OCR 프로그램을 돌릴 때와 문제를 사진 찍은 후 생성된 png 파일로 OCR을 돌릴 때의 실행시간과 인식 정도의 차이를 비교분석할 것. 이 프로그램은 기본적으로 컴퓨터 상에서 문제를 캡처해 OCR 프로그램을 돌릴 것으로 전제하고 작성되었지만, 실제 상황에선 문제를 사진 찍은 후 png 파일로 OCR을 돌리는 경우도 있을테니 그 정확도를 비교해 보겠다는 것.  

## 설치 및 진행
* 소스 다운로드 
``` 
git clone https://github.com/seol731/-project-ver2.0.git
```

* 설치 파일
```
pip install -r requirement.txt (이건 vscode에서 작업하는 경우에 한함. 필자는 에러가 나서 colab과 jupyter notebook 환경에서 작업.)
```

requirement.txt 중, 아래 3개는 OCR을 이용해 수식 사진을 LaTeX 포맷의 text로 변환하기 위해 필요한 library 

| !pip install Pillow -U -qq

| !pip install pix2tex -qq

| !pip install opencv-python-headless==4.1.2.30 -U -qq



 

## 전략 및 단계별 수행과정

첫 Research는 ocr부터 시작. 한글로 작성된 문서와 엑셀로 작성된 문서를 ocr로 읽어 오는 프로그램 작성. 하지만 수식이 들어가는 순간 문자가 깨지면서 불러오기 실패. ~~처음부터 난관봉착..~~  


### 🪜step1
| 수식 인식 
#### Try1 <이미지 경계선 자동 추출>
다음으로 시도한 방법은 이미지의 경계선을 자동으로 추출해주는 코드를 작성. 이를 발전시켜 수식만 인식하려고 함. 처음엔 글자란 글자는 다 경계선으로 검출. 그래서 해당 코드를 발전시켜 수식이 있는 부분을 직사각형 처리하고, 해당 width와 height값 이상의 직사각형만 추출해 crop시켜 저장하도록 함. 문제는 이상한 네모 박스까지 긁어왔다는 것.('감독자 확인' 박스 같은..) 그리고 심지어 수식이 있는 직사각형 처리부는 완전히 crop되지 않고 중간이 짤리는 기현상 발생. 그래서 결국 수동으로 긁어오는 게 최선임을 깨닫게 됨.

아래는 처음에 글자란 글자는 다 경계선을 검출한 것을 보여줌. 
<p align="center"><img src="https://user-images.githubusercontent.com/83863024/206688422-4183037d-ce54-4a90-bddd-864235687712.gif" width="100%" /></p>  

아래는 직사각형 처리후 crop시키는 것을 보여줌. 
<p align="center"><img src="https://user-images.githubusercontent.com/83863024/206689787-35a1efa8-bf4c-4732-8d3c-f1167b256422.gif" width="100%" /></p>  

그러던 와중에 이 프로그램의 유용성을 발견. 일정 width와 height값이 넘는 사각형을 검출하도록 설정하면 평면도 상에서 안방, 거실, 화장실 등의 공간을 따로 따로 crop해 저장해 줌. crop된 사진들로, 동떨어진 방이어도 이어 붙여 보게 하는 프로그램으로 발전시킬 수 있을듯. 
<p align="center"><img src="https://user-images.githubusercontent.com/83863024/206691646-6ee9aacb-aec2-47f8-bb76-600d21a90c95.gif" width="100%" /></p>  


#### Try2 <직사각형 영역 수동 추출>
| 경계선 자동 추출 방식이 어려워 수동 추출 방식으로 방법을 바꿈. 원하는 영역만 점을 찍어 추출할 수 있게 함. 점은 총 4개만 찍으면 됨. 4번째 점이 찍히는 순간 첫번째 점과 4번째 점이 이어져 자동으로 사각형이 출력됨. 정말 말그대로 사용자가 마음대로 영역을 정의할 수 있기 때문에, 글자와 수식이 왜곡되기 쉬움. 이러한 사고를 막고자 이미지가 자동 보정되도록 함. 특히 문제를 사진 찍어 OCR을 돌릴 경우를 생각해, 이미지 원근법 변형이 가능토록 함. 아래 영상이 이를 잘 활용한 전형적인 예시. 책 사진은 기울어진 경우가 많기에 보정을 해줘야 함. 이 프로그램을 따라 원하는 부분만 수동으로 추출하면 잘 추출되는 것을 볼 수 있음.     
<p align="center"><img src="https://user-images.githubusercontent.com/83863024/206682380-9425773e-c14a-4222-ad46-20e85f9fa991.gif"  width="100%"></p> 

문제는 이 프로그램을 문제지에 그대로 적용하는 경우임. 그대로 적용하면 crop된 사진은 일그러지게 됨. 문제를 사진 찍어 사용하는 경우 효과를 볼 수 있겠으나, 컴퓨터에서 캡처할 경우 이 방식은 역효과를 냄. 
<p align="center"><img src="https://user-images.githubusercontent.com/83863024/206684381-8824bafd-4630-4a3e-95d6-034adbf5b7d0.gif"  width="100%"></p>  
 



#### Try3 <관심영역 수동 드래그> 
| 정말 단순한 경우만 생각하기로 함. 컴퓨터 상에서 캡처해 OCR을 돌릴 것으로 가정했고, 임의로 사각형을 출력하는 대신, 원하는 만큼만 드래그해서 crop되도록 함. 최종적으로 이 프로그램을 사용했으므로, 아래 pre step2의 크롤링 코드와 붙여 영상을 게재함. (영상 내용: 문제지 앞 장의 문제 4개를 드래그해 crop시키고 열린 창을 닫는다. 닫는 순간 문제지 뒷 장이 뜬다. 뒷 장에서도 마찬가지로 드래그해 crop시키고 열린창을 닫는다. crop된 사진들은 png파일로써 드라이브에 자동 저장된다.- jupyter환경을 이용한 게 이렇게 자동 저장이 간편하게 하기 위해서.- 앞서 열린 창이 닫힘과 동시에 저장된 파일들은 내가 원하는 홈페이지에 자동 업로드 시킨다.)



### 🪜pre step2 - 
| 관심영역 수동 드래그 후 자동 업로드 by 크롤링  - [Reference](#Reference)의[ROI 수동 추출]코드 참고
```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://colab.research.google.com/drive/1FJFH7UWQjfSuCFTDeEsvnuXI1-P3kC3O#scrollTo=CBdcWZBtCYCZ")
driver.find_element_by_css_selector("input[type='file']").send_keys(r"C:\Users\Admin\Desktop\quiz7-1.png" width="40%", height ="40%") 
``` 
<C:\Users\Admin\Desktop\quiz7-1.png>파일을 colab의 'LaTeX변환' 코드가 작성된 창에 자동 업로드 되도록 설정.
위에서 주어진 코드와 png파일은 예시일 뿐, 실제로는 드래그해서 얻은 cropped파일이 send_keys에 적히도록 작성, 사용자가 드래그해서 수동으로 추출한 png파일들이 colab환경에 자동 업로드. 아래 코드는 이에 대한 예시. 사용자가 드래그해서 수동으로 추출한 여러 png파일들을 convert 홈페이지에 자동 업로드하는 과정. 
```
#크롤링 예시 - in convertor 홈페이지.(아래 gif영상 참고.)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import glob 

driver = webdriver.Chrome()
driver.get("https://convertio.co/kr/image-converter/")
output = glob.glob('C:\\Users\\Admin\\3,4. 자동업로드\\quiz7_crop*.png')
for i in range(1,len(output)+1): 
    driver.find_element_by_css_selector("input[type='file']").send_keys(f"C:\\Users\\Admin\\3,4. 자동업로드\\quiz7_crop{i}.png")
```
#### 💡tips: 
* send_keys명령은 절대경로만 인식하므로, jupyter notebook 환경 driver 파일 위치를 찾은 후 import glob를 사용해 quiz7_crop*.png로 output설정, for문을 이용해 전부 업로드시킨다.
* chromedriver.exe를 설치한 뒤 이를 실행 프로그램과 같은 파일에 위치하도록 설정해줘야 함. 안하면 크롤링 안됨!! 

<p align="center"><img src="https://user-images.githubusercontent.com/83863024/206695627-a13e3556-812c-4925-bc79-a4ed8e2d86f8.gif" width="100%" ></p>  

참고로, 크롤링으로 colab창을 띄우면 로그인 화면이 나옴. 비정상적인 접속을 차단하려는 의도로 보이는데, 이를 해결하기 위한 우회법은 다음 사이트를 참고.
https://onsoim.tistory.com/entry/undetectedchromedriver


### 🪜step2
| 수식을 LaTeX로 변환 - 아래 [Reference](#Reference)의 [1. research_converting equation to LaTex by using **mathocr**]을 참고. 

앞서 말한 패키지가 설치되었다면 이 부분 colab환경에서 자동 수행되게 함. 코드 상에서 from pix2tex import cli as pix2tex로, pix2tex를 import시키고 나면 load_model = pix2tex.LatexOCR()로 지정가능하고, 설정한 LaTeX형식에 맞게 수식이 출력됨. 
주의!! : colab에서 처음 실행시킬 경우, 세션이 한 번 다운됨. install 시키고 난 후 다시 세션을 켜는 것. 그래서 만약 세션이 한 번 다운 되면 걱정할 필요 없이 다시 코드를 실행시키면 됨. 

#### 시행결과 

실행코드            |  실행화면 
:-------------------------:|:-------------------------:
![기본 처리 사진-3분소요](https://user-images.githubusercontent.com/83863024/206849027-45972c4f-9490-470a-9af4-49d04c77f205.png)  | ![흑백처리 사진 - 1분 소요](https://user-images.githubusercontent.com/83863024/206849057-83181415-3122-4f03-9d55-95f176629f15.png)  

가령, 2번 문제를 찍어 얻은 LaTeX 수식은 다음과 같다.  \int_{1}^{e^{2}}(\ln x)^{2}\d x 

(lnx)^(2)의 피적분 함수를 적분구간 1부터 e^(2)까지 적분. 
위의 실행화면에서 LaTeX 수식 그 자체와 함께 해당 수식을 markdown 형식으로 출력한 그림이 나오는데 이는 사용자 정의에 따라 LaTeX 수식만 나오도록 할 수 있음. 



연구의 필요성에서 밝혔듯, 컴퓨터 상에서 캡처한 경우와, 문제지를 사진찍어 OCR을 돌린 경우를 비교해 봄. 동일 문제에 대해 인식하는 시간과 정확도를 비교해 본 것. ex1)은 기본 캡처한 사진, ex2)는 흑백으로 반전 시킨 것만 다름. 단 한번만 OCR을 돌린 후 실행시간과 정확도를 비교하는 데에는 한계가 있으므로 100번 시행하고 실행시간과 정확도의 평균값을 구함. 그리고 100개의 표본을 점으로 나타내고자 scatter()함수 이용. 여기서 x축은 실행시간, y축은 Matching rate을 나타냄. 실행시간과 Matching rate사이의 상관관계를 조사함. 참고로 정확도는 이미 알고 있는 정답과(다른 인터넷 프로그램에 돌려 보고 나서 알고 있는 값)내 코드가 산출한 LaTeX수식이 얼마나 차이나는지를 ratio로 나타낸 값으로 정함. 이는 아래 코드를 통해 구현 가능.
```
from difflib import SequenceMatcher
def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()
```
(여기서 아쉬운 점은 픽셀 사이즈가 동일하도록 설정해야 했는데, 세심함이 부족했음.추가로 필자의 잘못인데, 정확도평균값을 'matching_rate average'라고 쓴다는 걸 average_runtime이라고 써버림. 사진에서 두번째 average_runtime은 정확도 평균임.)

ex1) 기본 캡처            |  ex2) 흑백반전 캡처
:-------------------------:|:-------------------------:
![기본 처리 사진-3분소요](https://user-images.githubusercontent.com/83863024/206823159-7cb8b69b-95b9-4869-a145-cea1191b0ee1.png)  | ![흑백처리 사진 - 1분 소요](https://user-images.githubusercontent.com/83863024/206823160-ff9eb107-3d43-4f81-b304-60281380e72a.png)  





결과: 
ex1) 기본 캡처            |  ex2) 흑백반전 캡처
:-------------------------:|:-------------------------:
![기본 처리 사진-3분소요](https://user-images.githubusercontent.com/83863024/206862219-4796d4d6-bf8a-45bf-8a55-fc215c93f59e.png)  | ![흑백처리 사진 - 1분 소요](https://user-images.githubusercontent.com/83863024/206862104-f5c4457d-8b38-4848-9303-de6bf733c750.png)



사실 1과 2의 비교는 그렇게 유의미하지 않음. 실행시간의 평균 차이가 소수점 아래 세번째 자리에서부터 발생. 유효숫자로 보기엔 그 값이 너무 작음. 소소한 차이나 소숫점 아래 네번째 자리에서 반올림 한경우, 1.205 > 1.202(s)로 2가 평균적으로 더 빨리 수행됨. 흑백 반전을 한 경우에 OCR이 더 잘 돌아간다는 것. 한편 1은 정확도가 약 0.97, 2는 정확도가 1.0임. 흑백으로 반전해 캡처한 경우, 반전하지 않은 경우에 생길 수 있는 일말의 오류마저 잡아낸다는 뜻임. 1과 2 모두 2초를 넘어가는 경우가 없으며 한 부분에 집중적으로 몰려 있는 것으로 확인됨. 정규분포를 따를 것. 또한, 정확도에서 큰 문제를 일으키지 않았기에, 시간과 정확도 사이의 상관관계를 해석하는 데는 무리가 있음. 3과 4의 결과를 확인해봐야 해석할 수 있을 듯. 



ex1) 은 ex1)을 기본 촬영한 사진, ex4)는 ex2)를 촬영한 사진. 위에서 설명한 것과 다를 바 없음.

ex3) 기본 촬영사진            |  ex4) 흑백반전 촬영사진
:-------------------------:|:-------------------------:
![기본 처리 사진-3분소요](https://user-images.githubusercontent.com/83863024/206823400-3834ec39-5f4b-4263-ba72-43cef0a76dbd.jpg)  | ![흑백처리 사진 - 1분 소요](https://user-images.githubusercontent.com/83863024/206823395-fe3d36c8-bd4b-4fbd-82f1-4155ddae4abf.jpg)


결과: 
ex3) 기본 촬영사진            |  ex4) 흑백반전 촬영사진
:-------------------------:|:-------------------------:
![기본 처리 사진-3분소요](https://user-images.githubusercontent.com/83863024/206861203-dab18d8e-bc14-467a-ba85-9a11fe75dd5a.png)  | ![흑백처리 사진 - 1분 소요](https://user-images.githubusercontent.com/83863024/206861918-7e17fc34-cb86-4323-a363-40461e222487.png)


3은 1의 시간에 비해 약 5배 증가함. 4는 2의 시간에 비해 3배가량 증가함. 확실히 흑백반전 촬영을 한 경우 시간은 덜 증가함. 소숫점 아래 두번째 자리에서 반올림 한 경우, 3은 5.9, 4는 3.2s가 소요. 놀라운 점은 정확도. 1과 2에 비해 정확도가 급격하게 떨어짐. 소숫점 아래 세번째 자리에서 반올림 했을 때, 3은 0.14, 4는 0.35. 확실히 3에 비해 4의 정확도는 2배 이상 뛰어남. 
정확도가 현저히 떨어졌기에, 1과 2에서 하지 못한 상관관계 분석이 가능함. 3에서 시간과 정확도는 반비례하는 추세를 보임. 판독 시간이 늘어나는 표본은 잘못 인식한 경우일 확률이 높다는 것. 이에 반해 4는 그 추세가 눈에 띄게 감소함. 점의 분포가 우상향되어 있음.이는 소요시간이 오래 걸린다하더라도, 출력한 수식은 최대한 정답에 가깝게 출력한다는 뜻. 
변인통제하지 못한 부분이 있기에 속단할 수 있는 해석은 아니지만, 흑백반전을 해야 성능이 좋아진다는 사실은 명백해 보임. 그리고 ~~미적분 점수 말아먹기 싫으면~~ 사진으로 찍어서 프로그램 쓰지 말고 컴퓨터에서 캡처해 프로그램 돌릴 것. 



### 🪜step3 
| 계산 

~~이 부분 코드 짜다가 죽을 뻔.~~ step3부터 마무리까지 꼬박 이틀밤 샐 분량 나옴.(48시간?) 사실 완벽히 구현했다고 할 수 없음. 일부 복잡한 수식에 대해서는 아직 제대로 판독하지 못함. LaTeX특성상 어쩔 수 없음. 경우의 수가 너무 많음. LaTeX 문법을 보면 특수 문자 앞에는 전부 \ (backslash)가 들어가고, 경우에 따라 상수값을 {}로 처리해주기도, 안해주기도 함. 경우의 수가 너무 많았음. 심지어 \frac 에서 \f는 form feed로 인식해버려 이상하게 출력됐음. 어째든 이 부분 코드의 핵심은 정규표현식.
```
pattern2 = r"\}\\[a-z0-9]+"                            # 정규표현식 이용해 피적분함수값 추적.(무조건 수행됨.)
    matchedList2 = re.findall(pattern2,m)
    if matchedList2:
        intergrand = (str(matchedList2[0])[2:])
        bar = getattr(sympy, intergrand)
        function = bar(x) 
```
이 부분만 따로 떼어서 보면, Latex_equation = '\int_{0}^{\frac{\pi}{2}}}\sin^{2}x d x'라고 OCR 돌린 결과가 나왔을 때, 찾는 pattern2는 }\이 나온 후의 값임. 이 문제의 경우 sin값이어서 intergrand에는 sin이 들어감. 주의해야 할 건, \따로 쓰면 안되기에 \\형식으로 사용해야 하며, 특수 문자 앞에 항상 \를 붙여줘야 함. [a-z0-9]+s는 sin값을 찾도록 지정해줌. 하지만 여기서 끝나지 않는 건, 피적분함수가 sin이 아니라 sin^(2)x 임. 이를 또 경우 나눠 정규표현식으로 찾게 함.  

### 🪜step4 
| 출력 - 

github 코드 파일에 step4가 없는 이유는 step3코드와 함께 작성되었기 때문. 계산 후, 정답이(손글씨로) 문제지 화면에 바로 출력됨.

계산 된 값들은 answer list에 차례로 저장된 후(문제 수가 통상 7-8개로 주어지기 때문에 len(answer)값은 8을 넘지 않음.) '정답입력받기.txt' 파일에 자동 write()됨. (현재는 빈 상태) 그 후 문제 순서대로 지정된 문제지 좌표값 (xcord, ycord) 위치에 준비된 글꼴 사진을 붙여넣음.(pasting(xcord,ycord)) 문제지는 앞면, 뒷면이 있으므로 앞면과 뒷면 결과를 순서대로 show(). 

#### 💡tips: 
syntax Error:   "(unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape"  
solution:      가령, path = 'C:\Users\Downloads\broker.png'에서 '\'를 '/'로 변경, 또는 '\'대신 '\\'이용.


아래 사진은 3D그림판 환경에서 아스키코드에 맞는 문자를 필기체 형식으로 적고 파일로 저장하는 과정을 나타낸 것. 전부 필자가 입력하진 않았고, 아래 [Reference](#Reference)의 [step4 text2handwritng]코드와 파일을 참고했으며, 약 10여개의 특수문자를 추가했다.  
<p align="center"><img src="https://user-images.githubusercontent.com/83863024/204967023-70a5aa78-b40f-474b-9f76-e62a7f455c6f.png" width="100%" /></p>  



<p align="center"><img src="https://user-images.githubusercontent.com/83863024/206849502-2cf94b83-b4c0-495a-91d2-b12ac28112f3.png" width="100%" /></p>




### 최종 시행결과
<p align="center"><img src="https://user-images.githubusercontent.com/83863024/206853425-a14af98b-7587-4876-839b-430d1fed878d.gif" width="100%" /></p>



~~됐다! 드디어 미적분 교수님을 감쪽같이 속일 수 있게 됐다.~~ 사실 못 속인다. 출력은 서술형이 아니니까.. 그리고 정답 중에 sqrt(2) 같은 경우, 루트에 대한 아스키코드 값이 없어 sqrt와 같은 형식으로만 출력된다. (이 부분은 유니코드를 써서 해결할 수 있는데, 그렇게까지 할 시간이 없었다.) 그냥 정답 확인하는 용도로만...





## 아쉬운 부분
* step1 
   * 자동으로 한글과 수식을 분리해주는 기능을 넣지 못함. 아직은 수동으로 수식을 한글과 분리해야 함. ocr로 한글 텍스트 파일을 불러오는 데는 성공했으나, 수식만 따로 분리하는 데는 실패. 

* step2 
   * ocr(pix2tex.LatexOCR()이용)상 한계 존재. 사진이 흔들렸을 경우, 정확도는 급격하게 떨어짐. 아울러 사진에서 흑백을 반전하면, 수식을 인식하는 데 걸리는 시간이 줄어듬(자동으로 흑백을 반전하도록 개선할 필요 있음). (ex)작고 선명하지 않은 0값을 Θ로 인식함.)
   
* step3 
   * 수식 이미지 분리와 OCR Research에 많은 시간을 할애하는 바람에 다양한 문제에 풀이 알고리즘을 적용하지 못함. 특히 적분에 한정된 문제 풀이였음. 
* step4 
   * 특정 문제가 너무 길어져 한 면을 할애할 경우, 출력 위치를 설정하는데 어려움이 생김. 지금은 한 면에 4문제만 있어서 문제가 없지만, 가령 한 면에 2문제만 들어가면 출력 위치를 따로 설정해줘야 함.  


## 추후 필요한 연구
* 추후 편미분, 미분방정식, 선형대수 문제 풀이까지 확장해야 함, 선명하지 않은 사진에 대해서도 좋은 성능을 유지하도록 코드 수정 필요. 


## 📖 Reference
* [research_Korean_file(png)_reader: by using pyocr](https://www.zinnunkebi.com/python-tesseract-pyocr-kor-textbuilder/)
    * [sub reserch_digital_file(png)_reader: by using pyocr](https://www.zinnunkebi.com/python-tesseract-pyocr-digit/)
* [1. research_converting equation to LaTex by using **mathocr**](https://github.com/lukas-blecher/LaTeX-OCR)
* [2. research_converting equation to LaTex by using **mathocr**](https://github.com/harvardnlp/im2markup)
* [3. research_converting equation to LaTex by using **mathpixocr_wrapper** ](https://github.com/minyez/mathpixocr_wrapper)
* [4. research_MathOCR](https://github.com/AIRLegend/MathOCR)
* [step4 text2handwritng](https://itnext.io/convert-text-into-your-handwriting-91a1ed9aefd0)
* [ROI 수동 추출](https://inhovation97.tistory.com/57)


## :mortar_board: License 
This is licensed under the MIT License


