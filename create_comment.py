import requests


def create_comment(token, band_key, post_key, body):
    url = f'https://openapi.band.us/v2/band/post/comment/create'
    params = {
        'access_token': token,
        'band_key': band_key,
        'post_key': post_key,
        'body': body
    }
    try:
        response = requests.post(url, data=params)
        if response.status_code == 200:
            print("댓글이 성공적으로 작성되었습니다.")
        else:
            print(f"댓글 작성에 실패했습니다. 응답 코드: {response.status_code}")
    except Exception as e:
        print(f"댓글 작성 중 오류가 발생했습니다: {e}")
