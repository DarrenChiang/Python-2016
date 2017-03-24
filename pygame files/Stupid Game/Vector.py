import math

class Vector:
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.d_angle = angle
        self.r_angle = math.radians(angle)
        self.v_component = -1 * int(self.magnitude * math.sin(self.r_angle))
        self.h_component = int(self.magnitude * math.cos(self.r_angle))

    def angle_degrees(self):
        return self.d_angle

    def angle_radians(self):
        return self.r_angle

    def magnitude(self):
        return self.magnitude

    def vertical(self):
        return self.v_component

    def horizontal(self):
        return self.h_component

    def set_angle(self, value):
        self.d_angle = value
        self.r_angle = math.radians(value)
        self.update_components()

    def change_angle(self, value):
        self.d_angle += value
        self.r_angle = math.radians(value)
        self.update_components()

    def set_magnitude(self, value):
        self.magnitude = value
        self.update_components()

    def change_magnitude(self, value):
        self.magnitude += value
        self.update_components()

    def update_components(self):
        self.v_component = -1 * int(self.magnitude * math.sin(self.r_angle))
        self.h_component = int(self.magnitude * math.cos(self.r_angle))

    def set_horizontal(self, value):
        self.h_component = value
        self.update_vector()

    def change_horizontal(self, value):
        self.h_component += value
        self.update_vector()

    def set_vertical(self, value):
        self.v_component = value
        self.update_vector()

    def change_vertical(self, value):
        self.v_component += value
        self.update_vector()    

    def update_vector(self):
        self.r_angle = math.atan2(-1 * self.v_component, self.h_component)
        self.d_angle = math.degrees(self.r_angle)
        self.magnitude = (self.h_component ** 2 + self.v_component ** 2) ** 0.5

    def stop(self):
        self.magnitude = 0
        self.update_components()
        
