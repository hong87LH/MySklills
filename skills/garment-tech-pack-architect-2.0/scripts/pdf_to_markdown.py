import pdfplumber
import os
import sys
import io

def pdf_to_markdown_with_tables(pdf_path, extract_tables=True):
    """
    将PDF文件转换为Markdown格式文本，保留表格结构
    
    Args:
        pdf_path (str): PDF文件路径
        extract_tables (bool): 是否提取表格，默认True
    
    Returns:
        str|None: 转换成功返回Markdown文本，失败返回None
    """
    if not os.path.exists(pdf_path):
        print(f"错误：PDF文件不存在 - {pdf_path}", file=sys.stderr)
        return None
    
    text_content = []
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)
            print(f"开始处理PDF文件，共 {total_pages} 页", file=sys.stderr)
            
            for page_num, page in enumerate(pdf.pages, 1):
                text_content.append(f"## 第 {page_num} 页\n\n")
                
                if extract_tables:
                    tables = page.extract_tables()
                    
                    if tables:
                        has_tables = False
                        for table in tables:
                            if not table or not any(row for row in table if any(cell and str(cell).strip() for cell in row)):
                                continue
                            
                            cleaned_table = []
                            for row in table:
                                cleaned_row = [str(cell).strip() if cell is not None else "" for cell in row]
                                if any(cell for cell in cleaned_row):
                                    cleaned_table.append(cleaned_row)
                            
                            if not cleaned_table:
                                continue
                            
                            max_cols = max(len(row) for row in cleaned_table)
                            for row in cleaned_table:
                                while len(row) < max_cols:
                                    row.append("")
                            
                            header = cleaned_table[0]
                            markdown_table = "|" + "|".join(header) + "|\n"
                            markdown_table += "|" + "|".join(["---"] * max_cols) + "|\n"
                            
                            for row in cleaned_table[1:]:
                                markdown_table += "|" + "|".join(row) + "|\n"
                            
                            text_content.append(markdown_table + "\n")
                            has_tables = True
                        
                        if has_tables:
                            continue
                
                text = page.extract_text()
                if text:
                    lines = text.split('\n')
                    processed_lines = []
                    for line in lines:
                        if not any(keyword in line for keyword in ['Page ', 'Displaying ', '显示', '结果']):
                            processed_lines.append(line)
                    processed_text = '\n'.join(processed_lines)
                    text_content.append(processed_text + "\n\n")
        
        markdown_content = ''.join(text_content)
        print(f"✓ PDF转换完成，共 {total_pages} 页", file=sys.stderr)
        return markdown_content
        
    except Exception as e:
        print(f"✗ 转换过程中发生错误: {str(e)}", file=sys.stderr)
        return None

def main():
    """命令行入口函数"""
    # 设置编码（解决Windows控制台编码问题）
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    
    if len(sys.argv) < 2:
        print("用法: python pdf_to_markdown.py <pdf文件路径> [是否提取表格]", file=sys.stderr)
        print("示例: python pdf_to_markdown.py ./工艺单.pdf true", file=sys.stderr)
        print("      python pdf_to_markdown.py ./工艺单.pdf false", file=sys.stderr)
        print("参数说明:", file=sys.stderr)
        print("  <pdf文件路径>   - 必填，要转换的PDF文件路径", file=sys.stderr)
        print("  [是否提取表格]  - 可选，true/false，默认true，是否提取表格结构", file=sys.stderr)
        print("输出: 将转换后的Markdown文本输出到标准输出，日志信息输出到标准错误", file=sys.stderr)
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    extract_tables = False  # 默认不提取表格，只提取文本
    
    if len(sys.argv) >= 3:
        extract_tables = sys.argv[2].lower() in ['true', 'yes', '1', 'table', 'tables']
    
    print(f"PDF路径: {pdf_path}", file=sys.stderr)
    print(f"提取表格: {'是' if extract_tables else '否'}", file=sys.stderr)
    print("-" * 50, file=sys.stderr)
    
    markdown_content = pdf_to_markdown_with_tables(pdf_path, extract_tables)
    
    if markdown_content is not None:
        print(markdown_content, file=sys.stdout)
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
