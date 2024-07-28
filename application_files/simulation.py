# import pygame
# import numpy as np
# import csv
# import json
# from boid import Boid

# def load_initial_conditions(filename):
#     positions = []
#     velocities = []
#     with open(filename, 'r') as csvfile:
#         reader = csv.reader(csvfile)
#         next(reader)  # Skip header
#         for row in reader:
#             positions.append([float(row[0]), float(row[1])])
#             velocities.append([float(row[2]), float(row[3])])
#     return positions, velocities

# def load_config(filename):
#     with open(filename, 'r') as f:
#         return json.load(f)

# def load_environment(filename):
#     with open(filename, 'r') as f:
#         return json.load(f)

# def main():
#     pygame.init()

#     # Load configurations and initial conditions
#     config = load_config('config.json')
#     environment = load_environment('environment.json')
#     positions, velocities = load_initial_conditions('initial_conditions.csv')

#     screen = pygame.display.set_mode((config['width'], config['height']))
#     clock = pygame.time.Clock()

#     boids = [Boid(pos, vel) for pos, vel in zip(positions, velocities)]

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False

#         screen.fill((0, 0, 0))

#         # Draw obstacles
#         for obstacle in environment['obstacles']:
#             pygame.draw.circle(screen, (255, 0, 0), (obstacle['x'], obstacle['y']), obstacle['radius'])

#         for boid in boids:
#             boid.edges(config['width'], config['height'])

#             alignment = boid.align(boids, config['perception_radius'], config['max_speed'], config['max_force'])
#             cohesion = boid.cohesion(boids, config['perception_radius'], config['max_speed'], config['max_force'])
#             separation = boid.separation(boids, config['perception_radius'], config['max_speed'], config['max_force'])

#             boid.apply_force(alignment)
#             boid.apply_force(cohesion)
#             boid.apply_force(separation)

#             boid.update(config['max_speed'])
#             boid.show(screen)

#         pygame.display.flip()
#         clock.tick(60)

#     pygame.quit()

# if __name__ == '__main__':
#     main()










import pygame
import numpy as np
import csv
import json
from boid import Boid

def load_initial_conditions(filename):
    positions = []
    velocities = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            try:
                positions.append([float(row[0]), float(row[1])])
                velocities.append([float(row[2]), float(row[3])])
            except ValueError as e:
                print(f"Skipping malformed row: {row} - Error: {e}")
    return positions, velocities

def load_config(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def load_environment(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def main():
    pygame.init()

    # Load configurations and initial conditions
    config = load_config('config.json')
    environment = load_environment('environment.json')
    positions, velocities = load_initial_conditions('initial_conditions.csv')

    screen = pygame.display.set_mode((config['width'], config['height']))
    clock = pygame.time.Clock()

    boids = [Boid(pos, vel) for pos, vel in zip(positions, velocities)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        # Draw obstacles
        for obstacle in environment['obstacles']:
            pygame.draw.circle(screen, (255, 0, 0), (obstacle['x'], obstacle['y']), obstacle['radius'])

        for boid in boids:
            boid.edges(config['width'], config['height'])

            alignment = boid.align(boids, config['perception_radius'], config['max_speed'], config['max_force'])
            cohesion = boid.cohesion(boids, config['perception_radius'], config['max_speed'], config['max_force'])
            separation = boid.separation(boids, config['perception_radius'], config['max_speed'], config['max_force'])

            boid.apply_force(alignment)
            boid.apply_force(cohesion)
            boid.apply_force(separation)

            boid.update(config['max_speed'])
            boid.show(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
