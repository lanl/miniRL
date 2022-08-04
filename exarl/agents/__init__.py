from exarl.agents.registration import register, make
from exarl.utils.globals import ExaGlobals
try:
    agent = ExaGlobals.lookup_params('agent')
except:
    agent = None

if agent == 'DQN-v0':
    register(
        id=agent,
        entry_point='exarl.agents.agent_vault:DQN'
    )
elif agent == 'DDPG-v0':
    register(
        id=agent,
        entry_point='exarl.agents.agent_vault:DDPG'
    )
