import os

# 用户本地文件夹
HOME = os.path.expanduser('~')
# 该应用存放数据的文件夹
APP_DIR = os.path.join(HOME, 'AppData', 'Local', 'ZoneAmazon')
# 记录数据
EXCEL_FILE = os.path.join(HOME, 'AppData', 'Local', 'ZoneAmazon', 'target.xlsx')

# chrome用户信息 包含插件
USER_DATA_DIR = os.path.join(HOME, 'AppData', 'Local', 'Google', 'Chrome', 'User Data')

# 缓存文件位置
DUMP_FILE = os.path.join(HOME, 'AppData', 'Local', 'ZoneAmazon', 'dump.pickle')

# 结果文件位置
RES_FILE = os.path.join(HOME, 'Desktop', 'res.xlsx')
