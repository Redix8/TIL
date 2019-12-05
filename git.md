# Git 로컬 저장소 활용하기

> git 은 repository (저장소) 로 각각 프로젝트를 관리 한다.

## 0. 기본 설정

Git에서 이력을 남기기 위해 작성자(author)정보를 추가한다.

매 컴퓨터에서 최초로 한번만 설정

```bash
$ git config --global user.name (유저네임)
$ git config --global user.email (이메일)
```

* 이란적으로 `(유저네임)`, `(이메일)` 에는 github 정보를 넣는다.



설정한 정보를 확인

```bash
$ git config --global -l
```



## 1. 저장소 생성

``` bash
$ git init
Reinitialized existing Git repository in C:/Users/student/Documents/TIL/.git/

```

## 2. add

> 커밋 대상 파일을 staging area로 이동시킨다.
>
> 즉, 이력을 남길 파일을 담아놓는 것이다.

. 은 현재 디렉토리(폴더) 를 뜻한다. 

```bash
$ git add .
$ git add git.md
$ git add images/
```



* 항상 git status 명령어를 통해 상태를 확인하자.

```bash
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   git.md
        new file:   images/pikachu2.jpg
        new file:   "\353\247\210\355\201\254\353\213\244\354\232\264 \355\231\234\354\232\251\353\262\225.md"

```

* 이력을 확인하기 위해서는 `git log`를 활용한다.

```bash
$ git log
commit 158e87fbf98a2d01663ef35d2ed8601ddfdcf9a6 (HEAD -> master)
Author: Redix8 <kukko@paran.com>
Date:   Thu Dec 5 12:40:28 2019 +0900

    minor change

commit 088e4e71c42b85a982e33cf807abf09a9449b3e2
Author: Redix8 <kukko@paran.com>
Date:   Thu Dec 5 12:39:59 2019 +0900

    git basic

```



# GIt 원격 저장소 활용하기

## 0. 기본 설정

> 원격 저장소를 생성한다. (예 - github)



```bash
$ git remote add origin https://github.com/Redix8/TIL.git
$ git push -u origin master
```



## 1. 원격 저장소 등록

origin 이라는 이름으로 해당 url을 원격 저장소로 등록

최초에 한번만 하면된다.

```bash
$ git remote add origin https://github.com/Redix8/TIL.git
$ git remote -v # 원격 저장소 목록
origin  https://github.com/Redix8/TIL.git (fetch)
origin  https://github.com/Redix8/TIL.git (push)

```

## 2. Push

앞으로 변경되는 사항이 있으면 항상 `add`, `commit` , `push` 를 진행한다.

```bash
$ git push -u origin master
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 4 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (9/9), 30.48 KiB | 10.16 MiB/s, done.
Total 9 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), done.
To https://github.com/Redix8/TIL.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.


```

