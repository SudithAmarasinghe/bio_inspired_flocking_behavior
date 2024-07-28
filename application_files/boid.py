# import numpy as np
# import pygame
# import json

# class Boid:
#     def __init__(self, position, velocity):
#         self.position = np.array(position, dtype='float64')
#         self.velocity = np.array(velocity, dtype='float64')
#         self.acceleration = np.zeros(2)

#     def apply_force(self, force):
#         self.acceleration += force

#     def align(self, boids, perception_radius, max_speed, max_force):
#         steering = np.zeros(2)
#         total = 0
#         for boid in boids:
#             if np.linalg.norm(boid.position - self.position) < perception_radius:
#                 steering += boid.velocity
#                 total += 1
#         if total > 0:
#             steering /= total
#             steering = self.set_magnitude(steering, max_speed)
#             steering -= self.velocity
#             steering = self.limit(steering, max_force)
#         return steering

#     def cohesion(self, boids, perception_radius, max_speed, max_force):
#         steering = np.zeros(2)
#         total = 0
#         for boid in boids:
#             if np.linalg.norm(boid.position - self.position) < perception_radius:
#                 steering += boid.position
#                 total += 1
#         if total > 0:
#             steering /= total
#             steering -= self.position
#             steering = self.set_magnitude(steering, max_speed)
#             steering -= self.velocity
#             steering = self.limit(steering, max_force)
#         return steering

#     def separation(self, boids, perception_radius, max_speed, max_force):
#         steering = np.zeros(2)
#         total = 0
#         for boid in boids:
#             distance = np.linalg.norm(boid.position - self.position)
#             if distance < perception_radius and distance > 0:
#                 diff = self.position - boid.position
#                 diff /= distance
#                 steering += diff
#                 total += 1
#         if total > 0:
#             steering /= total
#             steering = self.set_magnitude(steering, max_speed)
#             steering -= self.velocity
#             steering = self.limit(steering, max_force)
#         return steering

#     def update(self, max_speed):
#         self.velocity += self.acceleration
#         self.velocity = self.limit(self.velocity, max_speed)
#         self.position += self.velocity
#         self.acceleration *= 0

#     def edges(self, width, height):
#         if self.position[0] > width:
#             self.position[0] = 0
#         elif self.position[0] < 0:
#             self.position[0] = width
#         if self.position[1] > height:
#             self.position[1] = 0
#         elif self.position[1] < 0:
#             self.position[1] = height

#     def show(self, screen):
#         pygame.draw.circle(screen, (255, 255, 255), (int(self.position[0]), int(self.position[1])), 3)

#     @staticmethod
#     def set_magnitude(vector, mag):
#         return vector / np.linalg.norm(vector) * mag

#     @staticmethod
#     def limit(vector, max_mag):
#         if np.linalg.norm(vector) > max_mag:
#             vector = Boid.set_magnitude(vector, max_mag)
#         return vector














import numpy as np
import pygame
import json

class Boid:
    def __init__(self, position, velocity):
        self.position = np.array(position, dtype='float64')
        self.velocity = np.array(velocity, dtype='float64')
        self.acceleration = np.zeros(2)

    def apply_force(self, force):
        self.acceleration += force

    def align(self, boids, perception_radius, max_speed, max_force):
        steering = np.zeros(2)
        total = 0
        for boid in boids:
            if np.linalg.norm(boid.position - self.position) < perception_radius:
                steering += boid.velocity
                total += 1
        if total > 0:
            steering /= total
            steering = self.set_magnitude(steering, max_speed)
            steering -= self.velocity
            steering = self.limit(steering, max_force)
        return steering

    def cohesion(self, boids, perception_radius, max_speed, max_force):
        steering = np.zeros(2)
        total = 0
        for boid in boids:
            if np.linalg.norm(boid.position - self.position) < perception_radius:
                steering += boid.position
                total += 1
        if total > 0:
            steering /= total
            steering -= self.position
            steering = self.set_magnitude(steering, max_speed)
            steering -= self.velocity
            steering = self.limit(steering, max_force)
        return steering

    def separation(self, boids, perception_radius, max_speed, max_force):
        steering = np.zeros(2)
        total = 0
        for boid in boids:
            distance = np.linalg.norm(boid.position - self.position)
            if distance < perception_radius and distance > 0:
                diff = self.position - boid.position
                diff /= distance
                steering += diff
                total += 1
        if total > 0:
            steering /= total
            steering = self.set_magnitude(steering, max_speed)
            steering -= self.velocity
            steering = self.limit(steering, max_force)
        return steering

    def update(self, max_speed):
        self.velocity += self.acceleration
        self.velocity = self.limit(self.velocity, max_speed)
        self.position += self.velocity
        self.acceleration *= 0
        self.ensure_valid_position()

    def edges(self, width, height):
        if self.position[0] > width:
            self.position[0] = 0
        elif self.position[0] < 0:
            self.position[0] = width
        if self.position[1] > height:
            self.position[1] = 0
        elif self.position[1] < 0:
            self.position[1] = height

    def show(self, screen):
        if not np.isnan(self.position).any():
            pygame.draw.circle(screen, (255, 255, 255), (int(self.position[0]), int(self.position[1])), 3)

    def ensure_valid_position(self):
        if np.isnan(self.position).any():
            self.position = np.zeros(2)
        if np.isnan(self.velocity).any():
            self.velocity = np.zeros(2)
        if np.isnan(self.acceleration).any():
            self.acceleration = np.zeros(2)

    @staticmethod
    def set_magnitude(vector, mag):
        if np.linalg.norm(vector) == 0:
            return vector
        return vector / np.linalg.norm(vector) * mag

    @staticmethod
    def limit(vector, max_mag):
        if np.linalg.norm(vector) > max_mag:
            vector = Boid.set_magnitude(vector, max_mag)
        return vector
