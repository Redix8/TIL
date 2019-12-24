# Data Visualization

## 0. Kaggle

Kaggle의 Hands-on Micro-course로 Seaborn 을 이용한 코스이다.

학습 후, 케글의 클라우드에서 예제(Exercise)를 이용 해 볼 수 있다.



## 1. Hello, Seaborn

`Seaborn` 은 `matplotlib` 를 베이스로한 시각화 라이브러리다.

파이썬을 아나콘다로 설치했다면 기본적으로 같이 설치되어있다.

### Setup

```python
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
print("Setup Complete")
```

기본적으로 쓰는것들을 `import` 해주는 setup line들이다.

### Data read

```python
# Path of the file to read
fifa_filepath = "../input/fifa.csv"

# Read the file into a variable fifa_data
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)
```

시각화에 필요한 데이터들을 `pandas`로 불러와야한다. 

`../` 는 상위폴더,  `./` 는 현재폴더를 의미한다.

`index_col` 은 첫번째 오는 column 을 구별하기위해 이름("Date")을 지어준다.

`parse_dates` 는 날짜를 `datetime`형식으로 변환할지 여부. 기본값은 `False`

### Data check

원하는대로 데이터가 불러와졌는지 확인해보자.

```python
# Print the first 5 rows of the data
fifa_data.head()
```

`.head()` 를 사용하면 데이터의 처음 5개줄을 출력하여 확인 할 수 있다.



### Data Plot

데이터를 그래프로 화면에 생성해보자

```python
# Set the width and height of the figure 사이즈 설정
plt.figure(figsize=(16,6))

# Line chart showing how FIFA rankings evolved over time 라인차트 생성
sns.lineplot(data=fifa_data)
```



## Line Chart

2017년과 2018년 Spotify 에서  인기곡 탑 5개의 데이터로 진행된다.

몇몇개는 missing value 가 있는 상황이다. (노래별 발매일(?) 이 다르기에)

데이터의 `.head()`를 출력하면 데이터가 없는 빈 공간은 `NaN(Not a Number)`으로 출력된다.

대신 `.tail()`을 사용하면 맨 뒤에서부터 5개를 출력하는데, 데이터가 전부 들어가있는것을 확인할 수 있다.



### Plot the data

```python
# Set the width and height of the figure
plt.figure(figsize=(14,6))

# Add title
plt.title("Daily Global Streams of Popular Songs in 2017-2018")

# Line chart showing daily global streams of each song 
sns.lineplot(data=spotify_data)
```

이전의 챕터에서처럼 `Seaborn` 의 `.lineplot` 을 호출하면 간단하게 차트를 띄울 수 있다.

`plt` 의 `figure`와 `title`로 크기와 제목을 설정해 줄 수 있다.

여기서 크기의 단위는 `inch`다 



### Plot a subset of the data

여태까지의 plot 은 전체 column의 데이터 셋을 이용했다면, 부분적인것도 출력해 보자.

```python
list(spotify_data.columns)
```

현재 data의 column 에는 어떤것들이 있는지 볼 수 있다.



```python
# Line chart showing daily global streams of 'Shape of You'
sns.lineplot(data=spotify_data['Shape of You'], label="Shape of You")

# Line chart showing daily global streams of 'Despacito'
sns.lineplot(data=spotify_data['Despacito'], label="Despacito")

# Add label for horizontal axis
plt.xlabel("Date")
```

