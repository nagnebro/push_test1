from ursina import *

from scene.renscene import RenScene
from ui.renconversation import RenConversation


class Node:
    __slots__ = ['index', 'indent_level', 'content', 'code', 'children', 'is_answer']

    def __str__(self):
        return 'Node:\n    ' + '\n    '.join([f'{e} = {getattr(self, e)}' for e in Node.__slots__])



app = Ursina()
window.borderless = False
# Urisina 실행   , borderless 창의 border를 없애겠느냐는 옵션

# wp = WindowPanel(
#     title='Custom Window',
#     content=(
#         Text('Name:'),
#         InputField(name='name_field'),
#         Button(text='Submit', color=color.azure),
#         Slider(),
#         Slider(),
#         ButtonGroup(('test', 'eslk', 'skffk'))
#     ),
# )
# wp.y = wp.panel.scale_y / 2 * wp.scale_y  # center the window panel



ground = Entity(model='plane', collider='box', scale=64, texture='brick', texture_scale=(4, 4))
ground.rotation_x = -90

editor_camera = EditorCamera(enabled=False, ignore_paused=True)

b1 = Entity(model='cube', scale=2, position=(-3, 1, -1))
b2 = Entity(model='cube', scale=(2, 4, 1), position=(0, 4, -0.5))
b3 = Entity(model='cube', scale=(2, 4, 1), position=(2, 4, -0.5))
b4 = Entity(model='cube', scale=4, position=(6, 4, -2))
b5 = Entity(model='cube', scale=(4, 2, 1), position=(0, -4, -0.5))

player_graphics = SpriteSheetAnimation('Tressa', tileset_size=(6, 5), fps=4, animations={
    'idle_left': ((1, 4), (1, 4)),
    'idle_right': ((0, 4), (0, 4)),



    'walk_down': ((0, 3), (4, 3)),
    'walk_up': ((0, 2), (4, 2)),
    'walk_left': ((0, 1), (4, 1)),
    'walk_right': ((0, 0), (4, 0)),
})



player_graphics.play_animation('idle_right')
player_graphics.z = -0.5
player_graphics.scale_x = 0.6
player_graphics.rotation_x = -90



def input(key):
    if key == 'd':
        player_graphics.play_animation('walk_right')
    elif key == 'a':
        player_graphics.play_animation('walk_left')
    elif key == 'w':
        player_graphics.play_animation('walk_up')
    elif key == 's':
        player_graphics.play_animation('walk_down')
    elif key == 'a up':
        player_graphics.play_animation('idle_left')
    elif key == 'd up':
        player_graphics.play_animation('idle_right')


def update():
    player_graphics.y += held_keys['w'] * time.dt * 2
    player_graphics.y -= held_keys['s'] * time.dt * 2
    player_graphics.x += held_keys['d'] * time.dt * 1.2
    player_graphics.x -= held_keys['a'] * time.dt * 1.2

    camera.position = (player_graphics.x, player_graphics.y - 18, -6)
    camera.rotation_x = -75



sun = DirectionalLight(color=color.rgba(255, 255, 220, 255), shadows=True)
sun.look_at(Vec3(0.5, 1, 1))

sun_sub = DirectionalLight(color=color.rgba(110, 110, 110, 255), shadows=False)
sun_sub.look_at(Vec3(-0.5, 1, 1))

Sky()

RenScene(Empty(
    evil=0,
    chaos=0,
    font="NanumSquareRoundR.ttf",
    bar_mission_solved=False,
))





# item = Entity(parent=camera.ui, model='quad', texture='blueprint', scale=.3, z=2)

# start running the game
app.run()

# if __name__ == '__main__':
#     app = Ursina()
#     # conversation.question.model = 'quad'
#     # for b in conversation.buttons:
#     #     b.model = 'quad'
#
#     convo = dedent('''
#     I'm looking for my sister. Can you help me find her, please? I haven't seen her in days! Who know what could've happened!?
#     I'm worried. Will you help me?
#         * Yes, of course. This can be a dangerous city.
#             Oh no! Do you think something happened to her?
#             What should I do?!
#                 * She's probably fine. She can handle herself.
#                     You're right. I'm still worried though.
#                         * Don't worry, I'll look for her.
#                 * Maybe. (stats.chaos += 1)
#                     Help me look for her, please! *runs off*
#         * I'm sorry, but I don't have time right now. (evil += 1)
#             A true friend wouldn't say that.
#         * I know where she is! (if bar_mission_solved)
#             Really? Where?
#                 * I saw her on a ship by the docks, it looked like they were ready to set off.
#                     Thank you! *runs off*
#     ''')
#     conversation.start_conversation(convo)
#
#
#     # conversation.parse_conversation(convo)
#     # def input(key):
#     #     if key == 'left mouse down' and mouse.hovered_entity in conversation.buttons:
#     #         print('add sound here')
#
#     def input(key):
#         if key == 'space':
#             print(variables.evil)
#             # conversation.start_conversation()
#
#
#     # window.color = color._16
#     window.size = window.fullscreen_size * .5
#     Sprite('shore', z=1)
#     a
