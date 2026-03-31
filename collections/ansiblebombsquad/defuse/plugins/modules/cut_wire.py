#!/usr/bin/python

DOCUMENTATION = r'''
---
module: cut_wire
short_description: Cut one of the wires on a bomb
description:
    - Ensure that one of the wires on a bomb is cut
version_added: "1.0.0"
options:
    name:
        description: Name of the bomb
        required: true
        type: str
    colour:
        description: Colour of the wire being cut
        required: true
        type: str
'''

EXAMPLES = r'''
- name: Cut the blue wire on the BIG bomb
  ansiblebombsquad.defuse.cut_wire:
    name: BIG
    colour: blue
'''

RETURN = r'''
changed:
    description: Whether the wire was cut
    type: bool
    returned: always
msg:
    description: Human-readable message about the state of the wire
    type: str
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.bomb_simulator import get_bomb, update_bomb

def main():
    module_args = dict(
        name = dict(type = 'str', required = True),
        colour = dict(type = 'str', required = True)
    )
    module = AnsibleModule(
        argument_spec = module_args,
        supports_check_mode = True
    )

    name = module.params['name']
    colour = module.params['colour']

    result = dict(
        changed = False,
        msg = ''
    )

    bomb = get_bomb(name)
    if bomb is None:
        module.fail_json(msg=f"Failed to find bomb details for bomb {name}", **result)

    if colour in bomb.wires:
        current_state = bomb.wires[colour]
        if current_state:
            # Already cut
            result.change = False
            result.msg = f"The {colour} wire of the {name} bomb had already been cut."
        else:
            result.change = True
            result.msg = f"Cut the {colour} wire of the {name} bomb."
            bomb.wires[colour] = True
            update_bomb(bomb)
    else:
        module.fail_json(msg=f"Failed to find {colour} wire in bomb {name}", **result)

    module.exit_json(**result)

if __name__ == '__main__':
    main()