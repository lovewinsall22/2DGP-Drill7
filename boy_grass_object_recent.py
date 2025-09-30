from pico2d import *
import random


# Game object class here
class Grass: # 클래스의 이름은 대문자로
    def __init__(self): #생성자함수
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x = 400
        self.frame = 0

    def draw(self):
        self.image.clip_draw(self.frame * 100,0,100,100,self.x, 90)

    def update(self):
        self.frame = (self.frame + 1) % 8


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False





def reset_world():
    global running
    global grass
    global boy

    running = True
    grass = Grass() # 클래스를 이용해 객체 생성
    boy = Boy()

def update_world():
    grass.update()
    boy.update()

def render_world():
    clear_canvas()
    grass.draw() # 객체의 메서드 호출
    boy.draw()
    update_canvas()



open_canvas()

# 초기화 코드
reset_world()

# 게임루프 코드
while running:
    # 입력 처리
    handle_events()
    # 게임 로직
    update_world()
    # 렌더링
    render_world()
    delay(0.05)


close_canvas()