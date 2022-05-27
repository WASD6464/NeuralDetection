from threading import Thread
from time import sleep

import gi

gi.require_version("Gst", "1.0")

from gi.repository import Gst, GLib


Gst.init()

main_loop = GLib.MainLoop()
thread = Thread(target=main_loop.run)
thread.start()

pipeline = Gst.parse_launch("filesrc location=weights/best_osnet_x0_25/your_video.mp4 ! decodebin ! videoconvert ! autovideosink")
pipeline.set_state(Gst.State.PLAYING)

try:
    while True:
        sleep(0.1)
except KeyboardInterrupt:
    pass

pipeline.set_state(Gst.State.NULL)
main_loop.quit()