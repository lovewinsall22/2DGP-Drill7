from pico2d import *
from random import randint

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
        self.x = randint(0,800)
        self.frame = randint(0,7)

    def draw(self):
        self.image.clip_draw(self.frame * 100,0,100,100,self.x, 90)

    def update(self):
        self.frame = (self.frame + 1) % 8

class Zombie:
    pass




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
    global world
    global grass
    #global boy
    global team

    running = True
    world = []

    grass = Grass() # 클래스를 이용해 객체 생성
    world.append(grass)
    #boy = Boy()
    team = [Boy() for _ in range(11)]
    world += team

def update_world():
    for gameObject in world:
        gameObject.update()

def render_world():
    clear_canvas()

    for gameObject in world:
        gameObject.draw()

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