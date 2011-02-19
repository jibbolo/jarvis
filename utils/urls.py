import os
from django.conf import settings
from django.views.generic.simple import direct_to_template

class StaticUrls(object):

    def listfiles(self,dir,path):
        files = []
        for res in os.listdir(dir):
            
            # Directory
            if os.path.isdir(os.path.join(dir,res)):
                # recursive call
                files += self.listfiles(
                                    dir=os.path.join(dir,res),
                                    path=os.path.join(path,res)
                                )
            # Files
            else:
                if res.endswith(".static.html"):
                    files.append({
                        "url":os.path.join(path,res.replace(".static.html","")),
                        "file":os.path.join(path,res),
                    })
                    
        return files
        
    def discover(self):
        template_dirs = settings.TEMPLATE_DIRS
        patterns = []
        for td in template_dirs:
            urls = self.listfiles(td,"")
            for url in urls:
                patterns.append((
                    r'^%s/$' % url['url'],
                    direct_to_template,
                    {'template':url['file']},
                ))
            
        return patterns