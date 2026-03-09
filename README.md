# Ambient Noise Generator

A Python tool for generating a wide variety of noise and ambient sounds for relaxation, sleep, meditation, or background atmosphere. Supports mixing multiple sounds with individual normalization, as well as random mixes.

## Features

- **Standard noises:** white, pink, brown
- **Natural/environmental:** water, fire, wind, rain, snow, breeze
- **Human/body:** heartbeat, breathing, womb, vibration
- **Space/abstract:** cosmic ambiance
- **Mixing:** combine multiple sources, normalize each individually, and normalize the final mix to avoid clipping
- **Random mode:** automatically generate a mix from a random set of sources

## Installation

```bash
git clone https://github.com/yourusername/ambient_noise_generator.git
cd ambient_noise_generator
pip install -r requirements.txt
```

## Usage

All generated files are saved in `output/` with filenames that include the sound sources, duration, and timestamp.

---

### 1. Generate a Single Sound Source

Generate one type of sound by passing a single value to `--sources`:

```bash
python generate_noise.py --sources white --duration 600      # 10 minutes of white noise
python generate_noise.py --sources rain --duration 300       # 5 minutes of rain
python generate_noise.py --sources womb --duration 1800      # 30 minutes of womb sound
python generate_noise.py --sources water --duration 3600     # 1 hour of water sound
```

### 2. Mix Multiple Sources

List multiple sources after `--sources` to create a custom mix:

```bash
python generate_noise.py --sources rain fire wind --duration 1200
python generate_noise.py --sources womb breathing brown --duration 1800
python generate_noise.py --sources water breeze cosmic --duration 900
```

### 3. Random Mix Mode

Let the tool pick random sources for you:

```bash
python generate_noise.py --random --num_random_sources 3 --duration 600
python generate_noise.py --random --num_random_sources 5 --duration 1800
```

### 4. Adjust Amplitude (Volume)

Control the normalization level with `--amplitude`:

```bash
python generate_noise.py --sources rain --duration 600 --amplitude 0.05
python generate_noise.py --sources white --duration 600 --amplitude 0.2
```

### 5. Change Output Directory

Override the default output folder with `--output_dir`:

```bash
python generate_noise.py --sources rain --duration 600 --output_dir output/rain_tracks
```

---

## Available Sound Sources

- **Noise:** `white`, `pink`, `brown`
- **Environmental:** `water`, `fire`, `wind`, `rain`, `snow`, `breeze`
- **Body:** `heartbeat`, `breathing`, `womb`, `vibration`
- **Space:** `cosmic`

## Output File Naming

Generated files include sources, duration, and timestamp, for example:

- `mix_white_600s_20260309_142300.wav`
- `mix_rain_fire_wind_1200s_20260309_142650.wav`
- `mix_womb_breathing_brown_1800s_20260309_143200.wav`

This makes it easy to organize and identify generated audio files.

## Command-Line Options

- `--sources`: List of sound types to mix (e.g., `water womb breeze`)
- `--random`: Enable random mix mode
- `--num_random_sources`: Number of sources to pick in random mode (default: 3)
- `--duration`: Output duration in seconds (default: 60)
- `--output_dir`: Output folder (default: `output/mix`)
- `--amplitude`: Target normalization amplitude (default: 0.1)

## Notes

- Each source is normalized individually before mixing.
- The final mix is normalized to avoid clipping.
- You can modify `noise_generator.py` to tweak sounds or add new types.

## Contributing

Fork the repository to add new sound types, improve mixing, or enhance randomization. Pull requests are welcome!
