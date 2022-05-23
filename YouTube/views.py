from django.shortcuts import render, redirect
from django.views import View
from YouTube.models import YouTube
from django.conf import settings

SEARCH = ""

class SearchVideoView(View):
    def get(self, request):
        YouTube.objects.all().delete()
        return render(request, "youtube.html")
    
    def post(self, request):
        SEARCH = request.POST["search"]
        if SEARCH != "":
            search_url = "https://www.googleapis.com/youtube/v3/search"
            video_url = "https://www.googleapis.com/youtube/v3/videos"
            channel_url = "https://www.googleapis.com/youtube/v3/channels?part=snippet&id='+commaSeperatedList+'&fields=items(id%2Csnippet%2Fthumbnails)&key={}".format(
                settings.YOUTUBE_DATA_API_KEY
            )
            para_search = {
                "part": "snippet",
                "q": SEARCH,
                "key": settings.YOUTUBE_DATA_API_KEY,
                "maxResults": 9,
                "type": "video",
            }

            search_response = requests.get(search_url, params=para_search)
            results = search_response.json()["items"]
            ids = []
            for result in results:
                ids.append(result["id"]["videoId"])

            para_videos = {
                "part": "snippet",
                "key": settings.YOUTUBE_DATA_API_KEY,
                "id": ",".join(ids),
            }
            video_response = requests.get(video_url, params=para_videos)
            results = video_response.json()["items"]

            dict_youtube = {}
            list_youtube = []
            channelIdList = []
            for result in results:
                dict_youtube = {
                    "title": result["snippet"]["title"],
                    "thumbnails": result["snippet"]["thumbnails"]["high"]["url"],
                    "channelId": result["snippet"]["channelId"],
                    "IdVideo": result["id"],
                }
                channelIdList.append(result["snippet"]["channelId"])
                list_youtube.append(dict_youtube)

            param_channel = {
                "part": "snippet,contentDetails,statistics",
                "key": settings.YOUTUBE_DATA_API_KEY,
                "id": ",".join(channelIdList),
            }
            channel_response = requests.get(channel_url, params=param_channel)
            results = channel_response.json()["items"]
            profile = []
            profile_dic = {}
            i = 0
            for result in results:
                profile_dic = {
                    "index": i + 1,
                    "channelId": result["id"],
                    "profile": result["snippet"]["thumbnails"]["default"]["url"],
                }
                i += 1
                profile.append(profile_dic)
            new_list = []

            for dic in profile:
                vids = filter(
                    lambda yt: yt["channelId"] == dic["channelId"], list_youtube
                )
                for vid in vids:
                    dic.update(vid)
                new_list.append(dic)

            for lst in new_list:
                YouTube.objects.create(
                    index=lst["index"],
                    channelId=lst["channelId"],
                    IdVideo=lst["IdVideo"],
                    profile=lst["profile"],
                    title=lst["title"],
                    thumbnails=lst["thumbnails"],
                ).save()

            return render(request, "youtube.html", {"videos": new_list})
        return render(request, "youtube.html", {"Empty": "אנא מלא את השדה"})
