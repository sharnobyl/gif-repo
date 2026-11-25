# Avicenna Briefing (private podcast feed)

Unlisted podcast feed (`itunes:block` = Yes). Add it in Apple Podcasts with Library > ... > Follow a Show by URL.

Add an episode: copy the MP3 here, append it to `episodes.json` (with byte size and duration), run `python3 build_feed.py` in this folder, commit and push. Then purge the jsDelivr cache: https://purge.jsdelivr.net/gh/sharnobyl/gif-repo@main/avicenna-podcast/feed.xml

Note: jsDelivr serves `audio/mpeg` only for files under 20 MB, so the feed points at a 48 kbps copy pinned to a commit (`@<sha>`). Full-quality 96 kbps MP3 is next to it. For new episodes: push the MP3, then use `https://cdn.jsdelivr.net/gh/sharnobyl/gif-repo@<commit-sha>/avicenna-podcast/<file>.mp3` as the episode `file`.
