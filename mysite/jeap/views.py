from django.shortcuts import render_to_response
from django.http import HttpResponse
from django import forms
from django.template import RequestContext
from jeap.models import Blog
from django.core import serializers
class UserForm(forms.Form):
    name = forms.CharField()

def test(request):
    test_value = Blog.objects.all()

    return render_to_response('test.html', locals(),context_instance=RequestContext(request))

def homejson(request):
    all = Blog.objects.all()
    data = serializers.serialize('json',all)
    # return render_to_response('homejosn.html',{'data':data})
    return HttpResponse(data)

# def test(req):
#     if req.method == 'POST':
#         form = UserForm(req.POST)
#         if form.is_valid():
#             print form.cleaned_data
#             return HttpResponse('ok')
#     else:
#         form = UserForm()
#     return render_to_response('test.html', {}, context_instance=RequestContext(request))
def new(request):
    a = Blog()
    a.name = request.POST['name']
    a.title = request.POST['title']
    a.context = request.POST['context']
    a.save()
    return HttpResponse("ok,save")

def delete(request,id):
    b = Blog.objects.get(id=int(id))
    b.delete()
    return HttpResponse('has delete')

def edit(request,id):
    edit_value = Blog.objects.get(id =int(id))
    return render_to_response('edit.html', locals(),context_instance=RequestContext(request))

def save(request,id):
    d = Blog.objects.get(id=int(id))
    d.context = request.POST['context']
    d.save()
    return HttpResponse('ok')
