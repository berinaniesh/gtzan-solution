import librosa

y,sr = librosa.load('vaaji.opus')
ms = librosa.feature.melspectrogram(y=y, sr=sr)

for i in ms:
    for k in i:
        if k>0:
            print(k, end=',')
    print("\n\n\n")
