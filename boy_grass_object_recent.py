from pico2d import *
import random


# Game object class here


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False




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