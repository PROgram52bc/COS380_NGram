import re
def tokenize_from_file_name(fname):
    with open(fname) as f:
        text = f.read()
        return re.findall('([A-Za-z]+|[",.!;:?])', text)

def tokenize_from_file(f):
    text = f.read()
    return re.findall('([A-Za-z]+|[",.!;:?])', text)
