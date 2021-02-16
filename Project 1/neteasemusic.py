import json
import requests


def get_comments(target_url):
    headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/73.0.3683.75 Safari/537.36",
               'referer': "https://music.163.com/song?id=1366903034"}
    params = "HzflPbhT1mnhBBqmNZv44p0og8Jj7E+jhTeuc6jcvD7e1SJot77iPwMky3kgSW8U" \
             "+YS36XsTgtuKexSHZBoTdxF0f4NPLlehGO5e5UvxEm/Oh1YLQDLG4c+ShUUx/rtlACcNGsX1jRGZ+IYqFqx0wi3OJwzLW" \
             "+1KLxpvizLO3PJvfz7FdLKS70kqf5b0VELh "
    encSecKey = "23b637a432eb3e34150ec1a545bfc8b627320d7ef52a900838aa1e8ab1a190f380252ee75c7dee419a93c207f567245b330ad79469ceaf1ba124f1fe088bb8996e7adeb29fad2a74899265834b1b876c0e869d9873c3da231316621cd00463ba9c3871ccb3a81cb4553d37bb319a4668a6dbf6504dc75572619c520839def834 "
    data = {'params': params, 'encSecKey': encSecKey}
    res = requests.post(target_url, headers=headers, data=data)
    return res


def get_hot_comments(res):
    comments_json = json.loads(res.text)
    hot_comments = comments_json['hotComments']
    for each in hot_comments:
        print(each['user']['nickname']+'\n')
        print(each['content']+'\n')
        print('----------------------------\n')


def main():
    target_url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_1366903034?csrf_token="
    res = get_comments(target_url)
    get_hot_comments(res)


if __name__ == '__main__':
    main()