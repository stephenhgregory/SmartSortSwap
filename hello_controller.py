import subprocess
subprocess.call(['g++ -g -std=c++11', 'hello.cpp'])
tmp = subprocess.call("./a.out")
print("printing result")
print(tmp)