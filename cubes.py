
import numpy as np


class AnimatedMovingCube(object):

    def __init__(
        self,
        init_lower_right,
        init_upper_left,
        run_seconds,
        tick_rate=10,
        is_static=False,
        velocity=np.array(0, 0, 0)
    ):
        self.init_lower_right = np.array(init_lower_right)
        self.init_upper_left = np.array(init_upper_left)

        # Previous positions
        self.prev_lower_right = self.init_lower_right
        self.prev_upper_left = self.init_upper_left

        # Current positions
        self.curr_lower_right = self.init_lower_right
        self.curr_upper_left = self.init_upper_left

        # Running time in seconds
        self.run_seconds = run_seconds

        # Number of ticks between two frames
        self.tick_rate = tick_rate

        # Running time in ticks (1 sec = 20 ticks)
        self.run_ticks = run_seconds * 20

        # Calculate total number of frames need to render
        self.num_frames = self.run_ticks // tick_rate


    def render(self):
        """
            Render to Minecraft commands
        """
        # Command blocks contain rendering commands
        blocks = []

        # For each frame, calculate the position, frame index in the animation frames
        # and then render
        for i in range(0, self.num_frames):
            # Render the current state
            self.frame_render(i)
            # Update to change state
            self.frame_update(i)

    def frame_update(self, frame_index):
        """
            Update the positions, ...
        """
        pass

    def frame_render(self, frame_index):
        """
            Render the current state
        """
        pass
