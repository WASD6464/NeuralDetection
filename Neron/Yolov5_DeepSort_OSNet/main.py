import os
import time
import requests
from flask import Flask, request, redirect, url_for, render_template, Response
from werkzeug.utils import secure_filename
from time import sleep
from werkzeug.utils import secure_filename
from threading import Thread
import gi
import subprocess

gi.require_version("Gst", "1.0")

from gi.repository import Gst, GLib


Gst.init()


UPLOAD_FOLDER = 'file_storage/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER





#Разрешённые типы файлов из ALLOWED_EXTENSIONS
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


#Главная страница для скачивания файла
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], "your_video.mp4"))#Все загруженные видео будут называться your_video.mp4
            return redirect('/track')
    return render_template('upload.html')

#Декоратор с шаблоном track.html
@app.route('/track', methods=['GET', 'POST'])
def tracking_file():
    return render_template('track.html')

#Декоратор с запуском трекинга через терминал
@app.route('/tracking_command/', methods=['GET'])
def tracking_command():
    home_dir = os.system("cd ~/PycharmProjects/video_app/Neron/Yolov5_DeepSort_OSNet")
    #os.system("cd Neron")
    #os.system("cd Yolov5_DeepSort_OSNet")
    os.system("python track.py --source /home/alex/PycharmProjects/video_app/Neron/Yolov5_DeepSort_OSNet/file_storage/your_video.mp4 --project /home/alex/PycharmProjects/video_app/Neron/ --save-txt --save-vid --yolo_model /home/alex/PycharmProjects/video_app/Neron/Yolov5_DeepSort_OSNet/weights/best.pt --exist-ok")
    return redirect(url_for("index"))



#filesrc location=video.mp4 ! decodebin ! videoconvert ! videoscale ! \
#video/x-raw,width=1920,height=1080 ! videoconvert ! \
#x264enc tune=zerolatency bitrate=16384 ! filesink location=video.mp4 -e
#gst-launch 1.0 filesrc location=file_storage/your_video.mp4 ! decodebin ! videoconvert ! hlssink playlist-root=http://127.0.0.1:5000/video_feed
#gst-launch-1.0 -v filesrc location = file_name.mp4 ! qtdemux ! video/x-h264 ! rtph264pay ! udpsink host=192.1XX.XX.XX port=9001 (от клиента к серверу)
#{{ url_for('video_feed') }}



#вывод видео с помощью gstreamer
def uploaded_file():
    main_loop = GLib.MainLoop()
    thread = Thread(target=main_loop.run)
    thread.start()
    #Делает из файла поток и через контейнер decodebin запускает его в отдельном окне
    pipeline = Gst.parse_launch("filesrc location=weights/best_osnet_x0_25/your_video.mp4 ! decodebin ! videoconvert ! autovideosink")
    pipeline.set_state(Gst.State.PLAYING)

    try:
        while True:
            sleep(0.1)
    except KeyboardInterrupt:
        pass

    pipeline.set_state(Gst.State.NULL)
    main_loop.quit()

#Декоратор с шаблоном videopl.html
@app.route('/index', methods=['GET', 'POST'])
def index():
    text = open("/home/alex/PycharmProjects/video_app/Neron/Yolov5_DeepSort_OSNet/weights/best_osnet_x0_25/tracks/your_video").read()
    return render_template('videopl.html',text=text)



#Декоратор с выводом потока из uploaded_file
@app.route('/video_feed')
def video_feed():
    return Response(uploaded_file(), mimetype='video/mp4')
#multipart/x-mixed-replace


if __name__ == "__main__":
    app.run(debug=True)