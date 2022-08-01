import requests

HR_BASEURL = "https://hacker-news.firebaseio.com"
HR_TOP_STORIES = '/v0/topstories.json'
HR_BEST_STORIES = '/v0/beststories.json'

def get_text(count=10):
    params = dict(
        print='pretty'
    )

    get_story_ids = requests.get(url=HR_BASEURL+HR_BEST_STORIES, params=params)
    story_ids = get_story_ids.json()

    stories = []
    for id in story_ids[:10]:
        story = requests.get(url=HR_BASEURL+ f"/v0/item/{id}.json", params=params)
        stories.append(story.json()['title'])
    return "\n".join(stories)

