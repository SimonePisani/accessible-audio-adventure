from playsound import playsound
import time
import cv2
import FingerCount as fg

def Ping(audio="Audios/_generic/Ping.mp3"):
    """
    Riproduce un audio di ping dopo un breve ritardo.
    """
    time.sleep(0.5)
    playsound(audio)

def AudioInput(audio2="", audio1="Audios/_generic/input.mp3"):
    """
    Riproduce due file audio in sequenza con un breve ritardo tra di loro.
    """
    time.sleep(0.5)
    playsound(audio1)
    time.sleep(0.5)
    playsound(audio2)

class FingerCountHandler:
    def __init__(self, parent_session):
        """
        Inizializza il gestore del conteggio delle dita con la sessione principale.
        """
        self.parent_session = parent_session
        self.numbers_of_fingers = None
        self.parent_session.is_speaking = True

    def start(self):
        """
        Avvia il processo di conteggio delle dita.
        """
        self.parent_session.is_speaking = False
        Ping()

        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            raise RuntimeError("Failed to open camera.")

        try:
            self.numbers_of_fingers = fg.FingerCounter().count_fingers(cap)
        finally:
            cap.release()

    def GetFingersCount(self):
        """
        Restituisce il numero di dita contate e riproduce un file audio corrispondente.
        """
        if self.numbers_of_fingers is not None:
            AudioInput(audio2=f"Audios/_generic/_numbers/{self.numbers_of_fingers}.mp3")
            return self.numbers_of_fingers
        return None
