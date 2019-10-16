Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from urllib.request import *
>>> urlretrieve('https://n2.sdlcdn.com/imgs/i/h/1/230X258_sharpened/618953333749_e0957-0c8af.png', 'tv.png')
('tv.png', <http.client.HTTPMessage object at 0x10e2354a8>)
>>> import os
>>> os.getcwd()
'/Users/anmolrajarora/Documents'
>>> res = urlopen('https://www.snapdeal.com/products/electronic-tv-accessories?q=Occasion_s%3ATV1%7C&sort=plrty&showAds=false')
>>> html = bs(res)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    html = bs(res)
NameError: name 'bs' is not defined
>>> from bs4 import BeautifulSoup as bs
>>> html = bs(res)
>>> images = html.find_all('img')
>>> len(images)
37
>>> for image in images:
	print(image)

	
<img class="lazy-load" data-src="https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png"/>
<img class="notIeLogoHeader aspectRatioEqual sdLogo cur-pointer" height="28" src="https://i3.sdlcdn.com/img/snapdeal/darwin/logo/sdLatestLogo.svg" title="Snapdeal" width="132"/>
<img class="ieLogoHeader aspectRatioEqual sdLogo cur-pointer" height="28" title="Snapdeal" width="132"/>
<img class="lazy-load cartProductImg" data-src=""/>
<img class="hidden imgUser"/>
<img class="js_svgLoader" height="32" lazysrc="https://i2.sdlcdn.com/img/sdDarwinLoader.svg" onerror="this.src='https://i1.sdlcdn.com/img/revamp/cyclicLoader.gif'; this.onerror=null;" width="32"/>
<img class="js_svgLoader" height="32" lazysrc="https://i2.sdlcdn.com/img/sdDarwinLoader.svg" onerror="this.src='https://i1.sdlcdn.com/img/revamp/cyclicLoader.gif'; this.onerror=null;" width="32"/>
<img height="32" onerror="this.src='https://i1.sdlcdn.com/img/revamp/cyclicLoader.gif'; this.onerror=null;" src="https://i2.sdlcdn.com/img/sdDarwinLoader.svg" width="32"/>
<img alt="" src=""/>
<img alt="" class="p-img" src=""/>
<img alt="" src=""/>
<img alt="" class="p-img" src=""/>
<img alt="" src=""/>
<img alt="" class="p-img" src=""/>
<img alt="" src=""/>
<img alt="" class="p-img" src=""/>
<img alt="" src=""/>
<img alt="" class="p-img" src=""/>
<img class="js_svgLoader" lazysrc="https://i2.sdlcdn.com/img/sdDarwinLoader.svg" onerror="this.src='https://i1.sdlcdn.com/img/revamp/cyclicLoader.gif'; this.onerror=null;"/>
<img class="product-image" src="https://n2.sdlcdn.com/imgs/i/h/1/230X258_sharpened/618953333749_e0957-0c8af.png" title="Activa 32D60 80 cm ( 32 ) Full HD (FHD) LED Television"/>
<img class="product-image" src="https://n1.sdlcdn.com/imgs/e/7/d/230X258_sharpened/ITH-ith-24-60-cm-SDL015088979-1-b88d8.jpg" title="ITH 24 60 cm ( 24 ) Full HD (FHD) LED Television"/>
<img class="product-image" src="https://n2.sdlcdn.com/imgs/h/j/y/230X258_sharpened/LONGWAY-LW-32D90-80-cm-SDL622573571-2-81fea.jpeg" title="LONGWAY LW-32D90 80 cm (32) Full HD (FHD) LED Television"/>
<img class="product-image" src="https://n1.sdlcdn.com/imgs/g/z/x/230X258_sharpened/621726454850-a3220.jpg" title="Activa 24A35 60 cm ( 24 ) Full HD (FHD) LED Television"/>
<img class="product-image lazy-load" data-src="https://n2.sdlcdn.com/imgs/b/2/9/230X258_sharpened/LG-24LH454A-60-cm-24-SDL182253006-1-5c3c7.jpg" title="LG 24LH454A / 24LK454 HD Ready LED Television 60 cm ( 24 ) "/>
<img class="product-image lazy-load" data-src="https://n4.sdlcdn.com/imgs/i/h/2/230X258_sharpened/Activa_ACT_32_SMART_80_SDL277739425_1_3bd1e_51b6a_222d8-6bcc8.jpg" title="Activa ACT-32 SMART Android 80 cm ( 32 ) Smart Full HD (FHD) LED Television"/>
<img class="product-image lazy-load" data-src="https://n1.sdlcdn.com/imgs/f/h/7/230X258_sharpened/Samsung-UA-32FH4003-R-81-SDL656490386-1-7a5eb.jpg" title="Samsung 32FH4003 (32) 80 CM HD Ready"/>
<img class="product-image lazy-load" data-src="https://n3.sdlcdn.com/imgs/h/9/1/230X258_sharpened/Micromax_32T7260_81_cm_32_SDL821290602_1_d0711-796bc.jpg" hd="" led="" ready="" television="" title="Micromax 32"/>
<img class="product-image lazy-load" data-src="https://n3.sdlcdn.com/imgs/f/b/r/230X258_sharpened/SDL006453173_1-a60a9.jpg" title="Activa 6003 80 cm ( 32 ) FULL HD (FHD) LED Television"/>
<img class="product-image lazy-load" data-src="https://n4.sdlcdn.com/imgs/i/f/v/230X258_sharpened/LONGWAY-S7005-80cm-32-Smart-SDL418146919-1-61bf3.jpg" title="LONGWAY S7005 80cm (32) Smart Full HD (FHD) LED Television With 1+1 Year Extended Warranty"/>
<img class="product-image lazy-load" data-src="https://n4.sdlcdn.com/imgs/e/q/g/230X258_sharpened/32j4003-552b9.jpg" title="Samsung 32N4003 HD Ready LED Television 80 CM"/>
<img class="product-image lazy-load" data-src="https://n2.sdlcdn.com/imgs/g/t/y/230X258_sharpened/LONGWAY-LW-7005-99-cm-SDL444843065-2-fb1e7.jpg" title="LONGWAY LW 7005 101 cm ( 40 ) Full HD (FHD) LED Television"/>
<img class="product-image lazy-load" data-src="https://n2.sdlcdn.com/imgs/b/s/k/230X258_sharpened/MiDE032v12-f17d7.jpg" title="Mitashi MiDE032v12 81 cm (32) HD Ready LED Television"/>
<img class="product-image lazy-load" data-src="https://n1.sdlcdn.com/imgs/b/1/v/230X258_sharpened/Panasonic-28D400DX-70-cm-28-SDL179601773-1-d3f29.JPG" title="Panasonic TH 28D400DX 70 cm ( 28 ) HD Ready LED Television"/>
<img class="product-image lazy-load" data-src="https://n4.sdlcdn.com/imgs/c/6/x/230X258_sharpened/Micromax-40Z3420FHD-101-6-cm-SDL170050344-1-41726.jpg" title="Micromax 40Z3420/40A6300FHD 101 cm ( 40 ) Full HD (FHD) LED Television "/>
<img class="product-image lazy-load" data-src="https://n3.sdlcdn.com/imgs/g/m/0/230X258_sharpened/ITH-ith-32-80-cm-SDL015606973-1-dd26b.jpeg" title="ITH ith 32 80 cm ( 32 ) Full HD (FHD) LED Television"/>
<img class="product-image lazy-load" data-src="https://n2.sdlcdn.com/imgs/h/u/f/230X258_sharpened/WESTWAY_WEL_3200_80_cm_SDL811049684_1_42ed9-a2935.JPG" title="WESTWAY by Weston WEL-3200 80 cm (32) HD Ready LED TV"/>
<img class="js_svgLoader" lazysrc="https://i2.sdlcdn.com/img/sdDarwinLoader.svg" onerror="this.src='https://i1.sdlcdn.com/img/revamp/cyclicLoader.gif'; this.onerror=null;" style="top:17px;"/>
>>> 
>>> images[0]
<img class="lazy-load" data-src="https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png"/>
>>> images[0]['class']
['lazy-load']
>>> images[0]['data-src']
'https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png'
>>> 
>>> for image in images:
	print(image['data-src'])

	
https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png
Traceback (most recent call last):
  File "<pyshell#20>", line 2, in <module>
    print(image['data-src'])
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/bs4/element.py", line 1016, in __getitem__
    return self.attrs[key]
KeyError: 'data-src'
>>> 
>>> for image in images:
	if str(image).find('data-src') > -1:
		print(image['data-src']
	else:
		      
SyntaxError: invalid syntax
>>> for image in images:
	if str(image).find('data-src') > -1:
		print(image['data-src']
	else:
		      
SyntaxError: invalid syntax
>>> for image in images:
	if str(image).find('data-src') > -1:
		print(image['data-src'])
	else:
		print('data-src attribute not found')

		
https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png
data-src attribute not found
data-src attribute not found

data-src attribute not found
data-src attribute not found
data-src attribute not found
data-src attribute not found
data-src attribute not found
data-src attribute not found
data-src attribute not found
data-src attribute not found
data-src attribute not found
data-src attribute not found
data-src attribute not found
data-src attribute not found
data-src attribute not found
data-src attribute not found
data-src attribute not found
data-src attribute not found
data-src attribute not found
data-src attribute not found
data-src attribute not found
https://n2.sdlcdn.com/imgs/b/2/9/230X258_sharpened/LG-24LH454A-60-cm-24-SDL182253006-1-5c3c7.jpg
https://n4.sdlcdn.com/imgs/i/h/2/230X258_sharpened/Activa_ACT_32_SMART_80_SDL277739425_1_3bd1e_51b6a_222d8-6bcc8.jpg
https://n1.sdlcdn.com/imgs/f/h/7/230X258_sharpened/Samsung-UA-32FH4003-R-81-SDL656490386-1-7a5eb.jpg
https://n3.sdlcdn.com/imgs/h/9/1/230X258_sharpened/Micromax_32T7260_81_cm_32_SDL821290602_1_d0711-796bc.jpg
https://n3.sdlcdn.com/imgs/f/b/r/230X258_sharpened/SDL006453173_1-a60a9.jpg
https://n4.sdlcdn.com/imgs/i/f/v/230X258_sharpened/LONGWAY-S7005-80cm-32-Smart-SDL418146919-1-61bf3.jpg
https://n4.sdlcdn.com/imgs/e/q/g/230X258_sharpened/32j4003-552b9.jpg
https://n2.sdlcdn.com/imgs/g/t/y/230X258_sharpened/LONGWAY-LW-7005-99-cm-SDL444843065-2-fb1e7.jpg
https://n2.sdlcdn.com/imgs/b/s/k/230X258_sharpened/MiDE032v12-f17d7.jpg
https://n1.sdlcdn.com/imgs/b/1/v/230X258_sharpened/Panasonic-28D400DX-70-cm-28-SDL179601773-1-d3f29.JPG
https://n4.sdlcdn.com/imgs/c/6/x/230X258_sharpened/Micromax-40Z3420FHD-101-6-cm-SDL170050344-1-41726.jpg
https://n3.sdlcdn.com/imgs/g/m/0/230X258_sharpened/ITH-ith-32-80-cm-SDL015606973-1-dd26b.jpeg
https://n2.sdlcdn.com/imgs/h/u/f/230X258_sharpened/WESTWAY_WEL_3200_80_cm_SDL811049684_1_42ed9-a2935.JPG
data-src attribute not found
>>> 
>>> links = []
>>> for image in images:
	if str(image).find('data-src') > -1:
		links.append(image['data-src'])

		
>>> len(links)
15
>>> for link in links:
	print(links)

	
['https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png', '', 'https://n2.sdlcdn.com/imgs/b/2/9/230X258_sharpened/LG-24LH454A-60-cm-24-SDL182253006-1-5c3c7.jpg', 'https://n4.sdlcdn.com/imgs/i/h/2/230X258_sharpened/Activa_ACT_32_SMART_80_SDL277739425_1_3bd1e_51b6a_222d8-6bcc8.jpg', 'https://n1.sdlcdn.com/imgs/f/h/7/230X258_sharpened/Samsung-UA-32FH4003-R-81-SDL656490386-1-7a5eb.jpg', 'https://n3.sdlcdn.com/imgs/h/9/1/230X258_sharpened/Micromax_32T7260_81_cm_32_SDL821290602_1_d0711-796bc.jpg', 'https://n3.sdlcdn.com/imgs/f/b/r/230X258_sharpened/SDL006453173_1-a60a9.jpg', 'https://n4.sdlcdn.com/imgs/i/f/v/230X258_sharpened/LONGWAY-S7005-80cm-32-Smart-SDL418146919-1-61bf3.jpg', 'https://n4.sdlcdn.com/imgs/e/q/g/230X258_sharpened/32j4003-552b9.jpg', 'https://n2.sdlcdn.com/imgs/g/t/y/230X258_sharpened/LONGWAY-LW-7005-99-cm-SDL444843065-2-fb1e7.jpg', 'https://n2.sdlcdn.com/imgs/b/s/k/230X258_sharpened/MiDE032v12-f17d7.jpg', 'https://n1.sdlcdn.com/imgs/b/1/v/230X258_sharpened/Panasonic-28D400DX-70-cm-28-SDL179601773-1-d3f29.JPG', 'https://n4.sdlcdn.com/imgs/c/6/x/230X258_sharpened/Micromax-40Z3420FHD-101-6-cm-SDL170050344-1-41726.jpg', 'https://n3.sdlcdn.com/imgs/g/m/0/230X258_sharpened/ITH-ith-32-80-cm-SDL015606973-1-dd26b.jpeg', 'https://n2.sdlcdn.com/imgs/h/u/f/230X258_sharpened/WESTWAY_WEL_3200_80_cm_SDL811049684_1_42ed9-a2935.JPG']
['https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png', '', 'https://n2.sdlcdn.com/imgs/b/2/9/230X258_sharpened/LG-24LH454A-60-cm-24-SDL182253006-1-5c3c7.jpg', 'https://n4.sdlcdn.com/imgs/i/h/2/230X258_sharpened/Activa_ACT_32_SMART_80_SDL277739425_1_3bd1e_51b6a_222d8-6bcc8.jpg', 'https://n1.sdlcdn.com/imgs/f/h/7/230X258_sharpened/Samsung-UA-32FH4003-R-81-SDL656490386-1-7a5eb.jpg', 'https://n3.sdlcdn.com/imgs/h/9/1/230X258_sharpened/Micromax_32T7260_81_cm_32_SDL821290602_1_d0711-796bc.jpg', 'https://n3.sdlcdn.com/imgs/f/b/r/230X258_sharpened/SDL006453173_1-a60a9.jpg', 'https://n4.sdlcdn.com/imgs/i/f/v/230X258_sharpened/LONGWAY-S7005-80cm-32-Smart-SDL418146919-1-61bf3.jpg', 'https://n4.sdlcdn.com/imgs/e/q/g/230X258_sharpened/32j4003-552b9.jpg', 'https://n2.sdlcdn.com/imgs/g/t/y/230X258_sharpened/LONGWAY-LW-7005-99-cm-SDL444843065-2-fb1e7.jpg', 'https://n2.sdlcdn.com/imgs/b/s/k/230X258_sharpened/MiDE032v12-f17d7.jpg', 'https://n1.sdlcdn.com/imgs/b/1/v/230X258_sharpened/Panasonic-28D400DX-70-cm-28-SDL179601773-1-d3f29.JPG', 'https://n4.sdlcdn.com/imgs/c/6/x/230X258_sharpened/Micromax-40Z3420FHD-101-6-cm-SDL170050344-1-41726.jpg', 'https://n3.sdlcdn.com/imgs/g/m/0/230X258_sharpened/ITH-ith-32-80-cm-SDL015606973-1-dd26b.jpeg', 'https://n2.sdlcdn.com/imgs/h/u/f/230X258_sharpened/WESTWAY_WEL_3200_80_cm_SDL811049684_1_42ed9-a2935.JPG']
['https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png', '', 'https://n2.sdlcdn.com/imgs/b/2/9/230X258_sharpened/LG-24LH454A-60-cm-24-SDL182253006-1-5c3c7.jpg', 'https://n4.sdlcdn.com/imgs/i/h/2/230X258_sharpened/Activa_ACT_32_SMART_80_SDL277739425_1_3bd1e_51b6a_222d8-6bcc8.jpg', 'https://n1.sdlcdn.com/imgs/f/h/7/230X258_sharpened/Samsung-UA-32FH4003-R-81-SDL656490386-1-7a5eb.jpg', 'https://n3.sdlcdn.com/imgs/h/9/1/230X258_sharpened/Micromax_32T7260_81_cm_32_SDL821290602_1_d0711-796bc.jpg', 'https://n3.sdlcdn.com/imgs/f/b/r/230X258_sharpened/SDL006453173_1-a60a9.jpg', 'https://n4.sdlcdn.com/imgs/i/f/v/230X258_sharpened/LONGWAY-S7005-80cm-32-Smart-SDL418146919-1-61bf3.jpg', 'https://n4.sdlcdn.com/imgs/e/q/g/230X258_sharpened/32j4003-552b9.jpg', 'https://n2.sdlcdn.com/imgs/g/t/y/230X258_sharpened/LONGWAY-LW-7005-99-cm-SDL444843065-2-fb1e7.jpg', 'https://n2.sdlcdn.com/imgs/b/s/k/230X258_sharpened/MiDE032v12-f17d7.jpg', 'https://n1.sdlcdn.com/imgs/b/1/v/230X258_sharpened/Panasonic-28D400DX-70-cm-28-SDL179601773-1-d3f29.JPG', 'https://n4.sdlcdn.com/imgs/c/6/x/230X258_sharpened/Micromax-40Z3420FHD-101-6-cm-SDL170050344-1-41726.jpg', 'https://n3.sdlcdn.com/imgs/g/m/0/230X258_sharpened/ITH-ith-32-80-cm-SDL015606973-1-dd26b.jpeg', 'https://n2.sdlcdn.com/imgs/h/u/f/230X258_sharpened/WESTWAY_WEL_3200_80_cm_SDL811049684_1_42ed9-a2935.JPG']
['https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png', '', 'https://n2.sdlcdn.com/imgs/b/2/9/230X258_sharpened/LG-24LH454A-60-cm-24-SDL182253006-1-5c3c7.jpg', 'https://n4.sdlcdn.com/imgs/i/h/2/230X258_sharpened/Activa_ACT_32_SMART_80_SDL277739425_1_3bd1e_51b6a_222d8-6bcc8.jpg', 'https://n1.sdlcdn.com/imgs/f/h/7/230X258_sharpened/Samsung-UA-32FH4003-R-81-SDL656490386-1-7a5eb.jpg', 'https://n3.sdlcdn.com/imgs/h/9/1/230X258_sharpened/Micromax_32T7260_81_cm_32_SDL821290602_1_d0711-796bc.jpg', 'https://n3.sdlcdn.com/imgs/f/b/r/230X258_sharpened/SDL006453173_1-a60a9.jpg', 'https://n4.sdlcdn.com/imgs/i/f/v/230X258_sharpened/LONGWAY-S7005-80cm-32-Smart-SDL418146919-1-61bf3.jpg', 'https://n4.sdlcdn.com/imgs/e/q/g/230X258_sharpened/32j4003-552b9.jpg', 'https://n2.sdlcdn.com/imgs/g/t/y/230X258_sharpened/LONGWAY-LW-7005-99-cm-SDL444843065-2-fb1e7.jpg', 'https://n2.sdlcdn.com/imgs/b/s/k/230X258_sharpened/MiDE032v12-f17d7.jpg', 'https://n1.sdlcdn.com/imgs/b/1/v/230X258_sharpened/Panasonic-28D400DX-70-cm-28-SDL179601773-1-d3f29.JPG', 'https://n4.sdlcdn.com/imgs/c/6/x/230X258_sharpened/Micromax-40Z3420FHD-101-6-cm-SDL170050344-1-41726.jpg', 'https://n3.sdlcdn.com/imgs/g/m/0/230X258_sharpened/ITH-ith-32-80-cm-SDL015606973-1-dd26b.jpeg', 'https://n2.sdlcdn.com/imgs/h/u/f/230X258_sharpened/WESTWAY_WEL_3200_80_cm_SDL811049684_1_42ed9-a2935.JPG']
['https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png', '', 'https://n2.sdlcdn.com/imgs/b/2/9/230X258_sharpened/LG-24LH454A-60-cm-24-SDL182253006-1-5c3c7.jpg', 'https://n4.sdlcdn.com/imgs/i/h/2/230X258_sharpened/Activa_ACT_32_SMART_80_SDL277739425_1_3bd1e_51b6a_222d8-6bcc8.jpg', 'https://n1.sdlcdn.com/imgs/f/h/7/230X258_sharpened/Samsung-UA-32FH4003-R-81-SDL656490386-1-7a5eb.jpg', 'https://n3.sdlcdn.com/imgs/h/9/1/230X258_sharpened/Micromax_32T7260_81_cm_32_SDL821290602_1_d0711-796bc.jpg', 'https://n3.sdlcdn.com/imgs/f/b/r/230X258_sharpened/SDL006453173_1-a60a9.jpg', 'https://n4.sdlcdn.com/imgs/i/f/v/230X258_sharpened/LONGWAY-S7005-80cm-32-Smart-SDL418146919-1-61bf3.jpg', 'https://n4.sdlcdn.com/imgs/e/q/g/230X258_sharpened/32j4003-552b9.jpg', 'https://n2.sdlcdn.com/imgs/g/t/y/230X258_sharpened/LONGWAY-LW-7005-99-cm-SDL444843065-2-fb1e7.jpg', 'https://n2.sdlcdn.com/imgs/b/s/k/230X258_sharpened/MiDE032v12-f17d7.jpg', 'https://n1.sdlcdn.com/imgs/b/1/v/230X258_sharpened/Panasonic-28D400DX-70-cm-28-SDL179601773-1-d3f29.JPG', 'https://n4.sdlcdn.com/imgs/c/6/x/230X258_sharpened/Micromax-40Z3420FHD-101-6-cm-SDL170050344-1-41726.jpg', 'https://n3.sdlcdn.com/imgs/g/m/0/230X258_sharpened/ITH-ith-32-80-cm-SDL015606973-1-dd26b.jpeg', 'https://n2.sdlcdn.com/imgs/h/u/f/230X258_sharpened/WESTWAY_WEL_3200_80_cm_SDL811049684_1_42ed9-a2935.JPG']
['https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png', '', 'https://n2.sdlcdn.com/imgs/b/2/9/230X258_sharpened/LG-24LH454A-60-cm-24-SDL182253006-1-5c3c7.jpg', 'https://n4.sdlcdn.com/imgs/i/h/2/230X258_sharpened/Activa_ACT_32_SMART_80_SDL277739425_1_3bd1e_51b6a_222d8-6bcc8.jpg', 'https://n1.sdlcdn.com/imgs/f/h/7/230X258_sharpened/Samsung-UA-32FH4003-R-81-SDL656490386-1-7a5eb.jpg', 'https://n3.sdlcdn.com/imgs/h/9/1/230X258_sharpened/Micromax_32T7260_81_cm_32_SDL821290602_1_d0711-796bc.jpg', 'https://n3.sdlcdn.com/imgs/f/b/r/230X258_sharpened/SDL006453173_1-a60a9.jpg', 'https://n4.sdlcdn.com/imgs/i/f/v/230X258_sharpened/LONGWAY-S7005-80cm-32-Smart-SDL418146919-1-61bf3.jpg', 'https://n4.sdlcdn.com/imgs/e/q/g/230X258_sharpened/32j4003-552b9.jpg', 'https://n2.sdlcdn.com/imgs/g/t/y/230X258_sharpened/LONGWAY-LW-7005-99-cm-SDL444843065-2-fb1e7.jpg', 'https://n2.sdlcdn.com/imgs/b/s/k/230X258_sharpened/MiDE032v12-f17d7.jpg', 'https://n1.sdlcdn.com/imgs/b/1/v/230X258_sharpened/Panasonic-28D400DX-70-cm-28-SDL179601773-1-d3f29.JPG', 'https://n4.sdlcdn.com/imgs/c/6/x/230X258_sharpened/Micromax-40Z3420FHD-101-6-cm-SDL170050344-1-41726.jpg', 'https://n3.sdlcdn.com/imgs/g/m/0/230X258_sharpened/ITH-ith-32-80-cm-SDL015606973-1-dd26b.jpeg', 'https://n2.sdlcdn.com/imgs/h/u/f/230X258_sharpened/WESTWAY_WEL_3200_80_cm_SDL811049684_1_42ed9-a2935.JPG']
['https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png', '', 'https://n2.sdlcdn.com/imgs/b/2/9/230X258_sharpened/LG-24LH454A-60-cm-24-SDL182253006-1-5c3c7.jpg', 'https://n4.sdlcdn.com/imgs/i/h/2/230X258_sharpened/Activa_ACT_32_SMART_80_SDL277739425_1_3bd1e_51b6a_222d8-6bcc8.jpg', 'https://n1.sdlcdn.com/imgs/f/h/7/230X258_sharpened/Samsung-UA-32FH4003-R-81-SDL656490386-1-7a5eb.jpg', 'https://n3.sdlcdn.com/imgs/h/9/1/230X258_sharpened/Micromax_32T7260_81_cm_32_SDL821290602_1_d0711-796bc.jpg', 'https://n3.sdlcdn.com/imgs/f/b/r/230X258_sharpened/SDL006453173_1-a60a9.jpg', 'https://n4.sdlcdn.com/imgs/i/f/v/230X258_sharpened/LONGWAY-S7005-80cm-32-Smart-SDL418146919-1-61bf3.jpg', 'https://n4.sdlcdn.com/imgs/e/q/g/230X258_sharpened/32j4003-552b9.jpg', 'https://n2.sdlcdn.com/imgs/g/t/y/230X258_sharpened/LONGWAY-LW-7005-99-cm-SDL444843065-2-fb1e7.jpg', 'https://n2.sdlcdn.com/imgs/b/s/k/230X258_sharpened/MiDE032v12-f17d7.jpg', 'https://n1.sdlcdn.com/imgs/b/1/v/230X258_sharpened/Panasonic-28D400DX-70-cm-28-SDL179601773-1-d3f29.JPG', 'https://n4.sdlcdn.com/imgs/c/6/x/230X258_sharpened/Micromax-40Z3420FHD-101-6-cm-SDL170050344-1-41726.jpg', 'https://n3.sdlcdn.com/imgs/g/m/0/230X258_sharpened/ITH-ith-32-80-cm-SDL015606973-1-dd26b.jpeg', 'https://n2.sdlcdn.com/imgs/h/u/f/230X258_sharpened/WESTWAY_WEL_3200_80_cm_SDL811049684_1_42ed9-a2935.JPG']
['https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png', '', 'https://n2.sdlcdn.com/imgs/b/2/9/230X258_sharpened/LG-24LH454A-60-cm-24-SDL182253006-1-5c3c7.jpg', 'https://n4.sdlcdn.com/imgs/i/h/2/230X258_sharpened/Activa_ACT_32_SMART_80_SDL277739425_1_3bd1e_51b6a_222d8-6bcc8.jpg', 'https://n1.sdlcdn.com/imgs/f/h/7/230X258_sharpened/Samsung-UA-32FH4003-R-81-SDL656490386-1-7a5eb.jpg', 'https://n3.sdlcdn.com/imgs/h/9/1/230X258_sharpened/Micromax_32T7260_81_cm_32_SDL821290602_1_d0711-796bc.jpg', 'https://n3.sdlcdn.com/imgs/f/b/r/230X258_sharpened/SDL006453173_1-a60a9.jpg', 'https://n4.sdlcdn.com/imgs/i/f/v/230X258_sharpened/LONGWAY-S7005-80cm-32-Smart-SDL418146919-1-61bf3.jpg', 'https://n4.sdlcdn.com/imgs/e/q/g/230X258_sharpened/32j4003-552b9.jpg', 'https://n2.sdlcdn.com/imgs/g/t/y/230X258_sharpened/LONGWAY-LW-7005-99-cm-SDL444843065-2-fb1e7.jpg', 'https://n2.sdlcdn.com/imgs/b/s/k/230X258_sharpened/MiDE032v12-f17d7.jpg', 'https://n1.sdlcdn.com/imgs/b/1/v/230X258_sharpened/Panasonic-28D400DX-70-cm-28-SDL179601773-1-d3f29.JPG', 'https://n4.sdlcdn.com/imgs/c/6/x/230X258_sharpened/Micromax-40Z3420FHD-101-6-cm-SDL170050344-1-41726.jpg', 'https://n3.sdlcdn.com/imgs/g/m/0/230X258_sharpened/ITH-ith-32-80-cm-SDL015606973-1-dd26b.jpeg', 'https://n2.sdlcdn.com/imgs/h/u/f/230X258_sharpened/WESTWAY_WEL_3200_80_cm_SDL811049684_1_42ed9-a2935.JPG']
['https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png', '', 'https://n2.sdlcdn.com/imgs/b/2/9/230X258_sharpened/LG-24LH454A-60-cm-24-SDL182253006-1-5c3c7.jpg', 'https://n4.sdlcdn.com/imgs/i/h/2/230X258_sharpened/Activa_ACT_32_SMART_80_SDL277739425_1_3bd1e_51b6a_222d8-6bcc8.jpg', 'https://n1.sdlcdn.com/imgs/f/h/7/230X258_sharpened/Samsung-UA-32FH4003-R-81-SDL656490386-1-7a5eb.jpg', 'https://n3.sdlcdn.com/imgs/h/9/1/230X258_sharpened/Micromax_32T7260_81_cm_32_SDL821290602_1_d0711-796bc.jpg', 'https://n3.sdlcdn.com/imgs/f/b/r/230X258_sharpened/SDL006453173_1-a60a9.jpg', 'https://n4.sdlcdn.com/imgs/i/f/v/230X258_sharpened/LONGWAY-S7005-80cm-32-Smart-SDL418146919-1-61bf3.jpg', 'https://n4.sdlcdn.com/imgs/e/q/g/230X258_sharpened/32j4003-552b9.jpg', 'https://n2.sdlcdn.com/imgs/g/t/y/230X258_sharpened/LONGWAY-LW-7005-99-cm-SDL444843065-2-fb1e7.jpg', 'https://n2.sdlcdn.com/imgs/b/s/k/230X258_sharpened/MiDE032v12-f17d7.jpg', 'https://n1.sdlcdn.com/imgs/b/1/v/230X258_sharpened/Panasonic-28D400DX-70-cm-28-SDL179601773-1-d3f29.JPG', 'https://n4.sdlcdn.com/imgs/c/6/x/230X258_sharpened/Micromax-40Z3420FHD-101-6-cm-SDL170050344-1-41726.jpg', 'https://n3.sdlcdn.com/imgs/g/m/0/230X258_sharpened/ITH-ith-32-80-cm-SDL015606973-1-dd26b.jpeg', 'https://n2.sdlcdn.com/imgs/h/u/f/230X258_sharpened/WESTWAY_WEL_3200_80_cm_SDL811049684_1_42ed9-a2935.JPG']
['https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png', '', 'https://n2.sdlcdn.com/imgs/b/2/9/230X258_sharpened/LG-24LH454A-60-cm-24-SDL182253006-1-5c3c7.jpg', 'https://n4.sdlcdn.com/imgs/i/h/2/230X258_sharpened/Activa_ACT_32_SMART_80_SDL277739425_1_3bd1e_51b6a_222d8-6bcc8.jpg', 'https://n1.sdlcdn.com/imgs/f/h/7/230X258_sharpened/Samsung-UA-32FH4003-R-81-SDL656490386-1-7a5eb.jpg', 'https://n3.sdlcdn.com/imgs/h/9/1/230X258_sharpened/Micromax_32T7260_81_cm_32_SDL821290602_1_d0711-796bc.jpg', 'https://n3.sdlcdn.com/imgs/f/b/r/230X258_sharpened/SDL006453173_1-a60a9.jpg', 'https://n4.sdlcdn.com/imgs/i/f/v/230X258_sharpened/LONGWAY-S7005-80cm-32-Smart-SDL418146919-1-61bf3.jpg', 'https://n4.sdlcdn.com/imgs/e/q/g/230X258_sharpened/32j4003-552b9.jpg', 'https://n2.sdlcdn.com/imgs/g/t/y/230X258_sharpened/LONGWAY-LW-7005-99-cm-SDL444843065-2-fb1e7.jpg', 'https://n2.sdlcdn.com/imgs/b/s/k/230X258_sharpened/MiDE032v12-f17d7.jpg', 'https://n1.sdlcdn.com/imgs/b/1/v/230X258_sharpened/Panasonic-28D400DX-70-cm-28-SDL179601773-1-d3f29.JPG', 'https://n4.sdlcdn.com/imgs/c/6/x/230X258_sharpened/Micromax-40Z3420FHD-101-6-cm-SDL170050344-1-41726.jpg', 'https://n3.sdlcdn.com/imgs/g/m/0/230X258_sharpened/ITH-ith-32-80-cm-SDL015606973-1-dd26b.jpeg', 'https://n2.sdlcdn.com/imgs/h/u/f/230X258_sharpened/WESTWAY_WEL_3200_80_cm_SDL811049684_1_42ed9-a2935.JPG']
['https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png', '', 'https://n2.sdlcdn.com/imgs/b/2/9/230X258_sharpened/LG-24LH454A-60-cm-24-SDL182253006-1-5c3c7.jpg', 'https://n4.sdlcdn.com/imgs/i/h/2/230X258_sharpened/Activa_ACT_32_SMART_80_SDL277739425_1_3bd1e_51b6a_222d8-6bcc8.jpg', 'https://n1.sdlcdn.com/imgs/f/h/7/230X258_sharpened/Samsung-UA-32FH4003-R-81-SDL656490386-1-7a5eb.jpg', 'https://n3.sdlcdn.com/imgs/h/9/1/230X258_sharpened/Micromax_32T7260_81_cm_32_SDL821290602_1_d0711-796bc.jpg', 'https://n3.sdlcdn.com/imgs/f/b/r/230X258_sharpened/SDL006453173_1-a60a9.jpg', 'https://n4.sdlcdn.com/imgs/i/f/v/230X258_sharpened/LONGWAY-S7005-80cm-32-Smart-SDL418146919-1-61bf3.jpg', 'https://n4.sdlcdn.com/imgs/e/q/g/230X258_sharpened/32j4003-552b9.jpg', 'https://n2.sdlcdn.com/imgs/g/t/y/230X258_sharpened/LONGWAY-LW-7005-99-cm-SDL444843065-2-fb1e7.jpg', 'https://n2.sdlcdn.com/imgs/b/s/k/230X258_sharpened/MiDE032v12-f17d7.jpg', 'https://n1.sdlcdn.com/imgs/b/1/v/230X258_sharpened/Panasonic-28D400DX-70-cm-28-SDL179601773-1-d3f29.JPG', 'https://n4.sdlcdn.com/imgs/c/6/x/230X258_sharpened/Micromax-40Z3420FHD-101-6-cm-SDL170050344-1-41726.jpg', 'https://n3.sdlcdn.com/imgs/g/m/0/230X258_sharpened/ITH-ith-32-80-cm-SDL015606973-1-dd26b.jpeg', 'https://n2.sdlcdn.com/imgs/h/u/f/230X258_sharpened/WESTWAY_WEL_3200_80_cm_SDL811049684_1_42ed9-a2935.JPG']
['https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png', '', 'https://n2.sdlcdn.com/imgs/b/2/9/230X258_sharpened/LG-24LH454A-60-cm-24-SDL182253006-1-5c3c7.jpg', 'https://n4.sdlcdn.com/imgs/i/h/2/230X258_sharpened/Activa_ACT_32_SMART_80_SDL277739425_1_3bd1e_51b6a_222d8-6bcc8.jpg', 'https://n1.sdlcdn.com/imgs/f/h/7/230X258_sharpened/Samsung-UA-32FH4003-R-81-SDL656490386-1-7a5eb.jpg', 'https://n3.sdlcdn.com/imgs/h/9/1/230X258_sharpened/Micromax_32T7260_81_cm_32_SDL821290602_1_d0711-796bc.jpg', 'https://n3.sdlcdn.com/imgs/f/b/r/230X258_sharpened/SDL006453173_1-a60a9.jpg', 'https://n4.sdlcdn.com/imgs/i/f/v/230X258_sharpened/LONGWAY-S7005-80cm-32-Smart-SDL418146919-1-61bf3.jpg', 'https://n4.sdlcdn.com/imgs/e/q/g/230X258_sharpened/32j4003-552b9.jpg', 'https://n2.sdlcdn.com/imgs/g/t/y/230X258_sharpened/LONGWAY-LW-7005-99-cm-SDL444843065-2-fb1e7.jpg', 'https://n2.sdlcdn.com/imgs/b/s/k/230X258_sharpened/MiDE032v12-f17d7.jpg', 'https://n1.sdlcdn.com/imgs/b/1/v/230X258_sharpened/Panasonic-28D400DX-70-cm-28-SDL179601773-1-d3f29.JPG', 'https://n4.sdlcdn.com/imgs/c/6/x/230X258_sharpened/Micromax-40Z3420FHD-101-6-cm-SDL170050344-1-41726.jpg', 'https://n3.sdlcdn.com/imgs/g/m/0/230X258_sharpened/ITH-ith-32-80-cm-SDL015606973-1-dd26b.jpeg', 'https://n2.sdlcdn.com/imgs/h/u/f/230X258_sharpened/WESTWAY_WEL_3200_80_cm_SDL811049684_1_42ed9-a2935.JPG']
['https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png', '', 'https://n2.sdlcdn.com/imgs/b/2/9/230X258_sharpened/LG-24LH454A-60-cm-24-SDL182253006-1-5c3c7.jpg', 'https://n4.sdlcdn.com/imgs/i/h/2/230X258_sharpened/Activa_ACT_32_SMART_80_SDL277739425_1_3bd1e_51b6a_222d8-6bcc8.jpg', 'https://n1.sdlcdn.com/imgs/f/h/7/230X258_sharpened/Samsung-UA-32FH4003-R-81-SDL656490386-1-7a5eb.jpg', 'https://n3.sdlcdn.com/imgs/h/9/1/230X258_sharpened/Micromax_32T7260_81_cm_32_SDL821290602_1_d0711-796bc.jpg', 'https://n3.sdlcdn.com/imgs/f/b/r/230X258_sharpened/SDL006453173_1-a60a9.jpg', 'https://n4.sdlcdn.com/imgs/i/f/v/230X258_sharpened/LONGWAY-S7005-80cm-32-Smart-SDL418146919-1-61bf3.jpg', 'https://n4.sdlcdn.com/imgs/e/q/g/230X258_sharpened/32j4003-552b9.jpg', 'https://n2.sdlcdn.com/imgs/g/t/y/230X258_sharpened/LONGWAY-LW-7005-99-cm-SDL444843065-2-fb1e7.jpg', 'https://n2.sdlcdn.com/imgs/b/s/k/230X258_sharpened/MiDE032v12-f17d7.jpg', 'https://n1.sdlcdn.com/imgs/b/1/v/230X258_sharpened/Panasonic-28D400DX-70-cm-28-SDL179601773-1-d3f29.JPG', 'https://n4.sdlcdn.com/imgs/c/6/x/230X258_sharpened/Micromax-40Z3420FHD-101-6-cm-SDL170050344-1-41726.jpg', 'https://n3.sdlcdn.com/imgs/g/m/0/230X258_sharpened/ITH-ith-32-80-cm-SDL015606973-1-dd26b.jpeg', 'https://n2.sdlcdn.com/imgs/h/u/f/230X258_sharpened/WESTWAY_WEL_3200_80_cm_SDL811049684_1_42ed9-a2935.JPG']
['https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png', '', 'https://n2.sdlcdn.com/imgs/b/2/9/230X258_sharpened/LG-24LH454A-60-cm-24-SDL182253006-1-5c3c7.jpg', 'https://n4.sdlcdn.com/imgs/i/h/2/230X258_sharpened/Activa_ACT_32_SMART_80_SDL277739425_1_3bd1e_51b6a_222d8-6bcc8.jpg', 'https://n1.sdlcdn.com/imgs/f/h/7/230X258_sharpened/Samsung-UA-32FH4003-R-81-SDL656490386-1-7a5eb.jpg', 'https://n3.sdlcdn.com/imgs/h/9/1/230X258_sharpened/Micromax_32T7260_81_cm_32_SDL821290602_1_d0711-796bc.jpg', 'https://n3.sdlcdn.com/imgs/f/b/r/230X258_sharpened/SDL006453173_1-a60a9.jpg', 'https://n4.sdlcdn.com/imgs/i/f/v/230X258_sharpened/LONGWAY-S7005-80cm-32-Smart-SDL418146919-1-61bf3.jpg', 'https://n4.sdlcdn.com/imgs/e/q/g/230X258_sharpened/32j4003-552b9.jpg', 'https://n2.sdlcdn.com/imgs/g/t/y/230X258_sharpened/LONGWAY-LW-7005-99-cm-SDL444843065-2-fb1e7.jpg', 'https://n2.sdlcdn.com/imgs/b/s/k/230X258_sharpened/MiDE032v12-f17d7.jpg', 'https://n1.sdlcdn.com/imgs/b/1/v/230X258_sharpened/Panasonic-28D400DX-70-cm-28-SDL179601773-1-d3f29.JPG', 'https://n4.sdlcdn.com/imgs/c/6/x/230X258_sharpened/Micromax-40Z3420FHD-101-6-cm-SDL170050344-1-41726.jpg', 'https://n3.sdlcdn.com/imgs/g/m/0/230X258_sharpened/ITH-ith-32-80-cm-SDL015606973-1-dd26b.jpeg', 'https://n2.sdlcdn.com/imgs/h/u/f/230X258_sharpened/WESTWAY_WEL_3200_80_cm_SDL811049684_1_42ed9-a2935.JPG']
['https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png', '', 'https://n2.sdlcdn.com/imgs/b/2/9/230X258_sharpened/LG-24LH454A-60-cm-24-SDL182253006-1-5c3c7.jpg', 'https://n4.sdlcdn.com/imgs/i/h/2/230X258_sharpened/Activa_ACT_32_SMART_80_SDL277739425_1_3bd1e_51b6a_222d8-6bcc8.jpg', 'https://n1.sdlcdn.com/imgs/f/h/7/230X258_sharpened/Samsung-UA-32FH4003-R-81-SDL656490386-1-7a5eb.jpg', 'https://n3.sdlcdn.com/imgs/h/9/1/230X258_sharpened/Micromax_32T7260_81_cm_32_SDL821290602_1_d0711-796bc.jpg', 'https://n3.sdlcdn.com/imgs/f/b/r/230X258_sharpened/SDL006453173_1-a60a9.jpg', 'https://n4.sdlcdn.com/imgs/i/f/v/230X258_sharpened/LONGWAY-S7005-80cm-32-Smart-SDL418146919-1-61bf3.jpg', 'https://n4.sdlcdn.com/imgs/e/q/g/230X258_sharpened/32j4003-552b9.jpg', 'https://n2.sdlcdn.com/imgs/g/t/y/230X258_sharpened/LONGWAY-LW-7005-99-cm-SDL444843065-2-fb1e7.jpg', 'https://n2.sdlcdn.com/imgs/b/s/k/230X258_sharpened/MiDE032v12-f17d7.jpg', 'https://n1.sdlcdn.com/imgs/b/1/v/230X258_sharpened/Panasonic-28D400DX-70-cm-28-SDL179601773-1-d3f29.JPG', 'https://n4.sdlcdn.com/imgs/c/6/x/230X258_sharpened/Micromax-40Z3420FHD-101-6-cm-SDL170050344-1-41726.jpg', 'https://n3.sdlcdn.com/imgs/g/m/0/230X258_sharpened/ITH-ith-32-80-cm-SDL015606973-1-dd26b.jpeg', 'https://n2.sdlcdn.com/imgs/h/u/f/230X258_sharpened/WESTWAY_WEL_3200_80_cm_SDL811049684_1_42ed9-a2935.JPG']
>>> for link in links:
	print(link)

	
https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep.png

https://n2.sdlcdn.com/imgs/b/2/9/230X258_sharpened/LG-24LH454A-60-cm-24-SDL182253006-1-5c3c7.jpg
https://n4.sdlcdn.com/imgs/i/h/2/230X258_sharpened/Activa_ACT_32_SMART_80_SDL277739425_1_3bd1e_51b6a_222d8-6bcc8.jpg
https://n1.sdlcdn.com/imgs/f/h/7/230X258_sharpened/Samsung-UA-32FH4003-R-81-SDL656490386-1-7a5eb.jpg
https://n3.sdlcdn.com/imgs/h/9/1/230X258_sharpened/Micromax_32T7260_81_cm_32_SDL821290602_1_d0711-796bc.jpg
https://n3.sdlcdn.com/imgs/f/b/r/230X258_sharpened/SDL006453173_1-a60a9.jpg
https://n4.sdlcdn.com/imgs/i/f/v/230X258_sharpened/LONGWAY-S7005-80cm-32-Smart-SDL418146919-1-61bf3.jpg
https://n4.sdlcdn.com/imgs/e/q/g/230X258_sharpened/32j4003-552b9.jpg
https://n2.sdlcdn.com/imgs/g/t/y/230X258_sharpened/LONGWAY-LW-7005-99-cm-SDL444843065-2-fb1e7.jpg
https://n2.sdlcdn.com/imgs/b/s/k/230X258_sharpened/MiDE032v12-f17d7.jpg
https://n1.sdlcdn.com/imgs/b/1/v/230X258_sharpened/Panasonic-28D400DX-70-cm-28-SDL179601773-1-d3f29.JPG
https://n4.sdlcdn.com/imgs/c/6/x/230X258_sharpened/Micromax-40Z3420FHD-101-6-cm-SDL170050344-1-41726.jpg
https://n3.sdlcdn.com/imgs/g/m/0/230X258_sharpened/ITH-ith-32-80-cm-SDL015606973-1-dd26b.jpeg
https://n2.sdlcdn.com/imgs/h/u/f/230X258_sharpened/WESTWAY_WEL_3200_80_cm_SDL811049684_1_42ed9-a2935.JPG
>>> 
>>> 
>>> #  img_{}.{}
>>> 
>>> links[0].rpartition('.')
('https://i4.sdlcdn.com/img/platinum09/downloadappicon2ndsep', '.', 'png')
>>> links[-1].rpartition('.')
('https://n2.sdlcdn.com/imgs/h/u/f/230X258_sharpened/WESTWAY_WEL_3200_80_cm_SDL811049684_1_42ed9-a2935', '.', 'JPG')
>>> links[-1].rpartition('.')[-1]
'JPG'
>>> links[0].rpartition('.')[-1]
'png'
>>> 
>>> 
>>> for i in range(len(links));
SyntaxError: invalid syntax
>>> for i in range(len(links)):
	urlretrieve(links[i], 'img_{}.{}'.format(i+1, links[i].rpartition('.')[-1]))

	
('img_1.png', <http.client.HTTPMessage object at 0x10f0d89e8>)
Traceback (most recent call last):
  File "<pyshell#52>", line 2, in <module>
    urlretrieve(links[i], 'img_{}.{}'.format(i+1, links[i].rpartition('.')[-1]))
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 247, in urlretrieve
    with contextlib.closing(urlopen(url, data)) as fp:
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 510, in open
    req = Request(fullurl, data)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 328, in __init__
    self.full_url = url
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 354, in full_url
    self._parse()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/urllib/request.py", line 383, in _parse
    raise ValueError("unknown url type: %r" % self.full_url)
ValueError: unknown url type: ''
>>> for i in range(len(links)):
	if links[i] != '':
		urlretrieve(links[i], 'img_{}.{}'.format(i+1, links[i].rpartition('.')[-1]))

		
('img_1.png', <http.client.HTTPMessage object at 0x10f0d8cc0>)
('img_3.jpg', <http.client.HTTPMessage object at 0x10f0d89b0>)
('img_4.jpg', <http.client.HTTPMessage object at 0x10f0d86a0>)
('img_5.jpg', <http.client.HTTPMessage object at 0x10f0d8a58>)
('img_6.jpg', <http.client.HTTPMessage object at 0x10f0d8d30>)
('img_7.jpg', <http.client.HTTPMessage object at 0x10f0d8c88>)
('img_8.jpg', <http.client.HTTPMessage object at 0x10f0d8c18>)
('img_9.jpg', <http.client.HTTPMessage object at 0x10f0d8940>)
('img_10.jpg', <http.client.HTTPMessage object at 0x10f0d87b8>)
('img_11.jpg', <http.client.HTTPMessage object at 0x10f0d89e8>)
('img_12.JPG', <http.client.HTTPMessage object at 0x10f0d8668>)
('img_13.jpg', <http.client.HTTPMessage object at 0x10f0d8e10>)
('img_14.jpeg', <http.client.HTTPMessage object at 0x10f0d8f60>)
('img_15.JPG', <http.client.HTTPMessage object at 0x10f0d8b38>)
>>> 
