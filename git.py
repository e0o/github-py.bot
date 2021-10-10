import os , random

for i in range(2000):
    d = str(i) + 'days ago'
    rand = random.randrange(1, 12)
    with open('test.txt','a') as file:
        file.write(d+'\n')
    os.system('git add test.txt')
    os.system('git commit --date=" 2020-'+str(rand)+'-'+d+'" -m 1')
os.system('git push -u origin main')

for i in range(2000):
    d = str(i) + 'days ago'
    rand = random.randrange(1, 12)
    with open('eto.css','a') as file:
        file.write(d+'\n')
    os.system('git add eto.css')
    os.system('git commit --date=" 2020-'+str(rand)+'-'+d+'" -m 1')
os.system('git push -u origin main')

for i in range(2000):
    d = str(i) + 'days ago'
    rand = random.randrange(1, 12)
    with open('eto.ejs','a') as file:
        file.write(d+'\n')
    os.system('git add eto.ejs')
    os.system('git commit --date=" 2020-'+str(rand)+'-'+d+'" -m 1')
os.system('git push -u origin main')

for i in range(2000):
    d = str(i) + 'days ago'
    rand = random.randrange(1, 12)
    with open('eto.js','a') as file:
        file.write(d+'\n')
    os.system('git add eto.js')
    os.system('git commit --date=" 2020-'+str(rand)+'-'+d+'" -m 1')
os.system('git push -u origin main')

for i in range(2000):
    d = str(i) + 'days ago'
    rand = random.randrange(1, 12)
    with open('eto.py','a') as file:
        file.write(d+'\n')
    os.system('git add eto.py')
    os.system('git commit --date=" 2020-'+str(rand)+'-'+d+'" -m 1')
os.system('git push -u origin main')
