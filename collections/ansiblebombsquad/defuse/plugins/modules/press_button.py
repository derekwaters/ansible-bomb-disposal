from ansible.module_utils.basic import AnsibleModule

def run_module():
    module = AnsibleModule(argument_spec={})
    module.exit_json(changed=True, msg="Hello from my module!")

if __name__ == '__main__':
    run_module()