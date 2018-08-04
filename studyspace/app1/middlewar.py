from .models import RequestTracker
class RequestTrackerMiddleware:
	def __init__(self, viewfun):
		self.view_fun = viewfun
	def __call__(self, request):
		#print "write something before processing"
		rt = RequestTracker(path=request.get_raw_uri(),
			ip=request.META.get("REMOTE_ADDR"))
		rt.save()
		resp = self.view_fun(request) # processing
		rt.status = resp.status_code
		rt.save()
		#print "after processing, before sendig resp, write someting"
		return resp

