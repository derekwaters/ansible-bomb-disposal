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
  ansiblebombsquad.defus.cut_wire:
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

    # Do something here with the status
    result.change = True
    result.msg = f"Cut the {colour} wire of the {name} bomb."

    

    module.exit_json(**result)

if __name__ == '__main__':
    main()