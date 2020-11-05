<h1 align="center">GitGram</h1>
<h3 align="center">Applied Social Network Analysis<h3>

#### Hosted App has a bug due to which results never shows up for a user with high number of following or follow ups, Fixing will take time because of other projects rush work. Till then, hit it locally! or maybe try your luck!


## Documentation
- You may read from [here](https://gitgram.herokuapp.com/documentation)
- Also suggested to read code inside utils folder where file name does'nt start with util
  - I may be writing docs too quickly and very briefly ignoring code
  
## Running web app locally
- clone the repo locally
- `pip install -r requirements.txt`
- `uvicorn server:app --reload`


## WebApp ScreenShots
![image](https://user-images.githubusercontent.com/41824020/97091109-e9c60780-1656-11eb-892a-658770664f8a.png)
![image](https://user-images.githubusercontent.com/41824020/97091074-a4093f00-1656-11eb-8314-2364296fc729.png)
![image](https://user-images.githubusercontent.com/41824020/97091083-b4211e80-1656-11eb-9bc0-055d9779a4a3.png)
![image](https://user-images.githubusercontent.com/41824020/97091282-73c2a000-1658-11eb-87dc-c3ef2792ce14.png)
![image](https://user-images.githubusercontent.com/41824020/97091556-4971e200-165a-11eb-9791-a30828225bce.png)
![image](https://user-images.githubusercontent.com/41824020/97091671-1a0fa500-165b-11eb-9465-e9aae2eea97d.png)
![image](https://user-images.githubusercontent.com/41824020/97091737-b9cd3300-165b-11eb-9806-f0b8507fd4ff.png)

## Some Graphs SS
![image](https://user-images.githubusercontent.com/41824020/97091015-3e1cb780-1656-11eb-850b-db7eb22709dd.png)
![image](https://user-images.githubusercontent.com/41824020/97091020-4e349700-1656-11eb-99a4-18553482dcff.png)
![image](https://user-images.githubusercontent.com/41824020/97091048-7f14cc00-1656-11eb-873a-e3ad514a3cbb.png)
![image](https://user-images.githubusercontent.com/41824020/97091056-8cca5180-1656-11eb-81c2-63e946e59d09.png)

## PRs Welcomed for
- [ ] Shift code to use GitHub API
- [ ] Parallelize the code
- [ ] Data cruching only once for complete analysis
- [ ] Add/Fix link to repositories in suggessted repositories

## Note:
- Be patient because their is hell lot of scraping happening in behind
  - GitHub api crashes when sending data of someone with above 5k followers, and some bots are their trying to does the same
  - I can easily control that part with this approach, although later I will shift it to api usage and make it multi threaded
  - Time Complexity / Scraping for each analysis: `((followers + following) of followers) * ((followers + following) of following)`
- It's Suggested to run locally
- Possible reason for heroku bug is request getting timeout, only effective way to handle this is to revamp the web app server code

*/>*
*f*
