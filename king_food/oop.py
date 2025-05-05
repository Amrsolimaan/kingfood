from bs4 import BeautifulSoup
import os

def process_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # تعديل الروابط
    for tag in soup.find_all(['link', 'script', 'img']):
        if tag.name == 'link' and tag.get('href'):
            href = tag['href']
            if not href.startswith(('http://', 'https://', '{% static')):
                tag['href'] = "{% static '" + href + "' %}"
        elif tag.name == 'script' and tag.get('src'):
            src = tag['src']
            if not src.startswith(('http://', 'https://', '{% static')):
                tag['src'] = "{% static '" + src + "' %}"
        elif tag.name == 'img' and tag.get('src'):
            src = tag['src']
            if not src.startswith(('http://', 'https://', '{% static')):
                tag['src'] = "{% static '" + src + "' %}"

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(str(soup))

# مسار الملف HTML الذي ترغب في تعديله
html_file_path = r'F:\projects\king_food\king_food\templates\product.html'

# تنفيذ السكريبت على الملف HTML
process_html_file(html_file_path)

print("تم تعديل الروابط بنجاح في ملف HTML.")
