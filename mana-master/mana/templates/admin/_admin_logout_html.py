# coding: utf-8

_admin_logout_html_code = '''
{% extends 'admin/base.html' %}

{% block access_control %}
{% if current_user.is_authenticated %}
<div class="btn-group pull-right">
    <a class="btn dropdown-toggle" data-toggle="dropdown" href="#">
        <i class="icon-user"></i> {{ current_user.login }} <span class="caret"></span>
    </a>
    <ul class="dropdown-menu">
        <li><a href="{{ url_for('auth.logout') }}">Log out</a></li>
    </ul>
</div>
{% endif %}
{% endblock %}

'''