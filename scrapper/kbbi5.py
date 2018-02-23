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

quote_page = 'https://kbbi.kemdikbud.go.id/entri/' + args.kata
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find( 'ol', attrs={ 'class' : '' })
name_box1 = soup.find( 'ul', attrs={ 'class' : 'adjusted-par' })
hasil1=name_box
hasil2=name_box1
#if hasil1 is not None:
#    hasil1 = name_box.text.strip()
#    print(hasil1)
if hasil1 is None:
    hasil2 = name_box1.text.strip()
    print('')
    print(hasil2)
    print('')
#if hasil2 is not None:
#    hasil2 = name_box1.text.strip()
#    print(hasil2)
if hasil2 is None:
    hasil1 = name_box.text.strip()
    print('')
    print(hasil1)
    print('')
if hasil1 and hasil2 is not None:
    hasil1 = name_box.text.strip()
    hasil2 = name_box1.text.strip()
    print('')
    print(hasil1)
    print('')
    print(hasil2)
    print('')
