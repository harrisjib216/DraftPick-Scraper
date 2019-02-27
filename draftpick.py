import requests
from bs4 import BeautifulSoup


class DraftPick():
    # init class
    def __init__(self, website):
        self.website = website


    # start scraper
    def start_scrape(self):
        page = open(self.website)
        soup = BeautifulSoup(page, "html.parser")

        # rankings
        athlete_list = soup.find_all('div', attrs={'class': 'primary'})
        for rank in athlete_list:
            print(rank.string)

        # profile images
        athlete_list = soup.find_all('img', attrs={'class': 'jsonly'})
        for img in athlete_list:
            print(img['src'])

        # names
        athlete_list = soup.find_all('a', attrs={'class': 'rankings-page__name-link'})
        for name in athlete_list:
            print(name.string)

        # school
        athlete_list = soup.find_all('span', attrs={'class': 'meta'})
        for school in athlete_list:
            print(school.string)

        # positions
        athlete_list = soup.find_all('div', attrs={'class': 'position'})
        for pos in athlete_list:
            print(pos.string)

        # height -- weight
        athlete_list = soup.find_all('div', attrs={'class': 'metrics'})
        for htwt in athlete_list:
            print(htwt.string)

        # rating
        athlete_list = soup.find_all('span', attrs={'class': 'score'})
        for raiting in athlete_list:
            print(raiting.string)


# my scrape
my_scrape = DraftPick("2019_Top_Basketball_Recruits.html")   # due to site crashing, the page was exported to an HTML file
my_scrape.start_scrape()



### WILL FIX ###
# my_scrape = DraftPick("https://247sports.com/Season/2019-Basketball/CompositeRecruitRankings/?InstitutionGroup=HighSchool")
# page = requests.get(self.website)
# soup = BeautifulSoup(page.text, 'html.parser')