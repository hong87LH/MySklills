
import re
import sys

def clean_urls(content):
    urls = []
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
        md_link_match = re.search(r'\[.*?\]\((https?://[^\)]+)\)', line)
        if md_link_match:
            url = md_link_match.group(1)
        else:
            url_match = re.search(r'(https?://[^\s]+)', line)
            if url_match:
                url = url_match.group(1)
            else:
                continue
        if 'xiaohongshu.com' in url or 'xhslink.com' in url:
            urls.append(url)
    return urls

def clean_urls_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return clean_urls(content)
    except Exception as e:
        print('[错误] 读取文件失败:', e)
        return []

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('用法: python url_cleaner.py <文件路径>')
        sys.exit(1)
    file_path = sys.argv[1]
    urls = clean_urls_from_file(file_path)
    if urls:
        print('找到', len(urls), '个小红书链接:')
        for url in urls:
            print(url)
    else:
        print('未找到有效的小红书链接')

