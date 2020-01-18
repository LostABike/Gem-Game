player.onChat("delete", function () {
    blocks.fill(
    AIR,
    pos(0 - radius, 0, 0 - radius),
    pos(radius, 15, radius),
    FillOperation.Replace
    )
    blocks.fill(
    GRASS,
    pos(0 - radius, 0, 0 - radius),
    pos(radius, -1, radius),
    FillOperation.Replace
    )
})
loops.runInBackground(function () {
    while (true) {
        if (timer == 0) {
            player.say("Time's up! Your score is " + score)
            mobs.kill(
            mobs.entitiesByType(CHICKEN)
            )
            loops.pause(2000)
            player.runChatCommand("delete")
            break;
        }
        loops.pause(1000)
        timer += 0 - 1
    }
})
mobs.onMobKilled(CHICKEN, function () {
    score += 1
    player.say(list[Math.randomRange(0, 9)])
})
player.onChat("chicken", function () {
    timer = 75
    blocks.fill(
    BLOCK_OF_QUARTZ,
    pos(0 - radius, -1, 0 - radius),
    pos(radius, 12, 0 - radius),
    FillOperation.Replace
    )
    blocks.fill(
    BLOCK_OF_QUARTZ,
    pos(0 - radius, -1, radius),
    pos(radius, 12, radius),
    FillOperation.Replace
    )
    blocks.fill(
    BLOCK_OF_QUARTZ,
    pos(0 - radius, -1, 0 - radius),
    pos(0 - radius, 12, radius),
    FillOperation.Replace
    )
    blocks.fill(
    BLOCK_OF_QUARTZ,
    pos(radius, -1, 0 - radius),
    pos(radius, 12, radius),
    FillOperation.Replace
    )
    blocks.fill(
    BLOCK_OF_QUARTZ,
    pos(0 - radius, -1, 0 - radius),
    pos(radius, -1, radius),
    FillOperation.Replace
    )
    blocks.fill(
    CYAN_STAINED_GLASS,
    pos(0 - radius, 12, 0 - radius),
    pos(radius, 12, radius),
    FillOperation.Replace
    )
    blocks.fill(
    NETHER_BRICK_FENCE,
    pos(-1, 0, -1),
    pos(1, 0, 1),
    FillOperation.Replace
    )
    shapes.circle(
    WATER,
    pos(0, -1, 0),
    6,
    Axis.Y,
    ShapeOperation.Outline
    )
    shapes.circle(
    LAVA,
    pos(0, -1, 0),
    8,
    Axis.Y,
    ShapeOperation.Outline
    )
    shapes.circle(
    BLOCK_OF_QUARTZ,
    pos(0, 3, 0),
    6,
    Axis.Y,
    ShapeOperation.Outline
    )
    mobs.teleportToPlayer(
    mobs.target(ALL_PLAYERS),
    mobs.target(LOCAL_PLAYER)
    )
    player.execute(
    "/clear @a"
    )
    player.execute(
    "/give @a bow"
    )
    player.execute(
    "/give @a arrow 100"
    )
    loops.pause(1000)
    player.say("You have 1 minute to shoot as many chickens as possible.")
    loops.pause(1000)
    player.say("Starting now!")
    while (timer > 0 && timer <= 60) {
        mobs.spawn(CHICKEN, positions.random(
        pos(0 - radius, 7, 0 - radius),
        pos(radius, 12, radius)
        ))
        loops.pause(1000)
    }
})
let score = 0
let radius = 0
let timer = 0
let list: string[] = []
list = ["Chicken slayer", "Head shot", "I didn't choose the chicken life", "KFC", "Popeyes", "Eggciting!", "Eggroll?", "Fry-day already", "Eggcellent!", "The chicken life chose me"]
timer = 70
radius = 13
