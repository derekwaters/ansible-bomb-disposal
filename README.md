# ansible-bomb-disposal

**Scenario:** You've been recruited to a bomb disposal division where they use Ansible to safely dispose of bombs. A criminal mastermind has started on a bombing spree and they need you help to clear things up as soon as possible!


1. Welcome to the Squad! *(Ansible Coding Basics)*

    1. The basics of a playbook
    2. Modules and debug
    3. Using Roles and Collections
    4. Templates and Vars
    5. Conditionals
    6. Loops
    7. Idempotency (Also tags, and multiple plays in a playbook)

2. Now Let's Work With The Team *(Code Reuse and Style)*

    1. Linting
    2. AAP Deployment
    3. Building a Role and Collection

3. Too Slow! *(GitOps and Event-Driven Automation)*

    1. GitOps and Webhooks
    2. Event-Driven Ansible

4. Too Insecure! *(Securing the Automation Process)*

    1. Credentials and Vaults
    2. Automation Content (Hub / EEs / Image Registries)
    3. Code Signing


Ansible code basics:
  -> modules + debug
  -> using collections
  -> templates and setting vars.  (examine bomb, get list of wires)
  -> conditionals (when)
  -> loops (cut multiple wires)
  -> idempotency? Rerun playbooks (state: cut)
Now coding style:
  -> lint it (custom lint rule?)
  -> deploy it to AAP (manually create project and sync, create job template then run)
Speed up the process:
  -> GitOps
  -> EDA
Secure the process:
  -> Credential Vaults
  -> Hub / EEs / Image Registry
  -> Code Signing
