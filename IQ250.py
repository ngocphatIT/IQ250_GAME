import pygame,math,os,time
pygame.init()
class Picture():

    def __init__(self,w,h,name):
        self.w=w
        self.h=h
        self.img=pygame.transform.scale(pygame.image.load(f"img\\{name}"),(w,h))
        self.alive=True
    def update(self,surface,x,y):
        if self.alive:
            global update_time
            surface.blit(self.img,(x,y))
            if pygame.mouse.get_pressed()[0]==1:
                pos=pygame.mouse.get_pos()
                if pos[0]>=x and pos[0] <=x+self.w and pos[1]>=y and pos[1]<=y+self.h and pygame.time.get_ticks()-update_time>500:
                    update_time=pygame.time.get_ticks()
                    self.alive=False
                    return True
class Button():
    def __init__(self,text='',font="Arial",size=40,fg=(255,255,255),bg1=(234,34,42),bg2=(100,105,250)):
        self.text=text
        self.text_img=pygame.font.SysFont(font,size).render(f'{self.text}',True,fg)
        self.w=self.text_img.get_width()+20
        self.h=self.text_img.get_height()+20
        self.bg1=bg1
        self.bg2=bg2
    def draw(self,x,y,surface):
        action=False
        pos=pygame.mouse.get_pos()
        if pos[0]>=x and pos[0]<=x+self.w and pos[1]>=y and pos[1]<=y+self.h:
            pygame.draw.rect(surface,self.bg2,(x,y,self.w,self.h))
            if pygame.mouse.get_pressed()[0]==1:
                action=True
        else:
            pygame.draw.rect(surface,self.bg1,(x,y,self.w,self.h))
        surface.blit(self.text_img,(x+10,y+10))
        return action
class Game():
    def __init__(self):
        self.surface=pygame.display.set_mode((screen_w,screen_h))
        pygame.display.set_caption("IQ250")
    def initialization(self):
        self.btStart=Button("START",size=40)
        self.img_list=[]
        self.level=0
        self.loadpicture()
        self.I1=[Picture(230,150,"rock.png"),Picture(230,150,"water.png"),Picture(230,150,"air.png")]
        self.I2=[Picture(230,150,"4.png"),Picture(230,150,"6.png"),Picture(230,150,"8.png")]
        self.I3=[Picture(230,150,"blue.png"),Picture(230,150,"red.png"),Picture(230,150,"green.png")]
        self.I4=[Picture(350,350,"rect1.png"),Picture(200,150,"rect2.png"),Picture(200,200,"rect2.png"),Picture(150,150,"rect2.png"),Picture(100,100,"rect2.png"),Picture(30,30,"rect2.png")]
        self.I6=[Picture(300,150,"sugar.png"),Picture(300,150,"street.png")]
        self.I7=[Picture(300,150,"Tokyo.png"),Picture(300,150,"Kyoto.png"),Picture(300,150,"Osaka.png")]
        self.I8=[Picture(230,150,"6.png"),Picture(230,150,"65.png"),Picture(230,150,"1036.png")]
        self.I9=[Picture(150,200,"cup1.png"),Picture(150,200,"cup2.png"),Picture(150,200,"cup3.png"),Picture(150,200,"cup4.png")]
        self.I11=[Picture(200,100,"english.png"),Picture(200,100,"chinese.png"),Picture(200,100,"spanish.png")]
        self.I12=[Picture(230,150,"blue.png"),Picture(230,150,"red.png"),Picture(230,150,"green.png")]
        self.I13=[Picture(50,50,"red.png"),Picture(230,150,"blue.png"),Picture(230,150,"red.png"),Picture(230,150,"green.png")]
        self.I=[self.I1,self.I2,self.I3,self.I4,self.I6,self.I7,self.I8,self.I9,self.I11,self.I12,self.I13]
        self.count=0
        self.update_time=pygame.time.get_ticks()
        self.endtime=5000
    def run(self):
        self.initialization()
        clock=pygame.time.Clock()
        FPS=60
        while True:
            self.display()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    return
            pygame.display.update()
    def display(self):
        self.surface.fill((117,234,176))
        self.surface.blit(pygame.font.SysFont("Times",80).render("IQ 250",True,(200,100,50)),(screen_w//2-6*20,10))
        if self.level==0:
            if self.btStart.draw(screen_w//2-70,200,self.surface):
                self.level=1
                self.update_time=pygame.time.get_ticks()
        else:
            if self.level!=15: 
                self.surface.blit(font_txt.render(f"Level: {self.level}",True,(255,255,255)),(10,100))
                pygame.draw.rect(self.surface,(252, 252, 0),(0,screen_h-100,screen_w,50))
                pygame.draw.rect(self.surface,(216, 3, 0),(0,screen_h-100,screen_w-int(screen_w*(pygame.time.get_ticks()-self.update_time)/self.endtime),50))
                if pygame.time.get_ticks()-self.update_time>=self.endtime:
                    self.lose()
            if self.level==1:
                self.level1()
            elif self.level==2:
                self.level2()
            elif self.level==3:
                self.level3()
            elif self.level==4:
                self.level4()
            elif self.level==5:
                self.level5()
            elif self.level==6:
                self.level6()
            elif self.level==7:
                self.level7()
            elif self.level==8:
                self.level8()
            elif self.level==9:
                self.level9()
            elif self.level==10:
                self.level10()
            elif self.level==11:
                self.level11()
            elif self.level==12:
                self.level12()
            elif self.level==13:
                self.level13()
            elif self.level==14:
                self.level14()
            elif self.level==15:
                self.level15()
    def level1(self):
        x=270
        y=200
        self.surface.blit(font_txt.render("Mặt trời          là thể gì?",True,(100,100,100)),(x,200))
        self.surface.blit(self.img_list[0],(x+7*20,180))
        if self.I1[2].update(self.surface,50,y+100):
            self.next()
        if self.I1[1].update(self.surface,330,y+100) or self.I1[0].update(self.surface,600,y+100):
            self.lose()
    def level2(self):
        x=220
        y=200
        self.surface.blit(font_txt.render("Cái áo này            có mấy lỗ?",True,(100,100,100)),(x,200))
        self.surface.blit(self.img_list[1],(x+9*20,180))
        if self.I2[0].update(self.surface,50,y+100) or self.I2[1].update(self.surface,330,y+100):
            self.lose()
        if self.I2[2].update(self.surface,600,y+100):
            self.next()
    def level3(self):
        x=220
        y=200
        self.surface.blit(font_txt.render("Click vào màu xanh để đi tiếp!",True,(100,100,222)),(x,200))
        if self.I3[1].update(self.surface,50,y+100) or self.I3[2].update(self.surface,330,y+100):
            self.lose()
        if self.I3[0].update(self.surface,600,y+100):
            self.next()
    def level4(self):
        self.surface.blit(font_txt.render("Click vào hình vuông từ lớn đến nhỏ!",True,(100,100,222)),(150,150))
        if self.I4[0].update(self.surface,300,390) or self.I4[1].update(self.surface,300,200):
            self.lose()
        if self.I4[2].update(self.surface,650,450):
            self.count+=1
            if self.count!=1:
                self.lose()
        if self.I4[3].update(self.surface,50,200):
            self.count+=1
            if self.count!=2:
                self.lose()
        if self.I4[4].update(self.surface,600,300):
            self.count+=1
            if self.count!=3:
                self.lose()
        if self.I4[5].update(self.surface,100,500):
            self.count+=1
            if self.count!=4:
                self.lose()
        if self.count==4:
            self.next()
    def level5(self):
        self.surface.blit(self.img_list[2],(100,100))
        self.surface.blit(self.img_list[3],(400,150))
        self.surface.blit(self.img_list[4],(200,450))
        if pygame.time.get_ticks()-self.update_time>=self.endtime/2:
            self.next()
    def level6(self):
        self.surface.blit(font_txt.render("Click vào đường đi.",True,(100,100,222)),(300,150))
        if self.I6[0].update(self.surface,100,300):
            self.lose()
        if self.I6[1].update(self.surface,500,300):
            self.next()
    def level7(self):
        self.surface.blit(font_txt.render("Click vào thủ đô của Nhật Bản!",True,(178,0,31)),(380,150))
        if self.I7[0].update(self.surface,50,150) or self.I7[1].update(self.surface,250,320) or self.I7[2].update(self.surface,450,490):
            self.lose()
        if pygame.time.get_ticks()-self.update_time>=self.endtime-1000:
            self.next()
    def level8(self):
        self.surface.blit(font_txt.render("Kết quả là:",True,(178,0,31)),(200,150))
        if self.I8[1].update(self.surface,200,400) or self.I8[2].update(self.surface,600,300):
            self.lose()
        if self.I8[0].update(self.surface,100,200):
            self.next()
    def level9(self):
        self.surface.blit(font_txt.render("Cốc nào nhiều nước nhất?",True,(178,0,31)),(200,150))
        if self.I9[0].update(self.surface,200,200) or self.I9[2].update(self.surface,600,200) or self.I9[1].update(self.surface,200,500):
            self.lose()
        if self.I9[3].update(self.surface,600,500):
            self.next()
    def level10(self):
        self.surface.blit(font_txt.render("Màu RGB, đó là (255,0,0).",True,(178,0,31)),(200,300))
        if pygame.time.get_ticks()-self.update_time>=self.endtime/2:
            self.next()
    def level11(self):
        self.surface.blit(font_txt.render("Ngôn ngữ nào được sử dụng nhiều nhất",True,(178,0,31)),(200,150))
        if self.I11[0].update(self.surface,200,400) or self.I11[2].update(self.surface,600,300):
            self.lose()
        if self.I11[1].update(self.surface,100,200):
            self.next()
    def level12(self):
        self.surface.blit(font_txt.render("Click vào màu đỏ để dừng lại!",True,(255,0,0)),(200,150))
        if self.I12[0].update(self.surface,50,200) or self.I12[2].update(self.surface,330,200):
            self.next()
        if self.I12[1].update(self.surface,600,200):
            self.lose()
    def level13(self):
        self.surface.blit(font_txt.render("Click vào       để đi tiếp!",True,(255,255,0)),(190,150))
        if self.I13[0].update(self.surface,200+150,150):
            self.next()
        if self.I13[3].update(self.surface,50,400) or self.I13[2].update(self.surface,330,400):
            self.lose()
        if self.I13[1].update(self.surface,600,400):
            self.lose()
    def level14(self):
        self.surface.blit(font_txt.render("Màu đó là",True,(255,255,0)),(190,150))
        if self.I13[3].update(self.surface,50,400) or self.I13[1].update(self.surface,330,400):
            self.lose()
        if self.I13[2].update(self.surface,600,400):
            self.next()
    def level15(self):
        self.surface.blit(font_txt.render("Cảm ơn bạn đã sử dụng",True,(0,0,0)),(200,200))
        self.surface.blit(font_txt.render("Những câu hỏi sẽ cập nhật sau.",True,(0,0,0)),(200,300))
        self.surface.blit(pygame.font.SysFont("Times",80).render("To be continue...",True,(0,0,0)),(200,400))
    def loadpicture(self):
        self.load("sun.png",80,80)
        self.load("shirt.png",100,100)
        self.load("mul1.png",250,250)
        self.load("mul2.png",250,250)
        self.load("mul3.png",400,200)
    def load(self,name,w,h):
        img=pygame.transform.scale(pygame.image.load(f"img\\{name}"),(w,h))
        self.img_list.append(img)
    def reset(self):
        for x in self.I:
            for i in x:
                i.alive=True
    def next(self):
        self.level+=1
        self.count=0
        time.sleep(0.2)
        self.update_time=pygame.time.get_ticks()
    def lose(self):
        self.level=0
        self.reset()
if __name__=="__main__":
    update_time=pygame.time.get_ticks()-500
    screen_w=900
    screen_h=800
    font_txt=pygame.font.SysFont("Times",40)
    screen=Game()
    screen.run()

