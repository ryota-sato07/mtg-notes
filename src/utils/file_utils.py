def save_text_to_file(text, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(text)
