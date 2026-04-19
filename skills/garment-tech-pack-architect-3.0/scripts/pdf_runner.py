#!/usr/bin/env python3

import sys
import os
import io

# 设置编码（解决Windows控制台编码问题）
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 添加当前目录到Python路径，确保可以导入pdf_to_markdown模块
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

def main():
    """轻量级中介脚本入口"""
    try:
        # 动态导入主要模块
        from pdf_to_markdown import pdf_to_markdown_with_tables
        
        # 检查参数
        if len(sys.argv) < 2:
            print("用法: python pdf_runner.py <pdf文件路径> [是否提取表格]", file=sys.stderr)
            print("示例: python pdf_runner.py ./工艺单.pdf true", file=sys.stderr)
            print("      python pdf_runner.py ./工艺单.pdf false", file=sys.stderr)
            sys.exit(1)
        
        pdf_path = sys.argv[1]
        extract_tables = False  # 默认不提取表格
        
        if len(sys.argv) >= 3:
            extract_tables = sys.argv[2].lower() in ['true', 'yes', '1', 'table', 'tables']
        
        # 调用主要函数
        result = pdf_to_markdown_with_tables(pdf_path, extract_tables, verbose=True)
        
        if result is not None:
            print(result)
            sys.exit(0)
        else:
            print("PDF转换失败", file=sys.stderr)
            sys.exit(1)
            
    except ImportError as e:
        print(f"导入模块失败: {e}", file=sys.stderr)
        print("请确保pdf_to_markdown.py在同一目录下", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"运行错误: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()