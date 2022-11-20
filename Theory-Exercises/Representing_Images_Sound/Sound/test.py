from scipy.io import wavfile

samplingRate, sounddata = wavfile.read(".\StarWars3.wav")
print(samplingRate)

with open("output.txt", "w") as f:
    f.write(str(samplingRate))

for i in sounddata:
    print(i)

print(samplingRate)