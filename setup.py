import cx_Freeze
import os


os.environ['TCL_LIBRARY'] = "C:\\python\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\python\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("don't_crash.py",icon="icon.ico")]

cx_Freeze.setup(
    name = "Don't Crash",
    options = {"build_exe":{"packages":["pygame"],
                            "include_files":[os.path.join('C:\python','DLLs','tk86t.dll'),
                                             os.path.join('C:\python','DLLs','tcl86t.dll'),
                                             "beach.png",
                                             "blue_car.png",
                                             "bus.png",
                                             "crash.wav",
                                             "explode.png",
                                             "icon.png",
                                             "icon.ico",
                                             "intro.jpg",
                                             "launch.wav",
                                             "missile.png",
                                             "police_car.png",
                                             "red_car.png",
                                             "ring.wav",
                                             "road.jpg",
                                             "rocket.png",
                                             "rocketicon.png",
                                             "The Easy Winners.mp3",
                                             "yellow_car.png"]}},
    version = "0.1",
    executables = executables
    )
