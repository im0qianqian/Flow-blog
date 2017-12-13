"""
This is some configuration.
"""
# import flow.models as md

# Mysql数据库配置
DATABASE_CONFIG = {
    'NAME': 'pyblog',   #DB_NAME
    'USER': 'root',     #Mysql username
    'PASSWORD': 'im0qianqian',  #Mysql user_password
    'HOST': '127.0.0.1',    #Mysql host
    'PORT': '3306',     #Mysql service port
}

# 每页显示最大文章数量
MAXIMUM_OF_PAGE = 3
SITE_URL = "http://127.0.0.1:8000"
BLOG_TITLE = "FLOW BLOG"
BLOG_DESCRIPTION = "Snow Memory"
LOGO_IMAGE = "http://static.dreamwings.cn/wp-content/uploads/2016/06/10102wq.jpg"


def get_config(request):
    from ..views import get_page
    return {'SITE_URL': SITE_URL,
            'BLOG_TITLE': BLOG_TITLE,
            'BLOG_DESCRIPTION': BLOG_DESCRIPTION,
            'LOGO_IMAGE': LOGO_IMAGE,
            'page_list': get_page(),
            }
