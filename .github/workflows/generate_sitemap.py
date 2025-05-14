import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# دالة للحصول على جميع الروابط في صفحة معينة
def get_links(url):
    try:
        # إرسال طلب HTTP إلى الصفحة
        response = requests.get(url)
        response.raise_for_status()  # للتحقق من وجود خطأ في الاستجابة

        # استخدام BeautifulSoup لتحليل محتوى HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # استخراج كل الروابط (الروابط تبدأ بـ <a href="...)
        links = set()
        for link in soup.find_all('a', href=True):
            full_url = urljoin(url, link['href'])  # التأكد من أن الرابط كامل
            links.add(full_url)

        return links
    except requests.exceptions.RequestException as e:
        print(f"حدث خطأ أثناء الاتصال بـ {url}: {e}")
        return set()

# دالة لإنشاء خريطة الموقع
def generate_sitemap(start_url):
    visited = set()  # لتخزين الروابط التي تمت زيارتها
    to_visit = [start_url]  # قائمة الصفحات التي يجب زيارتها
    sitemap = []

    while to_visit:
        url = to_visit.pop()
        if url not in visited:
            visited.add(url)
            sitemap.append(url)
            print(f"زيارة: {url}")
            links = get_links(url)
            to_visit.extend(links - visited)  # إضافة الروابط الجديدة إلى قائمة الزيارة

    return sitemap

# دالة لحفظ خريطة الموقع إلى ملف XML
def save_sitemap(sitemap, filename="sitemap.xml"):
    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''
    for url in sitemap:
        xml_content += f'  <url>\n    <loc>{url}</loc>\n  </url>\n'

    xml_content += '</urlset>'

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(xml_content)
    print(f"تم حفظ خريطة الموقع في {filename}")

# دالة رئيسية لتنفيذ الكود
if __name__ == "__main__":
    start_url = "https://rpd4games.blogspot.com/"  # استبدل هذا الرابط برابط مدونتك
    sitemap = generate_sitemap(start_url)
    save_sitemap(sitemap)
