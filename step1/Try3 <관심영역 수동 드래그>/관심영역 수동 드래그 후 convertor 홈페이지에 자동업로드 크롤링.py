#관심영역 드래그 
import cv2
import numpy as np

# 아래는 크롤링에 필요 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import glob 


isDragging = False                         # 마우스 드래그 상태 저장
x0,y0,w,h = -1,-1,-1,-1                    # 영역 선택 좌표 저장
blue,red = (255,0,0),(0,0,255)              # 색상 값
idx = 1 
def onMouse(event, x, y, flags, param):     # 마우스 이벤트 핸들 함수
    global isDragging, x0, y0, img,idx         # 전역 변수 참조
    if event == cv2.EVENT_LBUTTONDOWN:      # 왼쪽 마우스 버튼 다운, 드래그 시작
        isDragging = True
        x0 = x
        y0 = y
        
    elif event == cv2.EVENT_MOUSEMOVE:      # 마우스 움직임
        if isDragging:                       # 드래그 진행 중
            img_draw = img.copy()            # 사각형 그림 표현을 위한 이미지 복제 (매번 같은 이미지에 그려지면 이미지가 더러워짐)
            cv2.rectangle(img_draw, (x0,y0), (x,y), blue, 2)  # 드래그 진행 영역 표시
            cv2.imshow('img', img_draw)       # 사각형으로 표시된 그림 화면 출력
            
    elif event == cv2.EVENT_LBUTTONUP:       # 왼쪽 마우스 버튼 업
        if isDragging:                        # 드래그 중지
            isDragging = False               
            w= x - x0                         # 드래그 영역 폭 계산
            h= y - y0                         # 드래그 영역 높이 계산
            if w>0 and h>0:                  # 폭과 높이가 양수이면 드래그 방향이 옳음
                img_draw = img.copy()         # 선택 영역에 사각형 그림을 표시할 이미지 복제
                cv2.rectangle(img_draw, (x0, y0), (x, y), red, 2) # 선택 영역에 빨간색 사각형 표시
                cv2.imshow('img', img_draw)         # 빨간색 사각형이 그려진 이미지 화면 출력
               
            
                crop = img[y0:y0+h, x0:x0+w]   # 위에서 생성한 사각형들에 대해 별도의 파일을 만들것. 
                cv2.imshow(f'quiz7_crop{idx}',crop)  
                cv2.moveWindow(f'quiz7_crop{idx}', 0,0)     # 새 창을 화면 좌측 상단으로 이동
                cv2.imwrite(f'quiz7_crop{idx}.png',crop) # 별도 파일로 저장됨. 
                idx += 1
            else:
                print("try again!")
for i in range(1,3):
    fname = f'quiz7-{i}.png'          
    img = cv2.imread(fname)
    cv2.imshow('img', img)
    cv2.setMouseCallback('img', onMouse) # 마우스 이벤트 등록
    cv2.waitKey()
    cv2.destroyAllWindows()
    
   
   
   
## 아래 부분 부터 크롤링 
driver = webdriver.Chrome()
driver.get("https://convertio.co/kr/image-converter/")
output = glob.glob('C:\\Users\\Admin\\3,4. 자동업로드\\quiz7_crop*.png')
for i in range(1,len(output)+1): 
    driver.find_element_by_css_selector("input[type='file']").send_keys(f"C:\\Users\\Admin\\3,4. 자동업로드\\quiz7_crop{i}.png")    
    
