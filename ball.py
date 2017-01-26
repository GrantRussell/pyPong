import sys
import pygame

pygame.init()

size = width, height = 1000, 650
speed = [1.00, 1.0]
black = 0, 0, 0

gameOver = False
score = 0
screen = pygame.display.set_mode(size)

myfont = pygame.font.Font(None, 30)
score1font = pygame.font.Font(None, 300)
score2font = pygame.font.Font(None, 300)
gameOverScreen = myfont.render("ROUND OVER: Press SPACE to continue...", 5, (255, 255, 255))

p1score = 0
p2score = 0
incrementScore = False

paddle1 = pygame.image.load("paddle.jpg")
paddle1 = pygame.transform.rotate(paddle1, 90)
paddle1rect = paddle1.get_rect()
paddle1rect = paddle1rect.move(0, 275)
paddle1.fill((255, 255, 255))
paddle1orig = paddle1rect.copy()


paddle2 = pygame.image.load("paddle.jpg").convert_alpha()
paddle2 = pygame.transform.rotate(paddle2, 90)
paddle2rect = paddle2.get_rect()
paddle2rect = paddle2rect.move(980, 275)
paddle2.fill((255, 255, 255))
paddle2orig = paddle2rect.copy()

ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, (20, 20))
ballrect = ball.get_rect()
ballrect = ballrect.move(20, 350)
ballorig = ballrect.copy()

padOneMoveX = 0
padOneMoveY = 0
padTwoMoveX = 0
padTwoMoveY = 0


def render(paddle, paddlerect, x, y):
    paddlerect.move([x, y])
    screen.blit(paddle, paddlerect)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if gameOver:
            padOneMoveY = 0
            padTwoMoveY = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameOver = False
                    ballrect = ballorig
                    paddle2rect = paddle2orig
                    paddle1rect = paddle1orig
                    speed[0] = 2
                    speed[1] = 1
                    incrementScore = False
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if ballrect.collidepoint(pos):
                    speed[0] = -speed[0]
                    speed[1] = -speed[1]
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    speed[0] = -speed[0]
                    speed[1] = -speed[1]
                if event.key == pygame.K_DOWN:
                    if paddle2rect.bottom < height:
                        padTwoMoveY = 2
                    else:
                        paddle2rect.bottom = height
                        padTwoMoveY = 0

                if event.key == pygame.K_UP:
                    if paddle2rect.top > 0:
                        padTwoMoveY = -2
                    else:
                        paddle2rect.top = 0
                        padTwoMoveY = 0
                if event.key == pygame.K_s:
                    if paddle1rect.bottom < height:
                        padOneMoveY = 2
                    else:
                        paddle1rect = height
                        padOneMoveY = 0
                if event.key == pygame.K_w:
                    if paddle1rect.top > 0:
                        padOneMoveY = -2
                    else:
                        paddle1rect.top = 0
                        padOneMoveY = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    padTwoMoveY = 0
                if event.key == pygame.K_UP:
                    padTwoMoveY = 0
                if event.key == pygame.K_s:
                    padOneMoveY = 0
                if event.key == pygame.K_w:
                    padOneMoveY = 0

    ballrect = ballrect.move(speed)

    if ballrect.left < 0:
        speed[0] = 0
        speed[1] = 0
        gameOver = True
        if not incrementScore:
            p2score += 1
            incrementScore = True

    if ballrect.right > width:
        speed[0] = 0
        speed[1] = 0
        gameOver = True
        if not incrementScore:
            p1score += 1
            incrementScore = True

    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    if paddle1rect.colliderect(ballrect) or paddle2rect.colliderect(ballrect):
        speed[0] = -speed[0]

    paddle1rect = paddle1rect.move([padOneMoveX, padOneMoveY])
    paddle2rect = paddle2rect.move([padTwoMoveX, padTwoMoveY])

    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(paddle1, paddle1rect)
    screen.blit(paddle2, paddle2rect)

    if gameOver:
        screen.blit(gameOverScreen, (315, 275))
    label = myfont.render("Speed: " + str(speed[0]), 5, (255, 255, 255))
    player1label = score1font.render(str(p1score), 5, (255, 255, 255))
    player2label = score2font.render(str(p2score), 5, (255, 255, 255))
    screen.blit(player1label, (250, 5))
    screen.blit(player2label, (615, 5))
    #screen.blit(label, (350, 0))
    pygame.display.flip()
