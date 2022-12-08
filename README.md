# 🐭미퀴마우스ver2.0🖱️
<span style="color:red"> Calculus Quiz solving program</span> **미**분적분학 **퀴**즈 풀어주는 프로그램 (a.k.a  Micqui Mouse)  
#OCR #mathocr  


## 📋Table of content
* [연구의 필요성](#연구의-필요성)
* [설치 및 진행](#설치-및-진행)
* [전략 및 단계별 수행과정[핵심]](#전략-및-단계별-수행과정[핵심])
* [아쉬운 부분](#아쉬운-부분)
* [추후 필요한 연구](#추후-필요한-연구)
* [Reference](#Reference)
* [License](#License)



|Task|Date|
|---|---|
|수식 이미지 받아와 latex 포맷의 텍스트로 변환하고 문제의 답을 도출하는 문제|2022.11.1~2022.12.11|


## 연구의 필요성
 

## 설치 및 진행
* 소스 다운로드 
> git clone https://github.com/seol731/-project-ver2.0.git

* 설치 파일
> pip install -r requirement.txt (이건 vscode에서 작업하는 경우에 한함. 필자는 에러가 나서 colab과 jupyter notebook 환경에서 작업.)

requirement.txt 중, 아래 3개는 OCR을 이용해 수식 사진을 LaTeX 포맷의 text로 변환하기 위해 필요한 library 
!pip install Pillow -U -qq
!pip install pix2tex -qq
!pip install opencv-python-headless==4.1.2.30 -U -qq



## 전략 및 단계별 수행과정[핵심]

### 🪜step1
| 수식
### 🪜step2
| 수식을 LaTeX로 변환 - 아래 reference의 1. research_converting equation to LaTex by using **mathocr**을 참고. 
### 🪜step3 
| 계산 
### 🪜step4 
| 출력
#### 💡tips: 
syntax Error:   "(unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape"  
solution:      가령, path = 'C:\Users\Downloads\broker.png'에서 '\'를 '/'로 변경, 또는 '\'대신 '\\'이용.

<p align="center"><img src="https://user-images.githubusercontent.com/83863024/204967023-70a5aa78-b40f-474b-9f76-e62a7f455c6f.png" width="400" height="300"/></p>



## 아쉬운 부분
* step1 
   * 자동으로 한글과 수식을 분리해주는 기능을 넣지 못함. 아직은 수동으로 수식을 한글과 분리해야 함. ocr로 한글 텍스트 파일을 불러오는 데는 성공했으나, 수식만 따로 분리하는 데는 실패. 

* step2 
   * ocr(pix2tex.LatexOCR()이용)상 한계 존재. 사진이 흔들렸거나 흑백을 반전한 경우, 수식을 인식하는 데 걸리는 시간이 늘어남. (ex)작고 선명하지 않은 0값을 Θ로 인식함.)
   * 
* step3 
   * 수식 이미지 분리와 OCR Research에 많은 시간을 할애하는 바람에 다양한 문제에 풀이 알고리즘을 적용하지 못함. 특히 적분에 한정된 문제 풀이였음. 
* step4 
   * 특정 문제가 너무 길어져 한 면을 할애할 경우, 출력 위치를 설정하는데 어려움이 생김. 지금은 한 면에 4문제만 있어서 문제가 없지만, 가령 한 면에 2문제만 들어가면 출력 위치를 따로 설정해줘야 함.  

## 추후 필요한 연구
* 추후 편미분, 미분방정식, 선형대수 문제 풀이까지 확장해야 함, 최악의 OCR 성능 향상


## Reference
* [research_Korean_file(png)_reader: by using pyocr](https://www.zinnunkebi.com/python-tesseract-pyocr-kor-textbuilder/)
    * [sub reserch_digital_file(png)_reader: by using pyocr](https://www.zinnunkebi.com/python-tesseract-pyocr-digit/)
* [1. research_converting equation to LaTex by using **mathocr**](https://github.com/lukas-blecher/LaTeX-OCR)
* [2. research_converting equation to LaTex by using **mathocr**](https://github.com/harvardnlp/im2markup)
* [3. research_converting equation to LaTex by using **mathpixocr_wrapper** ](https://github.com/minyez/mathpixocr_wrapper)
* [4. research_MathOCR](https://github.com/AIRLegend/MathOCR)



## :mortar_board: License 
This is licensed under the MIT License


