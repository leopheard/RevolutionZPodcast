import requests
import re
from bs4 import BeautifulSoup

def get_soup(url1):
    page = requests.get(url1)
    soup = BeautifulSoup(page.text, 'html.parser')
    print "type: ", type(soup)
    return soup
get_soup("https://feeds.buzzsprout.com/330161.rss")

def get_playable_podcast1(soup):
    subjects = []
    for content in soup.find_all('item', limit=14):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
#            desc = content.find('description')
#            desc = desc.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')

        except AttributeError:
            continue
              
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': "https://storage.buzzsprout.com/variants/g58P4VdAXD5G1Sgb4DSRRmCm/f81607a3cd537406cf0cf506c726bfe2824c5e584c9e9dc5e04e42436c820a79?.jpg"
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
#            'info': podcast['desc'],
            'is_playable': True,
    })
    return items

def get_playable_podcast(soup):
    subjects = []
    for content in soup.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print "\n\nLink: ", link
            title = content.find('title')
            title = title.get_text()
#            desc = content.find('description')
#            desc = desc.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
#                'desc': desc,
                'thumbnail': "https://storage.buzzsprout.com/variants/g58P4VdAXD5G1Sgb4DSRRmCm/f81607a3cd537406cf0cf506c726bfe2824c5e584c9e9dc5e04e42436c820a79?.jpg",
        }
        subjects.append(item) 
    return subjects

def compile_playable_podcast(playable_podcast):
    items = []
    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })
    return items
