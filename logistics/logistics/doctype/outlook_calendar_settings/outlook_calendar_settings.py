# Copyright (c) 2026, www.agilasoft.com and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

from logistics.integrations.outlook.install import create_connected_app
from logistics.integrations.outlook.utils import get_outlook_connected_app_name


class OutlookCalendarSettings(Document):
	def validate(self):
		self._ensure_connected_app()
		self._sync_connected_app_endpoints()

	# Ensure install doesn't fail during init_singles when the default
	# "Microsoft Outlook" Connected App has not been created yet. zz
	def _ensure_connected_app(self):
		if self.connected_app and frappe.db.exists("Connected App", self.connected_app):
			return

		existing = get_outlook_connected_app_name()
		if existing and frappe.db.exists("Connected App", existing):
			self.connected_app = existing
			return

		self.connected_app = create_connected_app()

	def _sync_connected_app_endpoints(self):
		connected_app_name = self.connected_app or get_outlook_connected_app_name()
		if not connected_app_name or not self.azure_tenant_id:
			return
		if not frappe.db.exists("Connected App", connected_app_name):
			return

		tenant = self.azure_tenant_id.strip()
		connected_app = frappe.get_doc("Connected App", connected_app_name)
		connected_app.authorization_uri = (
			f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize"
		)
		connected_app.token_uri = f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token"
		connected_app.save(ignore_permissions=True)
		
# import frappe
# from frappe.model.document import Document

# from logistics.integrations.outlook.utils import get_outlook_connected_app_name


# class OutlookCalendarSettings(Document):
# 	def validate(self):
# 		self._sync_connected_app_endpoints()

# 	def _sync_connected_app_endpoints(self):
# 		connected_app_name = self.connected_app or get_outlook_connected_app_name()
# 		if not connected_app_name or not self.azure_tenant_id:
# 			return
# 		if not frappe.db.exists("Connected App", connected_app_name):
# 			return

# 		tenant = self.azure_tenant_id.strip()
# 		connected_app = frappe.get_doc("Connected App", connected_app_name)
# 		connected_app.authorization_uri = (
# 			f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize"
# 		)
# 		connected_app.token_uri = f"https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token"
# 		connected_app.save(ignore_permissions=True)
