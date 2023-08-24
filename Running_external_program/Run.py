import subprocess
result = subprocess.run(["ls", "-l"])
print(type(result))

print(result.args)  # gives which command we have executed
print(result.returncode)  # return 0 if command execute without error

print(result.stderr)
print(result.stdout)  # 0 because we print it on the terminal


# now Look if we want to store output of command into a stdout attribute


result = subprocess.run(["ls", "-l"], capture_output=True, text=True)


print(result.args)  # gives which command we have executed
print(result.returncode)  # return 0 if command execute without error

print(result.stderr)
print(result.stdout)

# We can run an other python file using run command

result = subprocess.run(["python3", "Test.py"])


print(result.args)  # gives which command we have executed
print(result.returncode)  # return 0 if command execute without error

print(result.stderr)
print(result.stdout)

# now  lets have a look on try block
try:

    result = subprocess.run(["python3", "Test.py"],
                            capture_output=True, text=True, check=True)

    print(result.args)  # gives which command we have executed
    print(result.returncode)  # return 0 if command execute without error

    print(result.stderr)
    print(result.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)
