import subprocess
import os

__version__ = "1.0"

class CPP:
    def __init__(self,src_code,location = os.getcwd()):
        self.__code = src_code

    def __check_compiler(self):
        try:
            subprocess.check_call(["g++","--version"])
            return True
        except subprocess.CalledProcessError:
            return False

    def compile(self,filename_out,save_src_code = False):
        if not self.__check_compiler():
            raise FileNotFoundError("g++ compiler not found! read docs from here {https://code.visualstudio.com/docs/cpp/config-mingw} and follow the directions")
        with open("temp.cpp","w") as file:
            file.write(self.__code)
        compile_process = subprocess.Popen(["g++","temp.cpp","-o",filename_out],stdout = subprocess.PIPE,stderr = subprocess.PIPE)
        compile_output,compile_error = compile_process.communicate()
        if compile_process.returncode == 0:
            print("compilation successful.\n")
        else:
            print("compilation failed! check your code\n")
            print(compile_error.decode("utf-8"))
        if not save_src_code:
            os.remove("temp.cpp")
    
    def run(self,filename_out):
        try:
            subprocess.run(["./" + filename_out])
        except FileNotFoundError:
            raise FileNotFoundError(f"'{filename_out}' executable file not found!")

