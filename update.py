import git, shutil, os

def update():
    repo = git.Repo.clone_from('https://github.com/wereno4/churchalbum.git','./tmp', branch='main')

    file_list = os.listdir('./tmp')
    for file in file_list:
        shutil.move('./tmp/'+file, './'+file)
    shutil.rmtree('./tmp')