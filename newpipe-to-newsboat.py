"""
                           _                __                          _                 _   
 _ __   _____      ___ __ (_)_ __   ___     \ \ _ __   _____      _____| |__   ___   __ _| |_ 
| '_ \ / _ \ \ /\ / / '_ \| | '_ \ / _ \_____\ \ '_ \ / _ \ \ /\ / / __| '_ \ / _ \ / _` | __|
| | | |  __/\ V  V /| |_) | | |_) |  __/_____/ / | | |  __/\ V  V /\__ \ |_) | (_) | (_| | |_ 
|_| |_|\___| \_/\_/ | .__/|_| .__/ \___|    /_/|_| |_|\___| \_/\_/ |___/_.__/ \___/ \__,_|\__|
                    |_|     |_|                                                               

SUMMARY:
    This Python script takes an export file from Newpipe and converts it to Newsboat format, so that these YouTube channels can be loaded as an RSS feed by Newsboat.

    Script should be used as follows:
    python3 newpipe-to-newsboat.py NEWPIPE_EXPORT_FILE.json

    A 'result.txt' file will automatically generate with the output. The output will also be printed to the terminal.
"""

import json
from sys import argv, exit
from pathlib import Path

assert len(argv) == 2, "Expected 1 argument, got {}.".format(len(argv)-1)
try:
    newpipe_file = open(argv[1])
except FileNotFoundError:
    print("Error: file '{file}' not found.".format(file=argv[1]))
    exit()

res = json.load(newpipe_file)

Path('result.txt').touch()
result = open('result.txt', 'w')

for subscription in res['subscriptions']:
    rss_url = "https://www.youtube.com/feeds/videos.xml?channel_id="
    rss_url += subscription['url'].split('/')[-1]

    rss_name = "\"~YouTube : "
    rss_name += subscription['name']

    new_line = "{} {}\n".format(rss_url, rss_name)

    print(new_line)
    result.write(new_line)