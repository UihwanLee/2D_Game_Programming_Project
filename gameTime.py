'''
    2DGP 게임에서 사용할 Time 모듈

    frame_rate
    frame_time

    변수를 관리 한다

'''

import time

class Time:
    frame_rate = 0.0
    frame_time = 0.0

    def __init__(self):
        Time.frame_rate = 0.0
        Time.frame_time = 0.0
        self.cur_time = time.time()
        self.start_time = time.time()
        self.elapsed_time = 0.0
        self.frame_count = 0

    def update(self):
        self.frame_count += 1
        self.cur_time = time.time()
        self.elapsed_time = self.cur_time - self.start_time

        Time.frame_rate = self.frame_count / self.elapsed_time
        Time.frame_time = 1.0 / Time.frame_rate

        self.frame_count = 0
        self.start_time = self.cur_time

        # print(f"프레임 속도: {Time.frame_rate:.2f} FPS")
        # print(f"프레임 시간: {Time.frame_time:.10f} mms")