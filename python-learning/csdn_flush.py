#!/bin/bash
import urllib2

url = "http://blog.csdn.net/github_33644920/article/details/56020800"
for x in range(100):
	urllib2.Request(url)
	print x

