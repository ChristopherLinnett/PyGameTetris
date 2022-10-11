from pygame import mixer

class AudioController:
    def __init__(self):
      self.mixer = mixer
      self.mixer.init()

    def startMenuMusic(self):
        self.mixer.music.load('assets/gamemusic.mp3')
        self.mixer.music.set_volume(1)
        self.mixer.music.play()

    def pauseMusic(self):
        self.mixer.music.pause()
    
    def resumeMusic(self):
        self.mixer.music.unpause()

class SFXController:
    def __init__(self):
       self.mixer =  mixer
       self.mixer.init()
    
    def clearRow(self):
        self.mixer.