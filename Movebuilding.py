import pygame

# Initialize Pygame
pygame.init()

# Set up your screen
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the Refinery image
BUILDING_SIZE = (100, 100)
refinery_surface = pygame.image.load('assets/Refinery/refinery0.png').convert_alpha()
refinery_surface = pygame.transform.scale(refinery_surface, BUILDING_SIZE)
refinery_building_rect = refinery_surface.get_rect(center=(1195, 353))

placed_buildings = []

dragging = False
dragged_surface = None
dragged_rect = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not dragging:
                # Check if the click is within the refinery_building_rect
                if refinery_building_rect.collidepoint(event.pos):
                    # Create a new surface (a copy of the original) and a new rect
                    dragged_surface = refinery_surface.copy()
                    dragged_rect = dragged_surface.get_rect(center=event.pos)

                    # Start dragging
                    dragging = True
            else:
                # Add the new surface and rect to the placed_buildings list
                placed_buildings.append((dragged_surface, dragged_rect))

                # Stop dragging
                dragging = False

    if dragging:
        # Update the position of the dragged surface to follow the mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dragged_rect.center = (mouse_x, mouse_y)

    screen.fill((0, 0, 0))
    screen.blit(refinery_surface, refinery_building_rect)

    # Draw the placed buildings
    for surface, rect in placed_buildings:
        screen.blit(surface, rect)

    # Draw the dragged surface
    if dragged_surface is not None and dragged_rect is not None:
        screen.blit(dragged_surface, dragged_rect)

    pygame.display.flip()

pygame.quit()
