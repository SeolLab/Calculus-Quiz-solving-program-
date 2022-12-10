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


## 연구의 필요성

첫 research는 ocr부터 시작. 한글로 작성된 문서와 엑셀로 작성된 문서를 ocr로 읽어 오는 프로그램 작성. 하지만 수식이 들어가는 순간 문자가 깨지면서 불러오기 실패. ~~처음부터 난관봉착..~~

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

### 🪜step1
| 수식 인식 
#### Try1 <이미지 경계선 자동 추출>


<p align="center"><img src="https://user-images.githubusercontent.com/83863024/206688422-4183037d-ce54-4a90-bddd-864235687712.gif" width="80%" /></p>  

<p align="center"><img src="https://user-images.githubusercontent.com/83863024/206691646-6ee9aacb-aec2-47f8-bb76-600d21a90c95.gif" width="80%" /></p>  

<p align="center"><img src="https://user-images.githubusercontent.com/83863024/206689787-35a1efa8-bf4c-4732-8d3c-f1167b256422.gif" width="80%" /></p>  

#### Try2 <직사각형 영역 수동 추출>
| 경계선 자동 추출 방식이 어려워 수동 추출 방식으로 방법을 바꿈. 원하는 영역을 내가 원하는 형태의  



<p align="center"><img src="https://user-images.githubusercontent.com/83863024/206684381-8824bafd-4630-4a3e-95d6-034adbf5b7d0.gif"  width="80%"></p>  
<p align="center"><img src="https://user-images.githubusercontent.com/83863024/206682380-9425773e-c14a-4222-ad46-20e85f9fa991.gif"  width="80%"></p>  



#### Try3 <관심영역 수동 드래그>


### 🪜pre step2 - 
| 관심영역 수동 드래그 후 자동 업로드 by 크롤링  
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
send_keys명령은 절대경로만 인식하므로, jupyter notebook 환경 driver 파일 위치를 찾은 후 import glob를 사용해 quiz7_crop*.png로 output설정, for문을 이용해 전부 업로드시킨다.

<p align="center"><img src="https://user-images.githubusercontent.com/83863024/206695627-a13e3556-812c-4925-bc79-a4ed8e2d86f8.gif" width="80%" ></p>  


### 🪜step2
| 수식을 LaTeX로 변환 - 아래 [Reference](#Reference)의 [1. research_converting equation to LaTex by using **mathocr**]을 참고. 








#### 시행결과 

실행코드            |  실행화면 
:-------------------------:|:-------------------------:
![기본 처리 사진-3분소요](https://user-images.githubusercontent.com/83863024/206849027-45972c4f-9490-470a-9af4-49d04c77f205.png)  | ![흑백처리 사진 - 1분 소요](https://user-images.githubusercontent.com/83863024/206849057-83181415-3122-4f03-9d55-95f176629f15.png)  

가령, 2번 문제를 찍어 얻은 LaTeX 수식은 다음과 같다.  \int_{1}^{e^{2}}(\ln x)^{2}\d x 

(lnx)^(2)의 피적분 함수를 적분구간 1부터 e^(2)까지 적분. 
위의 실행화면에서 LaTeX 수식 그 자체와 함께 해당 수식을 markdown 형식으로 출력한 그림이 나오는데 이는 사용자 정의에 따라 LaTeX 수식만 나오도록 할 수 있음. 





ex1) 기본 캡처            |  ex2) 흑백반전 캡처
:-------------------------:|:-------------------------:
![기본 처리 사진-3분소요](https://user-images.githubusercontent.com/83863024/206823159-7cb8b69b-95b9-4869-a145-cea1191b0ee1.png)  | ![흑백처리 사진 - 1분 소요](https://user-images.githubusercontent.com/83863024/206823160-ff9eb107-3d43-4f81-b304-60281380e72a.png)  




ex3) 기본 촬영사진            |  ex4) 흑백반전 촬영사진
:-------------------------:|:-------------------------:
![기본 처리 사진-3분소요](https://user-images.githubusercontent.com/83863024/206823400-3834ec39-5f4b-4263-ba72-43cef0a76dbd.jpg)  | ![흑백처리 사진 - 1분 소요](https://user-images.githubusercontent.com/83863024/206823395-fe3d36c8-bd4b-4fbd-82f1-4155ddae4abf.jpg)






### 🪜step3 
| 계산 


### 🪜step4 
| 출력 - 

github 코드 파일에 step4가 없는 이유는 step3코드와 함께 작성되었기 때문. 계산 후, 정답이(손글씨로) 문제지 화면에 바로 출력됨.

계산 된 값들은 answer list에 차례로 저장된 후(문제 수가 통상 7-8개로 주어지기 때문에 len(answer)값은 8을 넘지 않음.) '정답입력받기.txt' 파일에 자동 write()됨. (현재는 빈 상태) 그 후 문제 순서대로 지정된 문제지 좌표값 (xcord, ycord) 위치에 준비된 글꼴 사진을 붙여넣음.(pasting(xcord,ycord)) 문제지는 앞면, 뒷면이 있으므로 앞면과 뒷면 결과를 순서대로 show(). 

#### 💡tips: 
syntax Error:   "(unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape"  
solution:      가령, path = 'C:\Users\Downloads\broker.png'에서 '\'를 '/'로 변경, 또는 '\'대신 '\\'이용.


아래 사진은 3D그림판 환경에서 아스키코드에 맞는 문자를 필기체 형식으로 적고 파일로 저장하는 과정을 나타낸 것. 전부 필자가 입력하진 않았고, 아래 [Reference](#Reference)의 [step4 text2handwritng]코드와 파일을 참고했으며, 약 10여개의 특수문자를 추가했다.  
<p align="center"><img src="https://user-images.githubusercontent.com/83863024/204967023-70a5aa78-b40f-474b-9f76-e62a7f455c6f.png" width="80%" /></p>  



<p align="center"><img src="https://user-images.githubusercontent.com/83863024/206849502-2cf94b83-b4c0-495a-91d2-b12ac28112f3.png" width="80%" /></p>




### 최종 시행결과
<p align="center"><img src="https://user-images.githubusercontent.com/83863024/206853425-a14af98b-7587-4876-839b-430d1fed878d.gif" width="80%" /></p>



~~됐다! 드디어 미적분 교수님을 감쪽같이 속일 수 있게 됐다.~~ 사실 못 속인다. 출력은 서술형이 아니니까.. 그냥 정답 확인하는 용도로만...





## 아쉬운 부분
* step1 
   * 자동으로 한글과 수식을 분리해주는 기능을 넣지 못함. 아직은 수동으로 수식을 한글과 분리해야 함. ocr로 한글 텍스트 파일을 불러오는 데는 성공했으나, 수식만 따로 분리하는 데는 실패. 

* step2 
   * ocr(pix2tex.LatexOCR()이용)상 한계 존재. 사진이 흔들렸거나 흑백을 반전한 경우, 수식을 인식하는 데 걸리는 시간이 늘어남. (ex)작고 선명하지 않은 0값을 Θ로 인식함.)
   
* step3 
   * 수식 이미지 분리와 OCR Research에 많은 시간을 할애하는 바람에 다양한 문제에 풀이 알고리즘을 적용하지 못함. 특히 적분에 한정된 문제 풀이였음. 
* step4 
   * 특정 문제가 너무 길어져 한 면을 할애할 경우, 출력 위치를 설정하는데 어려움이 생김. 지금은 한 면에 4문제만 있어서 문제가 없지만, 가령 한 면에 2문제만 들어가면 출력 위치를 따로 설정해줘야 함.  


## 추후 필요한 연구
* 추후 편미분, 미분방정식, 선형대수 문제 풀이까지 확장해야 함, 선명하지 않은 사진에 대해서도 좋은 성능을 유지하도록 코드 수정 필요. 


## Reference
* [research_Korean_file(png)_reader: by using pyocr](https://www.zinnunkebi.com/python-tesseract-pyocr-kor-textbuilder/)
    * [sub reserch_digital_file(png)_reader: by using pyocr](https://www.zinnunkebi.com/python-tesseract-pyocr-digit/)
* [1. research_converting equation to LaTex by using **mathocr**](https://github.com/lukas-blecher/LaTeX-OCR)
* [2. research_converting equation to LaTex by using **mathocr**](https://github.com/harvardnlp/im2markup)
* [3. research_converting equation to LaTex by using **mathpixocr_wrapper** ](https://github.com/minyez/mathpixocr_wrapper)
* [4. research_MathOCR](https://github.com/AIRLegend/MathOCR)
* [step4 text2handwritng](https://itnext.io/convert-text-into-your-handwriting-91a1ed9aefd0)



## :mortar_board: License 
This is licensed under the MIT License


