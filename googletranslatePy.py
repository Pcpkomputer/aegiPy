#!/usr/bin/env python3
from textblob import TextBlob
import argparse
import re

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-m",
                        "--masukan",
                        dest="masukan",
                        action="store",
                        default=None,
                        required=True,
                        help="File ASS")
args = arg_parser.parse_args()
        
regex_dialog = re.compile(r"(?:Dialogue.*\d+,\d+,\d+,(?:\w*\s*)*,)(?:{.*})*(.+)")
regex_komen = re.compile(r"{.*}")
regex_enter = re.compile(r"(\w)?\\N(\w)?")
nama_keluaran = "id_" + args.masukan
with open(args.masukan, "r", encoding="utf-8") as bokong:
    keluaran = open(nama_keluaran, "w", encoding="utf-8")
    print("Proses menerjemahkan ....")
    for line in bokong:
        if not regex_dialog.match(line):
            keluaran.write(line)
        for dialog in regex_dialog.findall(line):
            ohboi = re.sub(regex_komen, "", dialog)
            ohboi = re.sub(regex_enter, r"\1 \2", ohboi)
            blob = TextBlob(ohboi)
            try:
                blob = blob.translate(to="id")
                print("[" + str(ohboi) + "]" + " [" + str(blob) + "]")
            except:
                pass
            hasil = line.replace(dialog, str(blob))
            keluaran.write(hasil)
keluaran.close()
