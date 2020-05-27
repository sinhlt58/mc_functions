import numpy as np

from aniblock.blocks import *
from aniblock.utils import *
from aniblock.blocks_writers import *


class AnimatedMovingCube(object):

    def __init__(
        self,
        init_lower_right,
        init_upper_left,
        run_seconds,
        out_file,
        tick_rate=10,
        is_stay=False,
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

        self.out_file = out_file
        self.velocity = velocity
        self.is_stay = is_stay

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
            blocks += self.frame_render(i)
            # Update to change state
            self.frame_update(i)

        if blocks:
            write_command_blocks(self.out_file, blocks)
            print(f"Done render {self.num_frames} frames")
        else:
            print("Nothing to render")

    def frame_update(self, frame_index):
        """
            Change to current sate to the next state
            Update the positions, ...
        """
        # Calculate the animation frame if has animation

        # Update positions if not is_stay
        if not self.is_stay:
            self.prev_lower_right = self.curr_lower_right
            self.prev_upper_left = self.prev_upper_left

            self.curr_lower_right += self.velocity
            self.curr_upper_left += self.velocity

    def frame_render(self, frame_index):
        """
            Render the current state and return command blocks
        """
        blocks = []

        # Render animation frame if there is any change in the animation
        # frame index if so, we don't need to render position (we copy from animation frames).
        render_position = True

        # Only render position if something changes
        if render_position and (self.curr_lower_right != self.prev_lower_right or \
            self.curr_upper_left  != self.prev_upper_left):

            begin_str = pos_to_str(self.prev_lower_right, POS_ABSOLUTE)
            end_str = pos_to_str(self.prev_upper_left, POS_ABSOLUTE)
            des_str = pos_to_str(self.curr_lower_right, POS_ABSOLUTE)

            blocks.append(
                CommandBlock(f"clone {begin_str} {end_str} {des_str} replace move")
            )

        # Add delay
        if blocks:
            blocks.append(
                CommandBlockDelay(delay_ticks=self.tick_rate)
            )

        return blocks
