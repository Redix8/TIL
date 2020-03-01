# How to win a data science competition

## Week 1

### Competition Mechanics

Data, Model, Submission, Evaluation, Leaderboard.

- Leaderboard - 전체 테스트셋을 public과 private 으로 나누어서 public만 공개.  예측은 모든 test set에 대해 시행함. 



### Real world application vs Competitions

#### Real world ML pipeline

- 문제에 대한 이해
- 문제의 공식화(문제 정의) - 무엇을 예측해야하는가
- 데이터 수집
- 데이터 전처리
- 모델링
- 평가
- 배포
- 모니터링 및 유지보수

데이터에 대한 통찰이 앙상블 결과보다 중요할수도 있다.

어떠한 문제는 머신러닝없이 분석만으로도 해결 가능하다.



### Recap of main ML algorithms

#### Linear

sparse high dimensional data 에 좋다

간단한 접근으로 두개를 구분할 수 없는 경우가 있다.(하나가 다른 하나를 감싼것 같은 모델.  삶은계란처럼)



#### Tree-based

의사 결정 트리를이용해 분할하여 정복하는 방법.

Randomforest, Gradient boosting

선형 종속성을 알아채기 힘들다. (Linear모델로는 간단하지만)

#### K-nn (K-nearest neighbor)

가까운 이웃 확인



#### Neural Networks

이미지 소리 문자 sequences 에 좋다



#### No free lunch

모든 작업에 대해 뛰어난 성능을 가진 해결법은 없다.



### Feature preprocessing and generation with respect to models

#### Feature preprocessing

타입과 모델에 따라 달라짐



#### Numeric features

- Preprocessing
  - Min-Max scaling
  - Standardize
  - rank transformation : 아웃라이어 제거가 힘들때 영향을 줄일수있다.
  - log transformation : non-tree-based model, 특히 Neural Network에 좋음. 
    - log transformation : np.log(1+x)
    - Raising to the power <1: np.sqrt(x+2/3)
- Feature generation
  - 상관관계가 있는 요소의 생성. ex) 가로 세로의 떨어진 거리가 주어진다면 직선으로 이어진 거리를 만들수있음
  - eda에 의한 생성
- Tree-based-model  - scaling 에 영향이 크게 없음
- Non-tree-based-model - 스케일링에 영향을 크게 받음



####  Categorical and Ordinal features

- Ordinal features
  - ticket class : 1,2,3
  - driver's license : A, B, C, D
  - Education: kindergarden, school, undergraduate, bachelor, master, doctoral
- label encoding
- frequency encoding
- one-hot encoding
- categorical feature를 합쳐서 새 feature를 만드는것은 linear models 과 knn 에서 더 나은 결과를 낼수도있다.



#### Datetime and Coordinates

- Datetime
  - 주기
  - 행독립 : id처럼 작동할수있는 데이터. ex) 1970.1월1일부터 지난 시간.
  - 행종속 : 이전 특정일부터 지난 기간처럼 이전행에 영향받음. ex) 다음 휴일까지 남은 시간
  - 두 날짜간 차이
- Coordinates
  - data로부터의 특정장소. ex) 현재 장소로부터 학교까지의 거리 등
  - Centers of clusters. 데이터 여러개로부터의 클러스터의 중심거리
  - 집계된 통계.  특정 포인트에 대한 통계치 ex) 이 포인트로부터 주변의 flat 의 개수



#### Handling missing values

어떻게 missing value를 판단할것인가.

- Nan이 아니고 숨겨져 있다면?
- histogram을 사용하여 확인해본다. 따로 떨어져있거나 or 평균값으로 되어있거나.

missing value를 어떻게 채워넣을것인가.

- -999, -1, etc. linear, NN model 에 좋지않음
- mean, median. tree 모델에 좋지않음
- Reconstruct value
- isnull feature 의 추가

Missing values reconstruction

feature generation 전에 replacing missing value를 피해라. feature 유용성이 줄어들수있음



#### 참고할 자료

https://machinelearningmastery.com/discover-feature-engineering-how-to-engineer-features-and-how-to-get-good-at-it/

https://www.quora.com/What-are-some-best-practices-in-Feature-Engineering



### Feature extraction from text and images

- preprocessing 
  - lowercase, stemming, lemmatization, stopwords

#### bag of words

TFiDF

N-gram

- very large vectors
- meaning of each value in vector is known



#### word2vec

word2vec, glove, fasttext

doc2vec

- relatively small vectors
- values in vector can be interpreted only in some cases
- the words with similar meaning often have similar embeddings

#### cnn

features can be extracted from different layers

careful choosing of pretrained network can help

data argumentation can be boosted



## Week 2

### Exploratory data analysis











