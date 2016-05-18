"""
salesperson assignment
"""

#salesperson's ID

salesperson = {'a':1, 'b':2, 'c':3, 'd':4}

# product number

productid = {'pa':1, 'pb':2, 'pc':3, 'pd':4, 'pe':5}

# product's amount

products = {
	'1': 100, '2':200, '3':50, '4':129, '5':100
}

# number of product sold

numprodsold = ''

sa = raw_input('input salesperson "a" number, productid and numprodsold at once. e.g 1 3 100\n')
ssa = sa.split()
sar = int(ssa[2]) * products[ssa[1]]

sb = raw_input('input salesperson "b" number, productid and numprodsold at once. e.g 1 3 100\n')
ssb = sb.split()
while ssb[1]==ssa[1] or int(ssb[1]) > 4:
	sb = raw_input('input salesperson "b" details again \n ensure product ID exist and has not been taken\n')
	ssb = sb.split()
sbr = int(ssb[2]) * products[ssb[1]]
sc = raw_input('input salesperson "c" number, productid and numprodsold at once. e.g 1 3 100\n')
ssc = sc.split()
while ssc[1]==ssa[1] or ssc[1]==ssb[1] or int(ssc[1]) > 4:
	sc = raw_input('input salesperson "c" details again \n ensure product ID exist and has not been taken\n')
	ssc = sc.split()
scr = int(ssc[2]) * products[ssc[1]]
sd = raw_input('input salesperson "d" number, productid and numprodsold at once. e.g 1 3 100\n')
ssd = sd.split()
while ssd[1]==ssa[1] or ssd[1]==ssb[1] or ssd[1]==ssc[1] or int(ssd[1]) > 4:
	sd = raw_input('input salesperson "d" details again \n ensure product ID exist and has not been taken\n')
	ssd = sd.split()
sdr = int(ssd[2]) * products[ssd[1]]

print "salesperson %d sold %d copies of item %s which equals %d" % (int(ssa[0]), int(ssa[2]), int(ssa[1]), sar)
print "salesperson %d sold %d copies of item %s which equals %d" % (int(ssb[0]), int(ssb[2]), int(ssb[1]), sbr)
print "salesperson %d sold %d copies of item %s which equals %d" % (int(ssc[0]), int(ssc[2]), int(ssc[1]), scr)
print "salesperson %d sold %d copies of item %s which equals %d" % (int(ssd[0]), int(ssd[2]), int(ssd[1]), sdr)

result = sar + sbr + scr + sdr


print "Total sales for the day is", result
