import os
import shutil

#paths
downloads = "/home/rbulanad/Downloads"
pictures = "/home/rbulanad/Pictures"
documents = "/home/rbulanad/Documents"
videos = "/home/rbulanad/Videos"

for name in os.listdir(downloads):
	src = os.path.join(downloads ,name)
	if os.path.isfile(src):
		_, ext = os.path.splitext(src)
        #Pictures
		if ext.lower() in (".png", ".jpg"):
			dst = os.path.join(pictures, name)
			shutil.move(src, dst)
			print(f"{name} moved to folder {pictures}");
        #Documents
		if ext.lower() in (".pdf"):
			dst = os.path.join(documents, name)
			shutil.move(src, dst)
			print(f"{name} moved to folder {documents}");
        #Videos
		if ext.lower() in (".avi", ".mov"):
			dst = os.path.join(videos, name)
			shutil.move(src, dst)
			print(f"{name} moved to folder {videos}");
		#More to be added when needed
