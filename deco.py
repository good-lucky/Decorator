
def priv_check(fn):
    def fx(name, x):
        print("正在权限验证...")
        fn(name, x)
    return fx


def message_send(fn):
    def fy(name, x):
        fn(name, x)
        print("短信: ", name, "发生了", x, "元的操作，余额是xxx")
    return fy


@priv_check
def save_money(name, x):
    print(name, "存钱", x, "元")


@message_send
@priv_check
def withdraw(name, x):
    print(name, "正在办理取钱", x, '元的业务')


save_money("小张", 200)
save_money("小赵", 500)
withdraw("小李", 300)