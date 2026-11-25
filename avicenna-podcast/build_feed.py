#!/usr/bin/env python3
"""Rebuild feed.xml for the Avicenna Briefing private podcast from episodes.json.
Add a new episode: put the MP3 in the repo folder, append an entry to episodes.json, run this, push."""
import json,os,email.utils,datetime
from xml.sax.saxutils import escape as e
HERE=os.path.dirname(os.path.abspath(__file__))
cfg=json.load(open(os.path.join(HERE,"show.json")))
eps=json.load(open(os.path.join(HERE,"episodes.json")))
def rfc(iso): return email.utils.format_datetime(datetime.datetime.fromisoformat(iso))
items=[]
for ep in sorted(eps,key=lambda x:x["pub"],reverse=True):
    items.append(f"""    <item>
      <title>{e(ep['title'])}</title>
      <description>{e(ep['description'])}</description>
      <itunes:summary>{e(ep['description'])}</itunes:summary>
      <pubDate>{rfc(ep['pub'])}</pubDate>
      <guid isPermaLink="false">{e(ep['guid'])}</guid>
      <enclosure url="{e(ep['file'] if ep['file'].startswith('http') else cfg['media_base']+ep['file'])}" length="{ep['bytes']}" type="audio/mpeg"/>
      <itunes:duration>{ep['duration']}</itunes:duration>
      <itunes:episodeType>full</itunes:episodeType>
      <itunes:episode>{ep['number']}</itunes:episode>
      <itunes:explicit>false</itunes:explicit>
      <itunes:image href="{e(cfg['media_base']+cfg['cover'])}"/>
    </item>""")
now=email.utils.format_datetime(datetime.datetime.now(datetime.timezone.utc))
xml=f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/">
  <channel>
    <title>{e(cfg['title'])}</title>
    <link>{e(cfg['link'])}</link>
    <atom:link href="{e(cfg['feed_url'])}" rel="self" type="application/rss+xml"/>
    <language>en</language>
    <description>{e(cfg['description'])}</description>
    <itunes:summary>{e(cfg['description'])}</itunes:summary>
    <itunes:author>{e(cfg['author'])}</itunes:author>
    <itunes:image href="{e(cfg['media_base']+cfg['cover'])}"/>
    <image><url>{e(cfg['media_base']+cfg['cover'])}</url><title>{e(cfg['title'])}</title><link>{e(cfg['link'])}</link></image>
    <itunes:category text="Business"/>
    <itunes:explicit>false</itunes:explicit>
    <itunes:type>episodic</itunes:type>
    <itunes:block>Yes</itunes:block>
    <lastBuildDate>{now}</lastBuildDate>
{chr(10).join(items)}
  </channel>
</rss>
"""
open(os.path.join(HERE,cfg["out_dir"],"feed.xml"),"w").write(xml); print("wrote feed.xml with",len(items),"episode(s)")
