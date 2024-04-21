import requests
import json

url = 'http://127.0.0.1:50021/'

# テキストと話者IDを指定する
text = 'こんにちは'
speaker_id = 3

# オーディオクエリのパラメータを設定する
query_params = {
    'text': text,
    'speaker': speaker_id
}

# オーディオクエリのエンドポイントにリクエストを送信する
res = requests.post(url + 'audio_query', params=query_params)

# レスポンスを確認する
res_json = res.json()
#print(res_json)

# 合成にこのレスポンスデータが必要であれば
query_data = res_json

# 合成のパラメータを設定する
synthesis_params = {
    # 必要に応じて合成パラメータを設定する
}

# 合成のエンドポイントにリクエストを送信する
res = requests.post(url + 'synthesis', params=synthesis_params, data=json.dumps(query_data))
print(res.content)