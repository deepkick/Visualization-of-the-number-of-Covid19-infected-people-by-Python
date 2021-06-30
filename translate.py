import re
from googletrans import Translator
 
def translate(text):
    comment_pattern = re.compile(r'//([^\n]*)')
    out = re.sub(comment_pattern, r'\1', text)
 
    out = re.sub(r'^\s*|\s*(?=\s)|\s*$', '', out)
    out = re.sub(r'[\r\n]', ' ', out)
    out = re.sub(r':\s+', r':\n', out)
    out = re.sub(r'\.\s+([A-Z])', r'.\n\1', out)
 
    out = ' '.join(
        '\n' + line if ' ' in line else line
        for line in out.splitlines())
    out = '\n'.join(
        re.sub(r' ([A-Z]\w+)', r' _\1_', line)
        for line in out.splitlines())
 
    for t in Translator().translate(out.strip().splitlines(), src='en', dest='ja'):
        return t.text