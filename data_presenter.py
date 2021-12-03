data = open("CupcakeInvoices.csv")

#for line in data:
#    print(line)

#for line in data:
#        cupcakes = line.split(',')
#        print(cupcakes[2])

#for line in data:
#    invoices = line.split(',')
#    total = int(invoices[3]) * float(invoices[4])
 #   print(total)

total = 0

for line in data:
    values = line.split(',')
    total = total + (int(values[3]) * float(values[4]))

print(total)
#data.close()