from pygame import mixer

# This class is responsible for playing audio files.
class AudioController:
    def __init__(self):
      self.mixer = mixer
      self.mixer.init()
      self.mixer.music.set_volume(1)
      self.initSounds()

    def initSounds(self):
        """
        The function initSounds() initializes the sounds dictionary with the sound files
        """
        self.sounds = {}
        self.sounds['brickDroppedSound'] = self.mixer.Sound('assets/brickdropped.mp3')
        self.sounds['endGameSound'] = self.mixer.Sound('assets/endgame.wav')
        self.sounds['levelUpSound'] = self.mixer.Sound('assets/levelup.wav')
        self.sounds['pauseGameSound'] = self.mixer.Sound('assets/pausegame.wav')
        self.sounds['saveHighScoreSound'] = self.mixer.Sound('assets/savehighscore.wav')
        self.sounds['clearRowSound'] = self.mixer.Sound('assets/clear.wav')

    def playSound(self, sound):
        """
        If the volume is greater than 0, play the sound
        
        :param sound: The name of the sound file to play
        """
        if self.mixer.music.get_volume()>0:
            self.sounds[f'{sound}'].play()

    def startMenuMusic(self):
        """
        If the music is playing, stop it. If it's not playing, load the music and play it
        """
        if self.mixer.music.get_busy():
            self.mixer.music.stop()
        self.mixer.music.load('assets/menumusic.mp3')
        self.mixer.music.play(loops=-1)

    def startGameMusic(self):
        """
        It stops the current music, loads the game music, and plays it on a loop
        """
        self.mixer.music.stop()
        self.mixer.music.load('assets/gamemusic.mp3')
        self.mixer.music.play(loops=-1)

    def pauseMusic(self):
        """
        It pauses the music
        """
        self.mixer.music.pause()
    
    def resumeMusic(self):
        """
        It unpauses the music
        """
        self.mixer.music.unpause()