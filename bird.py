from pico2d import load_image, get_time, load_font
from sdl2 import SDL_KEYDOWN, SDLK_SPACE, SDLK_RIGHT, SDL_KEYUP, SDLK_LEFT

import game_world
import game_framework
from state_machine import StateMachine

# Bird Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 100.0  # 100km/h
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # pixel per m

#Bird 한 프레임 크기 184x169
#새의 크기:

#Bird Action Speed
ACTION_PER_TIME = 5     #1초에 5회 날갯짓
FRAMES_PER_ACTION = 14

FRAMES_PER_SECOND = FRAMES_PER_ACTION / ACTION_PER_TIME


class Bird:
    image = None

    def __init__(self, x=0, y=500):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')

        self.font = load_font('ENCR10B.TTF', 16)
        self.item = None

        self.x, self.y = x, y
        self.frame = 0
        self.face_dir = 1

    def update(self):
        self.frame += FRAMES_PER_SECOND * game_framework.frame_time % 14
        self.x += game_framework.frame_time * PIXEL_PER_METER

    def draw(self):
        self.image.clip_draw(int(self.frame % 5) * 184, int(self.frame//5) * 169, 184, 169, self.x, self.y)


