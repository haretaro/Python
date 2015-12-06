import http.client

conn = http.client.HTTPConnection('www.hatena.ne.jp')
conn.request('GET','/')
res = conn.getresponse()
print(res.status,res.reason)
print(res.readall().decode('UTF-8'))
conn.close()
