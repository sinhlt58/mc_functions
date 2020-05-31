setblock ~0 ~0 ~-1 minecraft:command_block[facing=north]
data modify block ~0 ~0 ~-1 Command set value "say First delay 40 ticks"
setblock ~0 ~0 ~-2 minecraft:chain_command_block[facing=north]
data modify block ~0 ~0 ~-2 Command set value "summon minecraft:area_effect_cloud ~0 ~0 ~-1 {Tags:[\"TickCounter\"],Age:-40}"
setblock ~0 ~0 ~-3 minecraft:command_block[facing=north]
data modify block ~0 ~0 ~-3 Command set value "fill -12 22 84 -4 22 98 minecraft:air destroy"
setblock ~0 ~0 ~-4 minecraft:chain_command_block[facing=north]
data modify block ~0 ~0 ~-4 Command set value "kill @e[type=minecraft:item]"
setblock ~0 ~0 ~-5 minecraft:chain_command_block[facing=north]
data modify block ~0 ~0 ~-5 Command set value "summon minecraft:area_effect_cloud ~0 ~0 ~-1 {Tags:[\"TickCounter\"],Age:-10}"
setblock ~0 ~0 ~-6 minecraft:command_block[facing=north]
data modify block ~0 ~0 ~-6 Command set value "fill -12 18 84 -4 21 98 minecraft:air destroy"
setblock ~0 ~0 ~-7 minecraft:chain_command_block[facing=north]
data modify block ~0 ~0 ~-7 Command set value "kill @e[type=minecraft:item]"
setblock ~0 ~0 ~-8 minecraft:chain_command_block[facing=north]
data modify block ~0 ~0 ~-8 Command set value "summon minecraft:area_effect_cloud ~0 ~0 ~-1 {Tags:[\"TickCounter\"],Age:-10}"
setblock ~0 ~0 ~-9 minecraft:command_block[facing=north]
data modify block ~0 ~0 ~-9 Command set value "fill -12 14 84 -4 17 98 minecraft:air destroy"
setblock ~0 ~0 ~-10 minecraft:chain_command_block[facing=north]
data modify block ~0 ~0 ~-10 Command set value "kill @e[type=minecraft:item]"
setblock ~0 ~0 ~-11 minecraft:chain_command_block[facing=north]
data modify block ~0 ~0 ~-11 Command set value "summon minecraft:area_effect_cloud ~0 ~0 ~-1 {Tags:[\"TickCounter\"],Age:-10}"
setblock ~0 ~0 ~-12 minecraft:command_block[facing=north]
data modify block ~0 ~0 ~-12 Command set value "fill -12 10 84 -4 13 98 minecraft:air destroy"
setblock ~0 ~0 ~-13 minecraft:chain_command_block[facing=north]
data modify block ~0 ~0 ~-13 Command set value "kill @e[type=minecraft:item]"
setblock ~0 ~0 ~-14 minecraft:chain_command_block[facing=north]
data modify block ~0 ~0 ~-14 Command set value "summon minecraft:area_effect_cloud ~0 ~0 ~-1 {Tags:[\"TickCounter\"],Age:-10}"
