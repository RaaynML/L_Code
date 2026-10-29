#Variant to keep only the 1st instance in a str
#Still discards zeroes!
def dedup_str(in_str: str) -> str:
	if not in_str:
		return ""

	seen = set()
	out = []

	for char in in_str:
		if char == '0':
			continue
		if char not in seen:
			seen.add(char)
			out.append(char)

	return "".join(out)

if __name__ == "__main__":
	teststr_1 = "AAABBBCCCDDDDEFF"
	print(f"{teststr_1} -> {dedup_str(teststr_1)}")
