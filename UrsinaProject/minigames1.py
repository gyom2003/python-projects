from ursina import *

app = Ursina()
window.color = color._20

gold = 0

class Counter_ref(Text):
    def __init__(self, ):
        super().__init__(
            text='0', 
            origin = (0, 0),
            y=.25,
            scale=2, 
            background=True
        ),
        
class Button_ref(Button):
    def __init__(self, ):
        super().__init__(
            text='+', 
            color=color.azure, 
            scale= .125
        )
        
button_2 = Button(cost=10, x=.2, scale=.125, color=color.dark_gray, disabled=True)
button_2.tooltip = Tooltip(f'<gold>générateur d or\n<default>gagne 1 or toutes les secondes. Couts {button_2.cost} or.')

#references des classes
counter = Counter_ref()
button = Button_ref()

def button_click():
    global gold
    gold += 1
    counter.text = str(gold)

button.on_click = button_click

def buy_gold():
    global gold 
    if gold >= button_2.cost:
        gold -= button_2.cost
        counter.text = str(gold)
        invoke(generate_gold, 1, 1)
        
button_2.on_click = buy_gold()

def generate_gold():
    global gold
    gold += 1
    counter.text = str(gold)
    invoke(generate_gold, 1, 1)
    
def deuxbutton_click():
    global gold
    gold -= button_2.cost  
    counter.text = str(gold)
    

def update():
    #tourne en boucle 
    global gold
    for b in (button_2, ):
        if gold >= b.cost:
            b.disabled = False
            b.color = color.green
        else:
            b.disabled = True
            b.color = color.gray



app.run()