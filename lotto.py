import pandas as pd 
import requests 
from tqdm import tqdm 
import json
#https://somjang.tistory.com/entry/Python%EB%A1%9C%EB%98%90-api%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%98%EC%97%AC-%EC%97%AD%EB%8C%80-%EB%A1%9C%EB%98%90-%EB%8B%B9%EC%B2%A8-%EA%B2%B0%EA%B3%BC-%EB%B6%84%EC%84%9D%ED%95%B4%EB%B3%B4%EA%B8%B0

def getLottoWinInfo(minDrwNo, maxDrwNo): 
    drwtNo1 = []
    drwtNo2 = [] 
    drwtNo3 = [] 
    drwtNo4 = [] 
    drwtNo5 = [] 
    drwtNo6 = [] 
    bnusNo = [] 
    totSellamnt = [] 
    drwNoDate = [] 
    firstAccumamnt = [] 
    firstPrzwnerCo = [] 
    firstWinamnt = []
    for i in tqdm(range(minDrwNo, maxDrwNo + 1, 1)): 
        req_url = "http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=" + str(i) 
        req_lotto = requests.get(req_url) 
        lottoNo = req_lotto.json() 
        print(lottoNo)
        drwtNo1.append(lottoNo['drwtNo1']) 
        drwtNo2.append(lottoNo['drwtNo2']) 
        drwtNo3.append(lottoNo['drwtNo3']) 
        drwtNo4.append(lottoNo['drwtNo4']) 
        drwtNo5.append(lottoNo['drwtNo5']) 
        drwtNo6.append(lottoNo['drwtNo6']) 
        bnusNo.append(lottoNo['bnusNo']) 
        totSellamnt.append(lottoNo['totSellamnt']) 
        drwNoDate.append(lottoNo['drwNoDate']) 
        firstAccumamnt.append(lottoNo['firstAccumamnt']) 
        firstPrzwnerCo.append(lottoNo['firstPrzwnerCo']) 
        firstWinamnt.append(lottoNo['firstWinamnt']) 
        lotto_dict = {
            "추첨일": drwNoDate,
            "Num1": drwtNo1,
            "Num2": drwtNo2,
            "Num3": drwtNo3,
            "Num4": drwtNo4,
            "Num5": drwtNo5,
            "Num6": drwtNo6,
            "bnsNum": bnusNo,
            "총판매금액": totSellamnt,
            "총1등당첨금": firstAccumamnt,
            "1등당첨인원": firstPrzwnerCo,
            "1등수령액": firstWinamnt
        }
        df_lotto = pd.DataFrame(lotto_dict)
        return df_lotto

lotto_df = getLottoWinInfo(1,982)
