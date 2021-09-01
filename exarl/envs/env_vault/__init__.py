import exarl.utils.candleDriver as cd

env = cd.run_params['env']

if env == 'ExaCartPoleStatic-v0':
    from exarl.envs.env_vault.ExaCartpoleStatic import ExaCartpoleStatic
