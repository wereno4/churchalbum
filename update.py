import git, shutil, os

def update():
    repo = git.Repo.clone_from('https://github.com/wereno4/churchalbum.git','./tmp', branch='main')
    shutil.rmtree('./tmp/.git')
    file_list = os.listdir('./tmp')
    for file in file_list:
        shutil.move('./tmp/'+file, './'+file)
    shutil.rmtree('./tmp')

    if os.name == 'nt':
        os.system('./pipupdate.bat')
    else:
        os.system('sh ./pipupdate.sh')
