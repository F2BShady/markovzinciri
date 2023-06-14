import pyglet
import random

window = pyglet.window.Window(width=800, height=600)
batch = pyglet.graphics.Batch()

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

shapes = []
for color in colors:
    shape = pyglet.shapes.Circle(x=0, y=0, radius=50, color=color, batch=batch)
    shapes.append(shape)

markov_chain = [
    [0.2, 0.4, 0.4],
    [0.3, 0.2, 0.5],
    [0.5, 0.3, 0.2]
]

current_state = random.choice(range(len(colors)))

def update(dt):
    global current_state
    probabilities = markov_chain[current_state]
    next_state = random.choices(range(len(colors)), probabilities)[0]
    current_state = next_state
    shape = shapes[current_state]
    shape.x = random.randint(0, window.width - shape.radius * 2)
    shape.y = random.randint(0, window.height - shape.radius * 2)
    shape.radius = random.randint(20, 80)  

@window.event
def on_draw():
    window.clear()
    batch.draw()

pyglet.clock.schedule_interval(update, 1/5)

pyglet.app.run()
