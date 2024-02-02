import requests
from bs4 import BeautifulSoup


def get_letest_python_articles():
    url="http://www.python.org/"
#bring webpage in vs code by requests library
    response=requests.get(url)  

#parsing html content by Beautifulsoup library
    if response.status_code==200:
        soup=BeautifulSoup(response.text,"html.parser")
        latest_article=[]

#extract and save articals in a vairiable
        for article in soup.select(".blog-widget li"):
            title=article.a.text.strip()
            latest_article.append(title)

        return latest_article
    else:
        print(f"fail to retrive information.status code:{response.status_code}")
        return[]
if __name__=="__main__":
    python_articles=get_letest_python_articles()

#printing of articals with index value

    if python_articles:
        print("new news in the python.org section")
        for index,article in enumerate(python_articles,1):
            print(f"{index}.{article}")
    else:
        print("no article found")        

        