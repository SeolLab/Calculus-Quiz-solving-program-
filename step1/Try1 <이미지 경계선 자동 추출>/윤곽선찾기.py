
# 윤곽선 찾기 모드
# cv2.RETR_EXTERNAL : 가장 외곽의 윤곽선만 찾음
# cv2.RETR_LIST : 모든 윤곽선 찾음 (계층 정보 없음)
# cv2.RETR_TREE : 모든 윤곽선 찾음(계층 정보를 트리구조로 표현)
# 면적
# contourArea()

import sys
import cv2
fname = 'quiz7-1.png'
# if fname is None:
#     print('Image load failed')
#     sys.exit() 
original = cv2.imread(fname, cv2.IMREAD_COLOR)   
target_img = original.copy()   #출력위해 이미지 복사해 둠. 
gray = cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
ret,otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)     #오츠 알고리즘- 최적 임계치 자동 연산. 
contours,heirarchy =cv2.findContours(otsu,cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) # findContours -       윤곽선 검출 함수 
# 윤곽선 정보, 윤곽선 구조 = (이미지, 윤곽선 찾는 mode, 윤곽선 찾을 때 사용하는 근사치 method)
COLOR = (0,200,0) # 녹색 
cv2.drawContours(target_img,contours, -1, COLOR,2)#윤곽선 그리기     
#복사본에 윤곽선 그림,윤곽선 정보,'-1'은 찾은 모든 윤곽선 검출, 윤곽선 색깔,윤곽선 두께


cv2.imshow('Original', original)
cv2.imshow('gray', gray)
cv2.imshow('otsu',otsu)
cv2.imshow('contour',target_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
