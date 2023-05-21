from ursina import *



app = Ursina()
window.borderless = False
window.color = color._16
background = Entity(parernt = camera.ui, model ="quad", color = color.white,   scale=(100, 100),z=4,world_y=0)
cursor = Entity(parent=camera.ui, model="quad", texture="brain.png", color=color.white , scale=.2, y=0)

# text = Text(parent=cursor, text='x', z=-1, world_scale=25, y=1.25, origin=(0,0))
# mesh = Entity(parent=camera.ui, model=Mesh(mode='point', thickness=10), color=color.white).model

window.size = window.fullscreen_size * 1

app.run()