from pygame import mixer

class AudioController:
    def __init__(self):
      self.mixer = mixer
      self.mixer.music.set_volume(1)
      self.initSounds()

    def initSounds(self):
        self.sounds = {}
        self.sounds['brickDroppedSound'] = self.mixer.Sound('assets/brickdropped.mp3')
        self.sounds['endGameSound'] = self.mixer.Sound('assets/endgame.wav')
        self.sounds['levelUpSound'] = self.mixer.Sound('assets/levelup.wav')
        self.sounds['pauseGameSound'] = self.mixer.Sound('assets/pausegame.wav')
        self.sounds['saveHighScoreSound'] = self.mixer.Sound('assets/savehighscore.wav')

    def playSound(self, sound):
        if self.mixer.music.get_volume()>0:
            self.sounds[f'{sound}'].play()

    def startMenuMusic(self):
        if self.mixer.music.get_busy():
            self.mixer.music.stop()
        self.mixer.music.load('assets/menumusic.mp3')
        self.mixer.music.play(loops=-1)

    def startGameMusic(self):
        self.mixer.music.stop()
        self.mixer.music.load('assets/gamemusic.mp3')
        self.mixer.music.play(loops=-1)

    def pauseMusic(self):
        self.mixer.music.pause()
    
    def resumeMusic(self):
        self.mixer.music.unpause()