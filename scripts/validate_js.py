import requests
import subprocess

r = requests.get('http://127.0.0.1:5050/')
script = r.text.split('<script>')[1].split('</script>')[0]
with open('test_script.js', 'w', encoding='utf-8') as f:
    f.write(script)

res = subprocess.run(['node', '--check', 'test_script.js'], capture_output=True, text=True)
print('Node check code:', res.returncode)
if res.stderr:
    print('Node stderr:\n', res.stderr)
else:
    print('JavaScript syntax is 100% valid!')
