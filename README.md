# Async Image Downloader

This repository contains a Python script for asynchronously downloading images from a list of URLs using asyncio, aiohttp, and aiofiles. The script is designed to efficiently fetch multiple images concurrently, making it suitable for applications where large numbers of images need to be downloaded quickly.

## Features
- Asynchronously downloads images from a list of URLs.
- Supports various image formats such as jpg, jpeg, png, and gif.
- Handles HTTP errors gracefully and logs them.
- Utilizes aiohttp for efficient HTTP requests and aiofiles for asynchronous file I/O.
- Provides timing information for the overall download process.
  
## Usage
#### Clone the repository to your local machine:
```bash
git clone https://github.com/aunraza-dev/Async-Image-Downloader.git
```

#### Navigate to the project directory:
```bash
cd Async-Image-Downloader
```

Prepare a text file named urls-seperated.txt containing the list of image URLs, with each URL on a separate line.

#### Run the script:
```bash
python3 main.py
```
Once the script finishes execution, the downloaded images will be saved in a directory named img-seperated.
## Requirements
- Python 3.7+
- aiohttp
- aiofiles
