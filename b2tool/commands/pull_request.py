#coding: utf-8
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
@komandr.arg('cmd', 'cmd', choices=['list', 'accept', 'decline'], help="Available pull request subcommands. Use <subcommand> -h to see more.")
def pullrequest(cmd):
    _pullrequest.execute(sys.argv[2:])


@_pullrequest.command
@_pullrequest.arg('owner', required=True, type=str, help='')
@_pullrequest.arg('slug', required=True, type=str, help='')
@_pullrequest.arg('id', required=False, type=int, help='')
def list(owner=None, slug=None, id=None):

    print "URL {0}".format(BASE_URL_V2)


