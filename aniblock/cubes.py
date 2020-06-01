import numpy as np

from aniblock.blocks import *
from aniblock.utils import *
from aniblock.blocks_writers import *


class GeneralCube(object):

    def __init__(self, out_file):
        self.out_file = out_file
        # Command blocks contain rendering commands
        self.blocks = []

    def render_blocks(self):
        if self.blocks:
            write_command_blocks(self.out_file, self.blocks)
        else:
            print("Nothing to render")


class AnimatedMovingCube(GeneralCube):

    def __init__(
        self,
        init_lower_right,
        init_upper_left,
        run_steps,
        tick_rate,
        out_file,
        is_stay=False,
        velocity=[0, 0, 0],
        animation=None,
    ):
        super().__init__(out_file)

        self.init_lower_right = np.array(init_lower_right, dtype=int)
        self.init_upper_left = np.array(init_upper_left,  dtype=int)

        # Previous positions
        self.prev_lower_right = self.init_lower_right
        self.prev_upper_left = self.init_upper_left

        # Current positions
        self.curr_lower_right = self.init_lower_right
        self.curr_upper_left = self.init_upper_left

        # Number of running steps
        self.run_steps = run_steps

        # Number of ticks between two frames
        self.tick_rate = tick_rate

        self.velocity = np.array(velocity, dtype=int)
        self.is_stay = is_stay

        self.animation = animation

    def render(self):
        """
            Render to Minecraft commands
        """
        # For each frame, calculate the position, frame index in the animation frames
        # and then render
        for i in range(0, self.run_steps):
            # Render the current state
            self.blocks += self.frame_render(i)
            # Update to change state
            self.frame_update(i)

        self.render_blocks()
        if self.blocks:
            print(f"Render {self.run_steps} frames")

    def frame_update(self, frame_index):
        """
            Change to current sate to the next state
            Update the positions, ...
        """
        # Calculate the animation frame if has animation

        # Update positions if not is_stay
        if not self.is_stay:
            self.prev_lower_right = self.curr_lower_right.copy()
            self.prev_upper_left = self.curr_upper_left.copy()

            print(f"frame_index: {frame_index}, curr_lower_right: {self.curr_lower_right}, curr_upper_left: {self.curr_upper_left}")

            self.curr_lower_right += self.velocity
            self.curr_upper_left += self.velocity

    def frame_render(self, frame_index):
        """
            Render the current state and return command blocks
        """
        blocks = []

        # TODO: Animation later
        # Render animation frame if there is any change in the animation
        # frame index if so, we don't need to render position (we copy from animation frames).
        render_position = True
        if self.animation:
            begin_pos, end_pos = animation.get_frame_position(frame_index)
            begin_str = pos_to_str(begin_pos, POS_ABSOLUTE)
            end_str = pos_to_str(end_pos, POS_ABSOLUTE)
            des_str = pos_to_str(self.curr_lower_right, POS_ABSOLUTE)

            # TODO: add command blocks here

            render_position = False


        # Only render position if something changes
        if render_position and not self.is_stay:
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


class ReversedDestroyCube(GeneralCube):

        def __init__(
            self,
            init_lower_right,
            init_upper_left,
            out_file,
            tick_rate=10,
            first_delay_ticks=0,
            delete_x_size=None,
            delete_y_size=None,
            delete_z_size=None,
        ):
            super().__init__(out_file)

            self.init_lower_right = np.array(init_lower_right, dtype=int)
            self.init_upper_left = np.array(init_upper_left,  dtype=int)

            if delete_x_size is None:
                delete_x_size = abs(self.init_upper_left[0] - self.init_lower_right[0]) + 1
            if delete_y_size is None:
                delete_y_size = abs(self.init_upper_left[1] - self.init_lower_right[1]) + 1
            if delete_z_size is None:
                delete_z_size = abs(self.init_upper_left[2] - self.init_lower_right[2]) + 1

            self.delete_x_size = delete_x_size
            self.delete_y_size = delete_y_size
            self.delete_z_size = delete_z_size


            # Number of ticks between two frames
            self.tick_rate = tick_rate
            self.first_delay_ticks = first_delay_ticks

        def _get_num_parts(self, n, m):
            return n // m + int(n % m != 0)

        def _get_lower_upper(self, i, size, min_l, max_u):
            lower = i * size + min_l
            upper = lower + size - 1
            if upper > max_u:
                upper = max_u
            return lower, upper

        def render(self):
            first_pos = self.init_lower_right
            second_pos = self.init_upper_left

            num_y_parts = self._get_num_parts(
                abs(second_pos[1] - first_pos[1]) + 1, self.delete_y_size)
            num_x_parts = self._get_num_parts(
                abs(second_pos[0] - first_pos[0]) + 1, self.delete_x_size)
            num_z_parts = self._get_num_parts(
                abs(second_pos[2] - first_pos[2]) + 1, self.delete_z_size)

            for yi in reversed(range(0, num_y_parts)):
                lower_y, upper_y = self._get_lower_upper(yi, self.delete_y_size, first_pos[1], second_pos[1])
                for xi in range(0, num_x_parts):
                    lower_x, upper_x = self._get_lower_upper(xi, self.delete_x_size, first_pos[0], second_pos[0])
                    for zi in range(0, num_z_parts):
                        lower_z, upper_z = self._get_lower_upper(zi, self.delete_z_size, first_pos[2], second_pos[2])

                        if self.first_delay_ticks > 0:
                            self.blocks.extend([
                                CommandBlock(f"say "),
                                CommandBlockDelay(delay_ticks=self.first_delay_ticks),
                            ])
                            self.first_delay_ticks = 0

                        self.blocks.extend([
                            CommandBlock(f"fill {lower_x} {lower_y} {lower_z} {upper_x} {upper_y} {upper_z} minecraft:air destroy"),
                            CommandBlock("kill @e[type=minecraft:item]", "chain_command_block"),
                            CommandBlockDelay(delay_ticks=self.tick_rate),
                        ])

            self.render_blocks()
