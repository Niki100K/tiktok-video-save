import time
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import urllib.error

def downloadVideo(link, id):
    print(f"Downloading video {id} from: {link}")
    cookies = {

    }

    headers = {

    }


    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': '', # NOTE: This value gets changed, please use the value that you get when you copy the curl command from the network console
    }
    
    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    downloadSoup = BeautifulSoup(response.text, "html.parser")
    try:
        downloadLink = downloadSoup.a["href"]
        videoTitle = downloadSoup.p.getText().strip()

        # Remove invalid characters from video title
        videoTitle = re.sub(r'[<>:"/\\|?*]', '', videoTitle)

        mp4File = urlopen(downloadLink)
        # Feel free to change the download directory
        with open(f"C:/Users/GRIGS/Desktop/New folder/{id}-{videoTitle}.mp4", "wb") as output:
            while True:
                data = mp4File.read(4096)
                if data:
                    output.write(data)
                else:
                    break
    except KeyError:
        print(f"Unable to extract download link for video {id}. Skipping...")
        return id
    except urllib.error.URLError:
        print(f"Error accessing download link for video {id}. Skipping...")
        return id
    except Exception as e:
        print(f"An error occurred while downloading video {id}: {e}. Skipping...")
        return id

    return None

# List of TikTok links
tiktok_links = []


incorrectIndex = []

for index, url in enumerate(tiktok_links):
    result = downloadVideo(url, index)
    if result is not None:
        incorrectIndex.append(result)
    time.sleep(10)

print("Incorrect Index:", incorrectIndex)
