import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf

tf.get_logger().setLevel('ERROR')
tf.autograph.set_verbosity(0)

import logging

logging.getLogger('absl').setLevel(logging.ERROR)
logging.getLogger('mediapipe').setLevel(logging.ERROR)
logging.getLogger('tensorflow').setLevel(logging.ERROR)

import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='google.protobuf')
warnings.filterwarnings('ignore', category=UserWarning, module='tensorflow')
warnings.filterwarnings('ignore', category=FutureWarning, module='tensorflow')

import cv2

cv2.setLogLevel(3)

from collections import deque
import mediapipe as mp
import numpy as np
import time

class FingerCounter:
    def __init__(self):
        """
        Inizializza la classe FingerCounter, impostando le variabili necessarie
        per il conteggio delle dita.
        """
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands
        self.tipIds = [4, 8, 12, 16, 20]
        self.fingCount = {'Left': 0, 'Right': 0}
        self.prev_total = 0
        self.total_buffer = deque(maxlen=30)
        self.start_time = None

    def is_stable(self):
        """
        Verifica se il conteggio delle dita è stabile.
        Restituisce True se il conteggio è stabile, altrimenti False.
        """
        if len(self.total_buffer) < self.total_buffer.maxlen:
            return False

        last_value = self.total_buffer[-1][0]
        for total, _ in self.total_buffer:
            if total != last_value:
                return False

        return True

    def count_fingers(self, cap):
        """
        Avvia il conteggio delle dita utilizzando la fotocamera fornita.
        Restituisce il conteggio stabile delle dita quando viene trovato.
        """
        stable_total = None

        with self.mp_hands.Hands(
                model_complexity=0,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5) as hands:

            while cap.isOpened():
                success, image = cap.read()
                if not success:
                    continue

                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = hands.process(image)
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if results.multi_hand_landmarks:
                    labels = []
                    for h in results.multi_handedness:
                        labels.append(h.classification[0].label)

                    self.fingCount['Left'] = 0
                    self.fingCount['Right'] = 0

                    for h, hand in enumerate(results.multi_hand_landmarks):
                        p = np.array([[lm.x, lm.y] for lm in hand.landmark])

                        for id in range(1, 5):
                            if p[self.tipIds[id]][1] < p[self.tipIds[id] - 2][1]:
                                self.fingCount[labels[h]] += 1

                        if labels[h] == "Right":
                            if p[self.tipIds[0]][0] < p[self.tipIds[0] - 1][0]:
                                self.fingCount[labels[h]] += 1
                        else:
                            if p[self.tipIds[0]][0] > p[self.tipIds[0] - 1][0]:
                                self.fingCount[labels[h]] += 1

                    total = self.fingCount['Left'] + self.fingCount['Right']
                    current_time = time.time()
                    self.total_buffer.append((total, current_time))

                    if self.is_stable():
                        stable_total = self.total_buffer[-1][0]
                        break

                    for hand_landmarks in results.multi_hand_landmarks:
                        self.mp_drawing.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS,
                                                       self.mp_drawing_styles.get_default_hand_landmarks_style(),
                                                       self.mp_drawing_styles.get_default_hand_connections_style())

                cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))

                if cv2.waitKey(5) & 0xFF == 27:
                    break

            cap.release()
            cv2.destroyAllWindows()

            if stable_total is not None:
                print(f"Valore stabile trovato: {stable_total}")
                return stable_total
