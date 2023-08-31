import os


def get_user_setting_dir():
    user_home = os.path.expanduser('~')
    setting_dir = os.path.join(user_home, '.reedis/')
    if not os.path.isdir(setting_dir):
        os.mkdir(setting_dir)
    return setting_dir
