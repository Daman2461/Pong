import pygame
WIDTH, HEIGHT = 700,500
WIN =  pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

pygame.init()

FPS = 60

white=(255,255,255)

paddle_width,paddle_height=20,120

FONT = pygame.font.SysFont('consolas', 50)
WINNER_FONT = pygame.font.SysFont('couriernew', 50)

class Paddle:
    color = white
    vel = 4
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    
    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.height),border_radius=8)
    
    def move(self,up=True):
        
        if up and self.y>0:
            self.y -= self.vel
        
        if not up and ( self.y+self.height < HEIGHT):
                self.y += self.vel
class Ball:
    
    def __init__(self,x,y,radius):
        self.x=x
        self.y=y
        self.radius=radius 
        self.x_vel= 5
        self.y_vel=0
        
    def draw(self, win):
        pygame.draw.circle(win,(0,255,0),(self.x, self.y),self.radius)
        
    def move(self,paddles):
        self.x=self.x+self.x_vel
        self.y+=self.y_vel
        for i in paddles:
            if (i.x==self.x or i.x + i.width==self.x) and self.y in range (i.y+i.height//3,i.y+2*(i.height)//3):
                self.x_vel=-self.x_vel
                self.y_vel=0
            if (i.x==self.x or i.x + i.width==self.x) and self.y in range(i.y,i.y+(i.height)//3):
                self.x_vel=-self.x_vel
                self.y_vel=-2
                
            if (i.x==self.x or i.x + i.width==self.x) and self.y in range(i.y+2*(i.height)//3,i.y+i.height):
                self.x_vel=-self.x_vel
                self.y_vel=2
                
                
                
        if self.y==0:
            self.y_vel= -self.y_vel
        elif self.y == HEIGHT:
                self.y_vel =-self.y_vel
        

           
def draw(win,paddles,ball,scores):
    win.fill((0,0,0))
    
    left=FONT.render(f"{scores[0]}",1,(0, 255, 0))
    right=FONT.render(f"{scores[1]}",1,(0, 255, 0))
    
    win.blit(left, (WIDTH//4,20))
    win.blit(right, ((3*WIDTH)//4,20))
    
        
        
    for i in paddles:
        i.draw(win)
        
    ball.draw(win)  
    pygame.display.update()
    

def main():
    run = True
    clock = pygame.time.Clock()
  
    left_paddle=Paddle(10,HEIGHT//2-paddle_height//2 ,paddle_width,paddle_height)
    right_paddle=Paddle(WIDTH-paddle_width-10,HEIGHT//2-paddle_height//2,paddle_width,paddle_height)
    ball=Ball(WIDTH//2,HEIGHT//2, 11)
    
    left_score,right_score=0,0
    while run:
        
         
        clock.tick(FPS)
        
        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                
                pygame.quit()
        
         
        
        ball.move([left_paddle,right_paddle])
        
        keys=pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            left_paddle.move(up=True) 
        if keys[pygame.K_s]:
            left_paddle.move(up=False) 
        if keys[pygame.K_UP]:
            right_paddle.move(up=True) 
        if keys[pygame.K_DOWN]:
            right_paddle.move(up=False) 
        
        
        
        if ball.x<0:
            right_score+=1
            
            left_paddle=Paddle(10,HEIGHT//2-paddle_height//2 ,paddle_width,paddle_height)
            right_paddle=Paddle(WIDTH-paddle_width-10,HEIGHT//2-paddle_height//2,paddle_width,paddle_height)
            ball=Ball(WIDTH//2,HEIGHT//2, 11)
            pygame.time.wait(1000)
        if ball.x > WIDTH:
            left_score+=1
            
            ball=Ball(WIDTH//2,HEIGHT//2, 11)
            left_paddle=Paddle(10,HEIGHT//2-paddle_height//2 ,paddle_width,paddle_height)
            right_paddle=Paddle(WIDTH-paddle_width-10,HEIGHT//2-paddle_height//2,paddle_width,paddle_height)
            pygame.time.wait(1000)
            
        draw(WIN,[left_paddle,right_paddle],ball,[left_score,right_score])
        
        if (left_score==10):
            run=False
            a=WINNER_FONT.render("Left Player Won!", 1, (0,255,0))
            WIN.blit(a, (WIDTH//2-a.get_width()//2,HEIGHT//2))
            pygame.display.update()
            pygame.time.wait(5000)
            pygame.quit()
            
        if (right_score==10):
            run=False
            a=WINNER_FONT.render("Right Player Won!", 1, (0,255,0))
            WIN.blit(a, (WIDTH//2-a.get_width()//2,HEIGHT//2))
            pygame.display.update()
            pygame.time.wait(5000)
            pygame.quit()
  

if __name__ =='__main__':
    main()