#!/usr/bin/env python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-k",
                       "--kata",
                       dest="kata",
                       action="store",
                       default=None,
                        required=True,
                        help="Kata yang ingin dicari")
args = arg_parser.parse_args()

tautan = 'http://id.gegensatz-von.com/' + args.kata + '.html'
halaman = urlopen(tautan)
soup = BeautifulSoup(halaman, 'html.parser')
thesaurus = soup.find( 'div', attrs={ 'class' : 'infoblock_innerbox' })
hasil = thesaurus.text.strip()
print('')
print(hasil)
print('')
