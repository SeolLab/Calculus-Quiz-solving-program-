import sympy as sym
from sympy import Integral, Symbol
from sympy import pprint
from PIL import Image
from sys import argv
import sys
import glob 
import sympy
import re


# Latex_equation = "\int_{0}^{\frac{\pi}{2}}\sin^{2}x d x~"
# m = Latex_equation.replace('\f' ,'\\\\f')
# if 'int' in m:         #단일 적분
#     # print(1)
#     val = m.find('~') -1 
#     x = sym.Symbol(m[val])





#         # low_idx = m.find('_')+2 
#         # high_idx = m.find('_')+2 
    
      
    




#     # if 'frac' in Latex_equation:
#     #     Latex_equation.find('frac')
        
    
#     # if 'infty' in Latex_equation:  #무한대 값 설정. 

#     # if 'sqrt' in Latex_equation:   #근호 설정. 



Latex_equation = "\int_{0}^{\frac{\pi}{2}}\sin^{2}x d x~"
m = Latex_equation.replace('\f' ,'\\\\f')
if 'int' in m:         #단일 적분
    # print(1)
    val = m.find('~') -1 
    x = sym.Symbol(m[val])


    low_idx = m.find('_')+2 
    lst = m.split('\\')
    pattern = r"\{\\[a-z0-9]+\}"
    matchedList = re.findall(pattern,m)
    if matchedList:
        high_val= sym.pi/2



bar = getattr(sympy, 'sin')
result = bar(x)**2
val = (Integral(result,(x,m[low_idx],high_val)).doit()) 



    # 적분 출력 예시.
answer = [1,2,3,4,5]   
answer.append(val)
    



if 'iint' in Latex_equation: # 이중적분, 면적분
    print(2)
if 'iiint' in Latex_equation: # 삼중적분,부피적분, 체적적분
    print(3)
if 'oint' in Latex_equation: # 폐곡선(면) 적분
    print(4)
if 'partial'in Latex_equation: # 편미분 
    print(6)
if 'sum' in Latex_equation: # 시그마 
    print(5) 





def reading_answer(i):
    f = open("정답입력받기.txt", 'w')      # 정답 입력  
    f.write(str(answer[i]))
    f.close()


def pasting(gap,ht):
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
            BG.paste(cases, (gap, ht))
            size = cases.width
            height=cases.height
            gap+=size

            if sheet_width < gap or len(i)*115 >(sheet_width-gap):
                gap,ht=0,ht+140




BG=Image.open(f'지정글꼴/quiz7-1.png')
sheet_width=BG.width
for i in range(0,4): 
    if i == 0:
        gap, ht = 150, 500     # 1번문제
        reading_answer(i)
        pasting(gap,ht)
    elif i ==1: 
        gap, ht = 150, 1000    # 2번문제
        reading_answer(i)
        pasting(gap,ht)
    elif i == 2:
        gap, ht = 700, 500    # 3번문제
        reading_answer(i)
        pasting(gap,ht)
    elif i == 3: 
        gap, ht = 700, 1000   # 4번문제 
        reading_answer(i)
        pasting(gap,ht)
BG.show()




# --------------------------------------------------------------------------------------------------------------------------------
# 두번째 장 
BG=Image.open(f'지정글꼴/quiz7-2.png')
sheet_width=BG.width
for i in range(4,len(answer)): 
    if i == 4:
        gap, ht = 150, 500     # 5번문제
        reading_answer(i)
        pasting(gap,ht)
    elif i ==5: 
        gap, ht = 150, 1000    # 6번문제
        reading_answer(i)
        pasting(gap,ht)
    elif i == 6:
        gap, ht = 700, 500    # 7번문제
        reading_answer(i)
        pasting(gap,ht)
    elif i == 7: 
        gap, ht = 700, 1000   # 8번문제 
        reading_answer(i)
        pasting(gap,ht)

BG.show()









