import pygame

pygame.init()

#set colors for use
BLACK = (0,0,0)
RED = (255, 0, 0)
WHITE = (255,255,255)

#screen settings
WIDTH, HEIGHT = 800,800
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

#enable screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

#draw grid
def draw_grid(positions):
    for position in positions:
        col, row = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen,RED, (*top_left, TILE_SIZE, TILE_SIZE))
    
    for row in range(GRID_HEIGHT):
        pygame.draw.line(screen, WHITE, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))
        
    for col in range(GRID_WIDTH):
        pygame.draw.line(screen, WHITE, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))


def main():
    running = True
    
    positions = set()
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                pos = (col, row)
                
                if pos in positions:
                    positions.remove(pos)
                else:
                    positions.add(pos)
                
        screen.fill(BLACK)
        draw_grid(positions)
        pygame.display.update()
        
        
    pygame.quit()
    
if __name__ == "__main__":
    main()