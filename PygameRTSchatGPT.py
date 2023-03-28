import pygame
from sys import exit
pygame. init()

#Display size width & height
window_width = 1400
window_height = 600

screen = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Space Explorers RTS')
clock = pygame.time.Clock()
game_font = pygame.font.Font('font/Pixeltype.ttf', 40)



#Display Clock cycle
clock_cycle = 60

GUI_surface = pygame.image.load('assets/GUI/ui_big_pieces_Grid.png')
MiniMap_surface = pygame.image.load('assets/GUI/ui_big_pieces_MiniMap2 (1).png').convert_alpha()
# Set the size for the image
DEFAULT_IMAGE_SIZE = (250, 300)
UNIT_SIZE = (50,50)
BUILDING_SIZE = (65,80)
GUI_surface = pygame.transform.scale(GUI_surface, DEFAULT_IMAGE_SIZE)
ground_surface = pygame.image.load('assets/Ground/ground.jpg').convert()
text_surface = game_font.render('My game', False, 'Maroon').convert_alpha()
MiniMap_surface = pygame.transform.scale(MiniMap_surface, DEFAULT_IMAGE_SIZE).convert_alpha()
bullet_surface = pygame.image.load('assets/Units/Bullet.png').convert_alpha()
refinery_surface = pygame.image.load('assets/Refinery/refinery0.png').convert_alpha()
refinery_surface = pygame.transform.scale(refinery_surface, BUILDING_SIZE)
refinery_building_rect= refinery_surface.get_rect(center = (1195,353))

soldier_surface = [pygame.image.load('assets/Units/sprite_1/sprite_0.png').convert_alpha(),
                   pygame.image.load('assets/Units/sprite_1/sprite_1.png').convert_alpha(),
                   pygame.image.load('assets/Units/sprite_1/sprite_2.png').convert_alpha(),
                   pygame.image.load('assets/Units/sprite_1/sprite_3.png').convert_alpha(),
                   pygame.image.load('assets/Units/sprite_1/sprite_4.png').convert_alpha(),
                   pygame.image.load('assets/Units/sprite_1/sprite_5.png').convert_alpha(),
                   pygame.image.load('assets/Units/sprite_1/sprite_6.png').convert_alpha()]

refinery_surface_array = [pygame.image.load('assets/Refinery/refinery0.png').convert_alpha(),
                          pygame.image.load('assets/Refinery/refinery10.png').convert_alpha(),
                          pygame.image.load('assets/Refinery/refinery20.png').convert_alpha(),
                          pygame.image.load('assets/Refinery/refinery30.png').convert_alpha(),
                          pygame.image.load('assets/Refinery/refinery40.png').convert_alpha(),
                          pygame.image.load('assets/Refinery/refinery50.png').convert_alpha(),
                          pygame.image.load('assets/Refinery/refinery60.png').convert_alpha(),
                          pygame.image.load('assets/Refinery/refinery70.png').convert_alpha(),
                          pygame.image.load('assets/Refinery/refinery80.png').convert_alpha(),
                          pygame.image.load('assets/Refinery/refinery90.png').convert_alpha(),
                          pygame.image.load('assets/Refinery/refinery100.png').convert_alpha()]

frame_index = 0
soldier_center = (200,200)

# Scale the soldier images
scaled_soldier_images = []
scaled_soldier_rect = []
scaled_soldier_attack_rect = []
scaled_bullet_rect = []
for image in soldier_surface:
    scaled_image = pygame.transform.scale(image, UNIT_SIZE)
    soldier_rect = scaled_image.get_rect(center = (soldier_center[0] + 80, soldier_center[1] + 200))
    soldier_attack_rect = scaled_image.get_rect(center = (soldier_center[0] + 160, soldier_center[1] + 400))
    scaled_soldier_images.append(scaled_image)
    
    scaled_soldier_rect.append(soldier_rect)
    bullet_rect = bullet_surface.get_rect(midtop = soldier_rect.topright)
    scaled_soldier_attack_rect.append(soldier_attack_rect)

scaled_refinery_images = []
scaled_refinery_rect_array = []

for image in refinery_surface_array:
    scaled_image = pygame.transform.scale(image, BUILDING_SIZE)
    refinery_rect_array = scaled_image.get_rect(center = (1150, 600))
    scaled_refinery_images.append(scaled_image)
    scaled_refinery_rect_array.append(refinery_rect_array)


#Player Variables
player_resource = '0'

#Player Resources surface
text_resource = game_font.render('Al:', False, 'Maroon')
playerNum_resources = game_font.render(player_resource, False, 'Maroon')

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            mouse_current_position = event.pos
            print(event.pos)

        

    screen.fill('black') 

    #Text resources is 10 from top screen and resources value is 190 to the right of it with 10 from top
    screen.blit(ground_surface, (0,0))
    screen.blit(text_resource,(1120,10))
    screen.blit(playerNum_resources,(1150,10))
    screen.blit(GUI_surface,(1150,300))
    screen.blit(MiniMap_surface,(1150,0))
    screen.blit(refinery_surface,refinery_building_rect)
    old_refinery_rect = pygame.Rect(10,10,100,100)
    new_refinery_rect = pygame.Rect(10,10,100,100)
    old_refinery_rect = refinery_building_rect.copy()
    #Calls Soldier current position
    soldier_current_pos = scaled_soldier_rect[0]

    #Below we have 4 arrow key press functions and the space bar fire button
    #The arrow keys move the charater and checks for boundaries. Do not let the sprite outside the boundary, if outside move to fixed value
    keys = pygame.key.get_pressed()
    soldier_speed = 2
    if keys[pygame.K_RIGHT]:
        for x in range(len(scaled_soldier_rect)):
            if scaled_soldier_rect[x].centerx <= window_width-300:
                scaled_soldier_rect[x].centerx += soldier_speed
            else :
                scaled_soldier_rect[x].centerx = window_width-300
    if keys[pygame.K_LEFT]:
        for x in range(len(scaled_soldier_rect)):
            if scaled_soldier_rect[x].centerx >= 30:
                scaled_soldier_rect[x].centerx -= soldier_speed
            else :
                scaled_soldier_rect[x].centerx = 30
    if keys[pygame.K_DOWN]:
        for x in range(len(scaled_soldier_rect)):
            if scaled_soldier_rect[x].centery <= window_height-30:
                scaled_soldier_rect[x].centery += soldier_speed
            else :
                scaled_soldier_rect[x].centery = window_height-30
    if keys[pygame.K_UP]:
        for x in range(len(scaled_soldier_rect)):
            if scaled_soldier_rect[x].centery >= 30:
                scaled_soldier_rect[x].centery -= soldier_speed
            else :
                scaled_soldier_rect[x].centery = 30
    if keys[pygame.K_SPACE]:
        #This if statement calls the current position of the soldier rectangle and updates the position of the bullet when the space bar is pressed
        bullet_rect.midtop = soldier_current_pos.topright
        screen.blit(bullet_surface, bullet_rect)
    mouse_pos = pygame.mouse.get_pos()
    if (pygame.mouse.get_pressed() == (1, 0, 0)):
        new_refinery_rect = old_refinery_rect.copy()
        new_refinery_rect.move(mouse_current_position)
        screen.blit(new_refinery_rect, mouse_current_position)
        print('you clicked me')

    

    # Draw the current sprite frame
    screen.blit(scaled_soldier_images[frame_index], scaled_soldier_rect[frame_index])
    
    
    #Increase the Play's Resource
    player_resource = str(int(player_resource) + 1)
    #Reassign resource value for rendering
    playerNum_resources = game_font.render(player_resource, False, 'Maroon')


    pygame.display.update()

    # Increment the frame index
    frame_index = (frame_index + 1) % len(soldier_surface)

    clock.tick(clock_cycle)
