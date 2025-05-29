# togaAudioPlayer
A simple audio player widget for Toga

## Installation
download whl file and install
``` 
pip install ...
```
## Usage

```python
from togaAudioPlayer import AudioPlayer

class MyApp(toga.App):
    def startup(self):
        main_box = toga.Box()
        self.player = AudioPlayer(port=8080)
        main_box.add(self.player)
        self.player.playsound("example.mp3")
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

def main():
    return MyApp()
```

### AudioPlayer class
 ```python
 class AudioPlayer(toga.WebView)
 ```
### playsound method
```python
def playsound(self, soundfile):
```
- `soundfile` (str): the path of the sound file to be played.

### stopsound method



```python
def stopsound(self):
```



## Example

```python
# import the required modules
...
from togaAudioPlayer import AudioPlayer


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

```