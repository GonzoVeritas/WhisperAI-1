import whisper

# Ask user for input and output file names
input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")

model = whisper.load_model("base")
result = model.transcribe(input_file, fp16=False, language='English')

with open(output_file, "w") as file:
    file.write(result["text"])