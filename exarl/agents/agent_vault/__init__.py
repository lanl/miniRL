from exarl.utils.globals import ExaGlobals
try:
    agent = ExaGlobals.lookup_params('agent')
except:
    agent = None

if agent == 'DQN-v0':
    from exarl.agents.agent_vault.dqn import DQN
elif agent == 'DDPG-v0':
    from exarl.agents.agent_vault.ddpg import DDPG
