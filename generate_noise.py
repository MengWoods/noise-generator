import argparse
import os
import random
from datetime import datetime
from noise_generator import *

# Map sound types to functions
SOUND_TYPES = {
    "white": generate_white_noise,
    "pink": generate_pink_noise,
    "brown": generate_brown_noise,
    "water": generate_water_flow,
    "fire": generate_fire_sound,
    "wind": generate_wind_sound,
    "rain": generate_rain_sound,
    "snow": generate_snow_sound,
    "heartbeat": generate_heartbeat_sound,
    "womb": generate_womb_sound,
    "cosmic": generate_cosmic_sound,
    "breathing": generate_breathing_sound,
    "vibration": generate_subtle_vibration,
    "breeze": generate_mild_breeze
}

def save_sound(samples, output_dir, filename):
    os.makedirs(output_dir, exist_ok=True)
    full_path = os.path.join(output_dir, filename)
    save_wav(samples, full_path)
    print(f"Sound saved to {full_path}")

def normalize(samples, target_amplitude=0.1):
    """Normalize a numpy array to target amplitude"""
    max_val = max(1e-6, max(abs(samples)))  # prevent division by zero
    return samples * (target_amplitude / max_val)

def mix_sounds(sources, duration, sr=44100, amplitude=0.1):
    """Generate and mix multiple sources with per-source normalization"""
    mixed = None
    for src in sources:
        if src not in SOUND_TYPES:
            print(f"Warning: {src} is not a valid sound type, skipping")
            continue
        samples = SOUND_TYPES[src](duration, sr, amplitude)
        samples = normalize(samples, amplitude)  # normalize individually
        if mixed is None:
            mixed = samples
        else:
            mixed += samples
    if mixed is not None:
        # Final normalization
        mixed = normalize(mixed, amplitude)
        return mixed.astype('float32')
    return None

def main():
    parser = argparse.ArgumentParser(description="Generate and mix ambient sounds")
    parser.add_argument("--sources", type=str, nargs='+', help="List of sound types to mix")
    parser.add_argument("--random", action="store_true", help="Enable random mix mode")
    parser.add_argument("--num_random_sources", type=int, default=3, help="Number of random sources")
    parser.add_argument("--duration", type=int, default=60, help="Duration in seconds")
    parser.add_argument("--amplitude", type=float, default=0.1, help="Target amplitude")
    args = parser.parse_args()

    # Determine sources
    if args.random:
        sources = random.sample(list(SOUND_TYPES.keys()),
                                min(args.num_random_sources, len(SOUND_TYPES)))
        print(f"Randomly selected sources: {sources}")
    elif args.sources:
        sources = args.sources
    else:
        print("Error: you must provide --sources or enable --random")
        return

    # Determine output directory
    if args.random:
        output_dir = "output/mix"
    elif len(sources) == 1:
        output_dir = os.path.join("output", sources[0])
    else:
        output_dir = "output/mix"

    # Generate sound
    mixed_samples = mix_sounds(sources, args.duration, amplitude=args.amplitude)

    if mixed_samples is None:
        print("No valid sources to mix.")
        return

    source_str = "_".join(sources)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{source_str}_{args.duration}s_{timestamp}.wav"

    save_sound(mixed_samples, output_dir, filename)

if __name__ == "__main__":
    main()
