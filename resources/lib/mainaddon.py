import requests
import re
from bs4 import BeautifulSoup

def get_soup1(url1):
    page = requests.get(url1)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup1))
    return soup1
def get_soup2(url2):
    page = requests.get(url2)
    soup2 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup2))
    return soup2
def get_soup3(url3):
    page = requests.get(url3)
    soup3 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup3))
    return soup3
def get_soup4(url4):
    page = requests.get(url4)
    soup4 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup4))
    return soup4
def get_soup5(url5):
    page = requests.get(url5)
    soup5 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup5))
    return soup5
def get_soup6(url6):
    page = requests.get(url6)
    soup6 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup6))
    return soup6
def get_soup7(url7):
    page = requests.get(url7)
    soup7 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup7))
    return soup7
def get_soup8(url8):
    page = requests.get(url8)
    soup8 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup8))
    return soup8
def get_soup9(url9):
    page = requests.get(url9)
    soup9 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup9))
    return soup9
def get_soup10(url10):
    page = requests.get(url10)
    soup10 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup10))
    return soup10
def get_soup11(url11):
    page = requests.get(url11)
    soup11 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup11))
    return soup11
def get_soup12(url12):
    page = requests.get(url12)
    soup12 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup12))
    return soup12
def get_soup13(url13):
    page = requests.get(url13)
    soup13 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup13))
    return soup13
def get_soup14(url14):
    page = requests.get(url14)
    soup14 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup14))
    return soup14
def get_soup15(url15):
    page = requests.get(url15)
    soup15 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup15))
    return soup15
def get_soup16(url16):
    page = requests.get(url16)
    soup16 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup16))
    return soup16
def get_soup17(url17):
    page = requests.get(url17)
    soup17 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup17))
    return soup17
def get_soup18(url18):
    page = requests.get(url1)
    soup18 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup18))
    return soup18
def get_soup19(url19):
    page = requests.get(url19)
    soup19 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup19))
    return soup19
def get_soup20(url20):
    page = requests.get(url20)
    soup20 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup20))
    return soup20
def get_soup21(url21):
    page = requests.get(url21)
    soup21 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup21))
    return soup21

def get_playable_podcast1(soup1):
    subjects = []
    for content in soup1.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://content.production.cdn.art19.com/images/d9/39/91/23/d9399123-8bf9-48fe-8eba-6decaa435123/7051c02bb2276f820a098bbbe4e52b748ae7fc64bebd60f286df9bcb2661a76949557bfd104b66f318557532a11913e7235946df70d65b6a7e0f2a855d16e31e.jpeg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast2(soup2):
    subjects = []
    for content in soup2.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone.imgix.net/podcasts/d4a40cce-8162-11e9-9165-637fddd329ba/image/uploads_2F1567104770637-8pkljjeolx-f365415a80c0d1633100e954d891091c_2FLandOfTheGiants_Tile_3000x3000.png?ixlib=rails-2.1.2&w=400&h=400",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast2(playable_podcast2):
    items = []
    for podcast in playable_podcast2:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast3(soup3):
    subjects = []
    for content in soup3.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone.imgix.net/podcasts/5c6a4f4a-e69c-11e8-8066-17a10182e4c8/image/uploads_2F1567104881501-7jj9dux2ly5-bfe7d3d30c5a358d2ba6c0d71f251a82_2FRecodeDecode_Tile_3000x3000.png?ixlib=rails-2.1.2&w=400&h=400",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast3(playable_podcast3):
    items = []
    for podcast in playable_podcast3:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast4(soup4):
    subjects = []
    for content in soup4.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone.imgix.net/podcasts/e4384094-e69c-11e8-8066-d3e055e78c28/image/uploads_2F1567104900743-rtvu7dtns3-76e86cad7f21668ef32e8a8709245168_2FRecodeMedia_Tile_3000x3000.png?ixlib=rails-2.1.2&w=400&h=400",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast4(playable_podcast4):
    items = []
    for podcast in playable_podcast4:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast5(soup5):
    subjects = []
    for content in soup5.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone.imgix.net/podcasts/c3d471b8-0241-11e9-8252-f7f578d82949/image/uploads_2F1557246246753-gf3fxmif9rg-8d84c8dfd35333cdeed8f75d75760516_2FTrinet_5BPivot_5D-Podcast_5BRecode_5D-180925-km.jpg?ixlib=rails-2.1.2&w=400&h=400",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast5(playable_podcast5):
    items = []
    for podcast in playable_podcast5:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast6(soup6):
    subjects = []
    for content in soup6.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://content.production.cdn.art19.com/images/bb/ae/09/4a/bbae094a-2155-4d58-982d-de9dfcfe85ca/55e801beccc45e3cdb857bae3d179f37b5c75c1a2b5737362b925426291f053dee31948f7c7f173e5d64b3b739ecaa31e22741aae8de6d4cbdcd94ac0da7a346.jpeg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast6(playable_podcast6):
    items = []
    for podcast in playable_podcast6:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast7(soup7):
    subjects = []
    for content in soup7.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone.imgix.net/podcasts/c3f826bc-e112-11e8-90b5-2f1c4d81c4e2/image/uploads_2F1567105022544-ch1o26tqd95-fecf1a20d1def5565ccc084daeb18eb8_2FTheWeeds_Tile_3000x3000.png?ixlib=rails-2.1.2&w=400&h=400",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast7(playable_podcast7):
    items = []
    for podcast in playable_podcast7:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast8(soup8):
    subjects = []
    for content in soup8.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone.imgix.net/podcasts/984bd016-dedf-11e8-8a56-63fe725d0fbd/image/uploads_2F1567105046744-z0irh4hsyaa-52932ad29198cf3dbe18a1755f487e05_2FTile_3000x3000.png?ixlib=rails-2.1.2&w=400&h=400",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast8(playable_podcast8):
    items = []
    for podcast in playable_podcast8:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast9(soup9):
    subjects = []
    for content in soup9.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone.imgix.net/podcasts/d5e1ef20-e112-11e8-83b5-ff093e8a88a8/image/uploads_2F1567109122292-1arrrzgdq41-5f052f5cc51f50e2b13dd609d9fb43a5_2FTile_3000x3000.png?ixlib=rails-2.1.2&w=400&h=400",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast9(playable_podcast9):
    items = []
    for podcast in playable_podcast9:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast10(soup10):
    subjects = []
    for content in soup10.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone.imgix.net/podcasts/7ea0f224-259b-11e9-8f74-bb984384b1ce/image/uploads_2F1568116909339-44bfbtegvrj-f9c264c9cb827b2e5cc9cd3ef48e6d5f_2FTile_Art_3000x3000.png?ixlib=rails-2.1.2&w=400&h=400",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast10(playable_podcast10):
    items = []
    for podcast in playable_podcast10:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast11(soup11):
    subjects = []
    for content in soup11.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone.imgix.net/podcasts/72db9b9a-ff87-11e8-8485-f340ca89e5a9/image/432b0598a89818ca0f042a59e32094c0103185175b769b5bbe1ba14347ae21664c75f944796c99a137847731df00aad0731c2977c46a2045af83887ca876736a.jpeg?ixlib=rails-2.1.2&w=400&h=400",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast11(playable_podcast11):
    items = []
    for podcast in playable_podcast11:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast12(soup12):
    subjects = []
    for content in soup12.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone.imgix.net/podcasts/f8555518-ae3c-11e9-81ba-53d330a64b43/image/uploads_2F1564019196383-30c0j1u1m4o-06471d0c2fd11ac4826b5dd3f62b68c1_2FREC_LandOfGiants_Tile_Art.png?ixlib=rails-2.1.2&w=400&h=400",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast12(playable_podcast12):
    items = []
    for podcast in playable_podcast12:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast13(soup13):
    subjects = []
    for content in soup13.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone.imgix.net/podcasts/881571d4-a356-11e9-8c43-531bca2b753d/image/uploads_2F1563819506021-0qxy4ecl0bi-6416de24f65ed4a49330aa75ed76603b_2FVMPN_003_PWTV_TileArt.jpg?ixlib=rails-2.1.2&w=400&h=400",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast13(playable_podcast13):
    items = []
    for podcast in playable_podcast13:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast14(soup14):
    subjects = []
    for content in soup14.find_all('item'):
        try:
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://podcasts.voxmedia.com/perch/resources/ithinkyoureinteresting.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast14(playable_podcast14):
    items = []
    for podcast in playable_podcast14:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast15(soup15):
    subjects = []
    for content in soup15.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://podcasts.voxmedia.com/perch/resources/function.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast15(playable_podcast15):
    items = []
    for podcast in playable_podcast15:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast16(soup16):
    subjects = []
    for content in soup16.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone.imgix.net/podcasts/d0542ac6-e69b-11e8-8066-ab0e93921919/image/uploads_2F1567104973116-zfwlxhzcrdl-fe995e561c15b207b6c0befb7f58ae0b_2FTheHistoryOfFun_Tile_3000x3000.png?ixlib=rails-2.1.2&w=400&h=400",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast16(playable_podcast16):
    items = []
    for podcast in playable_podcast16:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast17(soup17):
    subjects = []
    for content in soup17.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://podcasts.voxmedia.com/perch/resources/ply0879polygonshowpodcasttile2019-1.jpg",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast17(playable_podcast17):
    items = []
    for podcast in playable_podcast17:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast18(soup18):
    subjects = []
    for content in soup18.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone.imgix.net/podcasts/770e09f0-e69b-11e8-8066-d356113272d4/image/uploads_2F1547747079245-z1rd2g5y0cr-ac4e0094ca14ff6f2cfe99eb6e3db2e1_2FQuality%2BControl.png?ixlib=rails-2.1.2&w=400&h=400",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast18(playable_podcast18):
    items = []
    for podcast in playable_podcast18:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast19(soup19):
    subjects = []
    for content in soup19.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://podcasts.voxmedia.com/perch/resources/wyptb-04.png",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast19(playable_podcast19):
    items = []
    for podcast in playable_podcast5:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast20(soup20):
    subjects = []
    for content in soup20.find_all('item'):
        try:
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone.imgix.net/podcasts/e4c412e6-e1f0-11e8-9bde-83f9d376f059/image/uploads_2F1567105071975-o6k62rq8bin-247a9596590486c06b16976bed1cefbc_2FVergecast_Tile_3000x3000.png?ixlib=rails-2.1.2&w=400&h=400",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast20(playable_podcast20):
    items = []
    for podcast in playable_podcast20:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast21(soup21):
    subjects = []
    for content in soup21.find_all('item'):
        try:
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://megaphone.imgix.net/podcasts/63f3fa80-e1d9-11e8-a08a-6f343a1465a3/image/uploads_2F1555703148322-1p507b25rdo-ec4c08d7dc6193c757f37bf9c1ecad9d_2FVerge%2BExtras.png?ixlib=rails-2.1.2&w=400&h=400",
        }
        subjects.append(item)
    return subjects
def compile_playable_podcast21(playable_podcast21):
    items = []
    for podcast in playable_podcast20:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items
