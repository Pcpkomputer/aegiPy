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

tautan = 'http://m.persamaankata.com/search.php?q=' + args.kata
halaman = urlopen(tautan)
soup = BeautifulSoup(halaman, 'html.parser')
thesaurus = soup.find( 'div', attrs={ 'class' : 'thesaurus_group' })
for nama in thesaurus:
    nama = thesaurus.find('h3')
    hasil_nama = nama.text.strip()
for hasil in thesaurus:
    hasil = thesaurus.find('ul')
    hasil_hasil = hasil.text.strip()
print('')
print(hasil_nama)
print('')
print(hasil_hasil)
print('')
