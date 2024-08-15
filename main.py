import streamlit as st
import requests
import time


# 사용자가 발급한 TOKEN으로 사용자가 속해있는 밴드 키를 가져옵니다.
def get_band_list(token):
    try:
        url = f'https://openapi.band.us/v2.1/bands?access_token={token}'
        response = requests.get(url)
        response.raise_for_status()  # HTTP 오류가 발생하면 예외를 발생시킵니다.
        json_dict = response.json()  # JSON 응답을 자동으로 파싱합니다.
        clean_bands = [{band['name']: band['band_key']} for band in json_dict['result_data']['bands']]
        return clean_bands
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except KeyError as e:
        print(f"Unexpected response format: {e}")


def get_new_post_key(token, band_key):
    url = 'https://openapi.band.us/v2/band/posts'
    params = {
        'access_token': token,
        'band_key': band_key,
        'locale': 'ko_KR'
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # HTTP 오류 발생 시 예외 발생
        json_dict = response.json()
        post_key = json_dict.get('result_data', {}).get('items', [{}])[0].get('post_key')
        print(f'post_key: {post_key}')
        return post_key
    except (requests.RequestException, IndexError, KeyError) as e:
        print(f"게시물 키를 가져오는 중 오류가 발생했습니다: {e}")
        return None

def checking_new_post(token, band_key, body):
    last_post_key = get_new_post_key(token, band_key)

    while True:
        current_post_key = get_new_post_key(token, band_key)
        if last_post_key != current_post_key:
            create_comment(TOKEN, BAND_KEY, current_post_key, MESSAGE)
            st.write("키가 변경되엇습니다.")
            break
        time.sleep(2)  # 60초 대기 후 다시 확인

# 메시지 작성
def create_comment(token, band_key, post_key, body):
    url = 'https://openapi.band.us/v2/band/post/comment/create'
    params = {
        'access_token': token,
        'band_key': band_key,
        'post_key': post_key,
        'body': body
    }

    try:
        response = requests.post(url, data=params)
        response.raise_for_status()  # HTTP 오류 발생 시 예외 발생
        print("댓글이 성공적으로 작성되었습니다.")
    except requests.RequestException as e:
        print(f"댓글 작성 중 오류가 발생했습니다: {e}")



# 메인 코드
TOKEN = st.text_input("Band의 TOKEN을 넣어주세요.")

if TOKEN:
    band_list = get_band_list(TOKEN)
    st.write(band_list)

    # 공백
    st.write("")
    st.write("")

    BAND_KEY = st.text_input("메크로 대상인 밴드의 TOKEN를 넣어주세요.")

    # 공백
    st.write("")
    st.write("")

    MESSAGE = st.text_input("댓글을 적어주세요.")

    if st.button("메크로 시작"):
        checking_new_post(TOKEN, BAND_KEY, MESSAGE)
