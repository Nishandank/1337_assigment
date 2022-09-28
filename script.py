from pathlib import Path
import requests
from scraper.TraverseWeb import TraverseWeb
from scraper.Utils import Utils
from concurrent.futures import ThreadPoolExecutor,as_completed

def main():
    url: str = 'https://1337.tech'
    try:
        traverse = TraverseWeb(domain=url, start_url=url, include_hashed_urls=True)
        print("Starting indexing")
        all_urls = traverse.run()
        print("Downloading started")
        downloader(all_urls,'https://1337.tech')
    except Exception as e:
        print(f"An error occured while running script {e}")

# Function to download all urls
def downloader(urls,domain):
    # define thread pool to be used
    executor = ThreadPoolExecutor(max_workers=5)
    root_path = Path(__file__).parent / 'downloaded' / '1337.tech'

    if not root_path.exists():
        root_path.mkdir(parents=True)
    
    files_downloaded = 0
    active_jobs = []
    # download and save url using thread
    for i in range(0,len(urls)):
        url = urls[i]
        job = executor.submit(download_and_save, url=url,root_path=root_path,domain=domain)
        active_jobs.append(job)
    
    # Update with progress on when download job is complete
    for active_job in as_completed(active_jobs):
        files_downloaded +=1
        print_progress(len(urls),files_downloaded)
   
def print_progress(total_files_to_download,file_downloaded_counter):
    print(f"[{'*'*file_downloaded_counter}] {file_downloaded_counter / total_files_to_download * 100 :.0f}%")

# Function to download and save one url at a time
def download_and_save(url,root_path,domain):
    response = requests.get(url)
    if response.ok:
        file_dir = create_dirs_from_url(domain,url,root_path)
        if Utils.is_html(url):
            url_split = url.split('/')
            filename = url_split[len(url_split)-1]
            file_dir = file_dir.joinpath(f'{filename}.html')
            file = open(file_dir,'w')
            file.write(response.text)
            file.close()
        else:
            url_split = url.split('/')
            filename = url_split[len(url_split)-1]
            file_dir = file_dir.joinpath(filename)
            file = open(file_dir,'w')
            file.write(response.text)
            file.close()



# Function to create directories based on url so the structure is correct
def create_dirs_from_url(domain,url,root_path):
    # remove domain from url to get the relative structure from root
    url = url.replace(domain,"")

    # split url and loop until the second last object (the last object is the name of the file)
    # in order to build up the folder structure
    url_split = url.split("/")
    for i in range(0, len(url_split)-1):
        root_path = root_path.joinpath(url_split[i])
    
    if not root_path.exists():
        root_path.mkdir(parents=True)

    return root_path



if __name__ == "__main__":
    main()
