with open('test_script.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the broken replace call
content = content.replace(
    "text.replace('Subject: ' + subject + '\n\n', '')",
    "text.replace('Subject: ' + subject + '\\n\\n', '')"
)
content = content.replace(
    "text.replace('Subject: ' + subject + '\r\n\r\n', '')",
    "text.replace('Subject: ' + subject + '\\n\\n', '')"
)

with open('test_script.js', 'w', encoding='utf-8') as f:
    f.write(content)

import subprocess
res = subprocess.run(['node', '--check', 'test_script.js'], capture_output=True, text=True)
print('New check code:', res.returncode)
if res.stderr:
    print('New stderr:\n', res.stderr)
else:
    print('SUCCESS! Valid JavaScript!')
