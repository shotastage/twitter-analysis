# -*- encoding:utf-8 -*-
from setuptools import setup, find_packages
import sys

sys.path.append('./tweetgetter')

if __name__ == "__main__":
    setup(
        name = "tweetgetter",
        version='0.0.1',
        author = "Shota Shimazu",
        author_email = "t16440ss@sfc.keio.ac.jp",
        packages = find_packages(),
        install_requires=[
            "requests_oauthlib",
            "numpy"
        ],
        entry_points = {
            'console_scripts':[
                'tweetgetter = tweetgetter.tweetgetter:main',
            ],
        },
        description = "Tweet getter",
        long_description = "Tweet getter for SFC DS class.",
        url = "https://github.com/shotastage/twitter-analysis",
        license = "MIT",
        platforms = ["POSIX", "Windows", "Mac OS X"],
    )
