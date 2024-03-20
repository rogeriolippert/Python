import pygame

pygame.init()

# Definindo as dimensões da janela
display_width = 800
display_height = 600

# Criando a janela
gameDisplay = pygame.display.set_mode((display_width,display_height))

# Definindo o nome da janela
pygame.display.set_caption('Meu jogo simplão em 2D!')

# Definindo cores
black = (0,0,0)
white = (255,255,255)

# Criando o jogador
player_width = 73
player_height = 73
playerImg = pygame.image.load('player.png')

# Movimentando o jogador
player_x = (display_width * 0.45)
player_y = (display_height * 0.8)
player_speed = 0
player_jump = False

# Criando as plataformas
platform_width = 70
platform_height = 10
platform_x = 400
platform_y = 300

# Mecânica de pulo
jump_height = 10

# Adicionando pontos e vidas
score = 0
lives = 3

# Função para desenhar o jogador
def player(x,y):
    gameDisplay.blit(playerImg,(x,y))

# Função para mover o jogador
def move_player(change_speed):
    global player_x, player_speed
    player_speed += change_speed
    player_x += player_speed

# Função para desenhar as plataformas
def platform():
    pygame.draw.rect(gameDisplay, black, [platform_x, platform_y, platform_width, platform_height])

# Função para realizar o pulo do jogador
def jump_player():
    global player_jump, player_y
    if not player_jump:
        player_jump = True
        player_y -= jump_height

# Função para exibir a pontuação
def score_display():
    font = pygame.font.SysFont(None, 25)
    text = font.render("Pontos: "+str(score), True, black)
    gameDisplay.blit(text,(0,0))

# Função para exibir as vidas
def lives_display():
    font = pygame.font.SysFont(None, 25)
    text = font.render("Vidas: "+str(lives), True, black)
    gameDisplay.blit(text,(0,30))

# Função para detectar colisões
def detect_collision():
    global lives, score, platform_y
    if player_y < platform_y + platform_height:
        if player_x > platform_x and player_x < platform_x + platform_width:
            platform_y = 0 - platform_height
            score += 1
        else:
            lives -= 1
            if lives == 0:
                game_over()

# Função para exibir mensagem de fim de jogo
def game_over():
    font_game_over = pygame.font.SysFont(None, 90)
    text_game_over = font_game_over.render("GAME OVER", True, black)
    gameDisplay.blit(text_game_over,(display_width/2 - text_game_over.get_width()/2, display_height/2 - text_game_over.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()
    quit()

# Loop do jogo
gameExit = False
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

        # Movimentando o jogador
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_player(-5)
            elif event.key == pygame.K_RIGHT:
                move_player(5)
            elif event.key == pygame.K_UP:
                jump_player()

    # Aplicando o plano de fundo branco
    gameDisplay.fill(white)

    # Mecânica de pulo
    if player_jump:
        player_y += jump_height
        if player_y >= (display_height * 0.8):
            player_jump = False

    # Verificando colisões
    detect_collision()

    # Desenhando os objetos na tela
    player(player_x,player_y)
    platform()

    # Adicionando os pontos e vidas
    score_display()
    lives_display()

    pygame.display.update()

pygame.quit()
quit()
