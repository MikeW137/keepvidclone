from flask import Flask, render_template, request
import requests
from urllib import parse
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/download', methods = ['GET'])
def download():
    name = request.args.get('name')
    r = requests.get(name)

    full_string = r.text
    search_string_720 = "itag=22"
    itag_location_720 = full_string.find(search_string_720)
    url_location = full_string.find("url", itag_location_720)
    end_of_url = full_string.find("\\", url_location)
    cut_of_full_string = full_string[url_location+4:end_of_url]
    finished_url_720 = parse.unquote(cut_of_full_string)

    search_string_audio = "itag=140"
    itag_location_audio = full_string.find(search_string_audio)
    url_location_audio = full_string.find("url", itag_location_audio)
    end_of_url_audio = full_string.find("\\", url_location_audio)
    cut_of_full_string_audio = full_string[url_location_audio+4:end_of_url_audio]
    finished_url_audio = parse.unquote(cut_of_full_string_audio)


    return render_template('result.html', message = finished_url_720, message1= finished_url_audio)


app.run(debug = True)
