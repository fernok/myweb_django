## Creating Virtual Environment
여러개의 프로젝트를 개발할 때 발생할 수 있는 패키지의 버전 문제를 해결  
가상 환경은 독립된 공간을 만들어 줘서 각각의 가상 환경 안에 다른 버전의 패키지를 사용할 수 있게 함
```
E:\PythonProjects>python -m venv django
```
```
E:\PythonProjects>cd django
E:\PythonProjects\django>Scripts\activate.bat
```
[Further Reference](https://dojang.io/mod/page/view.php?id=2470)

## About Git
- Initializing Git
```
git init
```
- User Configuration
```
git config --global user.name 'Hyuhng Min Kim'
git config --global user.email 'minkim918@gmail.com'
```
- Adding and Deleting Files from Stage
```
git add manage.py
git rm --cached manage.py
```
- Commit
```
git commit
>> hint: Waiting for your editor to close the file...
>> Aborting commit due to empty commit message.
```
```
git commit -m "manage.py modified"
```
- Git Ignore
```
touch .gitignore
```
Add names of files to be ignored when staging to .gitignore
The files will not be staged nor committed
- Branches
```
git branch login
```
Creates a new branch named 'login'
```
git checkout login
```
Switches to branch 'login'
```
git merge login
```
Merges 'master' branch with 'login' branch
```
git clean -d -f -f
```
When error `The following untracked working tree files would be overwritten by checkout` occurs

- Remote Repositories
```
git remote add origin https://github.com/fernok/myweb_django.git
git push -u origin master
```
When the local repository and the remote repository have distinct histories, it might refuse to push with an error message such as
```
error: failed to push some refs to 'https://github.com/fernok/myweb_django.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```
This happens because the two repositories have different status.
It is necessary to pull the remote repository first by
```
git pull origin master
(git pull <remote> <branch>)
```
However, this also failes to execute with an error message
```
fatal: refusing to merge unrelated histories
```
This can be solved by manually allowing the merge of repositories with unrelated histories.
```
git pull origin master --allow-unrelated-histories
```
All problems are solved and now the two repositories can be merged.
```
git push -u origin master
```

## Installing Django
```
pip install django
```
