from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
#https://cdn.vox-cdn.com/uploads/hub/sbnu_logo_minimal/441/touch_icon_iphone_retina_1000_yellow.755.png
url1 = "https://rss.art19.com/reset" #RESET
url2 = "https://feeds.megaphone.fm/landofthegiants"
url3 = "https://feeds.megaphone.fm/recodedecode"
url4 = "https://feeds.megaphone.fm/recodemedia"
url5 = "https://feeds.megaphone.fm/pivot"
url6 = "https://rss.art19.com/today-explained"
url7 = "https://feeds.megaphone.fm/theweeds"
url8 = "https://feeds.megaphone.fm/worldly"
url9 = "https://feeds.megaphone.fm/theezrakleinshow"
url10 = "https://feeds.megaphone.fm/switchedonpop"
url11 = "https://feeds.megaphone.fm/impact"
url12 = "https://feeds.megaphone.fm/futureperfect"
url13 = "https://feeds.megaphone.fm/primetime"
url14 = "https://feeds.megaphone.fm/ithinkyoureinteresting"
url15 = "http://feeds.megaphone.fm/function"
url16 = "https://feeds.megaphone.fm/historyoffun"
url17 = "https://feeds.megaphone.fm/thepolygonshow"
url18 = "https://feeds.megaphone.fm/qualitycontrol"
url19 = "https://feeds.megaphone.fm/wyptb"
url20 = "https://feeds.megaphone.fm/vergecast"
url21 = "https://feeds.megaphone.fm/verge-extras"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://content.production.cdn.art19.com/images/d9/39/91/23/d9399123-8bf9-48fe-8eba-6decaa435123/7051c02bb2276f820a098bbbe4e52b748ae7fc64bebd60f286df9bcb2661a76949557bfd104b66f318557532a11913e7235946df70d65b6a7e0f2a855d16e31e.jpeg"},
        {
            'label': plugin.get_string(30002), 
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/d4a40cce-8162-11e9-9165-637fddd329ba/image/uploads_2F1567104770637-8pkljjeolx-f365415a80c0d1633100e954d891091c_2FLandOfTheGiants_Tile_3000x3000.png?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes3'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/5c6a4f4a-e69c-11e8-8066-17a10182e4c8/image/uploads_2F1567104881501-7jj9dux2ly5-bfe7d3d30c5a358d2ba6c0d71f251a82_2FRecodeDecode_Tile_3000x3000.png?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30004),
            'path': plugin.url_for('episodes4'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/e4384094-e69c-11e8-8066-d3e055e78c28/image/uploads_2F1567104900743-rtvu7dtns3-76e86cad7f21668ef32e8a8709245168_2FRecodeMedia_Tile_3000x3000.png?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30005),
            'path': plugin.url_for('episodes5'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/c3d471b8-0241-11e9-8252-f7f578d82949/image/uploads_2F1557246246753-gf3fxmif9rg-8d84c8dfd35333cdeed8f75d75760516_2FTrinet_5BPivot_5D-Podcast_5BRecode_5D-180925-km.jpg?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30006),
            'path': plugin.url_for('episodes6'),
            'thumbnail': "https://content.production.cdn.art19.com/images/bb/ae/09/4a/bbae094a-2155-4d58-982d-de9dfcfe85ca/55e801beccc45e3cdb857bae3d179f37b5c75c1a2b5737362b925426291f053dee31948f7c7f173e5d64b3b739ecaa31e22741aae8de6d4cbdcd94ac0da7a346.jpeg"},
        {
            'label': plugin.get_string(30007),
            'path': plugin.url_for('episodes7'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/c3f826bc-e112-11e8-90b5-2f1c4d81c4e2/image/uploads_2F1567105022544-ch1o26tqd95-fecf1a20d1def5565ccc084daeb18eb8_2FTheWeeds_Tile_3000x3000.png?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30008),
            'path': plugin.url_for('episodes8'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/984bd016-dedf-11e8-8a56-63fe725d0fbd/image/uploads_2F1567105046744-z0irh4hsyaa-52932ad29198cf3dbe18a1755f487e05_2FTile_3000x3000.png?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30009),
            'path': plugin.url_for('episodes9'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/d5e1ef20-e112-11e8-83b5-ff093e8a88a8/image/uploads_2F1567109122292-1arrrzgdq41-5f052f5cc51f50e2b13dd609d9fb43a5_2FTile_3000x3000.png?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30010),
            'path': plugin.url_for('episodes10'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/7ea0f224-259b-11e9-8f74-bb984384b1ce/image/uploads_2F1568116909339-44bfbtegvrj-f9c264c9cb827b2e5cc9cd3ef48e6d5f_2FTile_Art_3000x3000.png?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30011),
            'path': plugin.url_for('episodes11'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/72db9b9a-ff87-11e8-8485-f340ca89e5a9/image/432b0598a89818ca0f042a59e32094c0103185175b769b5bbe1ba14347ae21664c75f944796c99a137847731df00aad0731c2977c46a2045af83887ca876736a.jpeg?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30012),
            'path': plugin.url_for('episodes12'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/f8555518-ae3c-11e9-81ba-53d330a64b43/image/uploads_2F1564019196383-30c0j1u1m4o-06471d0c2fd11ac4826b5dd3f62b68c1_2FREC_LandOfGiants_Tile_Art.png?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30013),
            'path': plugin.url_for('episodes13'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/881571d4-a356-11e9-8c43-531bca2b753d/image/uploads_2F1563819506021-0qxy4ecl0bi-6416de24f65ed4a49330aa75ed76603b_2FVMPN_003_PWTV_TileArt.jpg?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30014),
            'path': plugin.url_for('episodes14'),
            'thumbnail': "https://podcasts.voxmedia.com/perch/resources/ithinkyoureinteresting.jpg"},
        {
            'label': plugin.get_string(30015),
            'path': plugin.url_for('episodes15'),
            'thumbnail': "https://podcasts.voxmedia.com/perch/resources/function.jpg"},
        {
            'label': plugin.get_string(30016),
            'path': plugin.url_for('episodes16'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/d0542ac6-e69b-11e8-8066-ab0e93921919/image/uploads_2F1567104973116-zfwlxhzcrdl-fe995e561c15b207b6c0befb7f58ae0b_2FTheHistoryOfFun_Tile_3000x3000.png?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30017),
            'path': plugin.url_for('episodes17'),
            'thumbnail': "https://podcasts.voxmedia.com/perch/resources/ply0879polygonshowpodcasttile2019-1.jpg"},
        {
            'label': plugin.get_string(30018),
            'path': plugin.url_for('episodes18'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/770e09f0-e69b-11e8-8066-d356113272d4/image/uploads_2F1547747079245-z1rd2g5y0cr-ac4e0094ca14ff6f2cfe99eb6e3db2e1_2FQuality%2BControl.png?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30019),
            'path': plugin.url_for('episodes19'),
            'thumbnail': "https://podcasts.voxmedia.com/perch/resources/wyptb-04.png"},
        {
            'label': plugin.get_string(30020),
            'path': plugin.url_for('episodes20'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/e4c412e6-e1f0-11e8-9bde-83f9d376f059/image/uploads_2F1567105071975-o6k62rq8bin-247a9596590486c06b16976bed1cefbc_2FVergecast_Tile_3000x3000.png?ixlib=rails-2.1.2&w=400&h=400"},
        {
            'label': plugin.get_string(30021),
            'path': plugin.url_for('episodes21'),
            'thumbnail': "https://megaphone.imgix.net/podcasts/63f3fa80-e1d9-11e8-a08a-6f343a1465a3/image/uploads_2F1555703148322-1p507b25rdo-ec4c08d7dc6193c757f37bf9c1ecad9d_2FVerge%2BExtras.png?ixlib=rails-2.1.2&w=400&h=400"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items

@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items

@plugin.route('/episodes4/')
def episodes4():
    soup4 = mainaddon.get_soup4(url4)
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items

@plugin.route('/episodes5/')
def episodes5():
    soup1 = mainaddon.get_soup5(url5)
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items

@plugin.route('/episodes6/')
def episodes6():
    soup6 = mainaddon.get_soup6(url6)
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    items = mainaddon.compile_playable_podcast6(playable_podcast6)
    return items

@plugin.route('/episodes7/')
def episodes7():
    soup7 = mainaddon.get_soup7(url7)
    playable_podcast7 = mainaddon.get_playable_podcast7(soup7)
    items = mainaddon.compile_playable_podcast7(playable_podcast7)
    return items

@plugin.route('/episodes8/')
def episodes8():
    soup8 = mainaddon.get_soup8(url8)
    playable_podcast8 = mainaddon.get_playable_podcast8(soup8)
    items = mainaddon.compile_playable_podcast8(playable_podcast8)
    return items

@plugin.route('/episodes9/')
def episodes9():
    soup9 = mainaddon.get_soup9(url9)
    playable_podcast9 = mainaddon.get_playable_podcast9(soup9)
    items = mainaddon.compile_playable_podcast9(playable_podcast9)
    return items

@plugin.route('/episodes10/')
def episodes10():
    soup10 = mainaddon.get_soup10(url10)
    playable_podcast10 = mainaddon.get_playable_podcast10(soup10)
    items = mainaddon.compile_playable_podcast10(playable_podcast10)
    return items

@plugin.route('/episodes11/')
def episodes11():
    soup11 = mainaddon.get_soup11(url11)
    playable_podcast11 = mainaddon.get_playable_podcast11(soup11)
    items = mainaddon.compile_playable_podcast11(playable_podcast11)
    return items

@plugin.route('/episodes12/')
def episodes12():
    soup12 = mainaddon.get_soup12(url12)
    playable_podcast12 = mainaddon.get_playable_podcast12(soup12)
    items = mainaddon.compile_playable_podcast12(playable_podcast12)
    return items

@plugin.route('/episodes13/')
def episodes13():
    soup13 = mainaddon.get_soup13(url13)
    playable_podcast13 = mainaddon.get_playable_podcast13(soup13)
    items = mainaddon.compile_playable_podcast13(playable_podcast13)
    return items

@plugin.route('/episodes14/')
def episodes14():
    soup14 = mainaddon.get_soup14(url14)
    playable_podcast14 = mainaddon.get_playable_podcast14(soup14)
    items = mainaddon.compile_playable_podcast14(playable_podcast14)
    return items

@plugin.route('/episodes15/')
def episodes15():
    soup15 = mainaddon.get_soup15(url15)
    playable_podcast15 = mainaddon.get_playable_podcast15(soup15)
    items = mainaddon.compile_playable_podcast15(playable_podcast15)
    return items

@plugin.route('/episodes16/')
def episodes16():
    soup16 = mainaddon.get_soup16(url16)
    playable_podcast16 = mainaddon.get_playable_podcast16(soup16)
    items = mainaddon.compile_playable_podcast16(playable_podcast16)
    return items

@plugin.route('/episodes17/')
def episodes17():
    soup17 = mainaddon.get_soup17(url17)
    playable_podcast17 = mainaddon.get_playable_podcast17(soup17)
    items = mainaddon.compile_playable_podcast17(playable_podcast17)
    return items

@plugin.route('/episodes18/')
def episodes18():
    soup18 = mainaddon.get_soup18(url18)
    playable_podcast18 = mainaddon.get_playable_podcast18(soup18)
    items = mainaddon.compile_playable_podcast18(playable_podcast18)
    return items

@plugin.route('/episodes19/')
def episodes19():
    soup19 = mainaddon.get_soup19(url19)
    playable_podcast19 = mainaddon.get_playable_podcast19(soup19)
    items = mainaddon.compile_playable_podcast19(playable_podcast19)
    return items

@plugin.route('/episodes20/')
def episodes20():
    soup20 = mainaddon.get_soup20(url20)
    playable_podcast20 = mainaddon.get_playable_podcast20(soup20)
    items = mainaddon.compile_playable_podcast20(playable_podcast20)
    return items

@plugin.route('/episodes21/')
def episodes21():
    soup21 = mainaddon.get_soup21(url21)
    playable_podcast21 = mainaddon.get_playable_podcast21(soup21)
    items = mainaddon.compile_playable_podcast21(playable_podcast21)
    return items

if __name__ == '__main__':
    plugin.run()
