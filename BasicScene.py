from playsound import playsound
import time
from BasicSceneMapping import GetPossibleOutputs

def PlayAudio(audio_files):
    """Riproduce una lista di file audio uno dopo l'altro."""
    for audio in audio_files:
        time.sleep(0.5)
        playsound(audio)

class Scene:
    """Classe base per tutte le scene."""
    
    def __init__(self, scene_type):
        self.type = scene_type
        self.input_audio = None
        self.introduction_audio = None

    def IntroductionAudio(self):
        """Riproduce l'audio di introduzione della scena."""
        PlayAudio(self.introduction_audio)

    def InputAudio(self):
        """Riproduce l'audio di input della scena."""
        if self.input_audio:
            PlayAudio(self.input_audio)

    def GetInputAudio(self):
        """Restituisce l'audio di input della scena."""
        return self.input_audio

    def GetPossibleOutputs(self):
        """Restituisce una lista delle possibili azioni e degli output associati."""
        return list(GetPossibleOutputs(self.type).items())

class StartScene(Scene):
    """Scena del menu iniziale."""
    
    def __init__(self):
        super().__init__("StartMenu")
        self.introduction_audio = ["Audios/_startingMenu/introapp.mp3", "Audios/_startingMenu/im_intro.mp3"]
        self.input_audio = ["Audios/_startingMenu/im_input.mp3"]
        self.first_time_done = False

class MenuScene(Scene):
    """Scena del menu principale."""
    
    def __init__(self):
        super().__init__("Menu")
        self.introduction_audio = ["Audios/_gameMenu/gm_intro.mp3"]
        self.input_audio = ["Audios/_gameMenu/gm_input.mp3"]
        self.first_time_done = False

class SheetScene(Scene):
    """Scena del menu delle schede."""
    
    def __init__(self):
        super().__init__("SheetMenu")
        self.introduction_audio = ["Audios/_sheetScene/ss_intro.mp3"]
        self.input_audio = ["Audios/_sheetScene/ss_input.mp3"]
        self.first_time_done = False

class KeypadScene(Scene):
    """Scena del tastierino numerico."""
    
    def __init__(self):
        super().__init__("Keypad")
        self.introduction_audio = ["Audios/_keypad/kp_intro.mp3"]
        self.input_audio = ["Audios/_keypad/kp_input.mp3"]
        self.first_time_done = False

class HelpScene(Scene):
    """Scena di aiuto."""
    
    def __init__(self, help_message: list):
        super().__init__("HelpScene")
        self.introduction_audio = ["Audios/_helpMenu/hs_intro.mp3"]
        self.input_audio = ["Audios/_helpMenu/hs_input.mp3"]
        self.help_audio = help_message
        self.first_time_done = False

class GameScene(Scene):
    """Scena di gioco."""
    
    def __init__(self, scene_id: str, linked_scenes: list = None, items: list = None, mementos: list = None, has_help: bool = False, narration_audio: list = None, focus_audio: list = None, help_audio: list = None, comingback_audio: list = None) -> None:
        if not self._IsValidId(scene_id):
            raise ValueError("L'ID deve essere una stringa di 4 cifre.")
        super().__init__("GameScene")
        self.id = scene_id
        self.introduction_audio = ["Audios/_gameScene/gs_intro.mp3"] + [f"Audios/_generic/_numbers/{num}.mp3" for num in self.id]
        self.input_audio = ["Audios/_gameScene/gs_input.mp3"]
        self.linked_scenes = linked_scenes if linked_scenes else []
        self.items = items if items else []
        self.mementos = mementos if mementos else []
        self.has_help = has_help
        self.narration_audio = narration_audio
        self.focus_audio = focus_audio
        self.help_audio = help_audio
        self.comingback_audio = comingback_audio
        self.help_unlocked = False
        self.i_was_there = False

    def GetiD(self):
        """Restituisce l'ID della scena di gioco."""
        return self.id

    def ComingBackAudio(self):
        """Riproduce l'audio di ritorno."""
        if self.comingback_audio:
            PlayAudio(self.comingback_audio)

    def HelpAudio(self):
        """Riproduce l'audio di aiuto."""
        if self.help_audio:
            PlayAudio(self.help_audio)
    
    def FocusAudio(self):
        """Riproduce l'audio di focus."""
        if self.focus_audio:
            PlayAudio(self.focus_audio)

    def NarrationAudio(self):
        """Riproduce l'audio di narrazione."""
        if self.narration_audio:
            PlayAudio(self.narration_audio)

    def GetHelpAudio(self):
        """Restituisce l'audio di aiuto."""
        return self.help_audio   

    def GetNarrationAudio(self):
        """Restituisce l'audio di narrazione."""
        return self.narration_audio    

    def GetFocusAudio(self):
        """Restituisce l'audio di focus."""
        return self.focus_audio

    def HasHelp(self):
        """Verifica se la scena di gioco ha un aiuto disponibile."""
        return self.has_help

    def _IsValidId(self, scene_id: str) -> bool:
        """Verifica se l'ID della scena è valido (4 cifre)."""
        return isinstance(scene_id, str) and scene_id.isdigit() and len(scene_id) == 4
    
    def GetLinkedScenes(self):
        """Restituisce le scene collegate."""
        return self.linked_scenes

    def ActivateScene(self, session):
        """Attiva la scena, aggiungendo nuovi oggetti e ricordi alla sessione."""
        new_items = []
        new_mementos = []

        for item in self.items:
            session.AddItem(item)
            new_items.append(item)

        for memento in self.mementos:
            session.AddMemento(memento)
            new_mementos.append(memento)
