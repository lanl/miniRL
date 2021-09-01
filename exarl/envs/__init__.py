from gym.envs import registration
from gym.envs.registration import register
import exarl.utils.candleDriver as cd


env = cd.run_params['env']


if env == 'ExaCartPoleStatic-v0':
    register(
        id=env,
        entry_point='exarl.envs.env_vault:ExaCartpoleStatic'
    )

