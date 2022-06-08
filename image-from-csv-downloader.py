import pandas as pd
import urllib.request
import ssl
import certifi
import os


def download_img(img_url, img_name):
    ssl.SSLContext.verify_mode = ssl.VerifyMode.CERT_OPTIONAL
    req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
    with open(f'{img_name}.jpg', "wb") as f:
        with urllib.request.urlopen(req, context=ssl.create_default_context(cafile=certifi.where())) as r:
            f.write(r.read())


# Change columns accordingly
def downloader(csv_name):
    data = pd.read_csv(csv_name)
    df = pd.DataFrame(data, columns=['id', 'img'])
    for index, row in df.iterrows():
        download_img(row[1], row[0])


# Get all csv files in dir
files = os.listdir('Directory')
for file in files:
    if file[-3:] != 'csv':
        continue
    # Create directory where to store files
    os.mkdir(f'/directory/images/{file[:-4]}')
    # Change working directory
    os.chdir(rf'/directory/images/{file[:-4]}')
    downloader(f'/directory/{file}')
