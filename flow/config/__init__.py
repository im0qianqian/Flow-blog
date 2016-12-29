"""
There is some config about database.

E.g:
    database name
    user name
    user password
    The database server 's ip and port.
"""
# Mysql数据库配置
DATABASE_CONFIG = {
    'NAME': 'pyblog',
    'USER': 'root',
    'PASSWORD': 'im0qianqian',
    'HOST': '127.0.0.1',
    'PORT': '3306',
}

# 每页显示最大文章数量
MAXIMUM_OF_PAGE = 3


def get_config(request):
    return {'SITE_URL': "/",
            'BLOG_TITLE':'FLOW BLOG',
            'BLOG_DESCRIPTION':'Snow Memory',
            'LOGO_IMAGE':'http://static.dreamwings.cn/wp-content/uploads/2016/06/10102wq.jpg'
            }


"""
Installed:
    pip install markdown
    pip install django
    pip install Pillow
    pip install bootstrap
"""
