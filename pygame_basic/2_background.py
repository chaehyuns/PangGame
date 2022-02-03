import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width,screen_height)) #화면 크기 설정, screen이라는변수로 받아옴

#화면 타이틀 설정(제목)
pygame.display.set_caption("ChaeHyun GAME") #게임 이름

#배경이미지 불러오기
background = pygame.image.load("pygame_basic/background.png")

#동작을 검사하는 이벤트 루프가 계속 실행되어야 창이 바로 꺼지지 않음
#이벤트 루프
running = True #게임이 진행중인지 확인하는 역할
while running: 
    for event in pygame.event.get(): #어떤 이벤트가 발생했는지 체크
        if event.type == pygame.QUIT: #창끄는 x버튼 클릭시
            running = False #게임 종료


    #색으로 backgorund 지정
    #screen.fill((0,0,255))
    #이미지로 넣기
    screen.blit(background, (0,0)) #배경그리기 background image 시작점
    
    pygame.display.update() #게임화면을 다시 그리기
    
#running이 종료하면(false) 게임이 종료
pygame.quit()
