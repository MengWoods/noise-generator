import numpy as np
from scipy.io.wavfile import write

def generate_white_noise(duration_sec=60, sr=44100, amplitude=0.1):
    samples = np.random.normal(0, amplitude, sr*duration_sec)
    return samples.astype(np.float32)

def generate_pink_noise(duration_sec=60, sr=44100, amplitude=0.1):
    num_samples = sr*duration_sec
    num_columns = 16
    array = np.random.randn(num_columns, num_samples)
    pink = np.cumsum(array.sum(axis=0))
    pink = amplitude * pink / np.max(np.abs(pink))
    return pink.astype(np.float32)

def generate_brown_noise(duration_sec=60, sr=44100, amplitude=0.1):
    samples = np.cumsum(np.random.randn(sr*duration_sec))
    samples = amplitude * samples / np.max(np.abs(samples))
    return samples.astype(np.float32)

# ----- Simulated Environment / Ambient Sounds -----
def generate_water_flow(duration_sec=60, sr=44100, amplitude=0.05):
    white = np.random.normal(0, amplitude, sr*duration_sec)
    water = np.convolve(white, np.ones(100)/100, mode='same')
    return water.astype(np.float32)

def generate_fire_sound(duration_sec=60, sr=44100, amplitude=0.05):
    samples = np.zeros(sr*duration_sec)
    for i in range(0, len(samples), 500):
        burst = np.random.normal(0, amplitude, 50)
        end = min(i+50, len(samples))
        samples[i:end] = burst[:end-i]
    fire = np.convolve(samples, np.ones(20)/20, mode='same')
    return fire.astype(np.float32)

def generate_wind_sound(duration_sec=60, sr=44100, amplitude=0.05):
    white = np.random.normal(0, amplitude, sr*duration_sec)
    wind = np.convolve(white, np.ones(500)/500, mode='same')
    return wind.astype(np.float32)

def generate_rain_sound(duration_sec=60, sr=44100, amplitude=0.05):
    white = np.random.normal(0, amplitude, sr*duration_sec)
    rain = np.convolve(white, np.ones(50)/50, mode='same')
    return rain.astype(np.float32)

def generate_snow_sound(duration_sec=60, sr=44100, amplitude=0.02):
    white = np.random.normal(0, amplitude, sr*duration_sec)
    snow = np.convolve(white, np.ones(200)/200, mode='same')
    return snow.astype(np.float32)

def generate_heartbeat_sound(duration_sec=60, sr=44100, amplitude=0.05):
    samples = np.zeros(sr*duration_sec)
    interval = int(sr*0.8)  # 0.8s heartbeat interval
    for i in range(0, len(samples), interval):
        burst = np.random.normal(0, amplitude, 50)
        end = min(i+50, len(samples))
        samples[i:end] = burst[:end-i]
    heartbeat = np.convolve(samples, np.ones(10)/10, mode='same')
    return heartbeat.astype(np.float32)

def generate_womb_sound(duration_sec=60, sr=44100, amplitude=0.05):
    """Simulate maternal womb sound"""
    samples = generate_brown_noise(duration_sec, sr, amplitude*0.5)
    samples += generate_heartbeat_sound(duration_sec, sr, amplitude*0.5)
    return samples.astype(np.float32)

def generate_cosmic_sound(duration_sec=60, sr=44100, amplitude=0.03):
    """Simulate empty space / cosmic ambiance"""
    white = np.random.normal(0, amplitude, sr*duration_sec)
    cosmic = np.convolve(white, np.ones(1000)/1000, mode='same')
    return cosmic.astype(np.float32)

def generate_breathing_sound(duration_sec=60, sr=44100, amplitude=0.05):
    """Simulate slow deep breathing"""
    samples = np.zeros(sr*duration_sec)
    interval = int(sr*5)  # 5 seconds per breath
    for i in range(0, len(samples), interval):
        inhale = np.linspace(0, amplitude, interval//2)
        exhale = np.linspace(amplitude, 0, interval//2)
        breath = np.concatenate([inhale, exhale])
        end = min(i+interval, len(samples))
        samples[i:end] = breath[:end-i]
    return samples.astype(np.float32)

def generate_subtle_vibration(duration_sec=60, sr=44100, amplitude=0.02):
    """Simulate gentle vibration / rumble"""
    white = np.random.normal(0, amplitude, sr*duration_sec)
    vib = np.convolve(white, np.ones(200)/200, mode='same')
    return vib.astype(np.float32)

def generate_mild_breeze(duration_sec=60, sr=44100, amplitude=0.03):
    """Simulate gentle breeze / soft wind"""
    white = np.random.normal(0, amplitude, sr*duration_sec)
    breeze = np.convolve(white, np.ones(300)/300, mode='same')
    return breeze.astype(np.float32)

# ----- Save utility -----
def save_wav(samples, filename, sr=44100):
    write(filename, sr, samples)
