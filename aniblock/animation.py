import numpy as np


class Animation(object):

    def __init__(
        self,
        init_lower_right,
        init_upper_left,
        num_frame,
        frame_space_x=1,
        frame_space_z=1,
        max_x_frames=10,
        max_z_frames=10,
    ):
        self.init_lower_right = np.array(init_lower_right)
        self.init_upper_left = np.array(init_upper_left)
        self.num_frame = num_frame

        # Distance between 2 frames
        self.frame_space_z = frame_space_z
        self.frame_space_x = frame_space_x

        # Maximum number of frame in x direction
        self.max_x_frames = max_x_frames
        self.max_z_frames = max_z_frames

        self.frame_x_size = abs(init_upper_left[0] - init_lower_right[0]) + 1
        self.frame_z_size = abs(init_upper_left[2] - init_lower_right[2]) + 1

    def get_frame_position(self, frame_index):
        """
            Return the cube positions of the animation frame given the frame_index
        """
        #    -x(west)
        #    |
        #    |
        #    |________ -z(north)
        frame_index_shortten = frame_index % self.num_frame
        x_idx = frame_index_shortten % self.max_x_frames
        z_idx = frame_index_shortten // self.max_x_frames

        x_offset = x_idx * (self.frame_x_size + self.frame_space_x)
        z_offset = z_idx * (self.frame_z_size + self.frame_space_z)
        offset = np.array([-x_offset, 0, -z_offset])

        begin_pos = self.init_lower_right + offset
        end_pos = self.init_upper_left + offset

        print(f"frame_index: {frame_index}")
        print(f"frame_index_shortten: {frame_index_shortten}")
        print(f"init begin_pos: ", self.init_lower_right)
        print(f"init end_pos: ", self.init_upper_left)
        print(f"begin_pos: ", begin_pos)
        print(f"end_pos: ", end_pos)

        return begin_pos, end_pos
