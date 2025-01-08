

def all_variants(text):
    text_len = len(text)
    for l in range(text_len):
        for p in range(text_len - l):
            yield text[p:p+l+1]


a = all_variants("abc")
for i in a:
    print(i)

#print("12345"[0:len("1234")])