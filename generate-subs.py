import h5py
import os

input_file = "results.h5"
fps = 30

os.makedirs("output", exist_ok=True)
hdf = h5py.File("results.h5", "r")
for recording in hdf.keys():
    time = 0
    last_syllable = -1
    last_timestamp = "00:00.000"

    subs = open(f"output/{recording}.vtt", "w")
    subs.write("WEBVTT\n\n")

    syllables = hdf[recording]["syllable"]
    for syllable in syllables:
        time += 1/fps
        if syllable != last_syllable:
            minutes, seconds = divmod(time, 60)
            timestamp = str(int(minutes)).zfill(2)+":"+f"{seconds:.3f}".zfill(6)
            subs.write(f"{last_timestamp} --> {timestamp}\n")
            last_timestamp = timestamp
            subs.write(f"{syllable}\n\n")
    print(f"Processed {recording}")
