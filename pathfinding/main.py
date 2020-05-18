import numpy as np
import pygame
import os, sys, time
from pygame.constants import QUIT, K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN, MOUSEBUTTONUP, K_SPACE
import pygame.sprite as spriteclass


SCREEN_SIZE = (1200, 768)
os.environ['SDL_VIDEO_CENTERED'] = '1'


class BgImage(spriteclass.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.bg_image = pygame.image.load("bg.png").convert_alpha()
        self.rect = self.bg_image.get_rect()

        # return (self.bg_image)

    def ret_bg(self):
        return (self.rect)


class Wall(spriteclass.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("wall_block.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    def retLoc(self):
        return self.rect.x, self.rect.y

    def retSize(self):
        return self.image.get_size()


class Robot(spriteclass.Sprite):
    def __init__(self, pos):
        # initialize Sprite class
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.image.load("robot.jpeg").convert_alpha()
        self.image = self.original_image
        self.image = pygame.transform.scale(self.image, (30, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    # this returns the coordinates of the upper left corner of the robot
    def retLoc(self):
        return self.rect.x, self.rect.y

    # this returns the coordinates of the
    def retLocCenter(self):
        return self.rect.topleft

    # dims of the sprite
    def retSize(self):
        return self.image.get_size()

    # center the sprite
    def NewPos(self, pos):
        self.rect.center = pos

    # get the route and move the robot
    def moveRobot(self, dir, step):
        if dir == 'right':
            self.rect.x += step
            self.image = pygame.transform.rotate(self.original_image, 270)
            self.image = pygame.transform.scale(self.image, (30, 32))
        elif dir == 'left':
            self.rect.x -= step
            self.image = pygame.transform.rotate(self.original_image, 90)
            self.image = pygame.transform.scale(self.image, (30, 32))
        elif dir == "up":
            self.rect.y -= step
            self.image = self.original_image
            self.image = pygame.transform.scale(self.image, (30, 32))
        elif dir == "down":
            self.rect.y += step
            self.image = pygame.transform.rotate(self.original_image, 180)
            self.image = pygame.transform.scale(self.image, (30, 32))


class Target(spriteclass.Sprite):
    def __init__(self, loc):
        spriteclass.Sprite.__init__(self)
        self.image = pygame.image.load("target.png")
        self.image = pygame.transform.scale(self.image, (30, 32))
        self.rect = self.image.get_rect()
        self.rect.topleft = loc

    def NewPos(self, pos):
        self.rect.x = pos[0] - self.image.get_size()[0] / 2
        self.rect.y = pos[1] - self.image.get_size()[1] / 2

    def retLoc(self):
        return self.rect.x, self.rect.y

    def retLocCenter(self):
        return self.rect.center

    def retSize(self):
        return self.image.get_size()


class Grid(object):
    def __init__(self, screensize):
        self.image = pygame.image.load("wall_block.png").convert_alpha()
        self.grid = self.image.get_size()
        self.screensize = screensize

    # construct the grid along x axis
    def getXGrid(self):
        self.xrange = []
        t = 0
        while (t * self.grid[0] < self.screensize[0]):
            xval = t * self.grid[0]
            self.xrange.append(xval)
            t += 1

        self.xrange = np.asarray(self.xrange)
        return self.xrange

    # construct the grid along y axis
    def getYGrid(self):
        self.yrange = []
        s = 0
        while (s * self.grid[1] < self.screensize[1]):
            yval = s * self.grid[1]
            self.yrange.append(yval)
            s += 1

        self.yrange = np.asarray(self.yrange)
        return self.yrange

    # get the coordinates of the wall on the screen
    def getWallLoc(self, wallpos):
        self.true_xval = max(self.xrange[wallpos[0] > self.xrange])
        self.true_yval = max(self.yrange[wallpos[1] > self.yrange])
        return (self.true_xval, self.true_yval)

    # get the address of the wall in the matrix
    def retGridLoc(self, bingrid):
        self.binlocx = np.where(self.xrange == self.true_xval)
        self.binlocy = np.where(self.yrange == self.true_yval)
        return (self.binlocx, self.binlocy)


# A* pathfinding algorithm
# array with robot start location
# array with walls locations
# array with target/end location
def getPath(robotgrid, maingrid, targetgrid, screen):
    # array to store path locations
    direct_graph = {}
    # target location, returns a tuple
    target = np.where(targetgrid)
    # end location, returns locations
    start = np.where(robotgrid)
    # array of cost to travel so far
    g_cost_array = np.zeros(robotgrid.shape)
    g_cost_array[start] = 0
    total_g_cost = 0
    #array for heuristic cost
    h_cost_array = np.zeros(robotgrid.shape)
    #need to use a loop unfortunately...
    t = 0
    #possible steps
    steps = ((-1, 0), (+1, 0), (0, -1), (0, +1))
    for rows in h_cost_array:
        s = 0
        for cols in rows:
            #check if it's a wall! if not - get the distance to target
            loc = (t, s)
            if (maingrid[loc]):
                #pass: skip this element only
                #continue: the whole row
                pass
            else:
                dist = abs(target[0] - s) + abs(target[1] - t)
                h_cost_array[t, s] = dist
            s += 1
        t += 1
    #total cost =  f + g
    f_cost_array = g_cost_array + h_cost_array
    #closed and open sets
    open_set = []
    open_set.append(start)

    closed_set = []
    #actual path
    path = []
    path.append([tuple(target[0]), tuple(target[1])])
    solution_found = False
    while (open_set):
        open_f_cost = []
        #get the heuristic cost for the candidates in the open set
        for vals in open_set:
            open_f_cost.append(f_cost_array[vals])

        #the shortest heuristic now
        #the index of the candidate with the lowest distance/heuristic
        best_dist_now = open_f_cost.index(min(open_f_cost))
        #the current best position

        best_pos_now = open_set[best_dist_now]
        #if the destination is reached, finish!
        if (tuple(best_pos_now) == target):
            solution_found = True
            break
        else:
            #remove the best guy from the open_set and add it to the closed set
            closed_set.append(open_set.pop(best_dist_now))
            #analyze the steps from the current best

            for step in steps:
                cand = (best_pos_now[0] + step[0], best_pos_now[1] + step[1])
                #check if there's a wall or beyond the screen
                if cand[0] < 0 or cand[1] < 0 or cand[0] > 39 or cand[1] > 23:
                    #pass here, e.g. just proceed to the next candidate, not break out of the candidate loop
                    #because we're off the screen
                    pass
                #skip this candidate because it's a wall!
                elif maingrid[cand]:
                    pass
                #need an else clause here to weed out the off-screen locations
                else:
                    #check if the candidate is in the closed set
                    already_seen = False
                    for dead in closed_set:
                        if np.all(dead == cand):
                            already_seen = True
                            break
                    #if the cell is in the closed set, skip it
                    if already_seen:
                        pass
                    else:
                        approx_g_score = g_cost_array[best_pos_now] + 1
                        #check if it's in the open list:
                        new = True
                        for others in open_set:
                            if np.all(others == cand):
                                new = False
                                break
                        #if a new cell or improved
                        if (new or approx_g_score < g_cost_array[cand]):
                            direct_graph[tuple(cand[0]), tuple(cand[1])] = (
                                tuple(best_pos_now[0]), tuple(best_pos_now[1]))
                            g_cost_array[cand] = approx_g_score
                            f_cost_array[cand] = g_cost_array[cand] + h_cost_array[cand]
                        if new:
                            open_set.append(cand)

    if not solution_found:
        return None
    else:
        recurrentPath(path, direct_graph, target, start)

        return path


# takes a dictionary as input
def recurrentPath(final_path, raw_path, dest, origin):
    a = raw_path[tuple(dest[0]), tuple(dest[1])]
    final_path.append(a)
    if (a != origin):
        recurrentPath(final_path, raw_path, a, origin)
    else:
        return final_path

def set_sign(screen, write_3, write_3_size):
    screen.blit(write_3, (SCREEN_SIZE[0] / 2 - write_3_size[0] / 2, SCREEN_SIZE[1] - write_3_size[1]))

def main():
    clock = pygame.time.Clock()
    pygame.init()
    pygame.font.init()
    # set the font for text
    font_text = pygame.font.SysFont(None, 30)
    text_1 = "Selecció d'obstacles. Click SPACEBAR per acabar."
    text_2 = "Colocar el robot."
    text_3 = "Colocar el target. Click SPACEBAR per començar el A*"
    text_win = "FET!"
    text_fail = "La solució no existeix"
    text_astar = "Pensant..."
    write_1 = font_text.render(text_1, True, (0, 255, 0))
    write_2 = font_text.render(text_2, True, (0, 255, 0))
    write_3 = font_text.render(text_3, True, (0, 255, 0))
    write_fail = font_text.render(text_fail, True, (0, 255, 0))
    write_win=font_text.render(text_win, True, (0,255,0))
    write_astar = font_text.render(text_astar,True, (0,255,0))
    write_1_size = font_text.size(text_1)
    write_2_size = font_text.size(text_2)
    write_3_size = font_text.size(text_3)
    write_fail_size = font_text.size(text_fail)
    write_win_size = font_text.size(text_win)
    write_astar_size = font_text.size(text_astar)
    main_title = "iClean ROBOT pathfinding simulation"
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(main_title)
    bgimage = BgImage()

    wallsprite = pygame.sprite.RenderUpdates()
    targetGroup = pygame.sprite.RenderUpdates()

    pointer_robot = False
    pointer_target = False
    done_pointer = False
    done_locating = False
    distset = False
    input_on = False
    done_solving = False
    valid_path = False
    job_failed=False

    robot_for_mouse = Robot(pygame.mouse.get_pos())
    robotGroup = pygame.sprite.RenderUpdates()
    robotGroup.add(robot_for_mouse)
    robot_loc = []
    full_route = []
    grid = Grid(SCREEN_SIZE)
    xgrid = grid.getXGrid()
    ygrid = grid.getYGrid()
    maingrid = np.zeros([len(xgrid), len(ygrid)])
    wallgrid = []
    robotgrid = np.zeros([len(xgrid), len(ygrid)])
    targetgrid = np.zeros([len(xgrid), len(ygrid)])
    FPS = 60
    pygame.time.Clock()
    path_len = 0
    start = True
    
    # launch
    while (start):
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                #exit program
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)

                #find starting location for the robot
                elif (event.key == K_SPACE and not pointer_robot and not done_locating):
                    pointer_robot = True

                #finish locating, run A* pathfinder
                elif (event.key == K_SPACE and done_locating and distset):
                    input_on = True
                    distset = False
                    screen.blit(write_astar, (SCREEN_SIZE[0] / 2 - write_astar_size[0] / 2, SCREEN_SIZE[1] - write_astar_size[1]))
                    #robot_loc: coordinates of the upper left corner
                    #run the pathfinding heuristic algorithm; result is a tuple
                    full_route = getPath(robotgrid, maingrid, targetgrid, screen)

                    #check if the solution is found:
                    #if not, just say so!
                    if full_route is None:
                        job_failed=True
                    #if it is, input the path into the spacecraft movement method
                    else:
                        draw_line=True
                        valid_path = True
                        path = full_route[::-1]
                        path_reduce = full_route[::-1]
                        path_reduce.pop(0)
                        path_len = len(path) - 1
                        z_loc = 0

            #set walls
            elif (event.type == MOUSEBUTTONDOWN and event.button == 1 and not pointer_robot and not done_locating):
                pos = pygame.mouse.get_pos()
                wallpos = grid.getWallLoc(pos)
                this_grid_loc = grid.retGridLoc(maingrid)

                #if the grid is available for the wall
                if not maingrid[this_grid_loc]:
                    maingrid[this_grid_loc] = 1
                    wall = Wall(wallpos)
                    wallsprite.add(wall)
                    #store the location of the vertex
                    wallgrid.append(wallpos)
                else:
                    maingrid[this_grid_loc] = 0
                    j = 0
                    for j in range(len(wallgrid)):
                        if wallgrid[j] == wallpos:
                            wallgrid.remove(wallpos)
                            break

                    for walls in wallsprite:

                        posThis = walls.retLoc()
                        if (posThis[0] == wallpos[0] and posThis[1] == wallpos[1]):
                            wallsprite.remove(walls)
                            break

            #delete all wallblocks
            elif (event.type == MOUSEBUTTONDOWN and event.button == 3 and not pointer_robot and not done_locating):
                if wallsprite:
                    wallsprite.empty()
                    maingrid = np.zeros([len(xgrid), len(ygrid)])
                    wallgrid = []

            #put the target(after I've moved it around as a mousepointer
            elif event.type == MOUSEBUTTONDOWN and event.button and done_locating and pointer_target:
                pos = pygame.mouse.get_pos()
                targetpos = grid.getWallLoc(pos)
                target_grid_loc = grid.retGridLoc(targetpos)

                canFinish = True
                for walls in wallsprite:
                    if pygame.sprite.spritecollide(walls, targetGroup, False):
                        canFinish = False
                        break

                for robots in robotGroup:
                    if pygame.sprite.spritecollide(robots, targetGroup, False):
                        canFinish = False
                        break

                #valid location
                if canFinish:
                    pointer_target = False
                    targetgrid[target_grid_loc] = 1
                    target = Target(targetpos)
                    final_dest = targetpos
                    targetGroup.remove(target_mouse)
                    targetGroup.add(target)
                    distset = True
                    pygame.mouse.set_visible(1)

            #set a robot on the screen
            elif (event.type == MOUSEBUTTONDOWN and event.button and pointer_robot):
                #get the mouse poisiton
                pos = pygame.mouse.get_pos()
                #clamp the position to the grid
                robotpos = grid.getWallLoc(pos)
                #get the matrix element
                robot_grid_loc = grid.retGridLoc(robotgrid)
                robot = Robot(robotpos)
                canFinish = True

                for walls in wallsprite:
                    if pygame.sprite.spritecollide(walls, robotGroup, False):
                        canFinish = False
                        break

                #valid location
                if canFinish:
                    robotGroup.remove(robot_for_mouse)
                    robotGroup.add(robot)
                    done_locating = True
                    pointer_robot = False
                    robotgrid[robot_grid_loc] = 1
                    pointer_target = True
                    target_mouse = Target(pygame.mouse.get_pos())
                    targetGroup.add(target_mouse)

        #this runs all the time
        screen.blit(bgimage.bg_image, (0, 0))
        if pointer_robot:
            screen.blit(write_2, (SCREEN_SIZE[0] / 2 - write_2_size[0] / 2, SCREEN_SIZE[1] - write_2_size[1]))
            if (0 < pygame.mouse.get_pos()[0] < SCREEN_SIZE[0] and 0 < pygame.mouse.get_pos()[1] < SCREEN_SIZE[1]):
                pygame.mouse.set_visible(0)
                robot_for_mouse.NewPos(pygame.mouse.get_pos())
                robotGroup.update()
                robotGroup.draw(screen)

        if not done_locating and not pointer_robot:
            screen.blit(write_1, (SCREEN_SIZE[0] / 2 - write_1_size[0] / 2, SCREEN_SIZE[1] - write_1_size[1]))

        if done_locating:
            robotGroup.update()
            robotGroup.draw(screen)

        if pointer_target:
            set_sign(screen, write_3, write_3_size)
            target_mouse.NewPos(pygame.mouse.get_pos())
            targetGroup.update()
            targetGroup.draw(screen)

        if done_pointer:
            targetGroup.update()
            targetGroup.draw(screen)

        if input_on or distset:
            targetGroup.update()
            targetGroup.draw(screen)

        if valid_path:

            if (path_len):
                #draw the path
                t=0
                next_dest = path_reduce[0]
                pygame.draw.aaline(screen,(0,255,0),(robot.retLoc()[0]+15, robot.retLoc()[1]+16), (next_dest[0][0]*30+15, next_dest[1][0]*32+16),1)
                while t<len(path_reduce)-1:
                    now_dest = path_reduce[t]
                    next_dest = path_reduce[t+1]
                    pygame.draw.aaline(screen,(0,255,0), (now_dest[0][0]*30 +15, now_dest[1][0]*32 + 16),(next_dest[0][0]*30+15, next_dest[1][0]*32+16))
                    t+=1

                #move the robot
                now_loc = path[z_loc]
                next_loc = path[z_loc + 1]
                diff = [next_loc[0][0] * 30 - robot.retLoc()[0], next_loc[1][0] * 32 - robot.retLoc()[1]]

                #move right
                if diff[0] > 0 and diff[1] == 0:
                    robot.moveRobot('right', 2)
                    diff[0] -= 1
                elif diff[0] < 0 and diff[1] == 0:
                    robot.moveRobot('left', 2)
                    diff[0] += 1
                elif diff[1] > 0 and diff[0] == 0:
                    robot.moveRobot('down', 2)
                    diff[1] -= 1
                elif diff[1] < 0 and diff[0] == 0:
                    robot.moveRobot('up', 2)
                    diff[1] += 1
                elif diff[1] == 0 and diff[0] == 0:
                    z_loc += 1
                    path_len -= 1
                    path_reduce.pop(0)

            robotGroup.update()
            robotGroup.draw(screen)
            if not path_len:
                screen.blit(write_win, (SCREEN_SIZE[0] / 2 - write_win_size[0] / 2, SCREEN_SIZE[1] - write_win_size[1]))

        if job_failed:
            screen.blit(write_fail, (SCREEN_SIZE[0] / 2 - write_fail_size[0] / 2, SCREEN_SIZE[1] - write_fail_size[1]))

        wallsprite.update()
        wallsprite.draw(screen)



        pygame.display.flip()


if __name__ == "__main__":
    main()