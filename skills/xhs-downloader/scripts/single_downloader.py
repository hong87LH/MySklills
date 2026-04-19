
import sys
import os

from xhs_downloader import XHSDownloader

def single_download(url, download_dir, cookies=None, username_classification_enabled=True):
    downloader = XHSDownloader(download_dir=download_dir)
    
    if cookies:
        downloader.update_cookies(cookies)
    
    print(f"[单个下载] 开始下载: {url}")
    downloader.download_note(url, username_classification_enabled=username_classification_enabled)
    print("\n[单个下载] 任务完成！")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="小红书单个下载器")
    parser.add_argument("--url", required=True, help="小红书URL")
    parser.add_argument("--dir", required=True, help="下载目录")
    parser.add_argument("--cookies", help="Cookies字符串")
    parser.add_argument("--no-classify", action="store_true", help="不按用户名分类")
    
    args = parser.parse_args()
    
    single_download(
        url=args.url,
        download_dir=args.dir,
        cookies=args.cookies,
        username_classification_enabled=not args.no_classify
    )

