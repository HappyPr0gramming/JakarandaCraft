from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from math import sqrt
import random
from perlin_noise import PerlinNoise
from math import ceil


noise = PerlinNoise(octaves=3, seed=random.randint(1,100))

app = Ursina(fullscreen=True)
player = FirstPersonController()
player.position = (30, 5, 30)


sky = Sky()

blox = ['wood.png', 'stone.png', 'bricks.png', 'gold.png', 'grass.png']
bloxy = 1

radius = 20

all_boxes = []

def text(a):
    text = Text(text=a, origin=(0, 7), scale=2, color=color.black)
    invoke(destroy, text, delay=2)



arm = Entity(
    parent= camera.ui,
    model= 'cube',
    color = color.peach,
    position= (0.75, -0.6),
    rotation= (150, -10, 6),
    scale= (0.2, 0.2, 1.5)
)

def update():


    if held_keys['left mouse'] or held_keys['right mouse']:
        arm.position = (0.6, -0.5)
    else:
        arm.position = (0.75, -0.6)

    for box in all_boxes:
        distance = sqrt((box.position - player.position).length_squared())
        if distance <= radius:
            box.enabled = True
        else:
            box.enabled = False







for i in range(60):
    for j in range(60):
        height_value = ceil(noise([i / 60, j / 60]) * 10)
        box = Button(color=color.white, model='cube', position=(j,height_value,i),
            texture ='grass.png', parent=scene, origin_y=0.5)
        all_boxes.append(box)

plane = Entity(color=color.black, model='cube', position=(30,30,30), scale=(160,160,160), collider='box')





a = 1
inv = 0
kill = 0

def input(key):

    global bloxy, pro
    global kill


    for box in all_boxes:


        if box.hovered:
            if key == 'left mouse down':
                new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                             texture=blox[bloxy], parent=scene, origin_y=0.5)
                all_boxes.append(new)
            elif key == '1':
                text('Wood')
                bloxy = 0
                return bloxy
            elif key == '2':
                text('Stone')
                bloxy = 1
                return bloxy
            elif key == '3':
                text('Bricks')
                bloxy = 2
                return bloxy
            elif key == '4':
                text('Gold')
                bloxy = 3
                return bloxy
            elif key == '5':
                text('Grass')
                bloxy = 4
                return bloxy

            elif key == 'right mouse down':
                kill += 1
                if kill == 1:
                    box.texture = 'damaged.png'
                elif kill == 2:
                    box.texture = 'broken.png'
                elif kill == 3:
                    all_boxes.remove(box)
                    destroy(box)
                    kill = 0





app.run()