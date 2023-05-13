import requests

def get_top_video_link(api_key, query):
    # YouTube Data API v3에서 검색어에 해당하는 동영상 정보 요청
    search_url = f"https://www.googleapis.com/youtube/v3/search?part=id&q={query}&type=video&key={api_key}"
    response = requests.get(search_url)

    # 검색 결과 중 첫 번째 동영상의 ID 추출
    video_id = response.json()["items"][0]["id"]["videoId"]

    # 첫 번째 동영상의 링크 정보 출력
    return f"https://www.youtube.com/watch?v={video_id}"