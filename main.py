import asyncio
import aiohttp
import aiofiles
import os
import time
from pathlib import Path

async def fetch_image(session, url, path, index):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                ext = url.split('.')[-1]
                ext = ext if ext in ['jpg', 'jpeg', 'png', 'gif'] else 'png'
                fpath = path / f"image_{index}.{ext}"
                async with aiofiles.open(fpath, 'wb') as f:
                    content = await response.read()
                    await f.write(content)
                print(f"Downloaded: {url} -> {fpath}")
            else:
                print(f"Failed to download: {url} - HTTP Status: {response.status}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

async def download_images(urls, path):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for index, url in enumerate(urls):
            task = fetch_image(session, url, path, index)
            tasks.append(task)
        await asyncio.gather(*tasks)

async def main():
    start_time = time.time()

    async with aiofiles.open('urls-seperated.txt', 'r') as f:
        urls = await f.read()
    urls = urls.splitlines()
    
    img_path = Path("img-seperated")
    img_path.mkdir(exist_ok=True)

    await download_images(urls, img_path)

    elapsed_time = time.time() - start_time
    print(f"All downloads completed in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
