#coding: utf-8
try:
    import simplejson as json
except:
    import json
import sys

import requests
from clint.textui import puts, columns, colored
import komandr

from b2tool.conf import BASE_URL_V2, get_credentials
from b2tool import __projectname__


_pullrequest = komandr.prog(prog='{0} pull request'.format(__projectname__))

USERNAME, PASSWORD = get_credentials()

# Method has implements
# GETrepositories/{owner}/{repo_slug}/pullrequests/
# POSTrepositories/{owner}/{repo_slug}/pullrequests/
# GETrepositories/{owner}/{repo_slug}/pullrequests/{id}
# PUTrepositories/{owner}/{repo_slug}/pullrequests/{id}
# GETrepositories/{owner}/{repo_slug}/pullrequests/{id}
# GETrepositories/{owner}/{repo_slug}/pullrequests/activity
# GETrepositories/{owner}/{repo_slug}/pullrequests/{id}/activity
# GETrepositories/{owner}/{repo_slug}/pullrequests/{id}/commits
# GETrepositories/{owner}/{repo_slug}/pullrequests/{id}/patch
# GETrepositories/{owner}/{repo_slug}/pullrequests/{id}/diff
# POSTrepositories/{owner}/{repo_slug}/pullrequests/{id}/accept
# POSTrepositories/{owner}/{repo_slug}/pullrequests/{id}/decline
# GETrepositories/{owner}/{repo_slug}/pullrequests/{id}/comments
# GETrepositories/{owner}/{repo_slug}/pullrequests/{id}/comments/{comment_id}
# GETrepositories/{owner}/{repo_slug}/pullrequests/{id}/approvals

@komandr.command
@komandr.arg('cmd', 'cmd', choices=['list', 'accept', 'decline', 'oldest'], help="Available pull request subcommands. Use <subcommand> -h to see more.")
def pullrequest(cmd):
    _pullrequest.execute(sys.argv[2:])


@_pullrequest.command
@_pullrequest.arg('owner', required=True, type=str, help='')
@_pullrequest.arg('repo', required=True, type=str, help='')
def list(owner=None, repo=None):

    path = "{0}repositories/{1}/{2}/pullrequests/".format(BASE_URL_V2, owner, repo)
    res = requests.get(path, auth=(USERNAME, PASSWORD))
    pulls =  json.loads(res.content).get('values')

    # print pulls
    puts(colored.magenta(columns(['Id', 5], ['Status', 8], [str('Repository'), 12], ['Source branch', 45], ['Created on', 35])))
    for pull in pulls:
        puts(colored.green(columns([str(pull['id']), 5], [pull['state'], 8], [str(pull['source']['repository']['name']), 12], [pull['source']['branch']['name'], 45], [pull['created_on'], 35])))

@_pullrequest.command
@_pullrequest.arg('owner', required=True, type=str, help='')
@_pullrequest.arg('repo', required=True, type=str, help='')
@_pullrequest.arg('id', required=True, type=int, help='')
def accept(owner=None, repo=None, id=None):
    path = "{0}repositories/{1}/{2}/pullrequests/{3}/accept".format(BASE_URL_V2, owner, repo, id)
    res = requests.post(path, auth=(USERNAME, PASSWORD) )

    if res.status == 200:
        print "Pull request {0} accepetd successful".format(id)
    else:
        print "Ops, An error ocurred!"

@_pullrequest.command
@_pullrequest.arg('owner', required=True, type=str, help='')
@_pullrequest.arg('repo', required=True, type=str, help='')
@_pullrequest.arg('id', required=True, type=int, help='')
def decline(owner=None, repo=None, id=None):
    pass

@_pullrequest.command
@_pullrequest.arg('owner', required=True, type=str, help='')
@_pullrequest.arg('repo', required=True, type=str, help='')
def oldest(owner=None, repo=None):
    pass
