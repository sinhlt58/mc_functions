setblock ~0 ~0 ~-1 minecraft:command_block[facing=north]
data modify block ~0 ~0 ~-1 Command set value "clone 0 4 88 26 28 100 0 4 88 replace move"
setblock ~0 ~0 ~-2 minecraft:chain_command_block[facing=north]
data modify block ~0 ~0 ~-2 Command set value "summon minecraft:area_effect_cloud ~0 ~0 ~-1 {Tags:[\"TickCounter\"],Age:-10}"
setblock ~0 ~0 ~-3 minecraft:command_block[facing=north]
data modify block ~0 ~0 ~-3 Command set value "clone 0 4 88 26 28 100 0 5 88 replace move"
setblock ~0 ~0 ~-4 minecraft:chain_command_block[facing=north]
data modify block ~0 ~0 ~-4 Command set value "summon minecraft:area_effect_cloud ~0 ~0 ~-1 {Tags:[\"TickCounter\"],Age:-10}"
setblock ~0 ~0 ~-5 minecraft:command_block[facing=north]
data modify block ~0 ~0 ~-5 Command set value "clone 0 5 88 26 29 100 0 6 88 replace move"
setblock ~0 ~0 ~-6 minecraft:chain_command_block[facing=north]
data modify block ~0 ~0 ~-6 Command set value "summon minecraft:area_effect_cloud ~0 ~0 ~-1 {Tags:[\"TickCounter\"],Age:-10}"
