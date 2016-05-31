from django.conf.urls import patterns, url, include
from competition import views

urlpatterns = patterns('',
    url(r'^$', views.compWelcome, name="compWelcome"),
    url(r'^registration/$', views.registration, name="registration"),
    url(r'^register/$', views.register, name="register"),
    url(r'^judge-register/$', views.judge_register, name="judge_register"),
    url(r'^account/$', views.account, name="account"),
    url(r'^judge-account/', views.j_account, name="j_account"),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'competition/competition_login.html'}, name="login"),
    url(r'^login/process/$', views.process_login, name="process_login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '../login/'}, name="logout"),
    url(r'^results-2015/$', views.results_2015, name='results_2015'),
    url(r'^results-2014/$', views.results_2014, name='results_2014'),
    url(r'^results-2013/$', views.results_2013, name='results_2013'),
    url(r'^results-2012/$', views.results_2012, name='results_2012'),
    url(r'^sponsors/$', views.sponsors, name='sponsors'),
    url(r'^info/$', views.info, name="info"),
    url(r'^locations/$', views.locations, name="locations"),
    url(r'^account/print/(?P<e_pk>\d+)', views.print_label, name="print_label"),
    # form submission urls
    url(r'^address/$', views.address_page, name="address_page"),
    # UPDATE
    url(r'^account/address/$', views.update_address, name="update_address"),
    url(r'^account/profile/$', views.update_profile, name="update_profile"),
    url(r'^account/judge/$', views.update_judge, name="update_judge"),
    # DELETE
    url(r'^account/submission/remove/(?P<s_pk>\d+)$', views.delete_submission, name="delete_submission"),
    # ADD
    url(r'^account/submission/$', views.add_submission, name="add_submission"),
    # Tools
    url(r'^tools/table-manager/$', views.table_manager, name="table_manager"),
    url(r'^tools/table-manager/add', views.table_add, name="table_add"),
    url(r'^tools/table-manager/lock-category', views.lock_category, name="lock_category"),
    url(r'^tools/table-manager/unlock-category', views.unlock_category, name="unlock_category"),
    url(r'^tools/table-manager/judge/add', views.add_judge, name="add_judge"),
    url(r'^tools/table-manager/judge/remove', views.remove_judge, name="remove_judge"),
    url(r'^tools/view-judges', views.view_judges, name="view_judges"),
    url(r'^tools/switch-table', views.switch_table, name="switch_table"),
    url(r'^tools/table-manager/steward/add', views.add_steward, name="add_steward"),
    url(r'^tools/table-manager/steward/remove', views.remove_steward, name="remove_steward"),
    url(r'^tools/pullsheet/(?P<pk>\d+)', views.pull_sheet, name="pull_sheet"),
    url(r'^tools/table-score/(?P<pk>\d+)', views.table_score, name="table_score"),
    url(r'^tools/table-score/post/(?P<pk>\d+)', views.table_score_post, name="table_score_post"),
    url(r'^tools/view-submissions', views.view_submissions, name="view_submissions"),
    url(r'^tools/view-brewers', views.view_brewers, name="view_brewers"),
    # Password Reset
    url(r'^login/password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/competition/login/password/reset/done/'}, name="password_reset"),
    url(r'^login/password/reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    url(r'^login/password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/competition/login/password/done/'}, name="password_reset_confirm"),
    url(r'^login/password/done/$', 'django.contrib.auth.views.password_reset_complete', {'current_app' : '/competition/'}),
)