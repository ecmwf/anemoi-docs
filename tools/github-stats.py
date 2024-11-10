#!/usr/bin/env python3
# (C) Copyright 2024 Anemoi contributors.
#
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
#
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.


import argparse
import datetime
import logging
import os
from collections import defaultdict

import requests
from dotenv import load_dotenv

load_dotenv()

REPOS = (
    "datasets",
    "graphs",
    "inference",
    "models",
    "registry",
    "training",
    "utils",
    "transform",
)


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--opened-pull-requests", action="store_true")

# Add more options
# group.add_argument('--other-stat', action='store_true')

args = parser.parse_args()


LOG = logging.getLogger(__name__)

logging.basicConfig(
    level="INFO",
    format="%(asctime)s %(levelname)s %(message)s",
)


def opened_pull_requests(owner, repo):

    # Authentication
    token = os.environ["GITHUB_TOKEN"]
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    params = {"state": "all", "per_page": 100, "page": 1}

    events = defaultdict(int)
    while True:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        if isinstance(data, dict):
            raise ValueError(data["message"])

        if len(data) == 0:
            break

        for n in data:
            d = datetime.datetime.fromisoformat(n["created_at"].replace("Z", "")).date()
            events[d] += 1

        for n in data:
            if n["closed_at"]:
                d = datetime.datetime.fromisoformat(n["closed_at"].replace("Z", "")).date()
                events[d] -= 1

        params["page"] += 1

    min_date = min(events.keys())
    max_date = max(events.keys())

    k = min_date

    n = 0
    while k < max_date:
        if k not in events:
            v = n
        else:
            v = events[k]
            n += v

        yield ((str(k), n))

        k += datetime.timedelta(days=1)


if args.opened_pull_requests:
    stats = dict()
    print(",".join(["repo", "date", "opened"]))
    for repo in REPOS:
        for date, opened in opened_pull_requests("ecmwf", f"anemoi-{repo}"):
            print(",".join(str(_) for _ in [repo, date, opened]))
    exit(0)
