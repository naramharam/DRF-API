import pandas as pd
import numpy as np
import random
import pickle

pd.set_option('display.max_rows', 5000)  ##생략된 행 전부 출력


def recommend_volunteer(input_local, input_gender):
  # sido = pd.read_csv('/Users/jo-eun-yeob/Workspace/TIL/capstone/data/Resource/sido.csv')
  # gender = pd.read_csv('/Users/jo-eun-yeob/Workspace/TIL/capstone/data/Resource/age_gender.csv')
  # sido.to_pickle("sido.pkl")
  # gender.to_pickle("gender.pkl")
  sido = pd.read_pickle("/Users/jo-eun-yeob/Workspace/TIL/capstone/data/sido.pkl")
  gender = pd.read_pickle("/Users/jo-eun-yeob/Workspace/TIL/capstone/data/gender.pkl")

  man = []
  girl = []
  common = []
  man_choice = []
  girl_choice = []
  common_choice = []

  for i in range(2, 19):
    sido_choice = sido[i:i + 1]
    prop = int(sido_choice.iloc[0, 2]) / int(sido_choice.iloc[0, 1])

    for j in range(3, 8):
      man_choice.append(prop * (int(gender.iloc[2, j])) / int(gender.iloc[1, j]) * 0.5)
      girl_choice.append(prop * (int(gender.iloc[3, j])) / int(gender.iloc[1, j]) * 0.5)
      common_choice.append(prop * 0.5)
      if j < 7:
        prop = int(sido_choice.iloc[0, j]) / int(sido_choice.iloc[0, 1])
    man.append(man_choice)
    girl.append(girl_choice)
    common.append(common_choice)
    man_choice = []
    girl_choice = []
    common_choice = []

  ## 시설, 재가, 전문, 지역, 기타 봉사활동을 csv파일로 읽어와서 소분류와 내용을 제외하고 지역 컬럼 기준으로 정렬
  # siseol = pd.read_csv('/Users/jo-eun-yeob/Workspace/TIL/capstone/data/Resource/facility.csv').drop(['소분류', '내용'], axis=1).sort_values(by='지역')
  # jaega = pd.read_csv('/Users/jo-eun-yeob/Workspace/TIL/capstone/data/Resource/jaega.csv').drop(['소분류', '내용'], axis=1).sort_values(by='지역')
  # jeonmun = pd.read_csv('/Users/jo-eun-yeob/Workspace/TIL/capstone/data/Resource/professional.csv').drop(['소분류', '내용'], axis=1).sort_values(by='지역')
  # jiyeok = pd.read_csv('/Users/jo-eun-yeob/Workspace/TIL/capstone/data/Resource/community.csv').drop(['소분류', '내용'], axis=1).sort_values(by='지역')
  # gita = pd.read_csv('/Users/jo-eun-yeob/Workspace/TIL/capstone/data/Resource/other.csv').drop(['소분류', '내용'], axis=1).sort_values(by='지역')

  # ## sample_list에 csv 파일들 합치기
  # sample_list = pd.DataFrame(columns=["제목", "지역", "성별", "종류"])
  # sample_list = pd.concat([siseol, jaega, jeonmun, jiyeok, gita], keys=['시설', '재가', '전문', '지역', '기타'])
  # sample_list.to_pickle("sample_list.pkl")

  sample_list = pd.read_pickle("/Users/jo-eun-yeob/Workspace/TIL/capstone/data/sample_list.pkl")

  # 배열로 지역과 성별 문자열 저장
  sido_list = ['서울', '부산', '대구', '인천', '광주', '대전', '울산',
               '세종', '경기', '강원', '충북', '충남', '전북', '전남',
               '경북', '경남', '제주']
  gender_list = ['남', '여', '공통']
  volunteer_list = ['시설', '재가', '전문', '지역', '기타']

  ## 데이터프레임 형태로 저장
  prob_df = pd.DataFrame(columns=["지역", "성별", "시설봉사", "재가봉사", "전문봉사", "지역사회", "기타"])

  ## 반복문으로 데이터프레임에 지역과 성별과 그에 따른 확률 저장
  listdata = list(range(0, 17))
  for i, j in zip(range(0, 51, 3), listdata):
    prob_df.loc[i] = [sido_list[j], gender_list[0], man[j][0], man[j][1], man[j][2], man[j][3], man[j][4]]
    prob_df.loc[i + 1] = [sido_list[j], gender_list[1], girl[j][0], girl[j][1], girl[j][2], girl[j][3], girl[j][4]]
    prob_df.loc[i + 2] = [sido_list[j], gender_list[2], common[j][0], common[j][1], common[j][2], common[j][3],
                          common[j][4]]

  title_list = [[0 for i in range(15)] for j in range(17)]

  ## 랜덤하게 지역과 성별에 따라서 봉사활동 제목을 리턴하는 함수 정의
  def return_title(vlist, slist, glist):
    return sample_list.loc[volunteer_list[vlist]][
      (sample_list.loc[volunteer_list[vlist]]['지역'] == sido_list[slist]) &
      (sample_list.loc[volunteer_list[vlist]]['성별'] == gender_list[glist])]['제목'].values

  def repeat_add_prob(glist1, glist2, i, j, k):
    listdata = list(range(0, 5))
    for l, m in zip(range(i, j), listdata):
      if return_title(m, k, glist1).size == 0:
        if return_title(m, k, glist2).size == 0:
          title_list[k][l] = np.NaN
        else:
          title_list[k][l] = random.choice(return_title(m, k, glist2))
      else:
        title_list[k][l] = random.choice(return_title(m, k, glist1))

  ## 함수를 이용한 반복 생성
  for k in range(0, 17):  ## k는 지역에 대한 반복 입력
    repeat_add_prob(0, 2, 0, 5, k)  ## 남자에 대한 반복 입력
    repeat_add_prob(1, 2, 5, 10, k)  ## 여자 ...
    repeat_add_prob(2, 2, 10, 15, k)  ## 공통 ...

  ## 지역, 성별, 1순위, 2순위, 3순위 데이터프레임 생성
  prob_vol = pd.DataFrame(columns=["지역", "성별", "1순위", "2순위", "3순위", "4순위", "5순위", "6순위", "7순위", "8순위", "9순위", "10순위"])
  prob_vol.loc[0] = [input_local, input_gender, [], [], [], [], [], [], [], [], [], []]

  ## 남자일 경우의 가중치, 여자일 경우의 가중치, 공통에서 남자를 제외한 가중치, 여자를 제외한 가중치, 여자를 제외한 제목, 남자를 제외한 제목 리스트들 초기화
  man_weight = [[0 for i in range(15)] for j in range(17)]
  girl_weight = [[0 for i in range(15)] for j in range(17)]
  common_without_man = [[0 for i in range(15)] for j in range(17)]
  common_without_girl = [[0 for i in range(15)] for j in range(17)]
  title_list_man = [[0 for i in range(15)] for j in range(17)]
  title_list_girl = [[0 for i in range(15)] for j in range(17)]

  ## 남자, 여자 제목 리스트를 각각 경우에 맞게 제외시켜서 값을 넣어줌
  def title_list_clean():
    for k in range(0, 17):
      title_list_man[k].extend(title_list[k][0:5])
      title_list_man[k].extend(title_list[k][10:15])
      title_list_girl[k].extend(title_list[k][5:15])
      del title_list_man[k][0:15]
      del title_list_girl[k][0:15]

  ## 가중치도 마찬가지로 확률을 따로 계산하여 값을 넣어줌
  def weight_calculate():
    for k in range(0, 17):
      for i in range(0, 5):
        girl_weight[k][i] = girl[k][i] / (float(1) - sum(man[k]))
        common_without_man[k][i] = common[k][i] / (float(1) - sum(man[k]))
        man_weight[k][i] = man[k][i] / (float(1) - sum(girl[k]))
        common_without_girl[k][i] = common[k][i] / (float(1) - sum(girl[k]))
      del man_weight[k][5:15]
      del common_without_girl[k][5:15]
      del girl_weight[k][5:15]
      del common_without_man[k][5:15]

  title_list_clean()
  weight_calculate()

  for k in range(0, 17):
    if prob_vol.iloc[0].values[0] == sido_list[k]:
      if prob_vol.iloc[0].values[1] == '남':
        choice_prob = title_list_man[k]
        weight_prob = man_weight[k] + common_without_girl[k]
        prob_vol.iloc[0].values[2:12] = np.random.choice(choice_prob, 10, replace=False, p=weight_prob)
      elif prob_vol.iloc[0].values[1] == '여':
        choice_prob = title_list_girl[k]
        weight_prob = girl_weight[k] + common_without_man[k]
        prob_vol.iloc[0].values[2:12] = np.random.choice(choice_prob, 10, replace=False, p=weight_prob)
    else:
      continue
      # print("없는 지역입니다")

  msg = '&'.join(list(prob_vol.iloc[0].values[2:12]))
  msg_split = msg.split('&')
  return msg_split

