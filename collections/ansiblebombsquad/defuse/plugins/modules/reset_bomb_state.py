#!/usr/bin/python

DOCUMENTATION = r'''
---
module: reset_bomb_state
short_description: Reset the state of a bomb
description:
    - Reset the state of a bomb
version_added: "1.0.0"
options:
    bomb_name:
        description: Name of the bomb
        required: true
        type: str
'''

EXAMPLES = r'''
- name: Reset the state of the BIG bomb
  ansiblebombsquad.defuse.reset_bomb_state:
    bomb_name: BIG
'''

RETURN = r'''
state:
    description: The state of the bomb
    type: dict
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.bomb_simulator import reset_bomb

def main():
    module_args = dict(
        bomb_name = dict(type = 'str', required = True)
    )
    module = AnsibleModule(
        argument_spec = module_args,
        supports_check_mode = True
    )

    name = module.params['bomb_name']

    bomb = reset_bomb(name)
    if bomb is None:
        module.fail_json(msg=f"Failed to find bomb details for bomb {name}")

    module.exit_json(state=bomb)

if __name__ == '__main__':
    main()