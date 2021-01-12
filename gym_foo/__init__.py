from gym.envs.registration import register

register(
    id='GridWorld-v0' , # 环境名,版本号v0必须有
    entry_point='gym_foo.env:GridEnv' , # 文件夹名.文件名:类名
    # 根据需要定义其他参数
)
