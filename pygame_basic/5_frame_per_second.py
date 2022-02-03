import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width,screen_height)) #화면 크기 설정, screen이라는변수로 받아옴

#화면 타이틀 설정(제목)
pygame.display.set_caption("ChaeHyun GAME") #게임 이름

#FPS
clock = pygame.time.Clock()

#배경이미지 불러오기
background = pygame.image.load("pygame_basic/background.png")

#캐릭터(스트라이프) 불러오기
character = pygame.image.load("pygame_basic/character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] #character size의 첫번쨰 값이 width임
character_height = character_size[1] #character size의 첫번쨰 값이 height임
character_x_pos = (screen_width - character_width)/ 2 #character의 가로 위치 (중앙)
character_y_pos = screen_height - character_height #세로위치(맨 아래)

#이동할좌표
to_x = 0
to_y = 0

#이동 속도 
character_speed = 0.6

#동작을 검사하는 이벤트 루프가 계속 실행되어야 창이 바로 꺼지지 않음
#이벤트 루프
running = True #게임이 진행중인지 확인하는 역할
while running: 
    dt = clock.tick(60) #게임화면의 초당프레임 수를 결정
#캐릭터가 1초 동안에 100만큼 이동을 해야함
# 10 fps : 1초 동안에 10번 동작 -> 1번에 10만큼 이동 10*10 = 100
# 20 fps : 1초동안에 20번 동작 1번에 5만큼 이동해야 5*20 = 100
#이동속도 고정 필요
#   print("fps :" + str(clock.get_fps()))
    
    for event in pygame.event.get(): #어떤 이벤트가 발생했는지 체크
        if event.type == pygame.QUIT: #창끄는 x버튼 클릭시
            running = False #게임 종료
        
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로 움직
                to_x -= character_speed 
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로 움직
                to_x += character_speed 
            elif event.key == pygame.K_UP: #캐릭터를 위쪽으로 움직
                to_y -= character_speed 
            elif event.key == pygame.K_DOWN: #캐릭터를 아래쪽으로 움직
                to_y += character_speed 
                
        if event.type == pygame.KEYUP: #방향키뗴면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    #캐릭터의 위치잡기
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    
    #경계값 처리 - 화면밖으로 나가지 않도록 
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
        
    #색으로 backgorund 지정시 => screen.fill((0,0,255))
    #이미지로 넣기
    screen.blit(background, (0,0)) #배경그리기 background image 시작점
    
    screen.blit(character, (character_x_pos,character_y_pos))
    
    pygame.display.update() #게임화면을 다시 그리기
    
#running이 종료하면(false) 게임이 종료
pygame.quit()