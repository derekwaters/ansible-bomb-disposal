#!/usr/bin/python

DOCUMENTATION = r'''
---
module: press_button
short_description: Press one of the buttons on a bomb
description:
    - Ensure that one of the buttons on a bomb is pressed
version_added: "1.0.0"
options:
    bomb_name:
        description: Name of the bomb
        required: true
        type: str
    button:
        description: Name of the button being pressed
        required: true
        type: str
'''

EXAMPLES = r'''
- name: Press the CLEAR button on the BIG bomb
  ansiblebombsquad.defuse.press_button:
    bomb_name: BIG
    button: CLEAR
'''

RETURN = r'''
changed:
    description: Whether the button was pressed
    type: bool
    returned: always
msg:
    description: Human-readable message about the state of the button
    type: str
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.bomb_simulator import get_bomb, update_bomb

def main():
    module_args = dict(
        bomb_name = dict(type = 'str', required = True),
        button = dict(type = 'str', required = True)
    )
    module = AnsibleModule(
        argument_spec = module_args,
        supports_check_mode = True
    )

    name = module.params['bomb_name']
    button = module.params['button']

    result = dict(
        changed = False,
        msg = ''
    )

    bomb = get_bomb(name)
    if bomb is None:
        module.fail_json(msg=f"Failed to find bomb details for bomb {name}", **result)

    if button in bomb['buttons']:
        result['changed'] = True
        result['msg'] = f"Pressed the {button} button of the {name} bomb."
        bomb['buttons'][button] = True
        update_bomb(name, bomb)
    else:
        module.fail_json(msg=f"Failed to find {button} button in bomb {name}")

    module.exit_json(**result)

if __name__ == '__main__':
    main()