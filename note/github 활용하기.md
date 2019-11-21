# github 활용하기

## Git pull request

main repo 를 fork 떠서 내.repo 로 옮기고 clone해서 수정 후

pull request를 하면 검토 후 merge 시킴



**repo 주인**

> github-flow 폴더 만들고 그 폴더에 들어감
>
> README.md 파일 생성
>
> git init
>
> git add .
>
> git commit -m "first commit"
>
> 메인의 github  페이지로 이동
>
> repositories - New
>
> Repository name에 github-flow
>
> create repository
>
> 나오는 주소 복사
>
> git remote add origin (복사한 주소)
>
> git push origin master
>
> 주소 sub 에게 전달



**repo Sub**

> 전달받은 주소에 접속해서 fork 버튼 클릭
>
> clone or download 클릭해서 나오는 주소 복사
>
> git clone (복사한 주소)
>
> cd github-flow
>
> git remote 엔터치면 origin 나옴
>
> git remote add upstream (주인의 주소)
>
> git remote 엔터치면 origin, upstream 나옴 (origin이 sub꺼 upstream이 주인꺼)
>
> code . 해서 vscode 열어
>
> READEME.md 에 #github-flow 작성
>
> git add .
>
> git commit -m "updated README"
>
> git push origin master
>
> sub의 repo에서 code 옆에 pull request 들어감
>
> new pull request
>
> create pull request
>
> 내용 작성 후 create pull request



**주인**

> code  옆에 pull request 클릭
>
> merge pull request 클릭 confirm merge



**Sub**

> git pull upstream master (업데이트를 원본에서 반영)



## branch 

mkdir github-branch

> github-branch 들어가서 git init
>
> touch README.md
>
> git add .
>
> git commit -m "first commit"
>
> git checkout -b dev
>
> git branch (어느 branch에 있는지 확인 가능함)
>
> code .  -> readme에 글 쓰고 닫기
>
> git status
>
> git add .
>
> git commit -m "updated.README.md"
>
> git log
>
> git checkout master
>
> git merge dev
>
> code .

> git branch --d dev ( Merge 를 하면 사용했던 branch는 삭제한다. )



## 충돌 해결

### 충돌시키기

> git checkout -b dev
>
> code . (내용 수정하기)
>
> git commit -m "updated README.md"
>
> git checkout master
>
> code . (내용 수정)
>
> git add .
>
> git commit -m "updated reame"
>
> git merge dev



### 해결

> code . (내용 이외의 것들 지우기)
>
> git add .
>
> git commit -m "solving merge problem"
>
> git log
>
> git branch --d dev
>
> git branch