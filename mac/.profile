
# MacPorts Installer addition on 2009-12-17_at_09:04:05: adding an appropriate PATH variable for use with MacPorts.
export PATH=/usr/local/Cellar/ruby/1.9.1-p378/bin/:/usr/local/Cellar/python/2.7/bin:/opt/local/bin:/opt/local/sbin:$PATH
# Finished adapting your PATH environment variable for use with MacPorts.
alias mysqlstart='/usr/local/Cellar/mysql/5.1.41/bin/mysqld_safe &'
alias mysqlstop='/usr/local/Cellar/mysql/5.1.41/bin/mysqladmin -uroot -padmin shutdown'


function ss {
  if [ -e script/rails ]; then
    script/rails server $@
  else
    script/server $@
  fi
}
function sc {
  if [ -e script/rails ]; then
    script/rails console $@
  else
    script/console $@
  fi
}
function sg {
  if [ -e script/rails ]; then
    script/rails generate $@
  else
    script/generate $@
  fi
}

export CLICOLOR=true
