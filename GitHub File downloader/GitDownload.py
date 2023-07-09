import urllib.request, sys

url = sys.argv[1]
filename = url.split('/')[-1]   # In a link the last item is the file name

#specify url and file name
urllib.request.urlretrieve( url, filename )