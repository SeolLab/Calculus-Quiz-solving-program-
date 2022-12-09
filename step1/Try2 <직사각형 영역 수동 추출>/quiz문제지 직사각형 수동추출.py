import cv2
import numpy as np

point_list = []
src_img = cv2.imread('quiz7-1.png')    # source image
src_img2 = cv2.resize(src_img,None, fx= 0.5, fy= 0.5, interpolation=cv2.INTER_AREA)  #이미지 사이즈 조정.(비율은 유지되도록 설정)
COLOR = (100,0,100)   # 라인 색 설정 (보라색 사용)
THICKNESS = 1  # 라인 두께 설정 
drawing = False
def mouse_handler(event,x,y,flags,param):
    global drawing
    dst_img = src_img2.copy()
    if event == cv2.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼 DONW
        drawing = True
        point_list.append((x,y)) # 마우스 현재 위치 point_list에 append
        
    if drawing:
        prev_point = None #직선의 시작점 
        for point in point_list:
            cv2.circle(dst_img,point,3,COLOR,cv2.FILLED)     
            if prev_point:
                cv2.line(dst_img, prev_point, point,COLOR,THICKNESS, cv2.LINE_AA)  # 매끄럽게 출력되도록 함. 
            prev_point = point
        
        next_point =(x,y)
        if len(point_list) == 4: 
            show_result() #결과 출력
            next_point = point_list[0]
            
        cv2. line(dst_img, prev_point, next_point,COLOR,THICKNESS, cv2.LINE_AA)   # 매끄럽게 출력되도록 함.
        
    
        
    cv2.imshow('img',dst_img)    # 이미지 출력 
    
        
        
def show_result():
    width, height = 530,710
    src = np.float32(point_list)
    dst = np.array([[0,0],[width,0],[width,height],[0,height]],dtype=np.float32)
    # 좌상, 우상, 우하, 좌하(시계방향 4방향 정의 )    사진에서 기울어진 부분도 수평초점을 맞춰줌. 
    
    matrix = cv2.getPerspectiveTransform(src,dst) # Matrix얻어옴.
    result = cv2.warpPerspective(src_img2,matrix,(width, height))
    cv2.imshow('result',result)
    
cv2.namedWindow('img') 
# img라는 이름의 윈도우를 먼저 만들어 둠. 여기에 마우스 이벤트를 처리하기 위한 핸들러 적용 
cv2.setMouseCallback('img',mouse_handler)    
cv2.imshow('img',src_img2) 
cv2.waitKey(0)
cv2.destroyAllwindows()     
