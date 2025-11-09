---
title: YouTube URL Schemes
description:
created: 2025-07-17T14:15:08
modified: 2025-11-08T16:53:50
draft: false
featured: false
tags:
  - Today-I-Learned/url-schemes
sources: []
---

Today I learned how to customize YouTube URL schemes to make video sharing more effective:

1. **Watch Links**
	* Format
		* Regular version: `https://www.youtube.com/watch?v=<video_id>`
		* Short version: `https://youtu.be/<video_id>`
	* Query parameters
		* `t` → Starts the video at a specific timestamp, great for directly jumping to the key moments
			* For example:
				* `&t=60` starts the video 1 minute in
				* `&t=1m30s` starts the video 1 minute and 30 seconds in
			* Works for both watch link types:
				* <https://www.youtube.com/watch?v=cnQLp_DII2o&t=120>
				* <https://youtu.be/cnQLp_DII2o?t=120>
		* The following parameters are unnecessary and can be safely stripped from URLs:
			* `list` → Shows which **playlist** the video is from
				* Example: `&list=PLVELbpBnqC0qFKrWNBZupOEV6MX4xt_fM`
			* `ab_channel` → Shows which **channel** the video is from
				* Example: `&ab_channel=InspiringSquad`
		* `https://www.youtube.com/embed/<video_id>`
			* Use this to embed videos on websites [^1]
			* ⭐️ Also, this is helpful for [watching videos without any ads](https://gist.github.com/huaminghuangtw/be2eaee73f155187ca1ed0570b7268a0)!
			* Example: <https://www.youtube.com/watch?v=NcQQVbioeZk> → <https://www.youtube.com/embed/NcQQVbioeZk>
2. **Playlist Links**
	* Format: `https://www.youtube.com/playlist?list=<playlist_id>`
3. **Channel Links**
	* Format: `https://www.youtube.com/channel/@<channel_handle>`

[^1]: <https://developers.google.com/youtube/player_parameters>
