import sympy as sym
import sympy
from sympy import Integral, Symbol
from sympy import pprint
from PIL import Image
from sys import argv
import sys
import re



# Latex_equation = '\int_{0}^{\frac{\pi}{2}}\sin^{2}x d x~'
# def check_value():     # 분수, 제곱근, 무한대 값 check 

# if 'int' in Latex_equation:         #단일 적분
#     # print(1)
#     val = Latex_equation.find('~') -1 
#     x = sym.Symbol(Latex_equation[val])


#     low_idx = Latex_equation.find('_')+2
#     if Latex_equation[low_idx] == '\\' :
#         if Latex_equation[low_idx+1] == 'f':      # f stands for frac 
            
#         elif Latex_equation[low_idx+1] == 's':    # s stands for sqrt
#         elif Latex_equation[low_idx+1] == 'i':    # i stands for infty
#         else: 
#             low = Latex_equation[low_idx]

#     high_idx = Latex_equation.find('')+2
    
    

# # f = sym.sin(x)**2
# # (Integral(f,(x,low,(sym.pi)/2)).doit())
# Latex_equation= '\\int_{0}^{\\frac{\\pi}{2}}\\sin^{2}x d x~'

# for i in Latex_equation.split('\\'):
#     print(i)

# import re
# pattern = r"\{\\[a-z0-9]+\}"


# matchedList = re.findall(pattern,Latex_equation)# 매칭된 값은 리스트로 모두 반환
# if matchedList:
#     if (str(matchedList[0])[2:4]) == 'pi': 

# Latex_equation = '\int_{0}^{\frac{\pi}{2}}\sin^{2}x d x~'
# Latex_equation=Latex_equation.replace('\\' ,'\\')
# print(Latex_equation)


# import re
# Latex_equation = "\int_{0}^{\frac{\pi}{2}}\sin^{2}x d x~"
# m = Latex_equation.replace('\f' ,'\\\\f')
# print(m)

# pattern = r"\{\\[a-z0-9]+\}"
# matchedList = re.findall(pattern,m)
# if matchedList:
#     print(matchedList)





            
