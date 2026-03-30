#!/usr/bin/python

DOCUMENTATION = r'''
---
module: press_button
short_description: Press one of the buttons on a bomb
description:
    - Ensure that one of the buttons on a bomb is pressed
version_added: "1.0.0"
options:
    name:
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
    name: BIG
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
from ansible.module_utils import get_bomb, update_bomb

def main():
    module_args = dict(
        name = dict(type = 'str', required = True),
        button = dict(type = 'str', required = True)
    )
    module = AnsibleModule(
        argument_spec = module_args,
        supports_check_mode = True
    )

    name = module.params['name']
    button = module.params['button']

    result = dict(
        changed = False,
        msg = ''
    )

    bomb = get_bomb(name)
    if bomb is None:
        module.fail_json(msg=f"Failed to find bomb details for bomb {name}", **result)

    if button in bomb.buttons:
        result.change = True
        result.msg = f"Pressed the {button} button of the {name} bomb."
    else:
        module.fail_json(msg=f"Failed to find {button} button in bomb {name}", **result)

    module.exit_json(**result)

if __name__ == '__main__':
    main()