import numpy as np


class Animation(object):

    def __init__(
        self,
        init_lower_right,
        init_upper_left,
        num_frame,
        frame_space=1,
        max_x_frames=10,
    ):
        self.init_lower_right = np.array(init_lower_right)
        self.init_upper_left = np.array(init_upper_left)
        self.num_frame = num_frame

        # Distance between 2 frames
        self.frame_space = frame_space

        # Maximum number of frame in x direction
        self.max_x_frames = max_x_frames

        self.frame_x_size = abs(init_upper_left[0] - init_lower_right[0])
        self.frame_z_size = abs(init_upper_left[2] - init_lower_right[2])

    def get_frame(self, frame_index):
        """
            Return the cube positions of the animation frame given the frame_index
        """
        #    -x(west)
        #    |
        #    |
        #    |________ -z(north)
        x_idx = frame_index % self.max_x_frames
        z_idx = frame_index // self.max_z_frames

        x_offset = x_idx * (self.frame_x_size + self.frame_space)
        z_offset = z_idx * (self.frame_z_size + self.frame_space)
        offset = np.array([-x_offset, 0, -z_offset])

        begin_pos = self.init_lower_right + offset
        end_pos = self.init_upper_left + offset

        return begin_pos, end_pos
