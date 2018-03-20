url = 'http://www.google.com'
urllist = [];
urllist.extend(url)
print urllist
urllist.insert(4,'s')
print urllist
print reduce(lambda x,y:x+y,urllist)
