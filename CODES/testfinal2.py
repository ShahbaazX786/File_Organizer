import os
import ctypes
from del1 import*
from pathlib import Path

	
DIRECTORIES = {
        #web based files
	"WEB LINKS": [".asp",".cer",".cfm",".pl",".css",".html5",".htm", ".xhtml",".dhtml",".phtml",".jhtml",".zhtml"
                 ,".rhtml",".mhtml",".shtml",".css",".scss",".sass",".php","jsp",".rss",".js"],
	"IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", 
			".heif", ".psd",".ai",".ico",".ps",".tif",".tiff"], 
	"VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", 
			".qt", ".mpg", ".mpeg", ".3gp"], 
	"DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", 
				".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", 
				".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", 
				"pptx",".pdf"], 
	"ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", 
				".dmg", ".rar", ".xar", ".zip",".rpm",".z"],
        "DISK FILES": [".bin",".dmg",".toast",".iso",".vcd"],
        "EXECUTABLE FILES:": [".apk",".bat",".bin",".cgi",".pl",".com",".exe",".gadget",".jar",".wsf"],
        "FONTS": [".fnt",".fon",".otf",".ttf"],
                      
	"AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", 
			".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"], 
	"PLAINTEXT": [".txt", ".in", ".out"], 
	
        "PROGRAMS":[".c",".class",".cpp",".java",".php",".pl",".py",".cs",".sh",".vb",".net"]

} 

FILE_FORMATS = {file_format: directory 
				for directory, file_formats in DIRECTORIES.items() 
				for file_format in file_formats} 

def organize_junk(): 
	for entry in os.scandir(): 
		if entry.is_dir(): 
			continue
		file_path = Path(entry) 
		file_format = file_path.suffix.lower() 
		if file_format in FILE_FORMATS: 
			directory_path = Path(FILE_FORMATS[file_format]) 
			directory_path.mkdir(exist_ok=True) 
			file_path.rename(directory_path.joinpath(file_path)) 

		for dir in os.scandir(): 
			try: 
				os.rmdir(dir) 
			except: 
				pass





			
if __name__ == "__main__": 
	organize_junk()
	md5()
	rm_dup()
   
ctypes.windll.user32.MessageBoxW(0, "Files Organised Successfully!", "File Organizer", 1)
