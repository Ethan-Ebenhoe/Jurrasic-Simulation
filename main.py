# Import necessary libraries
import sys
import numpy as np
import pygame

# Set the background color and dimensions of the display
background_color = (80, 225, 25)
WIDTH, HEIGHT = 1282, 575

class Herbivore:
  def __init__(self):
    self.image1 = pygame.image.load("Herbivore.png")
    self.image2 = pygame.image.load("Herbivore-d.png")
    self.spawned = False
    self.pack = 0
  def spawn(self,parent,created):
    if created:
      self.pack = np.random.randint(1,2)
      
    else:
      self.x = parent.x
      self.y = parent.y
      self.pack = parent.pack
    self.image = self.image1
# Create the Tree class
class Tree:
  def __init__(self):
    # Load the tree image and scale it
    self.image = pygame.image.load("tree.png")
    self.image = pygame.transform.scale(self.image, (50, 50))
    self.spawned = False  # Flag to track if the tree has been spawned

  def spawn(self, surface):
    if not self.spawned:  # Check if the tree has been spawned
      self.spawned = True  # Set the flag to True once the tree is spawned
      self.x = np.random.randint(0, WIDTH - self.image.get_width())  # Set a random x position
      self.y = np.random.randint(0, HEIGHT - self.image.get_height())  # Set a random y position
    self.rect = self.image.get_rect()  # Get the bounding rectangle of the tree image
    self.rect.x = self.x  # Set the x coordinate of the rectangle
    self.rect.y = self.y  # Set the y coordinate of the rectangle
    surface.blit(self.image, self.rect)  # Draw the tree on the surface

def main():
  print("Main function called")  # Print a message to indicate that the main function is called
  pygame.init()  # Initialize pygame
  screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Set the display
  screen.fill(background_color)  # Fill the background

  trees = []  # Create an empty list to store trees
  for _ in range(50):  # Create 50 trees
    tree = Tree()  # Instantiate a new Tree object
    trees.append(tree)  # Add the tree to the list of trees

  running = True
  while running:
    for event in pygame.event.get():  # Event loop
      if event.type == pygame.QUIT:
        running = False

    screen.fill(background_color)  # Fill the background
    for tree in trees:
      tree.spawn(screen)  # Draw the tree on the screen
    pygame.display.flip()  # Update the display

  pygame.quit()  # Quit the game when the loop ends
  sys.exit()  # Exit

# Check if the file is being run as the main program
if __name__ == "__main__":
  main()  # Call the main function