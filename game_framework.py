import time
frame_time = 0.0

running = None
stack = None

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # pixel per m

def change_mode(mode):
    global stack
    if (len(stack) > 0):
        # execute the current mode's finish function
        stack[-1].finish()
        # remove the current mode
        stack.pop()
    stack.append(mode)
    mode.init()


def push_mode(mode):
    global stack
    if (len(stack) > 0):
        stack[-1].pause()
    stack.append(mode)
    mode.init()


def pop_mode():
    global stack
    if (len(stack) > 0):
        # execute the current mode's finish function
        stack[-1].finish()
        # remove the current mode
        stack.pop()

    # execute resume function of the previous mode
    if (len(stack) > 0):
        stack[-1].resume()


def quit():
    global running
    running = False


def run(start_mode):
    global running, stack
    running = True
    stack = [start_mode]
    start_mode.init()

    # 여기를 채우시오.
    global frame_time
    frame_time = 0.0
    current_time = time.time()

    while running:      #게임 로직 위아래로 시간 측정
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()

        # 여기를 채우시오.
        frame_time = time.time() - current_time
        frame_rate = 1.0 / frame_time   # 역수
        #print(f'Frame Time: {frame_time}, Frame Rate: {frame_rate}')
        current_time += frame_time

    # repeatedly delete the top of the stack
    while (len(stack) > 0):
        stack[-1].finish()
        stack.pop()
