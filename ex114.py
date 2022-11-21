import urllib
import urllib.request

def formatarSite(site):
    site = site.replace("https://", "")
    site = site.replace("http://", "")
    site = site.replace("www.", "")
    site = site.replace(".com", "")
    site = site.replace(".br", "")
    return site

try:
    site = "https://findtheinvisiblecow.com"
    site2 = formatarSite(site)
    urllib.request.urlopen(site)
except:
    print(f'O site "{site2}" NÃO está funcionando.')
else:
    print(f'O site "{site2}" está funcionando!')