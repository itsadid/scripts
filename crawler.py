import re

import requests


def get_url_from_user():
    url = input("enter url:")
    print("you entered %s" % url)
    return url


def get_webpage_from_url(url):
    webpage = requests.get(url)
    html_bytes = webpage.content
    html_string = html_bytes.decode('UTF-8')
    return html_string


def get_img_from_webpage(html_string):
    photo_match = re.findall("((http|https|ftp):\/\/[0-9a-zA-Z\"\'~%_,-]+[\/\.[0-9a-zA-Z%\"\'_,~\-]+?\.(jpeg|png|jpg|gif|mp4|webp))",html_string)
    #print(photo_match)
    for i, photo in enumerate(photo_match):
        pic_ptype = photo[2]
        print(photo)
        img_file = requests.get(photo[0])
        #print(img_file)
        with open('pictures_from_website/new_image_{n}.{ptype}'.format(n=i, ptype=pic_ptype),"wb") as f:
            f.write(img_file.content)

def main():
    url = get_url_from_user()
    webpage = get_webpage_from_url(url)
    get_img_from_webpage(webpage)
    #print("webpage")
    #print(webpage)


main()
