#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Simple XML parser for the RSS channel from BarraPunto
# Jesus M. Gonzalez-Barahona
# jgb @ gsyc.es
# TSAI and SAT subjects (Universidad Rey Juan Carlos)
# September 2009
#
# Just prints the news (and urls) in BarraPunto.com,
#  after reading the corresponding RSS channel.

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import urllib

class myContentHandler(ContentHandler):

    def __init__ (self):
        self.inItem = False
        self.inContent = False
        self.theContent = ""
        self.htmlFile = open("index.html","w")
    def startElement (self, name, attrs):
        if name == 'item':
            self.inItem = True
        elif self.inItem:
            if name == 'title':
                self.inContent = True
            elif name == 'link':
                self.inContent = True

    def endElement (self, name):

        if name == 'item':
            self.inItem = False
        elif self.inItem:
            if name == 'title':
                line = "<li>Title: " + self.theContent + "."
                # To avoid Unicode trouble
                self.htmlFile.write(line.encode('utf-8'))
                self.inContent = False
                self.theContent = ""
            elif name == 'link':

                self.htmlFile.write( "<a href =" + self.theContent.encode('utf-8') + ">Link</a></li> <br/>")
                self.inContent = False
                self.theContent = ""
    def characters (self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars

# --- Main prog
#if len(sys.argv)<2:
#    print "Usage: python xml-parser-barrapunto.py <document>"
#    print
#    print " <document>: file name of the document to parse"
#    sys.exit(1)

# Load parser and driver

#theParser = make_parser()
#theHandler = myContentHandler()
#theParser.setContentHandler(theHandler)

#file = urllib2.urlopen( 'http://barrapunto.com/index.rss')
#theParser.parse(file)
#print "Parse complete"
# Ready, set, go!

#xmlFile = open(sys.argv[1],"r")
#file = urllib.urlopen( 'http://barrapunto.com/index.rss')
#theParser.parse(file)
