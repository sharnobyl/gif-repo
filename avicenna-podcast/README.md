# Avicenna Briefing (private podcast feed)

Unlisted podcast feed (`itunes:block` = Yes). Add it in Apple Podcasts with Library > ... > Follow a Show by URL.

Add an episode: copy the MP3 here, append it to `episodes.json` (with byte size and duration), run `python3 build_feed.py` in this folder, commit and push. Then purge the jsDelivr cache: https://purge.jsdelivr.net/gh/sharnobyl/gif-repo@main/avicenna-podcast/feed.xml
