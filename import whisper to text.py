import whisper
model = whisper.load_model("base")
result = model.transcribe("sonnet_131.m4a", fp16=False, language='English')
file = open("Sonnet_text_retry.txt",  "w")
file.write(result["text"])