#coding: utf-8
import requests
from b2tool.conf import BASE_URL_V2

from b2tool import __projectname__
import sys
import komandr

_pullrequest = komandr.prog(prog='{0} pull request'.format(__projectname__))


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
@komandr.arg('cmd', 'cmd', choices=['list', 'accept', 'decline', 'older'], help="Available pull request subcommands. Use <subcommand> -h to see more.")
def pullrequest(cmd):
    _pullrequest.execute(sys.argv[2:])


@_pullrequest.command
@_pullrequest.arg('owner', required=True, type=str, help='')
@_pullrequest.arg('repo', required=True, type=str, help='')
def list(owner=None, repo=None):

    path = "{0}repositories/{1}/{2}/pullrequests/".format(BASE_URL_V2, owner, repo)
    res = requests.get(path, auth=('jesuejunior', '') )
    print res.content

@_pullrequest.command
@_pullrequest.arg('owner', required=True, type=str, help='')
@_pullrequest.arg('repo', required=True, type=str, help='')
@_pullrequest.arg('id', required=True, type=int, help='')
def accept(owner=None, repo=None, id=None):
    path = "{0}repositories/{1}/{2}/pullrequests/{3}/accept".format(BASE_URL_V2, owner, repo, id)
    res = requests.post(path, auth=('jesuejunior', '') )

    if res.status == 200:
        print "Pull request {0} accepetd successful".format(id)
    else:
        print "Ops, An error ocurred!"



