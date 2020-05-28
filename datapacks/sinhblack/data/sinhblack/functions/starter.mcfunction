gamerule doMobSpawning false
gamerule doWeatherCycle false
kill @e[type=!minecraft:player]
kill @e[type=!minecraft:player]
kill @e[type=!minecraft:player]
kill @e[type=!minecraft:player]
kill @e[type=!minecraft:player]
kill @e[type=!minecraft:player]
kill @e[type=!minecraft:player]
kill @e[type=!minecraft:player]
tp @p 0 6 0
setblock 0 4 0 minecraft:diamond_block
setblock 1 4 0 minecraft:red_concrete
setblock 0 4 1 minecraft:blue_concrete
give @p minecraft:grass_block
give @p minecraft:redstone_block
give @p minecraft:command_block 64
spawnpoint @p 0 6 0
# Spawn command blocks
setblock -2 4 0 minecraft:repeating_command_block
setblock -2 4 -1 minecraft:chain_command_block
setblock -2 4 -2 minecraft:chain_command_block
data modify block -2 4 0 auto set value 1b
data modify block -2 4 0 Command set value "execute if entity @e[tag=TickCounter,nbt={Age:-1}] run tag @e[tag=TickCounter,nbt={Age:-1}] add TickTrigger"
data modify block -2 4 -1 Command set value "execute at @e[tag=TickTrigger] run data modify block ~ ~ ~ auto set value 1b"
data modify block -2 4 -2 Command set value "execute at @e[tag=TickTrigger] run data modify block ~ ~ ~ auto set value 0b"
