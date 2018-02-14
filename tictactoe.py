import random, pygame
colors = [(1,1,1),(255,255,255),(255,1,1),(1,1,255)]
buttons = []
xButs, yButs = [], []
wins, losses = 0, 0
winStates = [ [1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7] ]

class Button:
    def __init__(self, x, y, num):
        self.rect = pygame.Rect((x,y),(200,200))
        self.owner = None
        self.color = colors[0]
        self.num = num

bNum = 0
for xx in range(0,600,200):
    for yy in range(0,600,200):
        bNum += 1
        buttons.append(Button(xx,yy,bNum))

pygame.init()
screen = pygame.display.set_mode((600, 600))
done = False
turn = True
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if turn:
                for i in buttons:
                    if i.rect.collidepoint(pygame.mouse.get_pos()):
                        if i.owner == None:
                            i.owner = 0
                            i.color = colors[2]
                            screen.fill(i.color, i.rect)
                            xButs.append(i.num)
                            print(xButs)
                            for i in winStates:
                                if i[0] in xButs and i[1] in xButs and i[2] in xButs:
                                    print("YOU WIN")
                                    wins += 1
                                    for i in buttons:
                                        i.owner = None
                                        i.color = colors[0]
                                        screen.fill(i.color, i.rect)
                                    xButs, yButs = [], []
                            turn = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            for i in buttons:
                i.owner = None
                i.color = colors[0]
                screen.fill(i.color, i.rect)
            xButs, yButs = [], []
    if not turn:
        while not turn:
            num = random.randint(0,8)
            if buttons[num].owner == None:
                buttons[num].owner = 1
                buttons[num].color = colors[3]
                screen.fill(buttons[num].color, buttons[num].rect)
                yButs.append(buttons[num].num)
                print(yButs)
                for i in winStates:
                    if i[0] in yButs and i[1] in yButs and i[2] in yButs:
                        print("YOU LOSE")
                        losses += 1
                        for i in buttons:
                            i.owner = None
                            i.color = colors[0]
                            screen.fill(i.color, i.rect)
                        xButs, yButs = [], []
                turn = True
                break
    pygame.draw.line(screen, colors[1], (200,0), (200, 600), 5)
    pygame.draw.line(screen, colors[1], (400, 0), (400, 600), 5)
    pygame.draw.line(screen, colors[1], (0, 200), (600, 200), 5)
    pygame.draw.line(screen, colors[1], (0, 400), (600, 400), 5)
    pygame.display.flip()