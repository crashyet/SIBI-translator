import os
import pickle
import cv2
import mediapipe as mp

# Inisialisasi MediaPipe Hands
mp_hands = mp.solutions.hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

# Folder dataset
DATA_DIR = './data'

data, labels = [], []

# Loop semua folder kelas
for label in os.listdir(DATA_DIR):
    folder_path = os.path.join(DATA_DIR, label)
    for img_name in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img_name)

        img = cv2.imread(img_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = mp_hands.process(img_rgb)

        if not results.multi_hand_landmarks:
            continue

        hand = results.multi_hand_landmarks[0]
        x_, y_, data_aux = [], [], []

        for lm in hand.landmark:
            x_.append(lm.x)
            y_.append(lm.y)

        for lm in hand.landmark:
            data_aux.extend([lm.x - min(x_), lm.y - min(y_)])

        data.append(data_aux)
        labels.append(label)

# Simpan ke file
with open('data.create', 'wb') as f:
    pickle.dump({'data': data, 'labels': labels}, f)
