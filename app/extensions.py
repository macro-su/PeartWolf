from flask_login import LoginManager

login_manager = LoginManager()


def extensions(app):
    login_manager.init_app(app)
    # 指定登录的端点
    login_manager.login_view = 'main.index'
    # 需要登录时的提示信息
    login_manager.login_message = '需要先登录'
    # 设置session保护级别
    # None：禁用session保护
    # 'basic'：基本的保护，默认选项
    # 'strong'：最严格的保护，一旦用户登录信息改变，立即退出登录
    login_manager.session_protection = 'strong'
