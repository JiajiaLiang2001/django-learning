from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string


# Create your views here.

def hello_world(request):
    return HttpResponse('Hello World')


def hello_china(request):
    return HttpResponse('Hello China')


def hello_html(request):
    html = """
    <html>
        <body>
            <h1 style="color:#f00">hello html</h1>
        </body>
    </html>
    """
    return HttpResponse(html)


def article_list(request, month):
    return HttpResponse('article: {}'.format(month))


def search(request):
    name = request.GET.get('name', '')
    print(name)
    return HttpResponse('查询成功')


def render_str(request):
    templ_name = 'index.html'
    html = render_to_string(template_name=templ_name)
    return HttpResponse(html)


def render_html(request):
    return render(request, 'index.html')


def http_request(request):
    print(request.method)

    print(request.META)
    print(request.headers)
    # print(request.headers['User-Agent'])

    name = request.GET.get('name', '')
    print(name)
    return HttpResponse('响应')


def http_response(request):
    resp = HttpResponse('响应内容')
    return resp


def http_json_response(request):
    user_info = {
        'name': '张三',
        'age': 34
    }
    resp = JsonResponse(user_info)
    return resp
