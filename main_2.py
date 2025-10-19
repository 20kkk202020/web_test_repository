import feedparser

# Googleニュースの日本語版RSS
rss = feedparser.parse("https://news.google.com/rss?hl=ja&gl=JP&ceid=JP:ja")

for e in rss.entries[:10]:
    print(e.title)
    print(e.link)
    print("-----")
