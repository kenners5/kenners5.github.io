# Some Things Happened
woke up one day and decided to do a thing

found site backups

set up git repo
added basic index
created github repo
added github ssh key back
pushed index
saw basic index in browser (yay)
configured github pages
updated DNS records to use github for wtb
found weird test email redirect
configured github pages custom domain
SSL not working
set up CAA record for letsencrypt
tried to manually certbot, couldn't publish the sentinel file
tried variations of paths and files

got mad at missing git aliases
forked gbernhardt dotfiles
wrote dotfiles symlink install script

concluded dotfiles and dotfolders aren't deployed to the web
ssl still not working, moving on

researched libraries
decided on next.js
wordpress articles suggest using graphQL in existing wordpress service, no thanks

configure nodesource apt repo
install nodejs
npx markdown from wordpress export

start by exporting from wordpress xml
exported posts, hooray
didn't export comments, might be some gems there for later
rats, no author name in exported metadata

maybe author information is in the db backup
spun up mariadb container
imported db backup (yay)
analyzed db schema
found author information in a separate table
join, dump to file

started writing python script to insert author metadata
got annoyed that script was showing me py3 as syntax error, cause py27 installed
installed python3.8 on windows
configured atom to use it and installed new pylint

wrote script, realized author dump was not including filename/slug
found slug in database as post_name
re-dumped author info
