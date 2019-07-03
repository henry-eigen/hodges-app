from flask import render_template, url_for
import os
from app import app

import time
import threading

from app.functions import load_floor
from PIL import Image


MAP_FOLDER = os.path.join('static')
app.config['UPLOAD_FOLDER'] = MAP_FOLDER


# -----------------------------------------------------------------

@app.before_first_request
def activate_job():
    def run_job():
        while True:
            for i in ["Floor 3", "Floor 4", "Floor 5", "Floor 6"]:
                f = load_floor(i)
                f.update()
                f.save_img()
            time.sleep(5)
            print("update complete")
            

    thread = threading.Thread(target=run_job)
    thread.start()

# -----------------------------------------------------------------

@app.route('/')
@app.route('/index')
def index():
        
    img_src_3 = os.path.join(app.config['UPLOAD_FOLDER'], 'floor_maps', 'map_3.png')
    img_src_4 = os.path.join(app.config['UPLOAD_FOLDER'], 'floor_maps', 'map_4.png')
    img_src_5 = os.path.join(app.config['UPLOAD_FOLDER'], 'floor_maps', 'map_5.png')
    img_src_6 = os.path.join(app.config['UPLOAD_FOLDER'], 'floor_maps', 'map_6.png')
    
    
    return render_template('grid.html', title='Home', 
                           user_image_3=img_src_3,
                           user_image_4=img_src_4,
                           user_image_5=img_src_5,
                           user_image_6=img_src_6)

@app.route('/video')
def video():
    
    
    return render_template('video.html', title='Video')

# -----------------------------------------------------------------






