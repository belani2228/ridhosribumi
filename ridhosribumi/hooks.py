# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "ridhosribumi"
app_title = "Ridhosribumi"
app_publisher = "Ridho Sribumi Solusindo"
app_description = "App for management ridhosribumi"
app_icon = "octicon octicon-diff"
app_color = "#F0465C"
app_email = "develop@ridhosribumi.com"
app_license = "GNU General Public License"

fixtures = ["Custom Field","Custom Script"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/files/custom.css"
# app_include_css = "/assets/ridhosribumi/css/ridhosribumi.css"
# app_include_js = "/assets/ridhosribumi/js/ridhosribumi.js"

# include js, css files in header of web template
web_include_css = "/files/frappe_theme.css"
# web_include_css = "/assets/ridhosribumi/css/ridhosribumi.css"
# web_include_js = "/assets/ridhosribumi/js/ridhosribumi.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "ridhosribumi.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "ridhosribumi.install.before_install"
# after_install = "ridhosribumi.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ridhosribumi.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ridhosribumi.tasks.all"
# 	],
# 	"daily": [
# 		"ridhosribumi.tasks.daily"
# 	],
# 	"hourly": [
# 		"ridhosribumi.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ridhosribumi.tasks.weekly"
# 	]
# 	"monthly": [
# 		"ridhosribumi.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "ridhosribumi.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ridhosribumi.event.get_events"
# }
