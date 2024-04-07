from faster_whisper import WhisperModel

model_size = "large-v3"

# Run on GPU with FP16
model = WhisperModel("large-v3", device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# model = WhisperModel(model_size, device="cpu", compute_type="int8")

segments, info = model.transcribe("audio.mp3", beam_size=5, task="translate")

# print(help(model.transcribe))

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

text = ""

for segment in segments:
    text = text +segment.text
print(text)
    # print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))