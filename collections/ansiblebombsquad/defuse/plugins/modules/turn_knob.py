#!/usr/bin/python

DOCUMENTATION = r'''
---
module: turn_knob
short_description: Turn one of the knobs on a bomb
description:
    - Ensure that one of the knobs on a bomb is turned to a specific value
version_added: "1.0.0"
options:
    name:
        description: Name of the bomb
        required: true
        type: str
    knob:
        description: Name of the knob being turned
        required: true
        type: str
    setting:
        description: Number to set the knob to
        required: true
        type: integer
'''

EXAMPLES = r'''
- name: Turn the Volume knob on the BIG bomb to 6
  ansiblebombsquad.defuse.turn_knob:
    name: BIG
    knob: Volume
    setting: 6
'''

RETURN = r'''
changed:
    description: Whether the knob was turned
    type: bool
    returned: always
msg:
    description: Human-readable message about the state of the knob
    type: str
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.bomb_simulator import get_bomb, update_bomb

def main():
    module_args = dict(
        name = dict(type = 'str', required = True),
        knob = dict(type = 'str', required = True),
        setting = dict(type = 'integer', required = True)
    )
    module = AnsibleModule(
        argument_spec = module_args,
        supports_check_mode = True
    )

    name = module.params['name']
    knob = module.params['knob']
    setting = module.params['setting']

    result = dict(
        changed = False,
        msg = ''
    )

    bomb = get_bomb(name)
    if bomb is None:
        module.fail_json(msg=f"Failed to find bomb details for bomb {name}", **result)

    if knob in bomb.knobs:
        current_state = bomb.knobs[knob]
        if current_state.current == setting:
            # Already set
            result.change = False
            result.msg = f"The {knob} knob of the {name} bomb was already set to {setting}."
        else if setting >= current_state.min and setting <= current_state.max:
            result.change = True
            result.msg = f"Set the {knob} knob of the {name} bomb to {setting}."
            bomb.knobs[knob].current = setting
            update_bomb(bomb)
        else:
            module.fail_json(msg=f"Failed to set {knob} knob in bomb {name} to {setting} as the value is out of range", **result)
    else:
        module.fail_json(msg=f"Failed to find {knob} knob in bomb {name}", **result)

    module.exit_json(**result)

if __name__ == '__main__':
    main()