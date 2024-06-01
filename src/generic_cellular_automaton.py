import pygame
import numpy as np

class GameOfLife:
    def __init__(self, rows, cols):
        # Initialize Pygame
        pygame.init()

        # Set up display
        self.width = rows * 10
        self.height = cols * 10

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Conway's Game of Life")

        # Define colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        # Define grid size
        self.cols = cols
        self.rows = rows
        self.cell_width = self.width // self.cols
        self.cell_height = self.height // self.rows

        # Initialize grid
        self.grid = np.zeros((rows, cols))

    # Function to draw the grid
    def draw_grid(self, surface, grid):
        for row in range(self.rows):
            for col in range(self.cols):
                color = self.WHITE if grid[row][col] == 1 else self.BLACK
                pygame.draw.rect(surface, color, (col * self.cell_width, row * self.cell_height, self.cell_width - 1, self.cell_height - 1))

    # Function to update the grid
    def update_grid(self, grid):
        new_grid = np.copy(grid)
        for row in range(self.rows):
            for col in range(self.cols):
                state = grid[row][col]
                neighbors = (
                    grid[row, (col - 1) % self.cols] + grid[row, (col + 1) % self.cols] +
                    grid[(row - 1) % self.rows, col] + grid[(row + 1) % self.rows, col] +
                    grid[(row - 1) % self.rows, (col - 1) % self.cols] + grid[(row - 1) % self.rows, (col + 1) % self.cols] +
                    grid[(row + 1) % self.rows, (col - 1) % self.cols] + grid[(row + 1) % self.rows, (col + 1) % self.cols]
                )
                if state == 0 and neighbors == 3:
                    new_grid[row][col] = 1
                elif state == 1 and (neighbors < 2 or neighbors > 3):
                    new_grid[row][col] = 0
        return new_grid
    
    def run(self):
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
                        col = x // self.cell_width
                        row = y // self.cell_height
                        grid[row][col] = 1 if grid[row][col] == 0 else 0

            if not paused:
                grid = self.update_grid(grid)

            self.window.fill(self.BLACK)
            self.draw_grid(self.window, grid)
            pygame.display.flip()

            pygame.time.delay(100)
        pygame.quit()
