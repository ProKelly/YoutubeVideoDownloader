# YoutubeVideoDownloader
Youtube Video Downloader with django + tailwindcss

## Output 
![Screenshot from 2024-09-07 06-20-16](https://github.com/user-attachments/assets/2657b7a7-af86-465f-a100-70e37e3dd447)

# Installation 
## clone repository
``` bash
https://github.com/ProKelly/YoutubeVideoDownloader.git
```

## set up virtual env 
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```
## Install dependencies 
```bash
pip install -r requirements.txt
```
# Configure tailwindcss 
## 1. Initialize the Tailwind CSS app:
```
 python manage.py tailwind init
```
## 2. install Tailwind dependencies:
 ```
  python manage.py tailwind install
```

## 3. start tailwind server 
```
python manage.py tailwind start
```
# Run Migrations
```bash
python manage.py migrate
```
# Start Development server 
```bash
python manage.py runserver
```
# Usage
    - Open your browser and go to http://127.0.0.1:8000.
    - Paste a YouTube video URL in the input box.
    - Select the format you want to download (MP4, MP3, etc.).
    - Click the Download button.

