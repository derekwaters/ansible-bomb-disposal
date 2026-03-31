import os
import json

DEF_FILE_NAME: str = "/tmp/bombs.json"

def get_bomb(name):
    defs = get_bombs_definition()
    if name in defs:
        return defs[name]
    return None

def update_bomb(name, bomb_defs):
    defs = get_bombs_definition()
    defs[name] = bomb_defs
    with open(DEF_FILE_NAME, "w") as f:
        json.dump(defs, f)
    
def get_bombs_definition():
    defs = dict()
    if os.path.isfile(DEF_FILE_NAME):
        with open(DEF_FILE_NAME, "r") as f:
            defs = json.load(f)
    else:
        defs = default_bombs_definition()
        with open(DEF_FILE_NAME, "w") as f:
            json.dump(defs, f)
    return defs

def default_bombs_definition():
    return dict(
        dummy = dict(
            wires = dict(
                yellow = False,
                red = False,
                green = False,
                blue = False
            ),
            buttons = dict(
                reset = False
            ),
            knobs = dict(
                volume = dict(
                    min = 1,
                    max = 10,
                    current = 1
                ),
                tone = dict(
                    min = 1,
                    max = 5,
                    current = 3
                )
            ),
            timer_type = 'gold watch'
        )
    )
