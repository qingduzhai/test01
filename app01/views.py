from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views import View


# Create your views here.
class TestView(View):
    def get(self, request, *args, **kwargs):
        pass

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = "*"
        response['Access-Control-Allow-Headers'] = "v1"
        response['Access-Control-Allow-Methods'] = "PUT,GET,POST,PATCH,DELETE"
        return response

    def put(self, request, *args, **kwargs):
        ret_msg_dict = {'status': "ojbk", 'msg': "omg"}
        response = JsonResponse(ret_msg_dict)
        response['Access-Control-Allow-Origin'] = "*"
        response['Access-Control-Expose-Headers'] = "v1"
        response['v1'] = 'ojbk'
        return response
