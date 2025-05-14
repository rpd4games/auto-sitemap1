import requests
import xml.etree.ElementTree as ET
from datetime import datetime

rss_url = "https://rpd4games.blogspot.com/feeds/posts/default?alt=rss"
response = requests.get(rss_url)
rss = ET.fromstring(response.content)

sitemap_header = '''<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'''
sitemap_footer = '</urlset>'

sitemap_urls = ""
for item in rss.findall('./channel/item'):
    link = item.find('link').text
    pubDate = item.find('pubDate').text
    lastmod = datetime.strptime(pubDate, "%a, %d %b %Y %H:%M:%S %z").isoformat()
    sitemap_urls += f"  <url>\n    <loc>{link}</loc>\n    <lastmod>{lastmod}</lastmod>\n    <priority>0.80</priority>\n  </url>\n"

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_header + sitemap_urls + sitemap_footer)
