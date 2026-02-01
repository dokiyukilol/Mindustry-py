def mem_generator(mem, index, value):
    if mem == 1:
        if value == None:
            v = Mem.cell4[index]
            return v
        else:
            Mem.cell4[index] = value
    elif mem == 2:
        if value == None:
            v = Mem.cell2[index]
            return v
        else:
            Mem.cell2[index] = value
    elif mem == 3:
        if value == None:
            v = Mem.cell3[index]
            return v
        else:
            Mem.cell3[index] = value




def mem_set(mem,index,value):
    mem_generator(mem,index,value)

def mem_append(mem:str,value):
    nums = mem_generator(mem,0,None)+1
    mem_generator(mem,nums,value)
    mem_generator(mem,0,nums)
def mem_at(mem,index):
    return mem_generator(mem,index,None)
def mem_len(mem):
    return mem_generator(mem,0,None)
def mem_push_left(mem,push_left_value):
    mem_nums = mem_at(mem,0)
    mem_nums_i = mem_nums
    while mem_nums_i >= 1:
       r = mem_nums_i + 1
       l = mem_nums_i
       rv = mem_at(mem,r)
       lv = mem_at(mem,l)
       mem_set(mem,r,lv)
       mem_nums_i -= 1
    mem_set(mem,1,push_left_value)

def random_int(min_val, max_val):
    return floor(min_val + rand(max_val - min_val + 1))


snake_x = 40
snake_y = 40
snake_vec_x = 0
snake_vec_y = 0
snake_move_speed = 3
snake_len = 1 # 蛇的长度，可以用于确定移动时要擦除的轨迹

back_color_R = 0
back_color_G = 0
back_color_B = 0





# Mem.cell2 蛇的宽度为2，80的屏幕大小 40个格子 
# cell2 存蛇的x坐标，cell3存蛇的y坐标
# cell1 2,3 存苹果坐标  
# cell1 4,是否正在进行，0到1时初始化，1到0时清空屏幕并结束

def sqrt(value):
    return value ** 0.5
def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def moving_vector():
    up = switch1.enabled 
    down = switch2.enabled
    left = switch3.enabled
    right = switch4.enabled
    if up:
        snake_vec_x = 0
        snake_vec_y = 2
    elif down:
        snake_vec_y = -2
        snake_vec_x = 0
    elif left:
        snake_vec_x = -2
        snake_vec_y = 0
    elif right:
        snake_vec_x = 2
        snake_vec_y = 0
    switch1.enabled(0)
    switch2.enabled(0)
    switch3.enabled(0)
    switch4.enabled(0)


def draw_snake_body(x,y,w):
    Screen.color(0,255,0)
    Screen.rect(x,y,w,w)

    
def wape_snake_body():
    # 删除最后一个元素,需要再绘制新元素前进行
    last_snake_len = mem_at(2,0)+1
    last_x = mem_at(2,last_snake_len)
    last_y = mem_at(3,last_snake_len)
    
    Screen.color(back_color_R,back_color_G,back_color_B)
    Screen.rect(last_x,last_y,2,2)
def is_snake_body(x,y):
    last_snake_len = mem_at(2,0)
    for i in range(last_snake_len):
        index = i + 1
        last_x = mem_at(2,index)
        last_y = mem_at(3,index)
        if last_x == x and last_y == y:
            return True
    return False
def is_apple(x,y):
    apple_x = mem_at(1,2) == x
    apple_y = mem_at(1,3) == y 
    if apple_x and apple_y:
        return True
    return False
    
def kill_game():
    Screen.clear(255,back_color_G,back_color_B)
    Screen.flush()
    switch1.enabled(0)
    switch2.enabled(0)
    switch3.enabled(0)
    switch4.enabled(0)
    switch5.enabled(0)
    

def spwan_apple():  
    ax = random_int(0,80)
    if ax%2 != 0:
        if ax + 1 <= 80:
            ax += 1
        elif ax - 1 >= 0:
            ax -= 1
    apple_x = ax
    ax = random_int(0,80)
    if ax%2 != 0:
        if ax + 1 <= 80:
            ax += 1
        elif ax - 1 >= 0:
            ax -= 1
    apple_y = ax 

    if apple_x > 80:
        apple_x = 80
    if apple_y > 80:
        apple_y = 80
    if apple_x < 0:
        apple_x = 0
    if apple_y < 0:
        apple_y = 0
    mem_set(1,2,apple_x)
    mem_set(1,3,apple_y)
def draw_apple():
    apple_x = mem_at(1,2)
    apple_y = mem_at(1,3) 
    Screen.color(255,0,0)
    Screen.rect(apple_x,apple_y,2,2)



def start_game():
    Screen.clear(back_color_R,back_color_G,back_color_B)
    snake_len = 1
    snake_x = 40
    snake_y = 40
    spwan_apple()
    draw_apple()
    Screen.flush()
    mem_set(2,1,snake_x)
    mem_set(3,1,snake_y)
    mem_set(2,0,snake_len)
    mem_set(3,0,snake_len)
    mem_set(1,4,1)
    switch1.enabled(0)
    switch2.enabled(0)
    switch3.enabled(0)
    switch4.enabled(0)
    for i in range(30):
        mem_set(4,i,0)
    for i in range(30):
        mem_set(2,i,0)
    for i in range(30):
        mem_set(3,i,0)
    
    
# 计算运动向量
# 获取下一个移动坐标
# 在该位置绘图，并擦去一个轨迹
# 如果该位置有苹果，长度+1
# 如果该位置为蛇的轨迹，设置结束
if switch5.enabled == True:
    print("运行中")
    start_game()
    while True:
        if switch5.enabled == False:
            print(f"结束,最终分数 {snake_len}")
            kill_game()
            break
        moving_vector()
       # if snake_vec_x == 0 and snake_vec_y == 0:
        #    continue
        snake_x += snake_vec_x
        snake_y += snake_vec_y

        if snake_x > 80 or snake_y > 80 or snake_x < 0 or snake_y < 0 or is_snake_body(snake_x,snake_y):
            print(f"结束,最终分数 {snake_len}")
            kill_game()
            break
        else:
            mem_push_left(2,snake_x)
            mem_push_left(3,snake_y)
            if not is_apple(snake_x,snake_y):
                wape_snake_body()
            else:# 是苹果
                snake_len += 1
                mem_set(2,0,snake_len)
                mem_set(3,0,snake_len)
                spwan_apple()
                draw_apple()
                print(f"分数 {snake_len}")

            draw_snake_body(snake_x,snake_y,2)

            Screen.flush()
