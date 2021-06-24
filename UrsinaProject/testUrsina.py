from ursina import * 
from ursina import camera


class Test_button(Button):
    def __init__(self, x, y):
        self.x = x, 
        self.y = y
        super().__init__(
            parent = scene,
            model = 'cube',
            texture = 'brick', 
            color = color.cyan, 
            highlight_color = color.lime, 
            pressed_color = color.red
        )
        
    def input(self, keyselected):
        if self.hovered:
            if keyselected == 'left mouse down':
                print("button pressed )")
                self.x += 2 * time.dt
                self.y += 1 * time.dt
            else:
                self.x = self.y
        else:
            print("il ne se pass rien")
                
        
def update():
    #entité sans classe
    if held_keys['z']:
        test_cube.y += 5 * time.dt
    elif held_keys['q']:
        test_cube.x -= 5 * time.dt
    elif held_keys['s']:
        test_cube.y -= 5 * time.dt
    elif held_keys['d']:
        test_cube.x += 5 * time.dt
    #animations
    elif held_keys['y']:
        test_cube.animate('rotation_y', test_cube.rotation_y + (90 * 0.5) / 2, duration = .1)
    elif held_keys['x']:
        test_cube.animate('rotation_x', test_cube.rotation_x + (90 * 0.5) / 2, duration = .1)
   
def red_button_click():
    print("click")   

test_cube = Entity(model = 'cube', color = color.red, scale = (2, 2), position = (2, 2), parent = camera.ui, collider = 'box', on_click = red_button_click)
thebutton_reference = Test_button(1, 2)


if __name__ == '__main__':
    app = Ursina()
    app.run()


#modèle collision 3d 

class Player(Entity):

    def update(self):
        self.direction = Vec3(
            self.forward * (held_keys['w'] - held_keys['s'])
            + self.right * (held_keys['d'] - held_keys['a'])
            ).normalized()  

        origin = self.world_position + (self.up*.5) 
        hit_info = raycast(origin , self.direction, ignore=(self,), distance=.5, debug=False)
        if not hit_info.hit:
            self.position += self.direction * 5 * time.dt

player = Player(model='cube', origin_y=-.5, color=color.orange)
wall_left = Entity(model='cube', collider='box', scale_y=3, origin_y=-.5, color=color.azure, x=-4)
wall_right = duplicate(wall_left, x=4)
camera.y = 2
