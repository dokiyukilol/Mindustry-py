copper = container1.copper
need_resources = copper == 0  # we're out of copper!

health = duo1.health / duo1.max_health
need_healing = health < 0.5  # less than 50% health!



print(f"{need_resources}")