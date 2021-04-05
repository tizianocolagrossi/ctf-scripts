
key_hex = 0x31465f57655f63344e5f6e30745f733076455f744f6733746832525f77455f3472455f6730316e475f744f5f4431655f614c306e650a
msg_hex = 0x727f00340e075a6b3a69146f2d3e3a67403c343e101d052b1a58623d3c1a0e53087c00245b6e00771d1f1005316e08693e24000714

sum_cal = key_hex + msg_hex
and_calc = key_hex & msg_hex
min_calc = key_hex - msg_hex
xor_calc = key_hex ^ msg_hex
or_calc = key_hex | msg_hex

print("and ", str(hex(and_calc)))
print("sum ", str(hex(sum_cal)))
print("min ", str(hex(min_calc)))
print("xor ", str(hex(xor_calc)))
print("or ", str(hex(or_calc)))

31 46 5f 57 65 5f 63 34 4e 5f 6e 30 74 5f 73 30 76 45 5f 74 4f 67 33 74 68 32 52 5f 77 45 5f 34 72 45 5f 67 30 31 6e 47 5f 74 4f 5f 44 31 65 5f 61 4c 30 6e 65 0a

72 7f 00 34 0e 07 5a 6b 3a 69 14 6f 2d 3e 3a 67 40 3c 34 3e 10 1d 05 2b 1a 58 62 3d 3c 1a 0e 53 08 7c 00 24 5b 6e 00 77 1d 1f 10 05 31 6e 08 69 3e 24 00 07 14
