#!/usr/bin/env python

import gtk
# from gi.repository import GObject as gobject

from bs4 import BeautifulSoup

import signal, os
import thread
import requests

class SpareTheAirIndicator:

	def __init__(self, indicator_id='staappindicator'):
		icon = gtk.status_icon_new_from_file('icons/sta-init_alert.png')
		icon.connect('popup-menu', on_right_click)
		icon.connect('activate', on_left_click)

		self.update_server_status_icon()

		gtk.main()

	def set_icon(self, icon_path):
		self.icon = os.path.dirname(os.path.realpath(__file__)) + '/' + icon_path

	def update_server_status_icon(self):
		URL = 'http://www.baaqmd.gov/Feeds/AlertRSS.aspx'

		try:
			r = requests.get( URL )
			soup = BeautifulSoup( r.text, 'html.parser' )
			status = soup.rss.channel.item.description.text
		except:
			status = False

		if status == 'No Alert':
			self.set_icon( 'icons/sta-no_alert.png' )
		elif status == 'Unstable!':
			self.set_icon( 'icons/sta-error_alert.png' )
		elif status == 'Alert In Effect':
			self.set_icon( 'icons/sta-active_alert.png' )

		self.change_app_icon()

	def change_app_icon(self):
		self.gtk.status_icon_new_from_file( self.get_icon() )
		#gobject.timeout_add_seconds( 60, self.update_server_status_icon )
		print("Add timeout here")

	def message(data=None):
		"Function to display messages to the user."
	  
		msg=gtk.MessageDialog(None, gtk.DIALOG_MODAL,
			gtk.MESSAGE_INFO, gtk.BUTTONS_OK, data)
		msg.run()
		msg.destroy()
	 
	def open_app(data=None):
		message(data)
	 
	def close_app(data=None):
		message(data)
		gtk.main_quit()
	 
	def make_menu(event_button, event_time, data=None):
		menu = gtk.Menu()
		open_item = gtk.MenuItem("Open App")
		close_item = gtk.MenuItem("Close App")
	  
		#Append the menu items  
		menu.append(open_item)
		menu.append(close_item)
		#add callbacks
		open_item.connect_object("activate", open_app, "Open App")
		close_item.connect_object("activate", close_app, "Close App")
		#Show the menu items
		open_item.show()
		close_item.show()
	  
		#Popup the menu
		menu.popup(None, None, None, event_button, event_time)
	 
	def on_right_click(data, event_button, event_time):
		make_menu(event_button, event_time)
	 
	def on_left_click(event):
		message("Status Icon Left Clicked")
 
if __name__ == '__main__':
	ap = SpareTheAirIndicator('sparetheairindicator')