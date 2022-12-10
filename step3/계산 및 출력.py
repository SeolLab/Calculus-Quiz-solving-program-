# 계산 위한 import 
import sympy
import re
import sympy as sym
from sympy import Integral, Symbol
import numpy as np 

# 출력 위한 import
from PIL import Image
from sys import argv
import sys
import glob 


Latex_equation = '\int_{0}^{\frac{\pi}{2}}}\sin^{2}x d x'  #예시 값. 
#참고.(변환된 값)
# Latex_equation =
# '''
# '\int_{1}^{e^{2}}{\frac{\ln x}{x^{2}}}d x'   # 1번 문제 
# '\int_{1}^{e^{2}}\ln^{2}x d x' #2번 문제
# '\int_{0}^{\frac{\pi}{3}}}\sin x \ln (\cos x) d x'   #3번 문제 
# '\int_{0}^{\frac{\pi}{2}}}\sin^{2}x d x'     # 4번문제
# '\int_{0}^{\frac{\pi}{4}}\sec^{3}x d x'   #5번 문제
# '\int_{0}^{1}\frac{x}{\sqrt{3-2x-x^{2}}}\ d x' # 6번 문제
# '{\frac{x^{2}}{a^{2}}}+{\frac{y^{2}}{b^{2}}}=1'   #7번 문제
# '''


# '\int_1^{e^2}(\ln x)^2 d x'
m = Latex_equation.replace('\f' ,'\\\\f')
# print(m)
if 'int' in m:         #단일 적분
    x = sym.Symbol(m[-1])      
    low_idx = m.find('_')+2                # 히위 적분구간 index 
    lst = m.split('\\')
    # print(lst)
    
    pattern0 = r"\{\\\\frac\{[a-z0-9\\]+\}\{[a-z0-9]+\}"                            # 정규표현식 이용해 pi값 추적. 
    matchedList0 = re.findall(pattern0,m)
    if matchedList0:
        # print(matchedList0)   
        semi_high_val = int(str(matchedList0[0])[13])
    

    
    
    
    pattern1 = r"\^\{[a-z0-9]\^\{[a-z0-9]\}\}"                            # 정규표현식 이용해 pi값 추적. 
    matchedList1 = re.findall(pattern1,m)
    if matchedList1:
        # print(matchedList1)
        semi_high_val = str(matchedList1[0])[2]
        semi_high_val_2 = int(str(matchedList1[0])[5])
        high_val= np.exp(semi_high_val_2)                                 # 상위 적분구간 값
        
    
        
    pattern = r"\{\\[a-z0-9]+\}"                            # 정규표현식 이용해 pi값 추적. 
    matchedList = re.findall(pattern,m)
    if matchedList:
        high_val= sym.pi/semi_high_val                                    # 상위 적분구간 값, 2구해옴. 
    
    pattern2 = r"\}\\[a-z0-9]+"                            # 정규표현식 이용해 피적분함수값 추적.(무조건 수행됨.)
    matchedList2 = re.findall(pattern2,m)
    if matchedList2:
        intergrand = (str(matchedList2[0])[2:])
        bar = getattr(sympy, intergrand)
        function = bar(x) 
        
        
    pattern3 = r"\}\\[a-z0-9]+\^\{[a-z0-9]\}"      # 정규표현식 이용해 피적분함수값 추적, 피적분함수가 제곱이나 그 이상이 아닌 경우 계산 안될 수 있음. 
    matchedList3 = re.findall(pattern3,m)
    if matchedList3:
        intergrand2 = int((str(matchedList3[0])[7]))
        function = bar(x)**(intergrand2)    # 제곱과 2 구해옴.

                                        
val = (Integral(function,(x,m[low_idx],high_val)).doit()) 
# print(high_val)
# print(val)






answer = []           # 위에서 구한 정답을 answer list에 차례로 저장. 
answer.append(val)




## 추가본. 
# if 'iint' in Latex_equation: # 이중적분, 면적분
#     print(2)
# if 'iiint' in Latex_equation: # 삼중적분,부피적분, 체적적분
#     print(3)
# if 'oint' in Latex_equation: # 폐곡선(면) 적분
#     print(4)
# if 'partial'in Latex_equation: # 편미분 
#     print(6)
# if 'sum' in Latex_equation: # 시그마 
#     print(5) 




## 출력부분 step4
def reading_answer(i):
    f = open("정답입력받기.txt", 'w')     # 정답입력받기.txt에 쓰기 모드로 입력. 
    f.write(str(answer[i]))
    f.close()


def pasting(xcord,ycord):
    fileName = "정답입력받기.txt" # path of your text file
    # read file that user wants converted from command line. If file can't be read, assign 
    # the file to a file in the directory


    try:
        txt=open(argv[1], "rt",encoding='UTF-8')
    except IndexError:
        txt=open(fileName, "r")
    except FileNotFoundError:
        txt=open(fileName, "r")   



    for i in txt.read().replace("\n",""):
            cases = Image.open("지정글꼴/{}.png".format(str(ord(i))))
            BackGround_Img.paste(cases, (xcord, ycord))
            size = cases.width
            height=cases.height
            xcord+=size
            if sheet_width < xcord or len(i)*115 >(sheet_width-xcord):
                xcord,ycord=0,ycord+140




BackGround_Img=Image.open(f'지정글꼴/quiz7-1.png')             # 첫화면에 정답 입력 
sheet_width=BackGround_Img.width
for i in range(0,4): 
    if i == 0:
        xcord, ycord = 120, 500     # 1번문제
        reading_answer(i)
        pasting(xcord,ycord)
    elif i ==1: 
        xcord, ycord = 40, 1000    # 2번문제
        reading_answer(i)
        pasting(xcord,ycord)
    elif i == 2:
        xcord, ycord = 550, 350    # 3번문제
        reading_answer(i)
        pasting(xcord,ycord)
    elif i == 3: 
        xcord, ycord = 700, 1000   # 4번문제 
        reading_answer(i)
        pasting(xcord,ycord)
BackGround_Img.show()




# --------------------------------------------------------------------------------------------------------------------------------
# 두번째 장 
BackGround_Img=Image.open(f'지정글꼴/quiz7-2.png')
sheet_width=BackGround_Img.width
for i in range(4,len(answer)): 
    if i == 4:
        xcord, ycord = 27, 200     # 5번문제
        reading_answer(i)
        pasting(xcord,ycord)
    elif i ==5: 
        xcord, ycord = 30, 1000    # 6번문제
        reading_answer(i)
        pasting(xcord,ycord)
    elif i == 6:
        xcord, ycord = 750, 200    # 7번문제
        reading_answer(i)
        pasting(xcord,ycord)
    elif i == 7: 
        xcord, ycord = 700, 1000   # 8번문제 
        reading_answer(i)
        pasting(xcord,ycord)

BackGround_Img.show()









