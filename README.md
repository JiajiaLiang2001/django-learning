## 需求分析

### 功能性需求

- 登陆
- 注册
- 景点、门票展示
- 在线预订门票
- 后台管理
- 统计报表

### 非功能性需求

- 首页
- 界面
- 移动端
- 时间有限
- 便于维护、按模块开发

## 技术栈

- Django
- Vue
- MySQL
- Redis

## 版本迭代计划

*v1.0*:首页的基本功能，无需登录

*v1.1*:景点详情、评论、搜索

*v1.2*:用户的注册和登录功能

*v1.3*:提交订单、订单管理

*v1.4*:后台管理、报表统计

## 技术部分

### 初识 Django 框架

- Django 安装及项目搭建
- Django 项目开发基本流程
- Django 请求到响应
- 视图、类视图、快捷视图函数、内置视图重写
- Django 模板部分
  - 模板引擎的选择和配置
  - 模板语法(变量、标签)
  - 模板的继承与包含
  - 过滤器、自定义过滤器

https://docs.djangoproject.com/en/4.1/

开发步骤：

1. 选择合适版本
2. 安装及配置
3. 生成项目结构
4. 内容开发
5. 迭代、上线、维护

### 基础

- 掌握 Django 的安装
- 掌握 Django 项目的创建
- 了解 Django 项目的文件目录结构
- 了解 Django 项目开发服务器的启动

### 开发流程

- 掌握开发服务器配置
- 掌握项目模块创建
- 理解项目开发流程，完成第一个页面

需要在 *settings.py* 配置 `ALLOWED_HOSTS` 允许访问的端口号

> python manage.py runserver PORT

<div align=left>
  <img src="images/1.png" title="Start Django" height="50%" width="50%">
</div>

> python manage.py startapp MODULE

<div align=left>
  <img src="images/2.png" title="Start Django" height="50%" width="50%">
</div>

完成第一个页面

1. *view.py* 中编写函数

   *hello/views.py*

   ```python
   from django.http import HttpResponse
   
   def hello_world(request):
       return HttpResponse('Hello World')
   ```

2. *urls.py* 中配置路由规则

   *DjangoLearning/urls.py*

   ```python
   urlpatterns = [
   	...
       path('hello/', hello_world)
   ]
   ```

<div align=left>
  <img src="images/3.png" title="Start Django" height="50%" width="50%">
</div>





### 从请求到响应

- 了解 URL 的设计及配置
- 掌握视图的定义及作用
- 掌握 URL 和视图的关系
- 了解视图响应的内容

URL设计：

正则表达式 && 指定参数类型

`path`(*route*,view*, *kwargs=None***,** *name=None*)

------

`include`(*module*, *namespace=None*)

`include`(*pattern_list*)

`include`(*(pattern_list*, *app_namespace)*, *namespace=None*)

用于模块化开发

*hello/views.py*

```python
def hello_world(request):
    return HttpResponse('Hello World')


def hello_china(request):
    return HttpResponse('Hello China')
```

*hello/urls.py*

```python
urlpatterns = [
    path('world/', hello_world),
    path('china/', hello_china)
]
```

*DjangoLearning/urls.py*

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls'))
]
```

| /hello/world/                | /hello/china/                |
| ---------------------------- | ---------------------------- |
| ![hello world](images/4.png) | ![hello china](images/5.png) |

### 在视图中处理业务逻辑

- 理解响应 HTML 内容
- 掌握如何获取 URL 参数
- 掌握如何获取 GET 参数

#### 响应 HTML 内容

*hello/views.py*

```python
def hello_html(request):
    html = """
    <html>
        <body>
            <h1 style="color:#f00">hello html</h1>
        </body>
    </html>
    """
    return HttpResponse(html)
```

*hello/urls.py*

```python
urlpatterns = [
    path('world/', hello_world),
    path('china/', hello_china),
    path('html/', hello_html)
]
```

| /hello/html/                |
| --------------------------- |
| ![hello html](images/6.png) |

#### 获取 URL 参数

*hello/views.py*

```python
def article_list(request, month):
    return HttpResponse('article: {}'.format(month))
```

*hello/urls.py*

```python
urlpatterns = [
    path('world/', hello_world),
    path('china/', hello_china),
    path('html/', hello_html),
    path('article/<int:month>/', article_list)
]
```

| /hello/article/2/           |
| --------------------------- |
| ![hello html](images/7.png) |

**用正则表达式匹配**

*hello/views.py*

```python
def article_list(request, month):
    return HttpResponse('article: {}'.format(month))
```

*hello/urls.py*

```python
urlpatterns = [
    path('world/', hello_world),
    path('china/', hello_china),
    path('html/', hello_html),
    # path('article/<int:month>/', article_list)
    re_path(r'^article/(?P<month>0?[1-9]|1[012])/$', article_list)
]
```

| /hello/article/02/          | /hello/article/12/          |
| --------------------------- | --------------------------- |
| ![hello html](images/8.png) | ![hello html](images/9.png) |

#### 获取 GET 请求参数

*hello/views.py*

```python
def search(request):
    name = request.GET.get('name', '')
    print(name)
    return HttpResponse('查询成功')
```

*hello/urls.py*

```python
urlpatterns = [
    path('world/', hello_world),
    path('china/', hello_china),
    path('html/', hello_html),
    # path('article/<int:month>/', article_list)
    re_path(r'^article/(?P<month>0?[1-9]|1[012])/$', article_list),
    path('search/', search)
]
```

| hello/search/?name=China     |
| ---------------------------- |
| ![hello html](images/10.png) |
| ![hello html](images/11.png) |

