from django.conf.urls import patterns, include, url

from django.contrib import admin
from views.view_test import render_base
from views.view_user import register_user, login_user, profile_user, check_user_name
from views.view_main import render_main_page, show_friend_albums, show_mine_albums, get_moods, upload_pic

admin.autodiscover()

#patterns
test_patterns = patterns('',
                         url(r'^base/$', render_base),
)

user_patterns = patterns('',
                         url(r'^reg-user/$', register_user),
                         url(r'^login/$', login_user),
                         url(r'^(?P<user_id>\d{1,})/$', profile_user),
                         )
album_patterns = patterns('',
                          url(r'^mine/(?P<user_id>\d{1,})/$', show_mine_albums),
                          url(r'^friends/$', show_friend_albums),
                          url(r'^upload/$', upload_pic),
                          )

api_patterns = patterns('',
                        url(r'^check-exist/(?P<user_name>\w+)$', check_user_name),
                        )
#url dispatcher
urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^test/', include(test_patterns)),
                       url(r'^user/', include(user_patterns)),
                       url(r'^album/', include(album_patterns)),
                       url(r'^api/', include(api_patterns)),
                       url(r'^$', render_main_page),
                       url(r'^/$', render_main_page),
                       url(r'^main/$', render_main_page),
                       url(r'^moods/$', get_moods),
)

