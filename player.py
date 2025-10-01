import pygame 

class Man(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path ="player4.png"): #placeholder sprite
        super().__init__()
        self.sprite_sheet = pygame.image.load(image_path).convert_alpha()
        self.sprite_sheet.set_colorkey((0, 0, 0))
        self.frames = {
            "idle": [self.get_frame(0, 0)],                     
            "down": [self.get_frame(0, i) for i in range(1, 3)], 
            "up": [self.get_frame(0, i) for i in range(3, 5)],   
            "left": [self.get_frame(2, i) for i in range(3,5)], 
            "right": [self.get_frame(2, i) for i in range(0, 2)], 
        }
        self.direction = "down"
        self.frame_index = 0
        self.image = self.frames[self.direction][self.frame_index]
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 4
        self.animation_timer = 1
        self.animation_speed = 200

    def get_frame(self, row, col):
        frame_width = self.sprite_sheet.get_width() // 6  # 6 columns
        frame_height = self.sprite_sheet.get_height() // 4  # 4 rows
        x = col * frame_width
        y = row * frame_height

        # Extract the exact frame without overlapping
        frame = self.sprite_sheet.subsurface(pygame.Rect(x, y, frame_width, frame_height)).copy()
        frame.set_colorkey((0, 0, 0)) 

        # Scale the frame down 
        scaled_width = int(frame_width)  
        scaled_height = int(frame_height)
        return pygame.transform.scale(frame, (scaled_width, scaled_height))

    def update(self):
        keys = pygame.key.get_pressed()
        moved = False
        self.frame_index = 0  
        self.image = self.frames[self.direction][self.frame_index]  
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.direction = "left"
            moved = True
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.direction = "right"
            moved = True
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            self.direction = "up"
            moved = True
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            self.direction = "down"
            moved = True
        if moved:
            self.animation_timer += pygame.time.Clock().tick(60)
            if self.animation_timer >= self.animation_speed:
                self.animation_timer = 0
                self.frame_index = (self.frame_index + 1) % len(self.frames[self.direction])
                self.image = self.frames[self.direction][self.frame_index]
        else:
            self.direction == "idle"
            self.frame_index = 0
            self.image = self.frames["idle"][self.frame_index]        


    def draw(self, screen):
        screen.blit(self.image, self.rect)

def main():
    pygame.init()

    # Screen dimensions
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Player Test")

    # Clock for controlling the frame rate
    clock = pygame.time.Clock()

    # Create an instance of the Man class
    player = Man(x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2)

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the player
        player.update()

        # Clear the screen
        screen.fill((0, 0, 0))  

        # Draw the player
        player.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

