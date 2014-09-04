b2tool
======

## bbtool is a command line tool to manage BitBucket

### List of commands and options

-----

* ###**auth**###

    * login
        * --username
        * --password

----
* ###**pullrequest**###
    
    **required options**
    * --owner **Organization or account on Bitbucket**
    * --repo  **Repository to connect**

    * listall
    * oldest
    * accept

----
## How to use ##

<pre><code>$ b2tool command options</pre></code>


***List all pull requests***

<pre><code>$ b2tool pullrequest listall --owner jesuejunior --repo projectA </pre></code>

***List oldest pull requests with ID and branch***

<pre><code>$ b2tool pullrequest oldest --owner jesuejunior --repo projectA </pre></code>

***Print only id of oldest pull requests***

<pre><code>$ b2tool pullrequest oldest --owner jesuejunior --repo projectA  --id True</pre></code>

***Print only branch of oldest pull requests***

<pre><code>$ b2tool pullrequest oldest --owner jesuejunior --repo projectA  --branch True</pre></code>

----