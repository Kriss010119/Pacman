import pyray
from raylib import colors
import datetime
import random

class Settings:
    WIDTH = 900
    HEIGHT = 900


class Ghost:
    def __init__(self, x, y, radius, color,pacmen,elf,kto):
        f = open('field.txt', 'r')
        self.pole = f.readlines()
        self.image = pyray.load_image(elf)
        self.texture = pyray.load_texture_from_image(self.image)
        pyray.unload_image(self.image)
        del self.image
        self.image2 = pyray.load_image('image/pryanik1.png')
        self.texture1 = pyray.load_texture_from_image(self.image2)
        pyray.unload_image(self.image2)
        del self.image2
        self.image2 = pyray.load_image('image/pryanik2.png')
        self.texture2 = pyray.load_texture_from_image(self.image2)
        pyray.unload_image(self.image2)
        del self.image2
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        self.pacmen = pacmen
        self.start = 0
        self.go = 1
        self.kto = kto
        self.solevoi = 0
        if kto == 0:
            self.pac_x = (self.pacmen.x - self.pacmen.radius)
            self.pac_y = self.pacmen.y
            self.kyda = 2
        if kto == 1:
            self.pac_x = (self.pacmen.x + self.pacmen.radius)
            self.pac_y = self.pacmen.y
            self.kyda = 0
        if kto == 2:
            self.pac_x = self.pacmen.x
            self.pac_y = self.pacmen.y + self.pacmen.radius
            self.kyda = 3
        if kto == 3:
            self.pac_x = self.pacmen.x
            self.pac_y = self.pacmen.y - self.pacmen.radius
            self.kyda = 2
    def draw(self):
        if self.solevoi == 0:
            pyray.draw_texture(self.texture,self.x, self.y, colors.WHITE)
        elif self.solevoi == 1:
            pyray.draw_texture(self.texture1,self.x, self.y, colors.WHITE)
        elif self.solevoi == 2:
            pyray.draw_texture(self.texture2,self.x, self.y, colors.DARKBROWN)
    def move(self):
        self.go+=1
        if self.solevoi == 0:
            self.go%=100
        elif self.solevoi == 1:
            self.go%=2
        elif self.solevoi == 2:
            self.go%=100000
        if self.kto == 0:
            if self.solevoi != 2:
                self.pac_x = (self.pacmen.x - self.pacmen.radius)
                self.pac_y = self.pacmen.y
            else:
                self.pac_x = 396
                self.pac_y = 396
        if self.kto == 1:
            if self.solevoi != 2:
                self.pac_x = (self.pacmen.x + self.pacmen.radius)
                self.pac_y = self.pacmen.y
            else:
                self.pac_x = 432
                self.pac_y = 396
        if self.kto == 2:
            if self.solevoi != 2:
                self.pac_x = self.pacmen.x
                self.pac_y = self.pacmen.y + self.pacmen.radius
            else:
                self.pac_x = 468
                self.pac_y = 396
        if self.kto == 3:
            if self.solevoi != 2:
                self.pac_x = self.pacmen.x
                self.pac_y = self.pacmen.y - self.pacmen.radius
            else:
                self.pac_x = 432
                self.pac_y = 432
        if self.go != 0 and not(self.x - self.pac_x == 0 and self.y - self.pac_y == 0):
            if self.start == 0 and self.kto == 0:
                if self.x == 254 and self.y == 324:
                    self.start = 1
                if self.start == 0 and self.y > 324:
                    self.y-=1
                elif self.start == 0 and self.x > 252:
                    self.x-=1
            elif self.start == 0 and self.kto == 1:
                if self.x == 612 and self.y == 324:
                    self.start = 1
                if self.start == 0 and self.y > 324:
                    self.y-=1
                elif self.start == 0 and self.x < 612:
                    self.x+=1
            elif self.start == 0 and self.kto == 2:
                if self.y == 310:
                    self.start = 1
                else:
                    self.y-=1
            elif self.start == 0 and self.kto == 3:
                if self.x == 240 and self.y == 324:
                    self.start = 1
                if self.start == 0 and self.y > 324:
                    self.y-=1
                elif self.start == 0 and self.x > 240:
                    self.x-=1
            else:
                if self.pole[(self.y+18)//36][(self.x+18)//36] == '4' or self.pole[(self.y+18)//36][(self.x+18)//36] == '3':
                    i = 0
                    varic = [-1,-1,-1]
                    colvo = 0
                    ky = -1
                    if ((self.pole[self.y//36][(self.x//36)+1] == '0' and self.pole[(self.y+self.radius-1)//36][(self.x//36)+1] == '0') or (self.pole[self.y//36][(self.x//36)+1] == '4' and self.pole[(self.y+self.radius-1)//36][(self.x//36)+1] == '4') or (self.pole[self.y//36][(self.x//36)+1] == '5' and self.pole[(self.y+self.radius-1)//36][(self.x//36)+1] == '5') or (self.solevoi == 2 and self.pole[self.y//36][(self.x//36)+1] == '3' and self.pole[(self.y+self.radius-1)//36][(self.x//36)+1] == '3')) and self.kyda != 2:
                        varic[i] = 0
                        i+=1
                    if ((self.pole[(self.y//36)+1][self.x//36] == '0' and self.pole[(self.y//36)+1][(self.x+self.radius-1)//36] == '0') or (self.pole[(self.y//36)+1][self.x//36] == '4' and self.pole[(self.y//36)+1][(self.x+self.radius-1)//36] == '4') or (self.pole[(self.y//36)+1][self.x//36] == '5' and self.pole[(self.y//36)+1][(self.x+self.radius-1)//36] == '5') or (self.solevoi == 2 and self.pole[(self.y//36)+1][self.x//36] == '3' and self.pole[(self.y//36)+1][(self.x+self.radius-1)//36] == '3')) and self.kyda != 3:
                        varic[i] = 1
                        i+=1
                    if ((self.pole[(self.y)//36][((self.x+self.radius-1)//36)-1] == '0' and self.pole[(self.y+self.radius-1)//36][((self.x+self.radius-1)//36)-1] == '0')or(self.pole[(self.y)//36][((self.x+self.radius-1)//36)-1] == '4' and self.pole[(self.y+self.radius-1)//36][((self.x+self.radius-1)//36)-1] == '4')or(self.pole[(self.y)//36][((self.x+self.radius-1)//36)-1] == '5' and self.pole[(self.y+self.radius-1)//36][((self.x+self.radius-1)//36)-1] == '5') or (self.solevoi == 2 and self.pole[(self.y)//36][((self.x+self.radius-1)//36)-1] == '3' and self.pole[(self.y+self.radius-1)//36][((self.x+self.radius-1)//36)-1] == '3')) and self.kyda != 0:
                        varic[i] = 2
                        i+=1
                    if ((self.pole[((self.y+self.radius-1)//36)-1][(self.x)//36] == '0' and self.pole[((self.y+35)//36)-1][(self.x+self.radius-1)//36] == '0') or (self.pole[((self.y+self.radius-1)//36)-1][(self.x)//36] == '4' and self.pole[((self.y+35)//36)-1][(self.x+self.radius-1)//36] == '4') or (self.pole[((self.y+self.radius-1)//36)-1][(self.x)//36] == '5' and self.pole[((self.y+35)//36)-1][(self.x+self.radius-1)//36] == '5') or (self.solevoi == 2 and self.pole[((self.y+self.radius-1)//36)-1][(self.x)//36] == '3' and self.pole[((self.y+35)//36)-1][(self.x+self.radius-1)//36] == '3')) and self.kyda != 1:
                        varic[i] = 3
                        i+=1
                    if (varic[0] == 0 and varic[1] == 2):
                        if self.x - self.pac_x >= 0 and self.solevoi != 1 or self.x - self.pac_x < 0 and self.solevoi == 1:
                            varic[0] = -1
                        if self.x - self.pac_x < 0 and self.solevoi != 1 or self.x - self.pac_x >= 0 and self.solevoi == 1:
                            varic[1] = -1
                    if (varic[0] == 0 and varic[2] == 2):
                        if self.x - self.pac_x >= 0 and self.solevoi != 1 or self.x - self.pac_x < 0 and self.solevoi == 1:
                            varic[0] = -1
                        if self.x - self.pac_x < 0 and self.solevoi != 1 or self.x - self.pac_x >= 0 and self.solevoi == 1:
                            varic[2] = -1
                    if (varic[1] == 0 and varic[2] == 2):
                        if self.x - self.pac_x >= 0 and self.solevoi != 1 or self.x - self.pac_x < 0 and self.solevoi == 1:
                            varic[1] = -1
                        if self.x - self.pac_x < 0 and self.solevoi != 1 or self.x - self.pac_x >= 0 and self.solevoi == 1:
                            varic[2] = -1

                    if (varic[0] == 1 and varic[1] == 3):
                        if self.y - self.pac_y >= 0 and self.solevoi != 1 or self.y - self.pac_y < 0 and self.solevoi == 1:
                            varic[0] = -1
                        if self.y - self.pac_y < 0 and self.solevoi != 1 or self.y - self.pac_y >= 0 and self.solevoi == 1:
                            varic[1] = -1
                    if (varic[0] == 1 and varic[2] == 3):
                        if self.y - self.pac_y >= 0 and self.solevoi != 1 or self.y - self.pac_y < 0 and self.solevoi == 1:
                            varic[0] = -1
                        if self.y - self.pac_y < 0 and self.solevoi != 1 or self.y - self.pac_y >= 0 and self.solevoi == 1:
                            varic[2] = -1
                    if (varic[1] == 1 and varic[2] == 3):
                        if self.y - self.pac_y >= 0 and self.solevoi != 1 or self.y - self.pac_y < 0 and self.solevoi == 1:
                            varic[1] = -1
                        if self.y - self.pac_y < 0 and self.solevoi != 1 or self.y - self.pac_y >= 0 and self.solevoi == 1:
                            varic[2] = -1
                    for i in varic:
                        if i != -1:
                            colvo+=1
                            ky = i
                    if colvo == 1:
                        self.kyda = ky
                    else:
                        if 0 in varic and 1 in varic:
                            if self.x - self.pac_x >= 0 and self.y - self.pac_y <= 0:
                                if self.solevoi != 1:
                                    self.kyda = 1
                                else:
                                    self.kyda = 0
                            if self.x - self.pac_x <= 0 and self.y - self.pac_y >= 0:
                                if self.solevoi != 1:
                                    self.kyda = 0
                                else:
                                    self.kyda = 1
                            elif (self.x - self.pac_x) <= (self.y - self.pac_y):
                                if self.solevoi != 1:
                                    self.kyda = 0
                                else:
                                    self.kyda = 1
                            elif (self.x - self.pac_x) >= (self.y - self.pac_y):
                                if self.solevoi != 1:
                                    self.kyda = 1
                                else:
                                    self.kyda = 0
                        if 2 in varic and 1 in varic:
                            if self.x - self.pac_x >= 0 and self.y - self.pac_y >= 0:
                                if self.solevoi != 1:
                                    self.kyda = 2
                                else:
                                    self.kyda = 1
                            if self.x - self.pac_x <= 0 and self.y - self.pac_y <= 0:
                                if self.solevoi != 1:
                                    self.kyda = 1
                                else:
                                    self.kyda = 2
                            elif (self.x - self.pac_x)*-1 <= (self.y - self.pac_y):
                                if self.solevoi != 1:
                                    self.kyda = 2
                                else:
                                    self.kyda = 1
                            elif (self.x - self.pac_x)*-1 >= (self.y - self.pac_y):
                                if self.solevoi != 1:
                                    self.kyda = 1
                                else:
                                    self.kyda = 2
                        if 2 in varic and 3 in varic:
                            if self.x - self.pac_x >= 0 and self.y - self.pac_y <= 0:
                                if self.solevoi != 1:
                                    self.kyda = 2
                                else:
                                    self.kyda = 3
                            if self.x - self.pac_x <= 0 and self.y - self.pac_y >= 0:
                                if self.solevoi != 1:
                                    self.kyda = 3
                                else:
                                    self.kyda = 2
                            elif (self.x - self.pac_x) <= (self.y - self.pac_y):
                                if self.solevoi != 1:
                                    self.kyda = 3
                                else:
                                    self.kyda = 2
                            elif (self.x - self.pac_x) >= (self.y - self.pac_y):
                                if self.solevoi != 1:
                                    self.kyda = 2
                                else:
                                    self.kyda = 3
                        if 0 in varic and 3 in varic:
                            if self.x - self.pac_x >= 0 and self.y - self.pac_y >= 0:
                                if self.solevoi != 1:
                                    self.kyda = 3
                                else:
                                    self.kyda = 0
                            if self.x - self.pac_x < 0 and self.y - self.pac_y < 0:
                                if self.solevoi != 1:
                                    self.kyda = 0
                                else:
                                    self.kyda = 3
                            elif (self.x - self.pac_x)*-1 <= (self.y - self.pac_y):
                                if self.solevoi != 1:
                                    self.kyda = 3
                                else:
                                    self.kyda = 0
                            elif (self.x - self.pac_x)*-1 > (self.y - self.pac_y):
                                if self.solevoi != 1:
                                    self.kyda = 0
                                else:
                                    self.kyda = 3
                if self.kyda == 0:
                    self.x +=1
                if self.kyda == 1:
                    self.y +=1
                if self.kyda == 2:
                    self.x -=1
                if self.kyda == 3:
                    self.y -=1
        elif self.x - self.pac_x == 0 and self.y - self.pac_y == 0 and self.solevoi == 2:
            self.solevoi = 0
            if self.kto == 0:
                self.pac_x = (self.pacmen.x - self.pacmen.radius)
                self.pac_y = self.pacmen.y
                self.kyda = 2
            if self.kto == 1:
                self.pac_x = (self.pacmen.x + self.pacmen.radius)
                self.pac_y = self.pacmen.y
                self.kyda = 0
            if self.kto == 2:
                self.pac_x = self.pacmen.x
                self.pac_y = self.pacmen.y + self.pacmen.radius
                self.kyda = 3
            if self.kto == 3:
                self.pac_x = self.pacmen.x
                self.pac_y = self.pacmen.y - self.pacmen.radius
                self.kyda = 2
            self.start = 0
        if collision(self.pacmen,self) == True and self.solevoi == 1:
            self.solevoi = 2
            return 1
        return 0

    def sol(self):
    	if self.solevoi == 0:
    		self.solevoi = 1
    		self.kyda = (self.kyda+2)%4
    def sol1(self):
    	if self.solevoi == 1:
	    	self.solevoi = 0
	    	self.kyda = (self.kyda+2)%4


class Pacman:
    def __init__(self, x, y, radius, color):
        f = open('field.txt', 'r')
        self.pole = f.readlines()
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        self.kyda = 0
        self.image = pyray.load_image('image/pacmen0.png')
        self.texture_0 = pyray.load_texture_from_image(self.image)
        pyray.unload_image(self.image)
        del self.image
        self.image = pyray.load_image('image/pacmen1.png')
        self.texture_1 = pyray.load_texture_from_image(self.image)
        pyray.unload_image(self.image)
        del self.image
        self.image = pyray.load_image('image/pacmen2.png')
        self.texture_2 = pyray.load_texture_from_image(self.image)
        pyray.unload_image(self.image)
        del self.image
        self.image = pyray.load_image('image/pacmen3.png')
        self.texture_3 = pyray.load_texture_from_image(self.image)
        pyray.unload_image(self.image)
        del self.image
        self.image = pyray.load_image('image/pacmen0_1.png')
        self.texture_0_1 = pyray.load_texture_from_image(self.image)
        pyray.unload_image(self.image)
        del self.image
        self.image = pyray.load_image('image/pacmen1_1.png')
        self.texture_1_1 = pyray.load_texture_from_image(self.image)
        pyray.unload_image(self.image)
        del self.image
        self.image = pyray.load_image('image/pacmen2_1.png')
        self.texture_2_1 = pyray.load_texture_from_image(self.image)
        pyray.unload_image(self.image)
        del self.image
        self.image = pyray.load_image('image/pacmen3_1.png')
        self.texture_3_1 = pyray.load_texture_from_image(self.image)
        pyray.unload_image(self.image)
        del self.image
        self.texture = self.texture_3
        self.start_time = datetime.datetime.now()

    def draw(self):
        pyray.draw_rectangle(self.x, self.y,self.radius,self.radius, colors.BLACK)
        pyray.draw_texture(self.texture,self.x, self.y, colors.WHITE)

    def move(self):
        if (self.x < 36 or self.x > 828) and self.kyda == 0:
            self.x-=1
            if self.x < -36:
                self.x = 900
        elif (self.x < 36 or self.x > 828) and self.kyda == 1:
            self.x+=1
            if self.x > 900:
                self.x = -36
        else:
            if pyray.is_key_down(pyray.KeyboardKey.KEY_A) and ((self.pole[(self.y)//36][((self.x+self.radius-1)//36)-1] == '0' and self.pole[(self.y+self.radius-1)//36][((self.x+self.radius-1)//36)-1] == '0')or(self.pole[(self.y)//36][((self.x+self.radius-1)//36)-1] == '2' and self.pole[(self.y+self.radius-1)//36][((self.x+self.radius-1)//36)-1] == '2')or(self.pole[(self.y)//36][((self.x+self.radius-1)//36)-1] == '4' and self.pole[(self.y+self.radius-1)//36][((self.x+self.radius-1)//36)-1] == '4')or(self.pole[(self.y)//36][((self.x+self.radius-1)//36)-1] == '5' and self.pole[(self.y+self.radius-1)//36][((self.x+self.radius-1)//36)-1] == '5')):
                self.x -= 1
                self.kyda = 0
                if (self.start_time - datetime.datetime.now()).microseconds % 1000000 <= 500000 or (self.start_time - datetime.datetime.now()).microseconds % 1000000 >= 750000:
                    self.texture = self.texture_2
                else:
                    self.texture = self.texture_2_1
            if pyray.is_key_down(pyray.KeyboardKey.KEY_D) and ((self.pole[self.y//36][(self.x//36)+1] == '0' and self.pole[(self.y+self.radius-1)//36][(self.x//36)+1] == '0') or (self.pole[self.y//36][(self.x//36)+1] == '2' and self.pole[(self.y+self.radius-1)//36][(self.x//36)+1] == '2') or (self.pole[self.y//36][(self.x//36)+1] == '4' and self.pole[(self.y+self.radius-1)//36][(self.x//36)+1] == '4') or (self.pole[self.y//36][(self.x//36)+1] == '5' and self.pole[(self.y+self.radius-1)//36][(self.x//36)+1] == '5')):
                self.x += 1
                self.kyda = 1
                if (self.start_time - datetime.datetime.now()).microseconds % 1000000 <= 500000 or (self.start_time - datetime.datetime.now()).microseconds % 1000000 >= 750000:
                    self.texture = self.texture_0
                else:
                    self.texture = self.texture_0_1
            if pyray.is_key_down(pyray.KeyboardKey.KEY_W) and ((self.pole[((self.y+self.radius-1)//36)-1][(self.x)//36] == '0' and self.pole[((self.y+35)//36)-1][(self.x+self.radius-1)//36] == '0') or (self.pole[((self.y+self.radius-1)//36)-1][(self.x)//36] == '4' and self.pole[((self.y+35)//36)-1][(self.x+self.radius-1)//36] == '4') or (self.pole[((self.y+self.radius-1)//36)-1][(self.x)//36] == '5' and self.pole[((self.y+35)//36)-1][(self.x+self.radius-1)//36] == '5')):
                self.y -= 1
                if (self.start_time - datetime.datetime.now()).microseconds % 1000000 <= 500000 or (self.start_time - datetime.datetime.now()).microseconds % 1000000 >= 750000:
                    self.texture = self.texture_3
                else:
                    self.texture = self.texture_3_1
            if pyray.is_key_down(pyray.KeyboardKey.KEY_S) and ((self.pole[(self.y//36)+1][self.x//36] == '0' and self.pole[(self.y//36)+1][(self.x+self.radius-1)//36] == '0') or (self.pole[(self.y//36)+1][self.x//36] == '4' and self.pole[(self.y//36)+1][(self.x+self.radius-1)//36] == '4') or (self.pole[(self.y//36)+1][self.x//36] == '5' and self.pole[(self.y//36)+1][(self.x+self.radius-1)//36] == '5')):
                self.y += 1
                if (self.start_time - datetime.datetime.now()).microseconds % 1000000 <= 250000 or (self.start_time - datetime.datetime.now()).microseconds % 1000000 >= 750000:
                    self.texture = self.texture_1
                else:
                    self.texture = self.texture_1_1

class Cell:
    def __init__(self, type, posX, posY):
        f = open('field.txt', 'r')
        self.pole = f.readlines()
        self.type = type
        self.posX = posX
        self.posY = posY
        self.weight = 36
        self.height = 36
        self.thickness = 6
        self.color = colors.BLACK
        if self.type == 'D':
            self.color = colors.DARKPURPLE
            self.type = '1'
        if self.type == 'G':
            self.color = colors.GREEN
            self.type = '1'
        if self.type == 'M':
            self.color = colors.MAGENTA
            self.type = '1'
        if self.type == 'Y':
            self.color = colors.YELLOW
            self.type = '1'
        if self.type == 'R':
            self.color = colors.RED
            self.type = '1'
        if self.type == 'S':
            self.color = colors.BLUE
            self.type = '1'

    def draw(self):
        if (self.type == '0' or self.type == '2' or self.type == '3' or self.type == '4' or self.type == '5'):
            pyray.draw_rectangle(self.posX, self.posY, self.weight, self.height, colors.BLACK)
        if (self.type == '1'):
            pyray.draw_rectangle(self.posX, self.posY, self.weight, self.height, colors.BLACK)
            if (self.posY//self.height) >= 1 :
                if self.pole[(self.posY//self.height)-1][self.posX//self.weight] == '0' or self.pole[(self.posY//self.height)-1][self.posX//self.weight] == '2' or self.pole[(self.posY//self.height)-1][self.posX//self.weight] == '3' or self.pole[(self.posY//self.height)-1][self.posX//self.weight] == '4' or self.pole[(self.posY//self.height)-1][self.posX//self.weight] == '5':
                    pyray.draw_rectangle(self.posX, self.posY, self.weight, self.thickness, self.color)
            else:
                pyray.draw_rectangle(self.posX, self.posY, self.weight, self.thickness, self.color)
            if (self.posX//self.weight) >= 1 :
                if self.pole[(self.posY//self.height)][self.posX//self.weight-1] == '0' or self.pole[(self.posY//self.height)][self.posX//self.weight-1] == '2' or self.pole[(self.posY//self.height)][self.posX//self.weight-1] == '3' or self.pole[(self.posY//self.height)][self.posX//self.weight-1] == '4' or self.pole[(self.posY//self.height)][self.posX//self.weight-1] == '5':
                    pyray.draw_rectangle(self.posX, self.posY, self.thickness, self.height, self.color)
            else:
                pyray.draw_rectangle(self.posX, self.posY, self.thickness, self.height, self.color)
            if (self.posX//self.weight) < 24 :
                if self.pole[(self.posY//self.height)][self.posX//self.weight+1] == '0' or self.pole[(self.posY//self.height)][self.posX//self.weight+1] == '2' or self.pole[(self.posY//self.height)][self.posX//self.weight+1] == '3' or self.pole[(self.posY//self.height)][self.posX//self.weight+1] == '4' or self.pole[(self.posY//self.height)][self.posX//self.weight+1] == '5':
                    pyray.draw_rectangle(self.posX+self.weight-self.thickness, self.posY, self.thickness, self.height, self.color)
            else:
                pyray.draw_rectangle(self.posX+self.weight-self.thickness, self.posY, self.thickness, self.height, self.color)
            if (self.posY//self.height) < 24 :
                if self.pole[(self.posY//self.height)+1][self.posX//self.weight] == '0' or self.pole[(self.posY//self.height)+1][self.posX//self.weight] == '2' or self.pole[(self.posY//self.height)+1][self.posX//self.weight] == '3' or self.pole[(self.posY//self.height)+1][self.posX//self.weight] == '4' or self.pole[(self.posY//self.height)+1][self.posX//self.weight] == '5':
                    pyray.draw_rectangle(self.posX, self.posY+self.height-self.thickness, self.weight, self.thickness, self.color)
            else:
                pyray.draw_rectangle(self.posX, self.posY+self.height-self.thickness, self.weight, self.thickness, self.color)

class Seed:
    def __init__(self,centerX,centerY):
        self.image = pyray.load_image('image/konfeta.png')
        self.texture = pyray.load_texture_from_image(self.image)
        pyray.unload_image(self.image)
        del self.image
        self.centerX = centerX
        self.centerY = centerY
        self.visible = 1
        self.o = 1
    def draw(self):
        if self.visible == 1:
            pyray.draw_texture(self.texture,self.centerX-8,self.centerY-2,colors.WHITE)
    def colis(self,pac):
        if self.centerX >= pac.x and self.centerX <= pac.x+36 and self.centerY >= pac.y and self.centerY <= pac.y+36 and self.o == 1:
            self.visible = 0
            self.o = 0
            return 1
        return 0


class BigSeed:
    def __init__(self,centerX,centerY):
        self.image = pyray.load_image('image/bigkonfeta.png')
        self.texture = pyray.load_texture_from_image(self.image)
        pyray.unload_image(self.image)
        del self.image
        self.centerX = centerX
        self.centerY = centerY
        self.visible = 1
        self.o = 1
    def draw(self):
        if self.visible == 1:
            pyray.draw_texture(self.texture,self.centerX-18,self.centerY-7,colors.WHITE)
    def colis(self,pac):
        if self.centerX >= pac.x and self.centerX <= pac.x+36 and self.centerY >= pac.y and self.centerY <= pac.y+36 and self.o == 1:
            self.visible = 0
            self.o = 0
            return 1
        return 0

class Field:
    def __init__(self):
        f = open('field.txt', 'r')
        self.pole = f.readlines()
        self.cemki = []
        self.bigcemki = []
        o=0
        O=0
        for i in range(len(self.pole)):
            for j in range(len(self.pole[i])-1):
                if self.pole[i][j] == '0' or self.pole[i][j] == '4':
                    self.cemki.insert(o,Seed(j*36+18,i*36+18))
                    o+=1
                if self.pole[i][j] == '5':
                    self.bigcemki.insert(O,BigSeed(j*36+18,i*36+18))
                    O+=1

    def draw(self):
        for i in range(len(self.pole)):
            for j in range(len(self.pole[i])-1):
                Cell(self.pole[i][j],j*36,i*36).draw()

    def end(self):
        for i in self.cemki:
            if i.visible == 1:
                return 0
        return 1



class LiveDraw:
    def __init__(self, x, y, radius, color):
        self.yes_no = 1
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.image = pyray.load_image('image/life.png')
        self.texture = pyray.load_texture_from_image(self.image)
        pyray.unload_image(self.image)
        del self.image

    def draw(self):
        if self.yes_no == 1:
            pyray.draw_rectangle(self.x, self.y, self.radius, self.radius, colors.BLACK)
            pyray.draw_texture(self.texture, self.x + 1, self.y + 1, colors.WHITE)

    def deletee(self):
        pyray.draw_rectangle(self.x, self.y, self.radius, self.radius, colors.BLACK)
        self.yes_no = 0


class Cherry:
    def __init__(self,posX,posY):
        self.posX = posX
        self.posY = posY
        self.visible = 0
        self.image = pyray.load_image('image/podarok.png')
        self.texture = pyray.load_texture_from_image(self.image)
        pyray.unload_image(self.image)
        del self.image
        self.vremi = datetime.datetime.now()


    def draw(self):
        if self.visible == 1:
            pyray.draw_texture(self.texture,self.posX, self.posY, colors.WHITE)



def collision(pacman, ghoast):
    return pyray.check_collision_recs(pyray.Rectangle(pacman.x,pacman.y,pacman.radius,pacman.radius),pyray.Rectangle(ghoast.x+9,ghoast.y,ghoast.radius-18,ghoast.radius))

class GameScene:
    def __init__ (self):
        pyray.init_window(Settings.WIDTH, Settings.HEIGHT, "Game")
        pyray.set_target_fps(120)  # FPS
        self.pacman = Pacman(432, 828, 36, colors.YELLOW)
        self.blinkyGhost = Ghost(396,396,36,colors.RED,self.pacman,'image/elf1.png',0)
        self.pinkyGhost = Ghost(432,396,36,colors.PINK,self.pacman,'image/elf2.png',1)
        self.inkyGhost = Ghost(468,396,36,colors.BLUE,self.pacman,'image/elf3.png',2)
        self.clydeGhost = Ghost(432,432,36,colors.GOLD,self.pacman,'image/elf4.png',3)
        self.pole = Field()
        self.life_1 = LiveDraw(380, 436, 40, colors.RED)
        self.life_2 = LiveDraw(420, 436, 40, colors.RED)
        self.life_3 = LiveDraw(460, 436, 40, colors.RED)
        self.paused = 1
        self.image = pyray.load_image('image/Illustration.png')
        self.texture = pyray.load_texture_from_image(self.image)
        pyray.unload_image(self.image)
        del self.image
        pyray.clear_background(colors.BLACK)
        self.pole.draw()
        self.vremia = datetime.datetime.now()
        self.o = 1
        self.score = 0
        file_records = open('records.txt', 'r+')
        self.max_score = file_records.readline()
        file_records.close()
        self.cherry = Cherry(900, 900)
    def start_game (self):
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_R):
            self.pacman = Pacman(432, 828, 36, colors.YELLOW)
            self.blinkyGhost = Ghost(396,396,36,colors.RED,self.pacman,'image/elf1.png',0)
            self.pinkyGhost = Ghost(432,396,36,colors.PINK,self.pacman,'image/elf2.png',1)
            self.inkyGhost = Ghost(468,396,36,colors.BLUE,self.pacman,'image/elf3.png',2)
            self.clydeGhost = Ghost(432,432,36,colors.GOLD,self.pacman,'image/elf4.png',3)
            self.pole = Field()
            self.life_1 = LiveDraw(380, 436, 40, colors.RED)
            self.life_2 = LiveDraw(420, 436, 40, colors.RED)
            self.life_3 = LiveDraw(460, 436, 40, colors.RED)
            self.paused = 1
            self.pole.draw()
            self.vremia = datetime.datetime.now()
            self.o = 1
            self.score = 0
        if pyray.is_key_pressed(pyray.KeyboardKey.KEY_P):
            if self.score > int(self.max_score):
                self.max_score = self.score
                file_records = open('records.txt', 'r+')
                file_records.flush()
                file_records.write(str(self.score))
                file_records.close()

            self.paused *=-1
            self.pole.draw()
            for i in self.pole.cemki:
                i.draw()
            for i in self.pole.bigcemki:
                i.draw()
            self.pacman.draw()
            self.blinkyGhost.draw()
            self.pinkyGhost.draw()
            self.inkyGhost.draw()
            self.clydeGhost.draw()
            self.life_1.draw()
            self.life_2.draw()
            self.life_3.draw()
            pyray.draw_rectangle(378,468,190,36,colors.BLACK)
            pyray.draw_text(f'score:{self.score}',326,468,36,colors.WHITE)
        if self.paused == 1:#HERE IS NOT A PAUSE
            if int(random.random()*1000)%1000 == 0 and self.cherry.visible == 0:
                ran1 = int(random.random()*1000) % 25
                ran2 = int(random.random()*1000) % 25
                while self.pole.pole[ran2][ran1] != '0' and self.pole.pole[ran2][ran1] != '4':
                    ran1 = int(random.random()*1000) % 25
                    ran2 = int(random.random()*1000) % 25
                pyray.draw_rectangle(self.cherry.posX,self.cherry.posY,36,36,colors.BLACK)
                self.cherry = Cherry(ran1*36,ran2*36)
                self.cherry.visible = 1
                self.cherry.vremi = datetime.datetime.now()
            if (datetime.datetime.now() - self.cherry.vremi).seconds >= 30:
                self.cherry.visible = 0
                pyray.draw_rectangle(self.cherry.posX,self.cherry.posY,36,36,colors.BLACK)
            if pyray.check_collision_recs(pyray.Rectangle(self.pacman.x,self.pacman.y,self.pacman.radius,self.pacman.radius),pyray.Rectangle(self.cherry.posX,self.cherry.posY,36,36)) and self.cherry.visible == 1:
                self.cherry.visible = 0
                self.score += 150
            for i in self.pole.cemki:
                i.draw()
                if i.colis(self.pacman) == 1:
                    self.score += 1
            for i in self.pole.bigcemki:
                i.draw()
                if i.colis(self.pacman) == 1:
                    self.blinkyGhost.sol()
                    self.pinkyGhost.sol()
                    self.inkyGhost.sol()
                    self.clydeGhost.sol()
                    self.vremia = datetime.datetime.now()
                    self.o = 0
            if self.o == 0:
                pyray.draw_text(str(5-(datetime.datetime.now() - self.vremia).seconds),328+36*(datetime.datetime.now() - self.vremia).seconds,400,36,colors.WHITE)
            if (datetime.datetime.now() - self.vremia).seconds >= 5 and self.o == 0:
                pyray.draw_rectangle(328,400,36*6,36,colors.BLACK)
                self.blinkyGhost.sol1()
                self.pinkyGhost.sol1()
                self.inkyGhost.sol1()
                self.clydeGhost.sol1()
                self.o = 1
            self.pacman.draw()
            self.pacman.move()
            self.blinkyGhost.draw()
            if self.blinkyGhost.move() == 1:
                self.score += 200
            self.pinkyGhost.draw()
            if self.pinkyGhost.move() == 1:
                self.score += 200
            self.inkyGhost.draw()
            if self.inkyGhost.move() == 1:
                self.score += 200
            self.clydeGhost.draw()
            if self.clydeGhost.move() == 1:
                self.score += 200
            if self.pole.end() == 1:
                self.paused = 2
            self.life_1.draw()
            self.life_2.draw()
            self.life_3.draw()
            self.cherry.draw()
            pyray.draw_rectangle(378,468,190,36,colors.BLACK)
            pyray.draw_text(f'score:{self.score}',326,468,36,colors.WHITE)
            if (self.blinkyGhost.solevoi == 0 and collision(self.pacman, self.blinkyGhost) == True or self.pinkyGhost.solevoi == 0 and collision(self.pacman, self.pinkyGhost) == True or self.inkyGhost.solevoi == 0 and collision(self.pacman, self.inkyGhost) == True or self.clydeGhost.solevoi == 0 and collision(self.pacman, self.clydeGhost) == True):
                self.pacman = Pacman(432, 828, 36, colors.YELLOW)
                self.blinkyGhost = Ghost(396,396,36,colors.RED,self.pacman,'image/elf1.png',0)
                self.pinkyGhost = Ghost(432,396,36,colors.PINK,self.pacman,'image/elf2.png',1)
                self.inkyGhost = Ghost(468,396,36,colors.BLUE,self.pacman,'image/elf3.png',2)
                self.clydeGhost = Ghost(432,432,36,colors.GOLD,self.pacman,'image/elf4.png',3)
                pyray.clear_background(colors.BLACK)
                self.pole.draw()
                if self.life_1.yes_no == 1:
                    self.life_1.deletee()
                elif self.life_2.yes_no == 1:
                    self.life_2.deletee()
                elif self.life_3.yes_no == 1:
                    self.life_3.deletee()
                    self.paused = 3
        elif self.paused == -1: #PUT HERE SOME TEXT. HERE IS A PAUSE
            if self.score > int(self.max_score):
                self.max_score = self.score
                file_records = open('records.txt', 'r+')
                file_records.flush()
                file_records.write(str(self.score))
                file_records.close()

            pyray.draw_texture(self.texture,180,144,colors.WHITE)
            pyray.draw_text('Max score: ', 590, 330, 18, colors.WHITE)
            pyray.draw_text(f'{self.max_score}', 630, 350, 18, colors.WHITE)
            pyray.draw_text('Your score: ', 220, 330, 18, colors.WHITE)
            pyray.draw_text(f'{self.score}', 260, 350, 18, colors.WHITE)
            if pyray.gui_button(pyray.Rectangle(213,155, 53, 50), 'Exit'):
                pyray.close_window()
            if pyray.gui_button(pyray.Rectangle(608, 155, 53, 50), 'Pause'):
                self.paused *=-1
                self.pole.draw()
                for i in self.pole.cemki:
                    i.draw()
                for i in self.pole.bigcemki:
                    i.draw()
                self.pacman.draw()
                self.blinkyGhost.draw()
                self.pinkyGhost.draw()
                self.inkyGhost.draw()
                self.clydeGhost.draw()
                self.life_1.draw()
                self.life_2.draw()
                self.life_3.draw()
                pyray.draw_rectangle(378,468,190,36,colors.BLACK)
                pyray.draw_text(f'score:{self.score}',326,468,36,colors.WHITE)
        elif self.paused == 2 or self.paused == -2: #YOU WIN + RESTART
            if self.score > int(self.max_score):
                self.max_score = self.score
                file_records = open('records.txt', 'r+')
                file_records.flush()
                file_records.write(str(self.score))
                file_records.close()

            pyray.draw_texture(self.texture,180,144,colors.WHITE)
            pyray.draw_text('you win',380,160, 43, colors.WHITE)
            pyray.draw_text('Max score: ', 590, 330, 18, colors.WHITE)
            pyray.draw_text(f'{self.max_score}', 630, 350, 18, colors.WHITE)
            pyray.draw_text('Your score: ', 220, 330, 18, colors.WHITE)
            pyray.draw_text(f'{self.score}', 260, 350, 18, colors.WHITE)

            if pyray.gui_button(pyray.Rectangle(213,155, 53, 50), 'Exit'):
                pyray.close_window()
            if pyray.gui_button(pyray.Rectangle(608, 155, 53, 50), 'Restart'):
                self.pacman = Pacman(432, 828, 36, colors.YELLOW)
                self.blinkyGhost = Ghost(396,396,36,colors.RED,self.pacman,'image/elf1.png',0)
                self.pinkyGhost = Ghost(432,396,36,colors.PINK,self.pacman,'image/elf2.png',1)
                self.inkyGhost = Ghost(468,396,36,colors.BLUE,self.pacman,'image/elf3.png',2)
                self.clydeGhost = Ghost(432,432,36,colors.GOLD,self.pacman,'image/elf4.png',3)
                self.pole = Field()
                self.life_1 = LiveDraw(380, 436, 40, colors.RED)
                self.life_2 = LiveDraw(420, 436, 40, colors.RED)
                self.life_3 = LiveDraw(460, 436, 40, colors.RED)
                self.paused = 1
                self.pole.draw()
                self.vremia = datetime.datetime.now()
                self.o = 1
                self.score = 0
        elif self.paused == 3 or self.paused == -3:
            if self.score > int(self.max_score):
                self.max_score = self.score
                file_records = open('records.txt', 'r+')
                file_records.flush()
                file_records.write(str(self.score))
                file_records.close()

            pyray.draw_texture(self.texture,180,144,colors.WHITE)
            pyray.draw_text('you lose',380,160, 43, colors.WHITE)
            pyray.draw_text('Max score: ', 590, 330, 18, colors.WHITE)
            pyray.draw_text(f'{self.max_score}', 630, 350, 18, colors.WHITE)
            pyray.draw_text('Your score: ', 220, 330, 18, colors.WHITE)
            pyray.draw_text(f'{self.score}', 260, 350, 18, colors.WHITE)

            if pyray.gui_button(pyray.Rectangle(213,155, 53, 50), 'Exit'):
                pyray.close_window()
            if pyray.gui_button(pyray.Rectangle(608, 155, 53, 50), 'Restart'):
                self.pacman = Pacman(432, 828, 36, colors.YELLOW)
                self.blinkyGhost = Ghost(396,396,36,colors.RED,self.pacman,'image/elf1.png',0)
                self.pinkyGhost = Ghost(432,396,36,colors.PINK,self.pacman,'image/elf2.png',1)
                self.inkyGhost = Ghost(468,396,36,colors.BLUE,self.pacman,'image/elf3.png',2)
                self.clydeGhost = Ghost(432,432,36,colors.GOLD,self.pacman,'image/elf4.png',3)
                self.pole = Field()
                self.life_1 = LiveDraw(380, 436, 40, colors.RED)
                self.life_2 = LiveDraw(420, 436, 40, colors.RED)
                self.life_3 = LiveDraw(460, 436, 40, colors.RED)
                self.paused = 1
                self.pole.draw()
                self.vremia = datetime.datetime.now()
                self.o = 1
                self.score = 0


def main_game():
    game = GameScene()

    while not pyray.window_should_close():
        pyray.begin_drawing()
        game.start_game()
        pyray.end_drawing()
    pyray.close_window()


if __name__ == '__main__':
    main_game()
