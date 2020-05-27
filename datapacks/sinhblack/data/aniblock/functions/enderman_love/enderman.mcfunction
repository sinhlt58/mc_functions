setblock ~0 ~0 ~0 minecraft:command_block[facing=north]
data modify block ~0 ~0 ~0 Command set value "clone 1 1 1 5 5 5 1 1 1 replace move"
setblock ~0 ~0 ~-1 minecraft:chain_command_block[facing=north]
data modify block ~0 ~0 ~-1 Command set value "summon minecraft:area_effect_cloud ~0 ~0 ~-2 {Tags:[\"TickCounter\"],Age:-10}"
setblock ~0 ~0 ~-2 minecraft:command_block[facing=north]
data modify block ~0 ~0 ~-2 Command set value "clone 1 1 1 5 5 5 0 1 1 replace move"
setblock ~0 ~0 ~-3 minecraft:chain_command_block[facing=north]
data modify block ~0 ~0 ~-3 Command set value "summon minecraft:area_effect_cloud ~0 ~0 ~-4 {Tags:[\"TickCounter\"],Age:-10}"
setblock ~0 ~0 ~-4 minecraft:command_block[facing=north]
data modify block ~0 ~0 ~-4 Command set value "clone 0 1 1 4 5 5 -1 1 1 replace move"
setblock ~0 ~0 ~-5 minecraft:chain_command_block[facing=north]
data modify block ~0 ~0 ~-5 Command set value "summon minecraft:area_effect_cloud ~0 ~0 ~-6 {Tags:[\"TickCounter\"],Age:-10}"
setblock ~0 ~0 ~-6 minecraft:command_block[facing=north]
data modify block ~0 ~0 ~-6 Command set value "clone -1 1 1 3 5 5 -2 1 1 replace move"
setblock ~0 ~0 ~-7 minecraft:chain_command_block[facing=west]
data modify block ~0 ~0 ~-7 Command set value "summon minecraft:area_effect_cloud ~-1 ~0 ~-7 {Tags:[\"TickCounter\"],Age:-10}"
setblock ~-1 ~0 ~0 minecraft:command_block[facing=west]
data modify block ~-1 ~0 ~0 Command set value "clone -2 1 1 2 5 5 -3 1 1 replace move"
setblock ~-1 ~0 ~-1 minecraft:chain_command_block[facing=south]
data modify block ~-1 ~0 ~-1 Command set value "summon minecraft:area_effect_cloud ~-1 ~0 ~0 {Tags:[\"TickCounter\"],Age:-10}"
setblock ~-1 ~0 ~-2 minecraft:command_block[facing=south]
data modify block ~-1 ~0 ~-2 Command set value "clone -3 1 1 1 5 5 -4 1 1 replace move"
setblock ~-1 ~0 ~-3 minecraft:chain_command_block[facing=south]
data modify block ~-1 ~0 ~-3 Command set value "summon minecraft:area_effect_cloud ~-1 ~0 ~-2 {Tags:[\"TickCounter\"],Age:-10}"
setblock ~-1 ~0 ~-4 minecraft:command_block[facing=south]
data modify block ~-1 ~0 ~-4 Command set value "clone -4 1 1 0 5 5 -5 1 1 replace move"
setblock ~-1 ~0 ~-5 minecraft:chain_command_block[facing=south]
data modify block ~-1 ~0 ~-5 Command set value "summon minecraft:area_effect_cloud ~-1 ~0 ~-4 {Tags:[\"TickCounter\"],Age:-10}"
setblock ~-1 ~0 ~-6 minecraft:command_block[facing=south]
data modify block ~-1 ~0 ~-6 Command set value "clone -5 1 1 -1 5 5 -6 1 1 replace move"
setblock ~-1 ~0 ~-7 minecraft:chain_command_block[facing=south]
data modify block ~-1 ~0 ~-7 Command set value "summon minecraft:area_effect_cloud ~-1 ~0 ~-6 {Tags:[\"TickCounter\"],Age:-10}"
setblock ~-2 ~0 ~0 minecraft:command_block[facing=north]
data modify block ~-2 ~0 ~0 Command set value "clone -6 1 1 -2 5 5 -7 1 1 replace move"
setblock ~-2 ~0 ~-1 minecraft:chain_command_block[facing=north]
data modify block ~-2 ~0 ~-1 Command set value "summon minecraft:area_effect_cloud ~-2 ~0 ~-2 {Tags:[\"TickCounter\"],Age:-10}"
setblock ~-2 ~0 ~-2 minecraft:command_block[facing=north]
data modify block ~-2 ~0 ~-2 Command set value "clone -7 1 1 -3 5 5 -8 1 1 replace move"
setblock ~-2 ~0 ~-3 minecraft:chain_command_block[facing=north]
data modify block ~-2 ~0 ~-3 Command set value "summon minecraft:area_effect_cloud ~-2 ~0 ~-4 {Tags:[\"TickCounter\"],Age:-10}"
