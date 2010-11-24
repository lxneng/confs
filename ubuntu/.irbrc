require 'rubygems'
require 'hirb'
Hirb::View.enable
if ENV.include?('RAILS_ENV')
  require 'logger'
  RAILS_DEFAULT_LOGGER = Logger.new(STDOUT)
end
