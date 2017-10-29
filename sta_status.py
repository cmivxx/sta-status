#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests

class SpareTheAirStatus:

	def __init__(self):

		self.get_sta_status()

	def get_sta_status(self):
		URL = 'http://www.baaqmd.gov/Feeds/AlertRSS.aspx'

		try:
			r = requests.get( URL )
			soup = BeautifulSoup( r.text, 'html.parser' )
			status = soup.rss.channel.item.description.text
		except:
			status = False

		if status == 'No Alert':
			self.set_sta_status('0')
		elif status == 'Alert In Effect':
			self.set_sta_status('1')

	def set_sta_status(self, alert_stat):

		if alert_stat == '0':
			print('Q it up!')
		elif alert_stat == '1':
			print('No Q for you!')

if __name__ == '__main__':
	status = SpareTheAirStatus()