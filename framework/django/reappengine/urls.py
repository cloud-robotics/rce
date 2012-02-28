#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       urls.py
#       
#       Copyright 2011 dominique hunziker <dominique.hunziker@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#   	

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    # start page
    url(r'^$', 'reappengine.site.views.users.index'),
    
    # user handling
    url(r'^login/$', 'reappengine.site.views.users.loginForm'),
    url(r'^login/check/$', 'reappengine.site.views.users.login'),
    url(r'^logout/$', 'reappengine.site.views.users.logout'),
    
    # service registration
    url(r'^service/select/$', 'reappengine.site.views.ros.select'),
    url(r'^service/select/([A-Za-z][\w_]*)/$', 'reappengine.site.views.ros.feedService'),
    url(r'^service/sumit/$', 'reappengine.site.views.ros.sumit'),
    
    # api
    url(r'^api/', include('reappengine.api.urls')),
)
