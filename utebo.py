import pygame
from math import ceil
from math import pi
import time

# Feito por Magnus, Rudigus e Caius e Luanus

placarJ1 = 0
placarJ2 = 0

def main():
    global placarJ1
    global placarJ2
    pygame.init()
    tempo = 0
    tempo1 = 0
    tempoInicial = 0
    tempoFinal = 0
    p = False
    o = True
    chute = False
    chuteAcabou = False
    infoTela = pygame.display.Info()
    largura = infoTela.current_w
    altura = infoTela.current_h
    screen = pygame.display.set_mode((800, 600))
    fontePlacar = pygame.font.SysFont("monospace", 90, 1)
    textoPlacar = str(placarJ1) + " " + str(placarJ2)
    placar = fontePlacar.render(textoPlacar, 0, (0, 0, 0))
    pygame.display.set_caption("UTEBO - %d X %d" % (placarJ1, placarJ2))
    done = True
    is_blue = True
    t=largura//2 # X do centro do círculo
    k=altura//2 # Y do centro do círculo
    tj = 20 # Tamanho do Jogador
    x = [largura - largura//15 - tj, largura//15]
    y = [altura / 2 - tj//2 , altura / 2 - tj//2]
    vel = 4
    r = 14
    tb = r * 2

    clock = pygame.time.Clock()

    while done:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                done = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_blue = not is_blue
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_p):
                chute = True
            if (event.type == pygame.KEYUP and event.key == pygame.K_p):
                chuteAcabou = True
        # Bola enconsta no lado esquerdo
        if(t - r < 0):
            if(not(t - r < 0 and k > altura//4 and k < 3 * altura//4)):
                t = r
        # Bola encosta no lado direito
        if(t + r > largura):
            if(not(t + r > largura and k > altura//4 and k < 3 * altura // 4)):
                t = largura - (r * 3) // 2
        # Bola encosta no teto
        if(k - r < 0):
            k = r
        # Bola encosta no chão
        if(k + r > altura):
            k = altura - (r * 3) // 2
        
        distX = abs(x[0] - x[1])
        distY = abs(y[0] - y[1])
        if(x[0] < t):
            distTX = (t - r) - (x[0] + tj)
        else:
            distTX = x[0] - (t + r)
        if(x[1] < t):
            distTX1 = (t - r) - (x[1] + tj)
        else:
           distTX1 = x[1] - (t + r)
        if(y[0] > k):
            distTY = y[0] - (k + r)
        else:
            distTY = (k - r) - (y[0] + tj) 
        if(y[1] > k):
            distTY1 = y[1] - (k + r)
        else:
            distTY1 = (k - r) - (y[1] + tj)
        pressed = pygame.key.get_pressed()
        # Movimento dos Jogadores (J1 e J2)
        if pressed[pygame.K_ESCAPE]:
            done = False
        if pressed[pygame.K_UP]:
            if(not(distX <= tj and abs(y[0] - vel - y[1]) <= tj and y[0] > y[1]) and (not(y[0] <= 0))):
                y[0] -= vel
        if pressed[pygame.K_DOWN]:
            if(not(distX <= tj and abs(y[0] + vel - y[1]) <= tj and y[0] < y[1]) and (not(y[0]+tj >= altura))):
                y[0] += vel
        if pressed[pygame.K_LEFT]:
            if(not(abs(x[0] - vel - x[1]) <= tj and distY <= tj and x[0] > x[1]) and (not(x[0] <= 0))):
                x[0] -= vel
        if pressed[pygame.K_RIGHT]:
            if(not(abs(x[0] + vel - x[1]) <= tj and distY <= tj and x[0] < x[1]) and (not(x[0] + tj >= largura))):
                x[0] += vel
        if pressed[pygame.K_w]:
            if(not(distX <= tj and abs(y[0] - (y[1] - vel)) <= tj and y[1] > y[0]) and (not(y[1] <= 0))):
                y[1] -= vel
        if pressed[pygame.K_s]:
            if(not(distX <= tj and abs(y[0] - (y[1] + vel)) <= tj and y[1] < y[0]) and (not(y[1]+tj >= altura))):
                y[1] += vel
        if pressed[pygame.K_a]:
            if(not(abs(x[0] - (x[1] - vel)) <= tj and distY <= tj and x[1] > x[0]) and (not(x[1] <= 0))):
                x[1] -= vel
        if pressed[pygame.K_d]:
            if(not(abs(x[0] - (x[1] + vel)) <= tj and distY <= tj and x[1] < x[0]) and (not(x[1]+tj >= largura))):
                x[1] += vel
        # Movimento da Bola
        velBola = ceil(vel)
        # Movimento da Bola pra Direita (J1)
        if(distTX<=0 and x[0]<t and distTY <= -4):
            t += velBola
            if pressed[pygame.K_RCTRL]:
##                clock = pygame.time.Clock()
##                clock.tick()
##                clock.tick()
##                clock.get_time()
                velchute = 0
                tempo1 = int(time.time())
                while(o):
                    clock = pygame.time.Clock()
                    clock.tick()
                    if(not(event.type == pygame.KEYUP and event.type == pygame.K_RCTRL)):
                        o = False
                    clock.tick()
                    clock.get_time()
                    velchute = 0
                else:
                    tempo2 = clock.get_time()
                    velchute = 16 + tempo2
                    print(tempo2 - tempo1)
                p = True
        # Movimento da Bola pra Esquerda (J1)
        if(distTX<=0 and x[0]>t and distTY <= -(velBola)):
            t -= velBola
##            if pressed[pygame.K_RCTRL]:
####                clock = pygame.time.Clock()
####                clock.tick()
####                clock.tick()
####                clock.get_time()
##                velchute = 0
##                clock = pygame.time.Clock()
##                tempo = int(time.time())
            if(chute):
                tempoInicial = time.time()
                print("EITAAA")
                chute = False
            if(chuteAcabou):
                print("OITTTTEEE")
                if(tempoFinal ==1):
                    tempoFinal =0
                    tempoInicial =0
                    chuteAcabou = False
                    velchute = 8
                else:    
                    tempoFinal = time.time()
                    tempoPercorrido = int(tempoFinal - tempoInicial)
                    print(tempoPercorrido)
                    chuteAcabou = False
                    velchute = 12 + 8*tempoPercorrido
                p = True
        elif(distTX>= 50):
            tempoInicial = 0
            tempoFinal = 1
        # Movimento da Bola pra Direita (J2)
        if(distTX1<=0 and x[1]<t and distTY1 <= -(velBola)):
            t += velBola
        # Movimento da Bola pra Esquerda (J2)
        if(distTX1<=0 and x[1]>t and distTY1 <= -(velBola)):
            t -= velBola
        # Movimento da Bola pra Baixo (J1)
        if(distTY<=0 and y[0]<k and distTX <= -(velBola)):
            k += velBola
        # Movimento da Bola pra Cima (J1)
        if(distTY<=0 and y[0]>k and distTX <= -(velBola)):
            k -= velBola
        # Movimento da Bola pra Baixo (J2)
        if(distTY1 <= 0 and y[1]<k and distTX1 <= -(velBola)):
            k += velBola
        # Movimento da Bola pra Cima (J2)
        if(distTY1 <= 0 and y[1]>k and distTX1 <= -(velBola)):
            k -= velBola
        # Gol do J2
        if(t + r > largura and k > altura//4 and k < 3 * altura // 4):
            print("GOL DO CAIO") # colocar isso no display, ou apagar
            placarJ1 += 1
            return main()
        # Gol do J1
        if(t - r < 0 and k > altura//4 and k < 3 * altura // 4):
            print("GOL DO MAGNUS") # colocar isso no display, ou apagar
            placarJ2 += 1
            return main()
        # Ferramenta de Debug
        if pressed[pygame.K_o]:
            print("jogador 1: ", distTX, distTY, "jogador 2: ", distTX1, distTY1 , t , k)
        screen.fill((0, 0, 0))
        if(p):
            if(x[0]<t):
                t += velchute
                velchute -= 1
                if(velchute<=0):
                    p = False
                    velchute = 0
            else:
                t -= velchute
                velchute -=1
                if(velchute<=0):
                    p = False
                    velchute = 0
        if is_blue:
            blue = (0, 0, 255)
            black = (0,0,0)
            orange = (255, 100, 0)
            white = (255,255,255)
            darkGreen = (0,100,0)
            cinza = (100, 100, 100)
        # Gramado
        pygame.draw.rect(screen,darkGreen,pygame.Rect(0,0,largura,altura))
        # Círcunferência Central
        pygame.draw.circle(screen,white,[largura//2,altura//2],70,1)
        # Linha Central
        pygame.draw.rect(screen,white,pygame.Rect(largura//2,0,1,altura))
        # Área Esquerda
        pygame.draw.rect(screen,white,pygame.Rect(0,altura//4,170,1))
        pygame.draw.rect(screen,white,pygame.Rect(0,3 * altura//4,170,1))
        pygame.draw.rect(screen,white,pygame.Rect(170,altura//4,1,altura//2))
        # Área Direita
        pygame.draw.rect(screen,white,pygame.Rect(largura - 170,altura//4,170,1))
        pygame.draw.rect(screen,white,pygame.Rect(largura - 170,3 * altura//4,170,1))
        pygame.draw.rect(screen,white,pygame.Rect(largura - 170,altura//4,1,altura//2))
        # Jogadores de Futebol
        pygame.draw.rect(screen, blue, pygame.Rect(x[0], y[0], tj, tj))
        pygame.draw.rect(screen, orange, pygame.Rect(x[1], y[1], tj, tj))
        # Bola
        pygame.draw.circle(screen, cinza, [t,k], r)
        pygame.draw.circle(screen, cinza, [t,k], r)
        # Placar
        screen.blit(placar, (largura//2 - 80, 60))
        
        pygame.display.flip()
        clock.tick(60)

main()
pygame.quit()
