from gym.envs.registration import register

from .ssbm_env import SSBMEnv, simpleSSBMEnv

register(
    id='vladfi1/SSBM-v0',
    entry_point='dolphin:simpleSSBMEnv',
    reward_threshold=1,
    max_episode_steps=9999999,
    kwargs=dict(
      cpu=9,
      gui=True,
      stage='battlefield',
      mute=True,
      speed=0,
    ),
    nondeterministic=True,
)

register(
    id='vladfi1/SSBM-headless-v0',
    entry_point='dolphin:simpleSSBMEnv',
    reward_threshold=1,
    max_episode_steps=9999999,
    kwargs=dict(
      cpu=9,
      stage='battlefield',
    ),
    nondeterministic=True,
)
