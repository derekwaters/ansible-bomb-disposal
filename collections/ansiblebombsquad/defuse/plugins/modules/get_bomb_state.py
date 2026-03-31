#!/usr/bin/python

DOCUMENTATION = r'''
---
module: get_bomb_state
short_description: Get the state of a bomb
description:
    - Get the state of a bomb
version_added: "1.0.0"
options:
    name:
        description: Name of the bomb
        required: true
        type: str
'''

EXAMPLES = r'''
- name: Get the state of the BIG bomb
  ansiblebombsquad.defuse.get_bomb_state:
    name: BIG
'''

RETURN = r'''
state:
    description: The state of the bomb
    type: dict
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.bomb_simulator import get_bomb

def main():
    module_args = dict(
        name = dict(type = 'str', required = True)
    )
    module = AnsibleModule(
        argument_spec = module_args,
        supports_check_mode = True
    )

    name = module.params['name']

    bomb = get_bomb(name)
    if bomb is None:
        module.fail_json(msg=f"Failed to find bomb details for bomb {name}")

    module.exit_json(state=bomb)

if __name__ == '__main__':
    main()