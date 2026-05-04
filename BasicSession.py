from playsound import playsound
import time
from BasicScene import *
from BasicSceneInitializer import InitializeScenes
from BasicFingerCountHandler import FingerCountHandler
from BasicSceneMapping import InputElaboration

def PlayAudio(audio_files):
    """
    Riproduce una lista di file audio con una pausa di 0,5 secondi tra ciascuno.
    """
    for audio in audio_files:
        time.sleep(0.5)
        playsound(audio)

class Session:
    def __init__(self):
        """
        Inizializza la sessione di gioco, impostando le scene e lo stato iniziale.
        """
        self.scenes = InitializeScenes()
        self.finger_count_handler = FingerCountHandler(self)
        self.is_speaking = False
        self.current_scene = None
        self.current_game_scene = None
        self.game_scene_initialized = False
        self.scene_initialized = False
        self.hourglass = 1
        self.items = []
        self.mementos = []
        self.current_code = ""
        self.is_ending = False
        self.first_game_scene_done = False

        self.start()

    def start(self):
        """
        Avvia la sessione impostando la scena iniziale e chiamando il gestore delle scene.
        """
        self.current_scene = self.scenes["StartMenu"]
        self.game_scene_initialized = False
        self.SceneHandler()

    def SceneHandler(self):
        """
        Ciclo principale per la gestione delle scene, riproduce l'audio e gestisce l'input dell'utente.
        """
        while True:
            self.HandleSceneAudio(self.current_scene)
            self.UpdateSceneFlags()
            possible_outputs = dict(self.current_scene.GetPossibleOutputs())
            choice = self.GetUserInput(possible_outputs)
            self.ProcessChoice(choice)

    def HandleSceneAudio(self, scene):
        """
        Gestisce l'audio della scena corrente.
        """
        if not self.scene_initialized:
            scene.IntroductionAudio()
            if isinstance(scene, GameScene):
                self.HandleGameSceneAudio(scene)
            else:
                if not scene.first_time_done:
                    time.sleep(1)
                    scene.InputAudio()

    def HandleGameSceneAudio(self, scene):
        """
        Gestisce l'audio specifico per le scene di gioco.
        """
        if not self.game_scene_initialized:
            time.sleep(1)
            if not scene.i_was_there:
                scene.NarrationAudio()
                time.sleep(1)
                if scene.GetiD() == "5347":
                    exit()
            elif scene.comingback_audio:
                scene.ComingBackAudio()
                time.sleep(1)
            if not self.first_game_scene_done:
                scene.InputAudio()

    def UpdateSceneFlags(self):
        """
        Aggiorna i flag delle scene per tenere traccia dello stato del gioco.
        """
        if not isinstance(self.current_scene, GameScene):
            self.current_scene.first_time_done = True
        if isinstance(self.current_scene, GameScene):
            self.first_game_scene_done = True
        self.game_scene_initialized = True
        self.scene_initialized = True

    def GetUserInput(self, possible_outputs):
        """
        Ottiene l'input dell'utente e verifica se è valido.
        """
        while True:
            choice = self.WaitAudioAndGetResult()
            if choice in possible_outputs:
                return choice
            else:
                PlayAudio(["Audios/_generic/invalidchoice.mp3"])

    def ProcessChoice(self, choice):
        """
        Processa la scelta dell'utente e chiama il gestore appropriato.
        """
        if isinstance(self.current_scene, KeypadScene):
            self.KeypadHandler(choice)
        else:
            self.ChoiceHandler(choice)

    def ChoiceHandler(self, choice):
        """
        Gestisce la scelta dell'utente e determina la scena successiva.
        """
        next_scene, output = InputElaboration(self, self.current_scene, choice, self.scenes, self.current_game_scene)
        if output:
            self.HandleOutput(output)
        if next_scene:
            self.SwitchScene(next_scene)

    def HandleOutput(self, output):
        """
        Gestisce l'output della scena corrente, inclusa la riproduzione di audio e l'utilizzo della clessidra.
        """
        if "Help" in output[0] and self.hourglass > 0:
            self.UseHourglass()
            self.current_scene = self.current_game_scene
        else:
            PlayAudio(output)
            if "closingApp" in output[0]:
                exit()

    def UseHourglass(self):
        """
        Utilizza una clessidra per sbloccare aiuti e gestisce il passaggio alla scena finale se necessario.
        """
        self.hourglass -= 1
        self.current_game_scene.HelpAudio()
        self.current_game_scene.help_unlocked = True
        if self.hourglass < 1 and not self.is_ending:
            self.is_ending = True
            self.game_scene_initialized = False
            self.SwitchScene(self.scenes["GameScene_5347"])

    def SwitchScene(self, next_scene):
        """
        Passa alla scena successiva, aggiornando gli stati e attivando la scena se necessario.
        """
        if isinstance(next_scene, GameScene):
            if isinstance(self.current_scene, (StartScene, KeypadScene)):
                self.game_scene_initialized = False
            self.current_game_scene = next_scene
            if not self.current_game_scene.i_was_there:
                self.current_game_scene.ActivateScene(self)
        self.scene_initialized = False
        self.current_scene.i_was_there = True
        self.current_scene = next_scene

    def KeypadHandler(self, choice):
        """
        Gestisce l'input dell'utente nella scena del tastierino numerico.
        """
        if choice == 10:
            self.ResetCurrentCode()
        elif 0 <= choice <= 9:
            self.UpdateCurrentCode(choice)
            if len(self.current_code) == 4:
                self.VerifyCode()

    def ResetCurrentCode(self):
        """
        Reimposta il codice corrente e torna alla scena di gioco corrente.
        """
        self.current_code = ""
        self.SwitchScene(self.current_game_scene)

    def UpdateCurrentCode(self, choice):
        """
        Aggiorna il codice corrente con la scelta dell'utente.
        """
        self.current_code += str(choice)
        self.PlayCurrentCodeAudio()

    def PlayCurrentCodeAudio(self):
        """
        Riproduce l'audio del codice corrente.
        """
        audio_files = ["Audios/_keypad/kp_currentCode.mp3"] + [f"Audios/_generic/_numbers/{num}.mp3" for num in self.current_code]
        PlayAudio(audio_files)

    def VerifyCode(self):
        """
        Verifica se il codice inserito è valido e gestisce la transizione di scena.
        """
        if self.current_code in self.current_game_scene.GetLinkedScenes():
            self.HandleValidCode()
        else:
            PlayAudio(["Audios/_generic/invalidcode.mp3"])
        self.current_code = ""

    def HandleValidCode(self):
        """
        Gestisce il caso in cui il codice inserito è valido.
        """
        new_scene_key = f"GameScene_{self.current_code}"
        if new_scene_key in self.scenes:
            new_scene = self.scenes[new_scene_key]
            if isinstance(new_scene, GameScene):
                PlayAudio(["Audios/_generic/validcode.mp3"])
                self.SwitchScene(new_scene)
                if not new_scene.i_was_there:
                    self.current_game_scene.ActivateScene(self)
            else:
                PlayAudio(["Audios/_generic/invalidcode.mp3"])
        else:
            PlayAudio(["Audios/_generic/invalidcode.mp3"])

    def WaitAudioAndGetResult(self):
        """
        Attende l'audio e ottiene il risultato del conteggio delle dita.
        """
        self.is_speaking = True
        self.finger_count_handler.start()
        return self.finger_count_handler.GetFingersCount()

    def AddItem(self, item):
        """
        Aggiunge un oggetto all'inventario dell'utente.
        """
        if item not in self.items:
            self.items.append(item)

    def AddMemento(self, memento):
        """
        Aggiunge un memento alla collezione dell'utente.
        """
        if memento not in self.mementos:
            self.mementos.append(memento)
