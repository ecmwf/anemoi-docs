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
import csv
import datetime
import logging
import os
import sys
from collections import defaultdict

import requests
from dotenv import load_dotenv

load_dotenv()

REPOS = (
    "anemoi-datasets",
    "anemoi-graphs",
    "anemoi-inference",
    "anemoi-models",
    "anemoi-registry",
    "anemoi-training",
    "anemoi-utils",
    "anemoi-transform",
)


def parse_comma_separated(arg):
    return arg.split(",")


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--opened-pull-requests", action="store_true")
group.add_argument("--pull-requests-activity", action="store_true")


# Add more options
# group.add_argument('--other-stat', action='store_true')

parser.add_argument("--owner", default="ecmwf", help="GitHub owner")
parser.add_argument("--repos", type=parse_comma_separated, default=REPOS, help="GitHub repositories")
parser.add_argument("--output", "-o", type=argparse.FileType("w"), default=sys.stdout, help="Output file")

args = parser.parse_args()


LOG = logging.getLogger(__name__)

logging.basicConfig(
    level="INFO",
    format="%(asctime)s %(levelname)s %(message)s",
)


def iterate_pages(owner, repo, what, state="all"):
    # Authentication
    token = os.environ["GITHUB_TOKEN"]
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }

    url = f"https://api.github.com/repos/{owner}/{repo}/{what}"
    params = {"state": state, "per_page": 100, "page": 1}

    while True:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        if isinstance(data, dict):
            raise ValueError(data["message"])

        if len(data) == 0:
            break

        for n in data:
            yield n

        params["page"] += 1


############################################
def opened_pull_requests():

    def opened_pull_requests_per_repo(repo):

        events = defaultdict(int)

        for pull in iterate_pages(args.owner, repo, "pulls"):

            d = datetime.datetime.fromisoformat(pull["created_at"].replace("Z", "")).date()
            events[d] += 1

            if pull["closed_at"]:
                d = datetime.datetime.fromisoformat(pull["closed_at"].replace("Z", "")).date()
                events[d] -= 1

        min_date = min(events.keys())
        max_date = max(events.keys())

        date = min_date

        pull = 0
        while date < max_date:
            if date not in events:
                v = pull
            else:
                v = events[date]
                pull += v

            yield ((str(date), pull))

            date += datetime.timedelta(days=1)

    writer = csv.writer(args.output)
    writer.writerow(["repo", "date", "opened"])
    for repo in args.repos:
        for date, opened in opened_pull_requests_per_repo(repo):
            writer.writerow([repo, date, opened])


############################################


def pull_requests_activity():
    writer = csv.writer(args.output)
    writer.writerow(
        [
            "repo",
            "number",
            "user",
            "state",
            "created_at",
            "closed_at",
            "merged_at",
            "draft",
            "labels",
            "author_association",
        ]
    )
    for repo in args.repos:

        for pull in iterate_pages(args.owner, repo, "pulls"):
            writer.writerow(
                [
                    repo,
                    pull["number"],
                    pull["user"]["login"],
                    pull["state"],
                    pull["created_at"],
                    pull["closed_at"],
                    pull["merged_at"],
                    pull["draft"],
                    ",".join(_["name"] for _ in pull["labels"]),
                    pull["author_association"],
                ]
            )


############################################

if args.opened_pull_requests:
    opened_pull_requests()

if args.pull_requests_activity:
    pull_requests_activity()
