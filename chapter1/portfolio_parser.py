#!/usr/bin/env python

portfolio = []
for line in open('portfolio.csv'):
  if not line[0] == '#':
    name, shares, price = line.rstrip().split(',')
    portfolio.append((name, int(shares), float(price)))

print portfolio

# calculate the total
total = 0.0

for name, shares, price in portfolio:
  total += shares * price

print "total is", total
