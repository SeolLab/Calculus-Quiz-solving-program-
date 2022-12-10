#LaTeX pix2tex
%reload_ext autoreload
%autoreload 2
# %autoreload 지금 모든 모듈을 자동으로 다시 로드.
# %autoreload 0 -> 자동 다시 로드를 비활성화. 
# %autoreload 1 -> 입력한 Python 코드를 실행하기 전에 매번 가져온 모든 모듈을 다시 로드.
# %autoreload 2 -> 입력된 Python 코드를 실행하기 전에 매번 모든 모듈( 로 제외된 모듈 제외)을 다시 로드.

import PIL
!pip install Pillow -U -qq
if int(PIL.__version__[0]) < 9:
    import os
    os.kill(os.getpid(), 9)

!pip install pix2tex -qq
!pip install opencv-python-headless==4.1.2.30 -U -qq

def upload_files():
  from google.colab import files
  from io import BytesIO
  uploaded = files.upload()
  return [(n, BytesIO(b)) for n, b in uploaded.items()]       

from pix2tex import cli as pix2tex
from PIL import Image
from IPython.display import HTML, Math
load_model = pix2tex.LatexOCR()                                     # loading load_model 
table = r'\begin{array} {} %s \end{array}'



import time 
import numpy as np
# import scipy.stats as stats 
import matplotlib.pyplot as plt
from difflib import SequenceMatcher

a = '\int_{1}^{e^{2}}(\ln x)^{2}\,d x'

def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()


arr = []                                                            # 실행시간 저장할 arr생성 
arr2 = [] 
files = upload_files()                                              # file 업로드(업로드 파일 이용)
for i in range(100):                                                # 100번 실행시간 측정 
  start = time.time()                                               # 실행시간 측정시작
  predictions = []                                                                          
  for n, f in files:
      png_file = Image.open(f)                                       
      Latex_equation = load_model(png_file)                          # png_file을 받아서 pix2tex.LatexOCR()에 넣고 ocr 수행 
      predictions.append('\\displaystyle{%s}'%(Latex_equation))  
      print(Latex_equation)                                          # Latex_equation Latex포맷으로 출력 
      b = Latex_equation
  Math(table%'\\\\'.join(predictions))  
  
 # 시간 및 Matching rate 측정
  runtime = time.time() - start                                      # 실행시간 측정완료
  arr.append(runtime)                
  
  sim = similar(a,b)                                                # Matching rate 
  arr2.append(sim)                                                    
  
  print("time :",runtime)                                            # 실행시간 출력 
average = np.mean(arr)                                            # 실행시간 평균치
print(f"average_runtime : {average}")                                # 실행시간 평균치 출력 

average2 = np.mean(arr2)                                            # Matching rate 평균치
print(f"average_runtime : {average2}")                                # # Matching rate 평균치 출력 


x = arr 
y = arr2
plt.scatter(x, y)
plt.xlabel("Time")
plt.ylabel("Matching Rate")
plt.show()
