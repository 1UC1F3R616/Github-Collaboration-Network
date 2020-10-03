import requests
from bs4 import BeautifulSoup as soup


def followers(username, page='1', followers_list=[]): 
    """
    :parameter-username: username of the GitHub User
    :parameter-page: page number
    :parameter-followers_list: list containing followers username
    :return: followers list
    """
    
    url = 'https://github.com/{}?page={}&tab=followers'.format(username, page)
    page_fetch = requests.get(url)
    
    page_soup = soup(page_fetch.text, 'html.parser')

    #####################Break Condition#########################
    stop_here = page_soup.find("p", {"class":"mt-4"})
    stop_here2 = page_soup.find("h3", {"class":"mb-1"})
    if  (stop_here or stop_here2):
        #print('\n\n\nAll Followers Fetched\n\n')
        #print(followers_list)
        return followers_list
    else:
        # print('\n\nMoving to Next Page\n\n')
        pass

    ######################Finding Users##########################
    users = page_soup.findAll("span", {"class":"link-gray"})
    
    for user in users:
        if user.text.strip():
            followers_list.append(user.text)
            #print(followers_list[-1])

    page_number = int(page)
    page = str(page_number + 1)
    return followers(username, page, followers_list)
    

def following(username, page='1', following_list=[]):
    """
    :parameter-username: username of the GitHub User
    :parameter-page: page number
    :parameter-following_list: list containing username of people that user is following
    :return: following list
    """
    
    url = 'https://github.com/{}?page={}&tab=following'.format(username, page)
    page_fetch = requests.get(url)

    page_soup = soup(page_fetch.text, 'html.parser')

    #####################Break Condition#########################
    stop_here = page_soup.find("p", {"class":"mt-4"})
    stop_here2 = page_soup.find("h3", {"class":"mb-1"})

    if  (stop_here or stop_here2):
        return following_list
    else:
        #print('\n\nMoving to Next Page\n\n')
        pass

    ######################Finding Users##########################
    users = page_soup.findAll("span", {"class":"link-gray"})
    
    for user in users:
        if user.text.strip():
            following_list.append(user.text)
            #print(following_list[-1])

    page_number = int(page)
    page = str(page_number + 1)
    return following(username, page, following_list)


# my_followers = followers('IMRO832000')
# print(my_followers)
# my_following = following('IMRO832000')
# print(my_following)


def get_repos(username, url='', repo_list=[]):
    """
    :parameter-username: username of the GitHub User
    :parameter-repo_list: list of repos
    :return: list of repos
    """
    if url == '':
        url = 'https://github.com/{}?tab=repositories'.format(username)
    page_fetch = requests.get(url)

    page_soup = soup(page_fetch.text, 'html.parser')

    
    #####################Break Condition#########################
    stop_here = page_soup.find("h3", {"class":"mb-1"})
    if stop_here:
        return repo_list
    #####################Break Condition#########################

    #####################Collecting Repos########################
    repos = page_soup.find_all('a', attrs={"itemprop":"name codeRepository"})
    clean_repos = [repo.text.strip() for repo in repos if repo.text.strip()]
    repo_list += clean_repos
    #####################Collecting Repos########################

    #####################Recursion Depth#########################
    buttons = page_soup.find_all('a', {'class':'btn btn-outline BtnGroup-item'})
    for button in buttons:
        if button.text.strip() == 'Next':
            next_page_url = button['href']
            break
    else:
        # This is also acting as a break condition
        return repo_list
    return get_repos(username, url=next_page_url, repo_list=repo_list)
    #####################Recursion Depth#########################


# print(get_repos('1UC1F3R616'))