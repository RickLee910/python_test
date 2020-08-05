from urllib import request
response = request.urlopen('http://flaglee.cn/')
fi = open("project1.txt", 'w')
page = fi.write(str(response.read()))
fi.close()