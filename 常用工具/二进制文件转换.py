import chardet


def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        print(f"检测到的文件编码: {encoding}")
        return encoding


def fix_html_encoding_auto(file_path, target_encoding='utf-8'):
    original_encoding = detect_encoding(file_path)
    if original_encoding:
        try:
            with open(file_path, 'r', encoding=original_encoding, errors='replace') as file:
                content = file.read()

            with open(file_path, 'w', encoding=target_encoding) as file:
                file.write(content)

            print(f"文件编码已从 {original_encoding} 转换为 {target_encoding}")
        except Exception as e:
            print(f"处理文件时出错: {e}")


# 使用示例
fix_html_encoding_auto('D:/犹新背单词/Grammarguide/blank.htm')
