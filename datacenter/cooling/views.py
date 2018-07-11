# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun(request):
	return HttpResponse("25.67")

def fun1(request):
	resp="""
	<html>
	<head>
		<title>
			title tag information
		</title>
	</head>
	<!-- <body bgcolor="#785148"> -->
		<body bgcolor="#52965d">
		this is body part
		<h1>
			This is h1 tag
		</h1>
		<h2>
			This is h2 tag
		</h2>
		<h3>
			This is h3 tag
		</h3>
		<h4>
			This is h4 tag
		</h4>
		<h5>
			This is h5 tag
		</h5>
		<h6>
			This is h6 tag
		</h6>
		<a href="http://www.google.com">GOTO GOOGLE</a><br>
		<a href="http://www.youtube.com">GOTO youtube</a><br>
		<a href="http://www.fb.com">GOTO facebook</a><br>

		<form>
			Username: <input type="text"></input><br>
			Password: <input type="password"></input><br>
			Email: <input type="email"></input><br>
			Gender: Male: <input type="radio"></input>FeMale: <input type="radio"></input><br>
			Do you want to join immediately?:<input type="checkbox"></input><br>
			Present address: <textarea></textarea><br>
			courses available:
			<select><br>
				<optgroup>
					<option>python</option>
					<option>python, ML</option>
					<option>python, Django</option>
					<option>python, IOT</option>
				</optgroup>
			</select>
			<input type="submit"></input><br>
		</form>

	</body>
</html>
	"""
	return HttpResponse(resp)
def fun2(request):
	#return render(request,"index.html")
	
	return render(request,"cooling/index.html")
