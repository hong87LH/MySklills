
import sys
import os
import time

from xhs_downloader import XHSDownloader

def batch_download(urls, download_dir, cookies=None, username_classification_enabled=True):
    downloader = XHSDownloader(download_dir=download_dir)
    
    if cookies:
        downloader.update_cookies(cookies)
    
    print(f"[批量下载] 开始下载 {len(urls)} 个笔记...")
    
    for i, url in enumerate(urls):
        print(f"\n>>> 进度 {i+1}/{len(urls)}")
        downloader.download_note(url, username_classification_enabled=username_classification_enabled)
        time.sleep(1)
    
    print("\n[批量下载] 所有任务处理完毕！")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="小红书批量下载器")
    parser.add_argument("--urls", nargs="+", help="小红书URL列表")
    parser.add_argument("--file", help="包含URL的文件路径")
    parser.add_argument("--dir", required=True, help="下载目录")
    parser.add_argument("--cookies", help="Cookies字符串")
    parser.add_argument("--no-classify", action="store_true", help="不按用户名分类")
    
    args = parser.parse_args()
    
    urls = []
    
    if args.urls:
        urls = args.urls
    elif args.file:
        from url_cleaner import clean_urls_from_file
        urls = clean_urls_from_file(args.file)
    
    if not urls:
        print("[错误] 未提供有效的URL")
        sys.exit(1)
    
    batch_download(
        urls=urls,
        download_dir=args.dir,
        cookies=args.cookies,
        username_classification_enabled=not args.no_classify
    )

