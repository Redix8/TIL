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

