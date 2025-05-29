

from http.server import HTTPServer, BaseHTTPRequestHandler
import os
from pathlib import Path
from urllib.parse import unquote

import toga
from toga.style import Pack
import threading
import toga



ext={'.acp':'x-mei-aac',
     '.aif':'aiff',
     '.aiff':'aiff',
     '.aifc':'aiff',
     '.au':'basic',
     '.la1':'x-liquid-file',
     '.lavs':'x-liquid-secure',
     '.lmsff':'x-la-lms',
     '.m3u':'mpegurl',
     '.midi':'mid',
     '.mid':'mid',
     '.mp2':'mp2',
     '.mp3':'mp3',
     '.mp4':'mp4',
     '.mnd':'x-musicnet-download',
     '.mp1':'mp1',
     '.mns':'x-musicnet-stream',
     '.mpga':'rn-mpeg',
     '.pls':'scpls',
     '.ram':'x-pn-realaudio',
     '.rmi':'mid',
     '.rmm':'x-pn-realaudio',
     '.snd':'basic',
     '.wav':'wav',
     '.wax':'x-ms-wax',
     '.wma':'x-ms-wma',
     } 
#ref: https://www.iana.org/assignments/media-types/media-types.xhtml

TEMP_URL=f"https://example.com/" #this is a temp url.

class AudioPlayer(toga.WebView):
    '''Use HttpServer to serve audio files to the webview.'''
    #webview=toga.WebView()
    port=8080
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            filePath = self.path.lstrip('/')
            filePath = unquote(filePath)
            filePath=os.path.abspath(filePath)
            fileName=filePath.split("/")[-1]
            fileExt=os.path.splitext(fileName)[1]
            if fileExt not in ext:
                raise ValueError(f"Unsupported file extension {fileExt}")
            if not os.path.exists(filePath):
                raise ValueError(f"File {filePath} does not exist")
            
            self.send_response(200)
            self.send_header('Content-type', f'audio/{ext[fileExt]}')
            self.end_headers()

            with open(Path(filePath), 'rb') as f:
                content = f.read()
            self.wfile.write(content)

    def __init__(self,port=8080):
        super().__init__(style=Pack(width=1,height=1))
        self.port=port
        self.server=HTTPServer(('localhost', self.port), self.Handler)
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.start()
    def playsound(self,file:str):
        self.url= TEMP_URL# have to do this. Or no audio will be played
        self.url=f"http://localhost:{self.port}/{file}"
    def stopsound(self):
        self.url=TEMP_URL
    def closeServer(self):
        self.server.shutdown()
    def __del__(self):
        self.closeServer()

# usage:

'''
class ts(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()
        self.player=AudioPlayer(port=8080)
        main_box.add(self.player)
        self.player.playsound("example.mp3")
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

        
def main():
    return ts()

'''