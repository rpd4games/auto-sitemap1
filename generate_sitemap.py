# generate_sitemap.py
urls = [
    "https://example.com/",
    "https://example.com/about",
    "https://example.com/contact"
]

sitemap = '''<?xml version="1.0" encoding="UTF-8"?>\n'''
sitemap += '''<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'''

for url in urls:
    sitemap += f"  <url><loc>{url}</loc></url>\n"

sitemap += '''</urlset>'''

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap)

print("✅ تم إنشاء ملف sitemap.xml بنجاح")
