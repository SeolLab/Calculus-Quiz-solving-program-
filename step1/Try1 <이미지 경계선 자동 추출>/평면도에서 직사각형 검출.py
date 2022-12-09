import sys
import cv2


## 평면도에서 직사각형 검출. 
fname = 'floor_img.jpg'


# if fname is None:
#     print('Image load failed')
#     sys.exit() 
original = cv2.imread(fname, cv2.IMREAD_COLOR)
original2 = cv2.resize(original, None, fx = 0.5, fy = 0.5,interpolation = cv2.INTER_AREA) #보간, cv2.INTER_AREA는 크기 줄일 때 사용  
target_img = original2.copy()   #출력위해 이미지 복사해 둠. 
gray = cv2.cvtColor(original2,cv2.COLOR_BGR2GRAY)
ret,otsu = cv2.threshold(gray , -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)     #오츠 알고리즘- 최적 임계치 자동 연산. 임계치를 넘으면 255로 변하도록 설정.
contours,heirarchy =cv2.findContours(otsu,cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) # findContours -       윤곽선 검출 함수 
# 윤곽선 정보, 윤곽선 구조 = (이미지, 윤곽선 찾는 mode, 윤곽선 찾을 때 사용하는 근사치 method)
COLOR = (200,0,0) # 파란색

idx = 1
# cv2.drawContours(target_img,contours, -1, COLOR,2)#윤곽선 그리기     
#복사본에 윤곽선 그림,윤곽선 정보,'-1'은 찾은 모든 윤곽선 검출, 윤곽선 색깔,윤곽선 두께
for cnt in contours:
    if cv2.contourArea(cnt) > 7000:   # 7000보다 면적이 클 때만 사각형을 잡아줌. 
        x,y,width,height = cv2.boundingRect(cnt) # 윤곽선을 둘러싼 사각형의 x,y좌표와 가로,세로 크기를 반환.
        cv2.rectangle(target_img,(x,y),(x+width,y+height),COLOR,2) # 사각형 정보 입력     


        crop = original2[y: y+height, x: x+height]   # 위에서 생성한 사각형들에 대해 별도의 파일을 만들것. 
        cv2.imshow(f'card_crop_{idx}',crop)  
        cv2.imwrite(f'card_crop_{idx}.png',crop) # 별도 파일로 저장됨. 
        idx += 1 

# cv2.imshow('Original2', original2)
# cv2.imshow('otsu',otsu)
cv2.imshow('contour',target_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
