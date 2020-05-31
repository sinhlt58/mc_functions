
from aniblock.constants import *
from aniblock.utils import *


class Block:
    pass


class CommandBlock(Block):

    def __init__(self, command, type="command_block"):
        self.command = command
        self.type = type

    def to_mc_commands(self, pos, facing, relative=POS_RELATIVE_W):
        pos_str = pos_to_str(pos, relative)
        return [
            f"setblock {pos_str} minecraft:{self.type}[facing={facing}]",
            f"data modify block {pos_str} Command set value \"{self.command}\""
        ]


class CommandBlockDelay(CommandBlock):

    def __init__(self, delay_ticks):
        super().__init__("")
        self.delay_ticks = delay_ticks

    def to_mc_commands(self, pos, facing, relative=POS_RELATIVE_W):
        delay_pos = facing_to_vec(facing)

        pos_str = pos_to_str(pos, relative)
        delay_pos_str = pos_to_str(delay_pos, relative)

        return [
            f"setblock {pos_str} minecraft:chain_command_block[facing={facing}]",
            f"data modify block {pos_str} Command set value \"summon minecraft:area_effect_cloud {delay_pos_str} {{Tags:[\\\"TickCounter\\\"],Age:{-self.delay_ticks}}}\""
        ]
