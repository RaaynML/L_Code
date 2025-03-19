def rle_pack(input_string) -> str:
	if not input_string:
		return ""

	packed = []
	count = 1

	for i in range(1, len(input_string)):
		if input_string[i-1] == "0":
			continue #skip zeroes
		elif input_string[i] == input_string[i-1]:
			count += 1
		else:
			if count > 1:
				packed.append(f"{input_string[i-1]}{count}")
			else:
				packed.append(f"{input_string[i-1]}")
			count = 1
	#Add last char
	if count > 1:
		packed.append(f"{input_string[-1]}{count}")
	else:
		packed.append(f"{input_string[-1]}")

	return "".join(packed)

# test
if __name__ == "__main__":
	print(rle_pack("BBBCCCCAAA")) #: B3C4A3
	print(rle_pack("CDDDDDFFFGGGGG")) #: CD5F3G5
	test_str_5437 = "54377997096d56f1b36aa85a2ccca4a42046bbb6ae209dfb80041b685777aeedcb97d9b0c"
	print(f"{test_str_5437} ->")
	print(rle_pack(test_str_5437))
	#: 5437292796d56f1b36a285a2c3a4a4246b36ae29dfb841b68573ae2dcb97d9bc