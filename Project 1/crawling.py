import requests
import bs4
import re


def open_url(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}
    res = requests.get(url, headers=headers)
    return res


def find_data(res):
    data = []
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    content = soup.find(id="Cnt-Main-Article-QQ")
    target = content.find_all("p", style="TEXT-INDENT: 2em")
    target = iter(target)
    for each in target:
        if each.text.isnumeric():
            data.append([
                re.search(r'\[(.+)\]', next(target).text).group(1),
                re.search(r'\d.+', next(target).text).group(),
                re.search(r'\d.+', next(target).text).group(),
                re.search(r'\d.+', next(target).text).group()])
    return data


def main():
    url = "https://news.house.qq.com/a/20170702/003985.htm"
    res = open_url(url)
    data = find_data(res)
    for each in data:
        print(each)


if __name__ == '__main__':
    main()
