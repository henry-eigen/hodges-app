from app import app

import numpy as np
import pickle
from PIL import Image

class Region():
    def __init__(self, coords, seats, camera_ip=None):
        self.coords = coords
        self.seats = seats
        self.camera_ip = camera_ip
        self.pop = 0
        self.intensity = [(i, 1 - i, 0) for i in np.linspace(0.2, 0.8, 11)]
        
    def set_pop(self, population):
        self.pop = population
        
    def get_intensity(self):
        return self.intensity[int(np.round((np.clip(self.pop, 0, self.seats) / self.seats) * 10))]
    
class Floor():
    def __init__(self, name, img, path, regions, model=None):
        self.name = name
        self.regions = regions
        self.image = img
        self.path = path
        self.model = model
    
    def seat_list(self):
        return [r.seats for r in self.regions]
    
    def update(self):
        for region in self.regions:
            #cam = cv2.VideoCapture(region.camera_ip)
            #ret_val, img = cam.read()
            #RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            #image = Image.fromarray(RGB_img)
            #population = self.model.detect_image(image)
            population = np.random.randint(0, region.seats)
            region.set_pop(population)
            
    def save_img(self):
        result = Image.fromarray(np.uint8(self.render_img() * 255))
        result.save(self.path)
    
    def render_img(self):
        temp_img = np.copy(self.image)
        for i in self.regions:
            temp_img[i.coords[0]:i.coords[1], i.coords[2]:i.coords[3]] = i.get_intensity()
        return temp_img
