from pathlib import Path


def main():
    pass


# Function to download all urls
def downloader():
    pass


# Function to download and save one url at a time
def download_and_save():
    pass



# Function to create directories based on url so the structure is correct
def create_dirs_from_url(domain,url):
    # remove domain from url to get the relative structure from root
    url = url.replace(domain,"")

    # split url and loop until the second last object (the last object is the name of the file)
    # in order to build up the folder structure

    root_path = Path(__file__).parent / "downloaded" / "1337.tech"
    url_split = url.split("/")
    for i in range(0, len(url_split)-1):
        root_path = root_path.joinpath(url_split[i])
    
    if not root_path.exists():
        root_path.mkdir(parents=True)

    return root_path



if __name__ == "__main__":
    # main()
    create_dirs_from_url("https://1337.tech","https://1337.tech/test/html")
