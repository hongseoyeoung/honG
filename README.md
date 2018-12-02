# CULION WEBPAGE
<br/>
<img src="https://user-images.githubusercontent.com/40227000/48993524-65745c80-f181-11e8-9d34-c65691eaad33.png" align="center"></img><br/><br>
<hr/>

 <h3>오픈소스인 python django 웹 프레임워크를 이용한 Dynamic Webpage 입니다.</h3><br/>
 <p>교내에 운영중인 전국 연합 동아리 <strong>'멋쟁이 사자처럼'</strong> 을 소개하고 부원들이 사용할 수 있는 커뮤니티 및 정보교환, 의사소통의 장으로 활용하기 위한 웹페이지를 제작합니다.<br/>
 웹페이지는 크게 공지사항 게시를 위한 게시판, 운영진이 수업을 진행하는데 사용했던 수업 자료 게시를 위한 게시판, 수업 진행 녹화물, 부원들이 주어진 과제를 완료하고 제출할 수 있는 게시판, 여러 궁금한 점 등을 서로 공유하고 자유롭게 질의응답할 수 있는 게시판, 동아리 내에서 본인이 원하는 공부를 함께할 스터디 멤버를 모집할 수 있는 게시판 등을 제공합니다.</p>
 <hr/>
 
 <h2>Webpage Preview</h2><br/>
 <ul>
 <li>공지사항 게시판은 간단하게 CRUD를 포함하고 모든 게시판에서 볼 수 있고 열람 가능한 형태입니다. 관리자는 모든 권한을 가지고, 운영진은 삭제를 제외한 모든 권한을 가지며, 일반 부원은 열람만 가능합니다. <br/>
 <img src="#"></img></li>
 <li>수업자료 게시판은 운영진이 수업을 진행할 때 사용했던 프레젠테이션 파일, 영상 파일 등을 업로드할 수 있는 기능을 포함하며 기본적인 CRUD를 제공하고 운영진은 모든 권한이 가능하며, 일반 부원은 열람만 가능한 형태입니다. <br/>
 <img src="#"></img></li>
 <li>과제업로드 게시판은 주어진 과제를 제출할 수 있게끔 파일 업로드 기능을 포함하며(소스파일, 이미지 파일 등) 기본적인 CRUD를 포함합니다. 관리자는 모든 권한을 가지고, 운영진은 열람만 가능하며, 일반 부원은 본인의 게시물만 보여지고 수정가능하며 삭제가능합니다.<br/>
 <img src="#"></img></li>
 <li>질의응답 게시판은 기본적인 CRUD와 이미지 업로드 기능 정도만 포함합니다. 관리자와 운영진은 모든 권한이 주어지며, 일반부원은 열람 외에는 본인의 게시물만 수정,삭제 등이 가능합니다.<br/>
 <img src="#"></img></li>
 </ul>
<hr/>

<h2>Development Environment</h2><br/>
<ul>
 <li><strong>python 3.6.2</strong></li><br/>
 <li><strong>django 2.1.2</strong></li><br/>
</ul>
<hr/>

<h2>Webpage Structure</h2><br/>
<img src="./culion.PNG"></img><br/>
<hr/>

<h2>How to Execution</h2><br/>
(본 실행과정은 Python 3.6.2버전과 리눅스 환경을 기준으로 합니다.)
<p>이 설명에서는 home 디렉토리 아래 <code>hongsam</code>라는 디렉토리를 새로 만들어 사용하도록 하겠습니다.<br/>
 <code>$ mkdir hongsam<br/>
 $ cd hongsam</code></p>

<h2>Release Note</h2><br/>
<h3>18.10.30</h3><br/>
<ul>
 <li>Project repository 생성</li>
 <li>Django Framework 기본 project 생성</li>
 <li>README.md 생성</li>
</ul><br/>

<h3>18.10.31</h3><br/>
<ul>
 <li>Python 3.6.2 version 으로 작업환경 동기화</li>
 <li>Django 2.1.2 version 으로 작업환경 동기화</li>
 <li>README.md update</li>
</ul><br/>

<h3>18.11.02</h3><br/>
<ul>
 <li>Frontend Template 적용으로 시각적인 부분 개선</li>
</ul><br/>

<h3>18.11.04</h3><br/>
<ul>
 <li>Template 상속으로 코드 간소화</li>
</ul><br/>

<h3>18.11.06</h3><br/>
<ul>
 <li>회원가입 기능 추가</li>
 <li>README.md update</li>
</ul><br/>

<h3>18.11.13</h3><br/>
<ul>
 <li>Webpage 구상도 추가</li>
 <li>README.md update</li>
</ul><br/>

<h3>18.11.17</h3><br/>
<ul>
 <li>기존 오류 수정</li>
 <li>lecture_note 추가</li>
</ul><br/>

<h3>18.11.18</h3><br/>
<ul>
 <li>충돌이 발생하는 cache 및 log 파일 .gitignore 추가</li>
 <li>lecture_note 개선</li>
 <li>Webpage base 수정 및 개선</li>
</ul><br/>

<h3>18.11.25</h3><br/>
<ul>
 <li>회원가입 기능 개선</li>
 <li>README.md html요소 추가 및 가독성 개선</li>
</ul><br/>

<h3>18.11.26</h3><br/>
<ul>
 <li>Signin&out 기능 추가</li>
 <li>Viewpage template 추가</li>
 <li>기존 Base Template 디자인 수정</li>
</ul><br/>

<h3>18.11.27</h3><br/>
<ul>
 <li>README.md 로고 추가 및 update</li>
</ul><br/>
