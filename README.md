# WhisperAI
Whisper is an easy to use audio-to-text transcription program just insert source audio and change text file name, OpenAI will process.

>Whisper is an automatic speech recognition (ASR) system trained on 680,000 hours of multilingual and multitask supervised data collected from the web. We show that the use of such a large and diverse dataset leads to improved robustness to accents, background noise and technical language. Moreover, it enables transcription in multiple languages, as well as translation from those languages into English. We are open-sourcing models and inference code to serve as a foundation for building useful applications and for further research on robust speech processing.

This script is short and simple:
```
import whisper
model = whisper.load_model("base")
result = model.transcribe("how.m4a", fp16=False, language='English')
file = open("ww2-2.txt",  "w")
file.write(result["text"])
```
## Directions to use:
It's simple, in the python code, simply substitute the 2 variables for the input file name and the output file name. The input is your audio file, and the output is the text file.
```
result = model.transcribe("INPUT AUDIO FILE NAME", fp16=False, language='English')
file = open("OUTPUT.txt",  "w")
```
Before you can run it, make sure all the prerequisites are loaded. 
1. Python
2. Pytorch
3. Homebrew
4. FFMPEG
5. Whisper AI

Typically, you'll have items 1-3 already loaded, so just load or update FFMPEG & Whisper...
```
brew install ffmpeg
pip install -u openai-whisper
```
Note: Check for updated name on 'openai-whisper'



[Note: Here are editing and format commands for GitHub README.md files](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
