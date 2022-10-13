from platform import python_version

import bs4
import pandas as pd
import requests

url_list = [
    "https://techcrunch.com/2022/10/12/after-selling-his-last-startup-to-google-this-founder-now-wants-to-automate-mundane-tasks-with-relay/",
    "https://techcrunch.com/2022/10/12/microsoft-brings-dall-e-2-to-the-masses-with-designer-and-image-creator/",
    "https://techcrunch.com/2022/10/12/6-tips-for-launching-a-blockchain-startup/",
    "https://techcrunch.com/2022/10/11/noom-tech-layoffs-diet-app/",
    "https://techcrunch.com/2022/10/12/katana-an-erp-for-smb-manufacturers-raises-34m/",
    "https://techcrunch.com/2022/10/12/folx-powers-lgbtq-telehealth-support-groups-with-30m-round/",
    "https://techcrunch.com/2022/10/12/gohenry-the-banking-service-for-under-18s-raises-55m-after-passing-2m-users/",
    "https://techcrunch.com/2022/10/12/daily-crunch-closed-early-access-product-relay-raises-5m-seed-round-to-tackle-collaborative-workflows/",
    "https://techcrunch.com/2022/10/12/founders-shouldnt-bet-on-a-q4-venture-capital-resurgence/",
    "https://techcrunch.com/2022/10/12/6-investors-share-where-they-draw-the-line-when-it-comes-to-ethical-issues/",
    "https://techcrunch.com/2022/10/12/check-out-our-partner-roundtable-topics-and-speakers-at-disrupt/",
    "https://techcrunch.com/2022/10/12/fintech-fundraising-has-reverted-to-the-mean/",

]



article_titles, article_contents, article_hrefs = [], [], []

for url in url_list:
    if url in 
    response = requests.get(url)

    soup = bs4.BeautifulSoup(response.text, "html.parser")

    tag_header = soup.find("h1", {"class": "article__title"})
    tag_content = soup.find("div", {"class": "article-content"})

    article_title = tag_header.get_text().strip()
    article_content = tag_content.get_text().strip().replace("\n", " ")

    article_titles.append(article_title)
    article_contents.append(article_content)
    article_hrefs.append(url)

df = pd.DataFrame({"title": article_titles, "content": article_contents, "url": url})

df.to_csv('tech_crunch.csv')


