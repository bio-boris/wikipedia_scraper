import wikipedia
from mediawiki import MediaWiki
import mwclient
from pprint import pprint
import time


def debug_page(input_term):
    site = mwclient.Site('en.wikipedia.org')
    page = site.pages[input_term]
    images = page.images()
    image = images.next()
    pprint(vars(image))
    
def debug_image(image):
    pprint(image.imageinfo)

term = u'Photosynthesis'
site = mwclient.Site('en.wikipedia.org')
page = site.pages[term]

structures = []
images = page.images()

try:
    for image in images :
        image = images.next()

      
        structure = {'image': image.imageinfo['url'],
                    'caption': image._info['title'],
                    'term' : term
                    }
        
        if structure['image'] == "https://upload.wikimedia.org/wikipedia/commons/5/55/Photosynthesis_en.svg":
            print("img")
            pprint(image)
            print("imginfo")
            pprint(image.imageinfo)
            print("image")
            pprint(vars(image))
  
            
        structures.append(structure)
except Exception as e :
    print(e)
    print("Something bad happened")
    
    
final_structure = {'input_term' : term, 
                'images_list' : structures}





# Pywikibot – Probably the most used bot framework.
# ceterach - An interface for interacting with MediaWiki
# wikitools—A Python-2 only lightweight bot framework that uses the MediaWiki API exclusively for getting data and editing, used and maintained by Mr.Z-man (downloads)
# mwclient—An API-based framework maintained by Bryan
# mwparserfromhell - A wikitext parser, maintained by The Earwig
# pymediawiki - A read-only MediaWiki API wrapper in Python, which is simple to use.


# w = MediaWiki()

# class extractTerm():
#     term = None
    
#     def __init__(self, term):
#         self.term = term
    
#     def create_output(self, term, images):
#         return {'input_term' : term,
#                'images_list' : images}


#     def get_caption(self, image):
#         caption = "unknown"

#     def get_images(self, term):
#         page = w.page(term)
#         return page.images
    
#     def combine(self, images):
#         structures = []
#         for i,url in enumerate(images):  
#             structures.append({"term" : self.term,
#                         "image" : url,
#                         "caption" : self.get_caption(url)})
        
#         for structure in structures:
#             print(structure)
        
#     def get_result(self):
#         images = self.get_images(self.term)
#         self.combine(images)
    

# et = extractTerm("cat")
# et.get_result()



