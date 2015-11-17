from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import RequestContext
from django import forms
from bookmarks.models import dangnhap
# def main_page(request):
#  template = get_template('main_page.html')
#  variables = Context({
#  'head_title': 'Django Bookmarks',
#  'page_title': 'Welcome to Django Bookmarks',
#  'page_body': 'Where you can store and share bookmarks!',
#  })
#  output = template.render(variables)
#  return HttpResponse(output)
def main_page(request):
    if request.method == 'POST':
        # form = Form(request.POST)
        # if form.is_valid():
        #     new_dangnhap=form.save()
        #     taikhoan = form.cleaned_data['taikhoan']
        #     matkhau = form.cleaned_data['matkhau']
        if request.POST.get("insert",""):
	    	taikhoan=request.POST['taikhoan']
	        matkhau=request.POST['matkhau']
	        p=dangnhap(
	            taikhoan=taikhoan,
	            matkhau=matkhau
	            )
	        p.save()
    	else:
	    	pass
        if request.POST.get("delete",""):
	    	khoa=request.POST['delete_val']
	    	p=dangnhap(
	    		id=khoa
	    		)
	    	p.delete();
    	else:
    		pass
        #     results=dangnhap.objects.all()
        # else:
        #     form.errors
    url='http://127.0.0.1:8000'
    data=dangnhap.objects.all()
    data1={"dangnhap1":data,"url":url}
    return render_to_response('main_page.html', data1, context_instance=RequestContext(request))

