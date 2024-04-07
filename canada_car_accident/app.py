from flask import Flask, render_template, request, jsonify
from pydub import AudioSegment
import speech_recognition as sr
#from faster_whisper import WhisperModel
import os
from vehicle_insurance import VI_main  # Ensure this module is correctly implemented

app = Flask(__name__)

#model = WhisperModel("base", device="cuda", compute_type="float16")  # Adjust as needed for your setup


@app.route('/', methods=['GET', 'POST'])
def index():
    where_you_were_options = [
        'same direction and same lane',
        'same direction and adjacent lane',
        'opposite direction',
        'parking lots/violate law',
        'intersection',
        'offence of drug'
    ]
    how_many_vehicles_options = [
        'two vehicles',
        'three or more vehicles'
    ]
    output_text = ''
    input_text = ''

    selected_where = ''
    selected_vehicles = ''

    if request.method == 'POST':
        selected_where = request.form['where_you_were']
        selected_vehicles = request.form['how_many_vehicles']
        input_text = request.form['input_text']
        print("Selected Where:", selected_where)
        print("Selected Vehicles:", selected_vehicles)
        print("Input Text:", input_text)
        output_text = VI_main(input_text, selected_where, selected_vehicles)
        print("Output Text:", output_text)
    return render_template('index.html', 
                           where_you_were_options=where_you_were_options,
                           how_many_vehicles_options=how_many_vehicles_options,
                           selected_where=selected_where,
                           selected_vehicles=selected_vehicles,
                           input_text=input_text,
                           output_text=output_text)

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file:
        # Save the file temporarily
        temp_file_path = "temp_audio.mp3"
        file.save(temp_file_path)

        # Use Whisper for transcription
        segments, info = model.transcribe(temp_file_path, beam_size=5, task="translate")
        os.remove(temp_file_path)  # Remove the temporary file

        text = "".join([segment.text for segment in segments])
        return jsonify({"transcription": text, "language": info.language, "language_probability": info.language_probability})

        


# @app.route('/transcribe', methods=['POST'])
# def transcribe_audio():
#     if 'file' not in request.files:
#         return "No file part", 400

#     file = request.files['file']
#     if file.filename == '':
#         return "No selected file", 400

#     if file:
#         # Convert the audio file to a compatible format
        
#         audio = AudioSegment.from_file(file, format="webm", codec="opus")
#         audio.export("temp.wav", format="wav")

#         # Use the converted audio file with speech_recognition
#         recognizer = sr.Recognizer()
#         with sr.AudioFile("temp.wav") as source:
#             audio_data = recognizer.record(source)
#         os.remove("temp.wav")  # Clean up the temporary file
#         try:
#             text = recognizer.recognize_google(audio_data)
#             return jsonify({"transcription": text})
#         except sr.UnknownValueError:
#             return jsonify({"transcription": "Transcription could not be understood."}), 400
#         except sr.RequestError as e:
#             return jsonify({"transcription": f"Could not request results; {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)



