get_bomb_state
==============

Get Bomb State (get_bomb_state) 

Requirements
------------

The role retrieves the state of a named bomb. 

Role Variables
--------------

The name of the bomb whose state will be retrieved should be set as 'bomb_name'. The state will be returned in a variable names 'bomb_state'

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: ansiblebombsquad.defuse.get_bomb_state, bomb_name: MOAB }

License
-------

GPL-v3.0

Author Information
------------------

Derek Waters
dwaters@redhat.com
