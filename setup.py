from cx_Freeze import setup, Executable

setup(
    name = "CyberDropMe-dl",
    version = "1.0.0",
    description = "Multithreaded Downloader for CyberDrop.me",
    author = "magnusjwatson2786@github",
    options = {'build_exe' : {'include_files' : ['mgw.ico']}},
    executables = [Executable(
    script="xt.py",
    base="Win32GUI",
    icon="mgw.ico")
    ] 
)