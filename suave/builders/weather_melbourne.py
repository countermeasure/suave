#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ftplib
import re

from urlparse import urlparse


def get_ftp_page(url):
    """
    Retrieves a page from an ftp server.
    Returns the page's contents as a list of its lines.
    """

    u = urlparse(url)
    ftp = ftplib.FTP(host=u.netloc, timeout=10)

    ftp.login()
    page = []
    ftp.retrlines('RETR %s' % u.path, page.append)
    ftp.quit()

    return page


def parse_temperature(temp_line):
    """Parses the temperature out of the line of text which contains it."""

    temp_regex = re.compile('>([-]?\d+)&deg;<')
    temperature = temp_regex.search(temp_line).group(1)

    return temperature


def parse_time(temp_line):
    """Parses the time out of the line of text which contains it."""

    time_regex = re.compile('<!--\s(\d{2}:\d{2}\s[ap]m)\sE[DS]T')
    time = time_regex.search(temp_line).group(1)

    return time


def parse_rainfall(rain_line):
    """Parses the rainfall out of the line of text which contains it."""

    rain_regex = re.compile('>(\d{1,3}\.\d\s)mm<')
    rainfall = rain_regex.search(rain_line).group(1)

    return rainfall


if __name__ == "__main__":
    # Get the raw data from the Bureau Of Meteorology.
    page = get_ftp_page('ftp://ftp2.bom.gov.au/anon/gen/fwo/IDA00101.html')

    # Check that this page contains the the data for Melbourne.
    header_regex = re.compile('Link to latest weather for Melbourne area')
    if header_regex.search(page[18]):
        print '\n  Melbourne weather\n'
        print '  Temperature:  %s°C (at %s)' % (
            parse_temperature(page[19]),
            parse_time(page[19])
        )
        print '  Rain:         %smm since 09:00' % parse_rainfall(page[20])
    else:
        print 'The data received couldn\'t be understood'
