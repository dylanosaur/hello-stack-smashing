set +e

g++ hello.cpp -fno-stack-protector -o -no-pie hello
# g++ hello.cpp -o hello

chmod u+x hello

./hello a
./hello "$(cat program_input)"

# to perform the stack smashing we also disable aslr
# echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
