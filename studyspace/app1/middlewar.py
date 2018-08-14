from .models import RequestTracker
from django.shortcuts import render
class RequestTrackerMiddleware:
	def __init__(self, viewfun):
		self.view_fun = viewfun
	def __call__(self, request):
		#print "write something before processing"
		# reqkey for cache
		# exapmle updated studyhall_get
		
		rt = RequestTracker(path=request.get_raw_uri(),
			ip=request.META.get("REMOTE_ADDR"))
		rt.save()
		resp = self.view_fun(request) # processing
		rt.status = resp.status_code
		if resp.status_code == 404:
			return render(request,"app1/404.html")
		if resp.status_code == 500:
			return render(request,"app1/500.html")
		rt.save()
		#update response for the table
		# updated value also for studayhall_get
		#print "after processing, before sendig resp, write someting"
		return resp

