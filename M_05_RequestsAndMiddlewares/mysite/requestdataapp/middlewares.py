from datetime import time

from django.http import HttpRequest
from django.shortcuts import render

from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseForbidden)

def set_useragent_on_request_middleware(get_response):
    print("initial")
    def middleware(request: HttpRequest):
        print("before get response")
        request.user_agent = request.META["HTTP_USER_AGENT"]
        response = get_response(request)
        print("after get response")
        return response
    return  middleware

class CountRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.responses_count = 0
        self.exceptions_count = 0
        self.request_time = {}

    def __call__(self, request: HttpRequest):
        time_delay = 10
        if not self.request_time:
            print('Это первый request после перезапуска сервера.')
        else:
            if (round(time.time()) * 1) - self.request_time['time'] < time_delay \
                    and self.request_time['ip_address'] == request.META.get('REMOTE_ADDR'):
                print('Прошло менее 10 сек. для повторного запроса с Вашего ip-адреса.')
                # return render(request, 'requestdataapp/error-request.html')
                return HttpResponseBadRequest('This view can not handle method {0}'.format(request.method), status=405)

        self.request_time = {'time': round(time.time() * 1),
                             'ip_address': request.META.get('REMOTE_ADDR')}

        self.requests_count += 1
        print("request count", self.requests_count)
        response = self.get_response(request)
        self.responses_count += 1
        print("response count", self.responses_count)
        return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exceptions_count += 1
        print("got", self.exceptions_count, "exceptions so far")