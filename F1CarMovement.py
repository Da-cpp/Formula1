import pygame
import math
import os

class F1Car:

    def __init__(self, position=(400, 300), angle=0, image_path="F1_red.png", screen=None):
        # Core movement properties (simple and predictable)
        self.position = pygame.math.Vector2(position) # Center position
        self.speed = 0  # Scalar speed
        self.angle = angle  # Direction car is facing (0 = up)
        self.screen=screen #stores the screen reference
        
        # tunable parameters
        self.config = {
            'max_speed': 5.0,       # Top speed
            'acceleration': 0.1,    # Speed increase per frame
            'braking': 0.2,         # Speed decrease when braking
            'steering_speed': 3.0,  # Degrees turned per frame
            'friction': 0.95        # Speed retention when coasting
        }
        
        # Visual setup
        self.original_image = None
        self._load_image(image_path)
    
    def _load_image(self, image_path):
        """Simple image loading - no scaling or transformations"""
        try:
            # Try direct path first
            if os.path.exists(image_path):
                self.original_image = pygame.image.load(image_path).convert_alpha()
            else:
                # Try relative to script directory
                script_dir = os.path.dirname(os.path.abspath(__file__))
                img_path = os.path.join(script_dir, image_path)
                self.original_image = pygame.image.load(img_path).convert_alpha()
                
        except Exception as e:
            print(f"Image load failed: {e}")
            self._create_default_car()
    
    def _create_default_car(self):
        """Simple triangle car (classic arcade style)"""
        self.original_image = pygame.Surface((30, 15), pygame.SRCALPHA)
        pygame.draw.polygon(self.original_image, (220, 0, 0), 
                           [(0, 7), (25, 0), (30, 7), (25, 14)])
    
    def update(self, keys, dt=1):
        """physics update based on input keys"""
        # Handle acceleration simply
        if keys[pygame.K_UP]:
            self.speed += self.config['acceleration']
        elif keys[pygame.K_DOWN]:
            self.speed -= self.config['braking']
        else:
            # Natural coasting friction
            self.speed *= self.config['friction']
        
        # Cap speed at maximum
        self.speed = max(-self.config['max_speed']/2, min(self.speed, self.config['max_speed']))
        
        # Steering affects direction directly based on current speed
        if keys[pygame.K_LEFT]:
            self.angle -= self.config['steering_speed']
        if keys[pygame.K_RIGHT]:
            self.angle += self.config['steering_speed']
        
        # Normalize angle (0-360 degrees)
        self.angle = self.angle % 360
        
        # Movement is ALWAYS in direction car is facing (multiplied by speed)
        radians = math.radians(self.angle)
        self.position.x += math.sin(radians) * self.speed
        self.position.y -= math.cos(radians) * self.speed  # Pygame's Y is inverted

        if self.screen:
            screen_width, screen_height = self.screen.get_size()
            car_width, car_height = self.original_image.get_size()
            
            marginX = 19
            marginY= 58

            #keep car inside boundaries of the screen/background place.
            self.position.x = max(car_width // 2 - marginX, min(self.position.x, screen_width - car_width // 2 + marginX))
            self.position.y = max(car_height // 2 - marginY, min(self.position.y, screen_height - car_height // 2 + marginY))
    def draw(self, surface):
        """Simple rotation without any scaling"""
        if self.original_image:
            rotated = pygame.transform.rotate(self.original_image, -self.angle)
            width, height = rotated.get_size()
            rotated = pygame.transform.scale(rotated, (width // 3, height // 3))
            rect = rotated.get_rect(center=(int(self.position.x), int(self.position.y)))
            surface.blit(rotated, rect)
    
    def get_state(self):
        # Convert speed to velocity vector for compatibility
        radians = math.radians(self.angle)
        vx = math.sin(radians) * self.speed
        vy = -math.cos(radians) * self.speed  # Pygame Y inversion
        
        return {
            'position': (self.position.x, self.position.y),
            'velocity': (vx, vy),
            'angle': self.angle,
            'speed': self.speed
        }

# Example usage
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock() 
    
    car = F1Car()  # Uses F1_red.png in game directory
    
    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        car.update(keys, dt)
        
        screen.fill((50, 50, 50))
        car.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
