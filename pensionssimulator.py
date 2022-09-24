from turtle import pensize

#!/usr/local/bin/python
# coding: latin-1
import os, sys

print("Välkomna till denna pensionssimulator \nVad heter du i förnamn?")
name = input()
print("Hur gammal är du?")
age = int(input())
pension = 65 - age
print("Hej", name + ". Du går i pension om", pension, "år.\nPress any key to continue...")
go_on = input()