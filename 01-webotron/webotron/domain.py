# -*- coding: utf-8 -*-

"""Classes for Route 53."""

class DomainManager:
	"""Manage for Route 53."""

	def __init__(self, session):
		"""Create DomainManager object."""
		self.session = session
