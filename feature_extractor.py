import re
import socket
from urllib.parse import urlparse
import tldextract
import requests
from bs4 import BeautifulSoup
import whois
from datetime import datetime

class FeatureExtractor:
    def __init__(self, url):
        self.url = url
        self.domain = urlparse(url).netloc
        self.path = urlparse(url).path
        self.tld = tldextract.extract(url)
        
    def get_features(self):
        features = {}
        
        # 1. URL Length
        features['url_length'] = len(self.url)
        
        # 2. Having @ Symbol
        features['have_at'] = 1 if '@' in self.url else 0
        
        # 3. Double slash redirect
        features['double_slash_redirect'] = 1 if self.url.rfind('//') > 7 else 0
        
        # 4. Prefix/Suffix '-' in domain
        features['prefix_suffix'] = 1 if '-' in self.domain else 0
        
        # 5. Having Subdomain
        subdomains = self.tld.subdomain.split('.')
        features['sub_domain'] = len(subdomains) if subdomains[0] else 0
        
        # 6. HTTPS
        features['https'] = 1 if urlparse(self.url).scheme == 'https' else 0
        
        # 7. Domain Age (Simplified/Mocked if WHOIS fails)
        # features['domain_age'] = age # WHOIS is slow and unreliable for real-time
        features['domain_age'] = 0 # Placeholder for now
            
        # 8. Presence of IP address in URL
        ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
        features['have_ip'] = 1 if re.search(ip_pattern, self.url) else 0
        
        # 9. Shortener Service
        shorteners = ['bit.ly', 'goo.gl', 'shorte.st', 'go2l.ink', 'x.co', 'ow.ly', 't.co', 'tinyurl.com', 'tr.im', 'is.gd', 'cli.gs', 'yfrog.com', 'migre.me', 'ff.im', 'tiny.cc', 'url4.eu', 'twit.ac', 'su.pr', 'twurl.nl', 'snipurl.com', 'short.to', 'BudURL.com', 'ping.fm', 'post.ly', 'Just.as', 'bkite.com', 'snipr.com', 'fic.kr', 'loopt.us', 'doiop.com', 'short.ie', 'kl.am', 'wp.me', 'u.bb', 'om.ly', 'to.ly', 'bit.do', 't.ny.me', 'lnkd.in', 'db.tt', 'qr.ae', 'adf.ly', 'goo.gl', 'bitly.com', 'cur.lv', 'tinyurl.com', 'ow.ly', 'bit.ly', 'ity.im', 'q.gs', 'is.gd', 'po.st', 'bc.vc', 'twitthis.com', 'u.to', 'j.mp', 'buzurl.com', 'cutt.us', 'u.bb', 'yourls.org', 'x.co', 'prettylinkpro.com', 'scrnch.me', 'filoops.info', 'vzturl.com', 'qr.net', '1url.com', 'tweez.me', 'v.gd', 'tr.im', 'link.zip.net']
        features['short_url'] = 1 if any(s in self.url for s in shorteners) else 0
        
        return features

if __name__ == "__main__":
    extractor = FeatureExtractor("https://www.google.com")
    print(extractor.get_features())
