from django.db import models
from django.conf.urls import patterns, include, url
from django.db import connection

class dangnhap(models.Model):
    taikhoan = models.CharField(max_length=200)
    matkhau=models.CharField(max_length=200)

    def __str__(self):
        return self.taikhoan

    def my_function(self):
    	cursor = connection.cursor()
    	cursor.execute("SELECT * FROM bookmarks_dangnhap")
    	result=cursor.fetchall()
    	return result 	
