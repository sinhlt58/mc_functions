setblock ~0 ~0 ~-1 minecraft:command_block[facing=north]
data modify block ~0 ~0 ~-1 Command set value "say "
setblock ~0 ~0 ~-2 minecraft:chain_command_block[facing=north]
data modify block ~0 ~0 ~-2 Command set value "summon minecraft:area_effect_cloud ~0 ~0 ~-1 {Tags:[\"TickCounter\"],Age:-20}"
setblock ~0 ~0 ~-3 minecraft:command_block[facing=north]
data modify block ~0 ~0 ~-3 Command set value "fill 18 61 55 32 61 71 minecraft:air destroy"
setblock ~0 ~0 ~-4 minecraft:chain_command_block[facing=north]
data modify block ~0 ~0 ~-4 Command set value "kill @e[type=minecraft:item]"
setblock ~0 ~0 ~-5 minecraft:chain_command_block[facing=north]
data modify block ~0 ~0 ~-5 Command set value "summon minecraft:area_effect_cloud ~0 ~0 ~-1 {Tags:[\"TickCounter\"],Age:-10}"
setblock ~0 ~0 ~-6 minecraft:command_block[facing=north]
data modify block ~0 ~0 ~-6 Command set value "fill 18 59 55 32 60 71 minecraft:air destroy"
setblock ~0 ~0 ~-7 minecraft:chain_command_block[facing=north]
data modify block ~0 ~0 ~-7 Command set value "kill @e[type=minecraft:item]"
setblock ~0 ~0 ~-8 minecraft:chain_command_block[facing=north]
data modify block ~0 ~0 ~-8 Command set value "summon minecraft:area_effect_cloud ~0 ~0 ~-1 {Tags:[\"TickCounter\"],Age:-10}"
