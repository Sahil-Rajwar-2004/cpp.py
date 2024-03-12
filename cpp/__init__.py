import subprocess
import os

__version__ = "1.1"

class CPP:
    def __init__(self,src_code):
        self.__code = src_code
        self.__error_flag = False

    def __check_compiler(self):
        try:
            subprocess.check_call(["g++","--version"])
            return True
        except subprocess.CalledProcessError:
            return False

    def compile(self,filename_out,filename_in = "temp.cpp",save_src_code = False):
        if not self.__check_compiler():
            raise FileNotFoundError("g++ compiler not found! read docs from here {https://code.visualstudio.com/docs/cpp/config-mingw} and follow the directions")
        with open(filename_in,"w") as file:
            file.write(self.__code)
        compile_process = subprocess.Popen(["g++",filename_in,"-o",filename_out],stdout = subprocess.PIPE,stderr = subprocess.PIPE)
        compile_output,compile_error = compile_process.communicate()
        if compile_process.returncode == 0:
            print("compilation successful.\n")
        else:
            print("compilation failed! check your code\n")
            print(compile_error.decode("utf-8"))
            self.__error_flag = True
        if not save_src_code:
            os.remove(filename_in)
    
    def run(self,filename_out):
        if self.__error_flag:
            print("error found in your C++ code during compilation!")
            return
        try:
            subprocess.run(["./" + filename_out])
        except FileNotFoundError:
            raise FileNotFoundError(f"'{filename_out}' executable file not found!")
