Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import urllib.request
>>> request.urlopen('https://www.flipkart.com/pens-stationery/pr?sid=dgv&p[]=facets.serviceability%5B%5D%3Dtrue&offer=nb:mp:094f497f05&fm=neo%2Fmerchandising&iid=M_5b27b13c-8ceb-4a86-a2d1-84c49506159e_2.MB21L5GVY389&ssid=if3ayznw000000001570687752400&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_4_2.dealCard.OMU_MB21L5GVY389_2&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_4_NA_view-all_2&cid=MB21L5GVY389')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    request.urlopen('https://www.flipkart.com/pens-stationery/pr?sid=dgv&p[]=facets.serviceability%5B%5D%3Dtrue&offer=nb:mp:094f497f05&fm=neo%2Fmerchandising&iid=M_5b27b13c-8ceb-4a86-a2d1-84c49506159e_2.MB21L5GVY389&ssid=if3ayznw000000001570687752400&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_4_2.dealCard.OMU_MB21L5GVY389_2&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_4_NA_view-all_2&cid=MB21L5GVY389')
NameError: name 'request' is not defined
>>> urllib.request.urlopen('https://www.flipkart.com/pens-stationery/pr?sid=dgv&p[]=facets.serviceability%5B%5D%3Dtrue&offer=nb:mp:094f497f05&fm=neo%2Fmerchandising&iid=M_5b27b13c-8ceb-4a86-a2d1-84c49506159e_2.MB21L5GVY389&ssid=if3ayznw000000001570687752400&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_4_2.dealCard.OMU_MB21L5GVY389_2&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_4_NA_view-all_2&cid=MB21L5GVY389')
<http.client.HTTPResponse object at 0x10557d358>
>>> from urllib.request import urlopen
>>> urlopen('https://www.flipkart.com/pens-stationery/pr?sid=dgv&p[]=facets.serviceability%5B%5D%3Dtrue&offer=nb:mp:094f497f05&fm=neo%2Fmerchandising&iid=M_5b27b13c-8ceb-4a86-a2d1-84c49506159e_2.MB21L5GVY389&ssid=if3ayznw000000001570687752400&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_4_2.dealCard.OMU_MB21L5GVY389_2&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_4_NA_view-all_2&cid=MB21L5GVY389')
<http.client.HTTPResponse object at 0x10392cb00>
>>> httpResponse = urlopen('https://www.flipkart.com/pens-stationery/pr?sid=dgv&p[]=facets.serviceability%5B%5D%3Dtrue&offer=nb:mp:094f497f05&fm=neo%2Fmerchandising&iid=M_5b27b13c-8ceb-4a86-a2d1-84c49506159e_2.MB21L5GVY389&ssid=if3ayznw000000001570687752400&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_4_2.dealCard.OMU_MB21L5GVY389_2&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_4_NA_view-all_2&cid=MB21L5GVY389')
>>> httpResponse
<http.client.HTTPResponse object at 0x10557d2b0>
>>> 
>>> import bs4   #used to get html page from http response
>>> bs4.BeautifulSoup(httpResponse)

>>> htmlPage = bs4.BeautifulSoup(httpResponse)
>>> htmlPage

>>> 
>>> 
>>> 
>>> httpResponse = urlopen('https://www.flipkart.com/pens-stationery/pr?sid=dgv&p[]=facets.serviceability%5B%5D%3Dtrue&offer=nb:mp:094f497f05&fm=neo%2Fmerchandising&iid=M_5b27b13c-8ceb-4a86-a2d1-84c49506159e_2.MB21L5GVY389&ssid=if3ayznw000000001570687752400&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_4_2.dealCard.OMU_MB21L5GVY389_2&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_4_NA_view-all_2&cid=MB21L5GVY389')
>>> htmlPage = bs4.BeautifulSoup(httpResponse)
>>> htmlPage

>>> htmlPage.find('a', class='_2cLu-l')
SyntaxError: invalid syntax
>>> htmlPage.find('a', class_ = '_2cLu-l')
<a class="_2cLu-l" href="/vatsmart-pen-light-multi-function/p/itm2a584e68700a0?pid=PENFKCHHSMZNXG9Z&amp;lid=LSTPENFKCHHSMZNXG9ZUGZN3D&amp;marketplace=FLIPKART&amp;srno=b_1_1&amp;otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_4_2.dealCard.OMU_MB21L5GVY389_2&amp;otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_4_NA_view-all_2&amp;fm=organic&amp;iid=en_la5Wm5M3JMhX5lSld9YSKlfq7D5zDC3%2BfW0vR1qzIe7HesBRFfzbZEgQosZFBTRn2g35LHByfWZJ0afZh98Uqg%3D%3D&amp;ssid=gl63qybgo00000001570689735587" rel="noopener noreferrer" target="_blank" title="VATSMART PEN WITH LIGHT Multi-function Pen">VATSMART PEN WITH LIGHT Multi-function Pen</a>
>>> htmlPage.find('a', class_ = '_2cLu-l').text
'VATSMART PEN WITH LIGHT Multi-function Pen'
>>> htmlPage.find('div', class_ = '_1vC4OE').text
'₹179'
>>> 
>>> htmlPage.find('div', class_ = 'VGWI6T')
<div class="VGWI6T"><span>40% off</span></div>
>>> htmlPage.find('div', class_ = 'VGWI6T')
<div class="VGWI6T"><span>40% off</span></div>
>>> 
>>> 
>>> div = htmlPage.find('div', class_ = 'VGWI6T')
>>> div
<div class="VGWI6T"><span>40% off</span></div>
>>> div.find('span')
<span>40% off</span>
>>> div.find('span').text
'40% off'
>>> 
>>> 
>>> divsList = htmlPage.find_all('div', class_ = '_3liAhj')
>>> len(divsList)
40
>>> 
>>> 
>>> for div in divsList:
	print(div.find('a', class_ = '_2cLu-l').text + " - " + div.find('div', class_ = '_1vC4OE').text + " - " + div.find('div', class_ = 'VGWI6T').find('span').text)

	
VATSMART PEN WITH LIGHT Multi-function Pen - ₹179 - 40% off
toss faux leather file folder - ₹191 - 61% off
Flipkart SmartBuy A5 Notebook - ₹199 - 57% off
toss faux leather Display Book - ₹191 - 61% off
MASHKI PUBG KAR98 & M24 GUN WITH HELMET Key Chain - ₹215 - 54% off
BBS DEAL Marvel Avengers Infinity War Thor Axe-Hammer &... - ₹178 - 74% off
Xpra Combo Watch & Pen Gift Set Pen Gift Set - ₹649 - 81% off
Xpra Combo Watch & Pen Gift Set Pen Gift Set - ₹649 - 81% off
Xpra Combo Watch & Pen Gift Set Pen Gift Set - ₹649 - 81% off
Xpra Combo Watch & Pen Gift Set Pen Gift Set - ₹649 - 81% off
Productmine 10 Card Holder - ₹151 - 74% off
TOSS Faux Leather File Folder - ₹375 - 53% off
VEDY ARMY BULLET KEY CHAIN Locking Key Chain - ₹220 - 55% off
seasons Drive Safe I Need You Here with Me metal matte ... - ₹111 - 25% off
Flipkart SmartBuy Military Keychain with Torch, Screwdr... - ₹299 - 40% off
orchid engineers 4 Compartments iron REMOTE STAND - ₹375 - 24% off
orchid engineers 2 Compartments iron remote stand - ₹249 - 50% off
Flipkart SmartBuy Regular Notebook - ₹199 - 42% off
orchid engineers 2 Compartments iron REMOTE STAND - ₹299 - 40% off
SCRIZ "Executive Medic Collection" Metal Body With Doct... - ₹429 - 78% off
TnW 10 Card Holder - ₹133 - 55% off
Xpra Zilch Premium Roller Ball Pen - ₹379 - 70% off
Baoke Gel Gel Pen - ₹178 - 67% off
Auteur Slim with Screw for All Pen Brands Refill - ₹215 - 56% off
KitchenFest Premium Quality Small, Medium, Large Plasti... - ₹165 - 66% off
SCRIZ "Crown Collection" Fountain Pen - ₹449 - 82% off
orchid engineers 4 Compartments iron REMOTE STAND - ₹375 - 31% off
MASHKI Gold Sniper With Antique Helmet Key Chain - ₹172 - 78% off
Flipkart SmartBuy Exclusive Debit Card-Holder Dark Brow... - ₹399 - 20% off
Tuelip 4 In 1-Laser,Torch,Pointer,Antenna Multi-functio... - ₹240 - 75% off
Xpra Combo Watch Pen Gift Set Pen Gift Set - ₹599 - 72% off
Auteur Stylish Matt Black With Designer Clip Ball Pen - ₹325 - 50% off
Stealodeal Retro Style Metal 70mm 10X Magnifying Glass - ₹209 - 58% off
orchid engineers 4 Compartments metal Remote Stand/Hold... - ₹350 - 49% off
SCRIZ "Vector Collection" Shining Finish Metal Body Wit... - ₹329 - 78% off
Stealodeal Exclusive Black High Quality 11 Slot Leather... - ₹399 - 20% off
Flipkart SmartBuy Silver Military Keychain with Torch, ... - ₹299 - 40% off
Stealodeal Black Waterproof Limited Edition Metal Atm (... - ₹449 - 55% off
MASHKI MARVEL Avengers Endgame THOR Hammer(Mjolinr) & C... - ₹175 - 82% off
Doodle A5 Diary - ₹138 - 60% off
>>> httpResponse = urlopen('https://www.flipkart.com/wearable-smart-devices/pr?sid=ajy&p[]=facets.serviceability%5B%5D%3Dtrue&offer=nb:mp:095ee4bd09&fm=neo%2Fmerchandising&iid=M_c9ab4688-df09-4529-ae49-86ea46c87760_2.1X7S3CTF2TIL&ppt=hp&ppn=hp&ssid=31p259u4cw0000001570690332761&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_3_2.dealCard.OMU_1X7S3CTF2TIL_2&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_3_NA_view-all_2&cid=1X7S3CTF2TIL')
>>> htmlPage = bs4.BeautifulSoup(httpResponse)
>>> divsList = htmlPage.find_all('div', class_ = '_3liAhj')
>>> for div in divsList:
	print(div.find('a', class_ = '_2cLu-l').text + " - " + div.find('div', class_ = '_1vC4OE').text + " - " + div.find('div', class_ = 'VGWI6T').find('span').text)

	
Opta SB-0042 Activity Tracking Fitness Band - ₹3,142 - 37% off
Chris Merchant CE017 phone Smartwatch - ₹719 - 60% off
Mizco DZ09 phone Gold Smartwatch - ₹732 - 70% off
E-LIVE DZ09 4g calling health notifier Gold and Black S... - ₹567 - 81% off
Enew DZ09-GOLD 7-GTX-A phone Gold Smartwatch - ₹699 - 73% off
Mizco DZ09 Sliver Smartwatch - ₹672 - 73% off
HD Eagle M3 Band Health Band - ₹809 - 67% off
blueseed 4G touch FB compatible With All Phones Smartwa... - ₹719 - 64% off
EWELL 4G touchscreen,Sim,SD card all smart ph black Sma... - ₹808 - 73% off
EWELL Band with pedometer - ₹624 - 68% off
EWELL M3 Band XD compatible all smartphones - ₹538 - 73% off
EWELL M3 Smart Band Fitness Tracker Watch - ₹444 - 55% off
Enew DZ09-GOLD 0087 phone Gold Smartwatch - ₹532 - 81% off
JP ENTERPRISES PDXRY#2 Fitness Smart Band - ₹809 - 59% off
MPA DZ09 UN Black Smartwatch - ₹708 - 76% off
Influx GT08(i) phone Gold Smartwatch - ₹897 - 85% off
Rock DZ09 Black Android, 4G calling Smartwatch - ₹588 - 73% off
Roboster A1 Bluetooth & Camera Smart Watch Multicolor S... - ₹764 - 45% off
Rock Dz09 silver Smartwatch - ₹764 - 79% off
EWELL 4G,Sim,SD,Camera Compatible all Phones golden Sma... - ₹894 - 70% off
Enew DZ09-GOLD FNC7-X phone Gold Smartwatch - ₹672 - 74% off
i-Birds A1 phone Smartwatch - ₹1,033 - 65% off
Mizco DZ09 Black Smartwatch - ₹846 - 66% off
Rock Dz09 Smartwatch - ₹694 - 80% off
UV Global U8 Smart Watch Smartwatch - ₹697 - 82% off
drums F1 + color latest health smart band - ₹1,214 - 79% off
Zodo DZ09 Smartwatch Black Smartwatch - ₹858 - 78% off
Sai Enterprises A1 Smart watch black Smartwatch - ₹809 - 72% off
blueseed A1 phone Watch (Black Strap Free Size) Smartwa... - ₹710 - 64% off
K V ELECTRONICS DZ09 phone Smartwatch - ₹719 - 31% off
AF AFE0009 Fitness Smart Band - ₹840 - 47% off
Rock DZ09 Black 4G calling , Android Smartwatch - ₹579 - 73% off
Suroskie A1 phone Smartwatch - ₹899 - 59% off
SS DZ09 Fitness Black Smartwatch - ₹692 - 35% off
Estar M2 BLACK.ML.3 Fitness Smart Band - ₹808 - 63% off
SPORTZEE DZ09 BLACK Smartwatch - ₹719 - 82% off
SYL M9.Black.bh4 phone BLACK Smartwatch - ₹799 - 60% off
Enew DZ09-GOLD FC07-1SMW phone Rose Gold Smartwatch - ₹717 - 72% off
EWELL BT,4G Sim,sd Card slot for M_I phone Golden Smart... - ₹808 - 73% off
Mizco DZ09 Black Smartwatch - ₹718 - 71% off
>>> 
