# 인하공업전문대학 컴퓨터정보과 3학년 2024-02 빅데이터 처리 포트폴리오

### 프로젝트 주제: 국내에서 판매 중인 에너지드링크 제품별 키워드 분석

### 프로젝트 설명

시중에 판매되고 있는 에너지 드링크 중 대표 에너지 드링크 제품들을 선별하여 각 제품별 많이 언급되는 키워드들을 분석한다.
대표 에너지 드링크 항목은 아래와 같다.

-   '롯데칠성음료'사의 핫식스
-   '몬스터 에너지'사의 몬스터 에너지 드링크
-   '레드불'사의 레드불 에너지 드링크
-   'GS25'사의 넷플릭스 에너지 드링크

### 사용 데이터 및 데이터 수집 방법

#### 사용 데이터

<hr/>
에너지 드링크 4종과 관련된 네이버 블로그, 네이버 뉴스의 본문을 가져온다.

#### 데이터 수집 방법

<hr/>
① 네이버 검색 API를 발급한다.

② '핫식스 에너지드링크', '몬스터 에너지드링크', '레드불 에너지드링크', '넷플릭스 에너지드링크' 순으로 검색어를 입력한 다음 네이버 블로그나 네이버 뉴스에 해당하는 query와 함께 API 요청을 시도한다.

③ API 요청시 API 접근에 대한 Request를 전송하고 이에 대한 Response를 json 파일로 받는다.

④ json 파일에서 description 부분을 추출하여 description 내용을 형태소 분석기 라이브러리를 통해 단어를 분리한 다음 품사를 부여한다.

⑤ 여러 품사 중 명사로 부여받은 단어들을 추출해서 개수를 확인한다.

⑥ 단어와 단어의 개수를 가지고 워드클라우드를 구성한다.

### 데이터 시각화

#### 뉴스

**핫식스 에너지드링크**

![핫식스 에너지드링크_naver_news_cloud](https://github.com/user-attachments/assets/941134ce-1816-4b28-aada-1b8698ae4590)

**몬스터 에너지드링크**

![몬스터 에너지드링크_naver_news_cloud](https://github.com/user-attachments/assets/967761cb-8fe1-4eb5-a965-d3a24071ede7)

**레드불 에너지드링크**

![레드불 에너지드링크_naver_news_cloud](https://github.com/user-attachments/assets/ed84d239-9d5d-4b0f-8ad8-dd78ad226ec0)

**넷플릭스 에너지드링크**

![넷플릭스 에너지드링크_naver_news_cloud](https://github.com/user-attachments/assets/69a39d89-05e3-4a7d-aa5d-6e87d064f016)

#### 블로그

**핫식스 에너지드링크**

![핫식스 에너지드링크_naver_blog_cloud](https://github.com/user-attachments/assets/400d9b51-f9e4-4c34-ab83-5207afd84e6f)

**몬스터 에너지드링크**

![몬스터 에너지드링크_naver_blog_cloud](https://github.com/user-attachments/assets/61c01fd1-f579-4b4c-993f-012f8879cd2f)

**레드불 에너지드링크**

![레드불 에너지드링크_naver_blog_cloud](https://github.com/user-attachments/assets/9eafda28-3dac-4fba-8cec-72797b153d12)

**넷플릭스 에너지드링크**

![넷플릭스 에너지드링크_naver_blog_cloud](https://github.com/user-attachments/assets/e2adc3de-d191-4ed3-b86b-a1b7f1c391fc)
