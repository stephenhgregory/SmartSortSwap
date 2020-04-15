import cpp_controller

print("Hello, world! I am Python.")

cpp_controller.compile_cpp_file("hello.cpp")
print("About to pass args to cpp...")
cpp_controller.pass_args_to_cpp("hello", 5, "Stephen Gregory", 500)
print("Done passing args to cpp.")
