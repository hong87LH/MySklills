import requests
import re
import json
import os
import time
import sys
import csv
from urllib.parse import urlparse, unquote

class XHSDownloader:
    def __init__(self, cookies=None, download_dir=None):
        # 如果用户没有指定路径，使用脚本目录下的 downloads
        if download_dir is None or not download_dir.strip():
            base_dir = os.path.dirname(os.path.abspath(__file__))
            self.download_dir = os.path.join(base_dir, "downloads")
        else:
            # 使用用户指定的路径
            self.download_dir = download_dir

        # CSV 数据库文件始终跟随下载目录
        self.csv_file_path = os.path.join(self.download_dir, "xhs_notes.csv") 
        
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1"
        }
        self.cookies = cookies if cookies else {}
        
        # 确保目录存在
        if not os.path.exists(self.download_dir):
            try:
                os.makedirs(self.download_dir)
                print(f"[初始化] 已创建目录: {self.download_dir}")
            except Exception as e:
                print(f"[错误] 无法创建目录 {self.download_dir}: {e}")
                sys.exit(1)
        else:
            print(f"[初始化] 目标目录: {self.download_dir}")

        # 加载该目录下的历史记录
        self.history_timestamps = self._load_history()

    def _load_history(self):
        history = {}
        if not os.path.exists(self.csv_file_path): return history
        try:
            with open(self.csv_file_path, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    url = row.get('原链接')
                    ts = row.get('download_time')
                    if url and ts and url not in history: history[url] = ts
        except Exception: pass 
        return history

    def update_cookies(self, cookie_str):
        if not cookie_str: return
        try:
            for cookie in cookie_str.split(';'):
                if '=' in cookie:
                    key, value = cookie.strip().split('=', 1)
                    self.cookies[key] = value
        except Exception as e: print(f"[错误] Cookies 解析失败: {e}")

    def get_redirect_url(self, url):
        try:
            response = requests.head(url, headers=self.headers, allow_redirects=True)
            return response.url
        except Exception: return url

    def clean_filename(self, filename):
        return re.sub(r'[\\/*?:"<>|]', "", filename).strip()

    def get_note_data(self, url):
        if "xhslink.com" in url: url = self.get_redirect_url(url)
        try:
            response = requests.get(url, headers=self.headers, cookies=self.cookies)
            response.raise_for_status()
            html = response.text
            
            # --- 优化：直接从 HTML meta 标签提取 og:image 封面 ---
            og_image_match = re.search(r'<meta (?:name|property)="og:image" content="(.*?)"', html)
            og_image_url = og_image_match.group(1) if og_image_match else None
            # --------------------------------------------------

            pattern = r'<script>window\.__INITIAL_STATE__=(.*?)</script>'
            match = re.search(pattern, html, re.DOTALL)
            if not match:
                pattern = r'<script type="text/javascript">window\.__INITIAL_STATE__=(.*?)</script>'
                match = re.search(pattern, html, re.DOTALL)
            if match:
                json_str = match.group(1).replace("undefined", "null")
                data = json.loads(json_str)
                if og_image_url:
                    data['_meta_og_image'] = og_image_url
                return data, url 
            else: return None, url
        except Exception as e:
            print(f"[错误] 请求失败: {e}")
            return None, url

    def _save_markdown_info(self, note_dir, title, username, content, original_url):
        file_name = f"{self.clean_filename(title)}.txt"
        file_path = os.path.join(note_dir, file_name)
        if content: content = re.sub(r'#(.+?)\[话题\]#', r'#\1 ', content)
        md_content = [f"# {title}", f"**{username}**", "\n---\n", content if content else "", "\n---\n", original_url]
        try:
            with open(file_path, 'w', encoding='utf-8') as f: f.write('\n'.join(md_content))
        except Exception as e: print(f"[错误] txt保存失败: {e}")

    def download_note(self, original_url, username_classification_enabled=False):
        data, final_url = self.get_note_data(original_url)
        if not data: return

        try:
            note_data = None
            if 'note' in data:
                note_root = data['note']
                if 'currentNoteId' in note_root and 'noteDetailMap' in note_root:
                    note_data = note_root['noteDetailMap'].get(note_root['currentNoteId'])
                if not note_data and 'firstNoteId' in note_root and 'noteDetailMap' in note_root:
                     note_data = note_root['noteDetailMap'].get(note_root['firstNoteId'])
                if not note_data and 'noteDetailMap' in note_root:
                    for v in note_root['noteDetailMap'].values():
                        if v and 'title' in v: note_data = v; break
                if not note_data and 'note' in note_root: note_data = note_root['note'] 
            if note_data and 'note' in note_data and isinstance(note_data['note'], dict): note_data = note_data['note']

            if not note_data:
                print("[错误] 无法定位笔记数据。")
                return

            if final_url in self.history_timestamps: download_timestamp = self.history_timestamps[final_url]
            else:
                download_timestamp = int(time.time())
                self.history_timestamps[final_url] = download_timestamp

            title = note_data.get('title', '无标题')
            if not title: title = note_data.get('desc', '无标题')[:20]
            username = note_data.get('user', {}).get('nickname', '未知用户')
            note_text = note_data.get('desc', '')
            tag_list = note_data.get('tagList', [])
            csv_tags_str = ','.join([tag.get('name') for tag in tag_list if tag.get('name')])

            safe_title = self.clean_filename(title)
            if len(safe_title) > 50: safe_title = safe_title[:50]
            
            relative_path_parts = []
            if username_classification_enabled:
                user_dir_name = self.clean_filename(username)
                base_download_path = os.path.join(self.download_dir, user_dir_name)
                note_dir_name = safe_title
                if not os.path.exists(base_download_path): os.makedirs(base_download_path)
                relative_path_parts = [user_dir_name, note_dir_name]
            else:
                base_download_path = self.download_dir
                note_dir_name = safe_title
                relative_path_parts = [note_dir_name]

            note_dir = os.path.join(base_download_path, note_dir_name)
            if not os.path.exists(note_dir): os.makedirs(note_dir)
            local_folder_str = "/".join(relative_path_parts)

            print(f"[信息] 笔记: {safe_title}")
            self._save_markdown_info(note_dir, title, username, note_text, final_url)

            video_links = []
            image_links = []
            type_ = note_data.get('type')
            
            if type_ == 'video':
                print("[信息] 视频下载中...")
                video_info = note_data.get('video', {})
                video_url = None
                
                # --- 封面图下载 ---
                cover_url = data.get('_meta_og_image')
                if not cover_url: cover_url = note_data.get('cover', {}).get('url_default')
                if not cover_url: cover_url = note_data.get('cover', {}).get('url')
                if cover_url:
                    if cover_url.startswith('//'): cover_url = 'https:' + cover_url
                    print("[信息] 下载视频封面...")
                    self._download_file(cover_url, os.path.join(note_dir, f"{safe_title}_cover.jpg"))

                download_success = False
                media = video_info.get('media', {})
                stream = media.get('stream', {})
                for codec in ['h265', 'h264']:
                    if download_success: break
                    codec_streams = stream.get(codec, [])
                    if codec_streams:
                        best_stream = sorted(codec_streams, key=lambda x: (x.get('height', 0), x.get('avgBitrate', 0)), reverse=True)[0]
                        if best_stream.get('masterUrl'):
                            video_url = best_stream.get('masterUrl')
                            download_success = self._download_file(video_url, os.path.join(note_dir, f"{safe_title}.mp4"))
                if not download_success:
                     origin_key = video_info.get('consumer', {}).get('originVideoKey')
                     if origin_key:
                         video_url = f"http://sns-video-bd.xhscdn.com/{origin_key}"
                         download_success = self._download_file(video_url, os.path.join(note_dir, f"{safe_title}.mp4"))
                if download_success: video_links.append(video_url)
            else:
                print("[信息] 图文下载中...")
                images = note_data.get('imageList', [])
                for idx, img in enumerate(images):
                    img_url = None
                    if img.get('traceId'): img_url = f"https://sns-webpic-qc.xhscdn.com/{img['traceId']}"
                    if not img_url:
                        for info in img.get('infoList', []):
                            if info.get('imageScene') == 'CR_1080P': img_url = info.get('url'); break
                    if not img_url: img_url = img.get('urlDefault') or img.get('url')
                    if img_url:
                        if 'liveVideoUrl' in img: self._download_file(img['liveVideoUrl'], os.path.join(note_dir, f"{safe_title}_{idx+1}_live.mp4"))
                        if self._download_file(img_url, os.path.join(note_dir, f"{safe_title}_{idx+1}.jpg")): image_links.append(img_url)
            
            print(f"[完成] {safe_title}")
            print("-" * 30)

            csv_data = {
                '原链接': final_url,
                '视频下载链接': '\n'.join(video_links),
                '图片下载链接': '\n'.join(image_links),
                'username': username,
                'title': title,
                'note-text': note_text,
                'hash-tag': csv_tags_str,
                'local_folder': local_folder_str,
                'safe_title': safe_title,
                'download_time': download_timestamp
            }
            self._write_to_csv(csv_data)
        except Exception as e: print(f"[错误] 处理失败: {e}")

    def _download_file(self, url, path):
        if os.path.exists(path): return True
        try:
            r = requests.get(url, headers=self.headers, stream=True)
            if r.status_code == 200:
                with open(path, 'wb') as f:
                    for chunk in r.iter_content(1024): f.write(chunk)
                return True
            return False
        except Exception: return False

    def _write_to_csv(self, data):
        fieldnames = ['原链接', '视频下载链接', '图片下载链接', 'username', 'title', 'note-text', 'hash-tag', 'local_folder', 'safe_title', 'download_time']
        file_exists = os.path.exists(self.csv_file_path)
        try:
            with open(self.csv_file_path, 'a', newline='', encoding='utf-8-sig') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                if not file_exists: writer.writeheader()
                writer.writerow(data)
        except Exception as e: print(f"[错误] CSV写入失败: {e}")

def main():
    print("="*50)
    print("   小红书下载工具 v2.1 (多库支持+默认分类)")
    print("   支持自定义下载路径")
    print("="*50)

    # 1. 设置下载路径 (新增功能)
    print("请输入下载保存路径 (例如 D:\\MyXHS 或 /Users/name/XHS)")
    custom_path = input("路径 (直接回车默认 ./downloads): ").strip()
    
    # 2. 设置 Cookies
    cookies_input = input("\n请输入 Cookies (回车跳过): ").strip()
    
    # 初始化下载器，传入路径
    downloader = XHSDownloader(download_dir=custom_path if custom_path else None)
    if cookies_input: downloader.update_cookies(cookies_input)

    # 3. 询问分类 (修改默认为 Y)
    username_classify_choice = input("是否按用户名分类文件夹？(Y/n，默认Y): ").strip().lower()
    # 只要不输入 'n'，都视为 True (回车、y、yes 等)
    username_classification_enabled = (username_classify_choice != 'n')

    base_dir = os.path.dirname(os.path.abspath(__file__))
    urls_file = os.path.join(base_dir, 'urls.txt')

    while True:
        print("\n" + "="*50)
        user_input = input("请输入 [链接] 或 [file] 加载urls.txt (q退出): ").strip()
        
        if user_input.lower() in ['q', 'exit']: break
        if not user_input: continue

        urls_to_process = []
        
        if user_input == 'file':
            if os.path.exists(urls_file):
                with open(urls_file, 'r', encoding='utf-8') as f:
                    urls_to_process = [line.strip() for line in f if line.strip()]
                
                if urls_to_process:
                    print(f"\n[已读取] urls.txt 中包含 {len(urls_to_process)} 个链接")
                    print("请选择下载顺序 (用于还原发布时间线):")
                    print("1. 从上到下 (默认 - 适合新链接在文件【末尾】)")
                    print("2. 从下到上 (倒序 - 适合新链接在文件【开头】)")
                    order_choice = input("请输入 (1/2): ").strip()
                    
                    if order_choice == '2':
                        urls_to_process.reverse()
                        print("[提示] 已启用倒序处理。")
                    else:
                        print("[提示] 已启用顺序处理。")
                else:
                    print("[提示] urls.txt 为空。")
            else:
                print(f"[错误] 未找到 urls.txt")
        else:
            urls_to_process = [user_input]

        if urls_to_process:
            for i, url in enumerate(urls_to_process):
                print(f"\n>>> 进度 {i+1}/{len(urls_to_process)}")
                downloader.download_note(url, username_classification_enabled)
                time.sleep(1)
            print("\n[完成] 本轮任务处理完毕。")

if __name__ == "__main__":
    main()