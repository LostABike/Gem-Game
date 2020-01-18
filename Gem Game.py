from mcpi.minecraft import Minecraft
from mcpi import block
import time
import random

mc = Minecraft.create("18.144.26.47", 4711)
# Please use your own username here
#player_id = mc.getPlayerEntityId("Coder10")
#player_pos = mc.entity.getPos(player_id)

x, y, z = mc.player.getPos()

#area inside the room that the gem will spawn
roomCoord1= (x-12, y, z)
roomCoord2= (x+11, y+7, z+37)

#setup the room surrounding player
for i in range(-15, 16):
    for j in range(-1, 12):
        for k in range(-2, 40):
            type = block.AIR.id
            if j == -1:
                type = block.WOOD_PLANKS.id
            if j == 11:
                type = block.GLASS_PANE.id
            elif i == -15 or i == 15:
                type = block.DIAMOND_BLOCK.id
            elif k == -2 or k == 39:
                type = block.BEDROCK.id
            mc.setBlock(x + i, y + j, z + k, type) 

n = 0
#set up stairs in the room
for j in range (0, 11):
    n+=1
    for i in range (-14, 11):
        for k in range (-1, 35):
            type = block.AIR.id
            if (n < 6):
                if (k%5 == 0 and i%5 == 0):
                    type = block.BEDROCK.id
                if (n == 5):
                    n = 0
    
            mc.setBlock(x+i+n, y+j, z+k+n, type)
            


find a block that is in possible space within the room
def findGoodBlock():
    while (True):
        i = random.randint(int(roomCoord1[0]), int(roomCoord2[0]))
        j = random.randint(int(roomCoord1[1]), int(roomCoord2[1]))
        k = random.randint(int(roomCoord1[2]), int(roomCoord2[2]))
        if (mc.getBlock(i, j, k) == block.AIR.id):
            return (i, j, k)


mc.postToChat("You have 2 minutes to collect 5 gems that will randomly spawn in this maze.")
time.sleep(2)
mc.postToChat("Be hasty! A gem will not last too long!")


gameState = True
score = 0
start_time = time.time()
gem = findGoodBlock()
mc.setBlock(gem[0], gem[1], gem[2], 133)
gem_time = start_time


#stage design of game logic
while (gameState):
    remaining_time = 120 - (time.time()- start_time)

    #if the gem is no longer there, player gets 1 score
    #the gem respawns somewhere else
    if (mc.getBlock(gem[0], gem[1], gem[2]) != 133):
        score+=1
        if (score != 5):
            mc.postToChat(str(5-score) + " more to go!")
            gem = findGoodBlock()
            mc.setBlock(gem[0], gem[1], gem[2], 133)
            gem_time = time.time()
        #if the player meets the objective in time,
        #they won and an exit door will open
        elif (score == 5):
            mc.postToChat("Congratulations! You won!")
            time.sleep(1)
            mc.postToChat("You are now free to exit this maze")
            #create exit
            mc.setBlocks(roomCoord2[0]-10, roomCoord2[1]-5, roomCoord2[2]+2, roomCoord2[0]-13, roomCoord2[1]-8, roomCoord2[2]+2, block.AIR.id)
            gameState = False

    #however if the gem is still there after 15s,
    #it respawns at a different location
    elif((time.time()-gem_time)>15):
        if (mc.getBlock(gem[0], gem[1], gem[2]) == 133):
            mc.setBlock(gem[0], gem[1], gem[2], block.AIR.id)
            gem = findGoodBlock()
            mc.setBlock(gem[0], gem[1], gem[2], 133)
            gem_time = time.time()


    if (59.9 < remaining_time <= 60):
        mc.postToChat("You have 1 minute left")
    
    if (19.9 < remaining_time <= 20):
        mc.postToChat("20 seconds!")

    if (4.9 < remaining_time <= 5):
        mc.postToChat("uh-oh...5 seconds")

    if (remaining_time < 0 and score != 5):
        mc.postToChat("You lost")
        time.sleep(1)
        mc.postToChat("Try again next time?")
        mc.setBlocks(roomCoord1[0]-2, roomCoord1[1]-1, roomCoord1[2]-1, roomCoord2[0]+3,roomCoord1[1]-1, roomCoord2[2]+1, block.LAVA.id)
        gameState = False





