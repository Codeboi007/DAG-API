import librosa
import soundfile as sf
import numpy as np

def augment(file_path, method):
    y, sr = librosa.load(file_path)

    if method == "pitch":
        y_aug = librosa.effects.pitch_shift(y, sr, n_steps=4)
    elif method == "noise":
        noise = 0.005 * np.random.randn(len(y))
        y_aug = y + noise
    elif method == "stretch":
        y_aug = librosa.effects.time_stretch(y, rate=1.2)
    else:
        y_aug = y

    output_path = file_path.replace(".", "_augmented.")
    sf.write(output_path, y_aug, sr)
    return output_path
