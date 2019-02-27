# import requests
from bs4 import BeautifulSoup


class DraftPick():
    # init class
    def __init__(self, website):
        self.website = website


    # start scraper
    def start_scrape(self):
        page = open(self.website)
        soup = BeautifulSoup(page, "html.parser")
        ranks = []
        imgs = []
        names = []
        schools = []
        pos = []
        hwght = []
        raitings = []
        complete = []

        # rankings
        athlete_list = soup.find_all('div', attrs={'class': 'primary'})
        for rank in athlete_list:
            ranks.append(str(rank.string))

        # profile images
        athlete_list = soup.find_all('img', attrs={'class': 'jsonly'})
        for img in athlete_list:
            imgs.append(str(img['src']))

        # names
        athlete_list = soup.find_all('a', attrs={'class': 'rankings-page__name-link'})
        for name in athlete_list:
            names.append(str(name.string))

        # school
        athlete_list = soup.find_all('span', attrs={'class': 'meta'})
        for school in athlete_list:
            schools.append(str(school.string))

        # positions
        athlete_list = soup.find_all('div', attrs={'class': 'position'})
        for position in athlete_list:
            pos.append(str(position.string))

        # height -- weight
        athlete_list = soup.find_all('div', attrs={'class': 'metrics'})
        for htwt in athlete_list:
            hwght.append(str(htwt.string))

        # rating
        athlete_list = soup.find_all('span', attrs={'class': 'score'})
        for raiting in athlete_list:
            raitings.append(str(raiting.string))
        
        # combine all the data into one array
        for key in ranks:
            complete.append({
                'rank': ranks[int(key) - 1],
                'profile': imgs[int(key) - 1],
                'name': names[int(key) - 1],
                'school': schools[int(key) - 1],
                'pos': pos[int(key) - 1],
                'htwt': hwght[int(key) - 1],
                'raiting': raitings[int(key) - 1]
            })
        
        print(complete)
            


# my scrape
my_scrape = DraftPick("2019_Top_Basketball_Recruits.html")   # due to site crashing, the page was exported to an HTML file
my_scrape.start_scrape()


### WILL FIX ###
# my_scrape = DraftPick("https://247sports.com/Season/2019-Basketball/CompositeRecruitRankings/?InstitutionGroup=HighSchool")
# page = requests.get(self.website)
# soup = BeautifulSoup(page.text, 'html.parser')