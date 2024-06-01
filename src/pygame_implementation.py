import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conway's Game of Life")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define grid size
cols, rows = 50, 50
cell_width = width // cols
cell_height = height // rows

# Initialize grid
grid = np.zeros((rows, cols))

# Function to draw the grid
def draw_grid(surface, grid):
    for row in range(rows):
        for col in range(cols):
            color = WHITE if grid[row][col] == 1 else BLACK
            pygame.draw.rect(surface, color, (col * cell_width, row * cell_height, cell_width - 1, cell_height - 1))

# Function to update the grid
def update_grid(grid):
    new_grid = np.copy(grid)
    for row in range(rows):
        for col in range(cols):
            state = grid[row][col]
            neighbors = (
                grid[row, (col - 1) % cols] + grid[row, (col + 1) % cols] +
                grid[(row - 1) % rows, col] + grid[(row + 1) % rows, col] +
                grid[(row - 1) % rows, (col - 1) % cols] + grid[(row - 1) % rows, (col + 1) % cols] +
                grid[(row + 1) % rows, (col - 1) % cols] + grid[(row + 1) % rows, (col + 1) % cols]
            )
            if state == 0 and neighbors == 3:
                new_grid[row][col] = 1
            elif state == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[row][col] = 0
    return new_grid

# Main loop
running = True
paused = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if paused:
                x, y = pygame.mouse.get_pos()
                col = x // cell_width
                row = y // cell_height
                grid[row][col] = 1 if grid[row][col] == 0 else 0

    if not paused:
        grid = update_grid(grid)

    window.fill(BLACK)
    draw_grid(window, grid)
    pygame.display.flip()

    pygame.time.delay(100)

pygame.quit()
