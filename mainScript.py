
from re import purge
from ursina import * 
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.editor_camera import *
from ursina import camera
from ursina import mouse


app = Ursina()

grass = load_texture("image/grass_block.png")
stone = load_texture("image/stone_block.png")
brick = load_texture("image/brick_block.png")
dirt = load_texture("image/dirt_block.png")
sky = load_texture("assets/skybox.png")
arm_texture = load_texture("image/arm_texture.png")
arm_sound = Audio("assets/punch_sound", loop = False, autoplay = False)
block_pick_number = 1

def updtate():
    
    if held_keys['left mouse'] or held_keys['right mouse']:
        #hand.active()
        pass
    else:
        #hand.passive()
        pass
    
    
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene, 
            model = 'sphere',
            texture= sky, 
            scale = 150, 
            double_sided = True,  
        )
        
class Hand(Entity):
    def __init__():
        super().__init__(
            parent = camera.ui,
            model =  load_model('assets/arm'), 
            texture = arm_texture, 
            scale = 0.2,
            rotation = Vec3(120, -10, 0),  
            position = Vec2(0.4, -0.6))
        
    def active(self):
        self.position = Vec2(0.3, -0.5)
    
    def passive(self):
        self.position = Vec2(0.4, -0.6)
        
        

    

class Voxel(Button):
    def __init__(self, position=(0,0,0), texture = grass):
        super().__init__(
            parent = scene,
            position = position,
            model = load_model('assets/block'), 
            origin_y = .5,
            texture = texture, #'white_cube'
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.lime,
            scale = 0.5, 
        )


    def input(self, key):       
        if self.hovered:
            if key == 'left mouse down':
                global block_pick_number
                if held_keys['1']:block_pick_number = 1
                if held_keys['2']:block_pick_number = 2
                if held_keys['3']:block_pick_number = 3
                if held_keys['4']:block_pick_number = 4 
                
                if block_pick_number == 1:
                    voxel = Voxel(position=self.position + mouse.normal, texture = grass)
                elif block_pick_number == 2:
                    voxel = Voxel(position=self.position + mouse.normal, texture = stone)
                elif block_pick_number == 3:
                    voxel = Voxel(position=self.position + mouse.normal, texture = brick)
                elif block_pick_number == 4:
                    voxel = Voxel(position=self.position + mouse.normal, texture = dirt)
                arm_sound.play()
               
                    

            if key == 'right mouse down':
                arm_sound.play()
                destroy(self)


for z in range(20):
    for x in range(20):
        voxel = Voxel(position=(x,0,z))


player = FirstPersonController()
sky = Sky()
#hand = Hand()
app.run()