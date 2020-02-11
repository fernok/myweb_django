### Creating Virtual Environment
여러개의 프로젝트를 개발할 때 발생할 수 있는 패키지의 버전 문제를 해결  
가상 환경은 독립된 공간을 만들어 줘서 각각의 가상 환경 안에 다른 버전의 패키지를 사용할 수 있게 함
```
E:\PythonProjects>python -m venv django
```
```
E:\PythonProjects>cd django
E:\PythonProjects\django>Scripts\activate.bat
```

### Creating Git Repository
- Initializing git
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
git commit -m "First commit"
```

[Further Reference](https://dojang.io/mod/page/view.php?id=2470)

### Installing Django
```
pip install django
```
