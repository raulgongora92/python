#Supongamos que quiere ofrecer un determinado descuento a los clientes si gastan más de $100. También proporcionará un descuento adicional si ese cliente forma parte de un programa de fidelización. Si el cliente no forma parte del programa de fidelización y no gastó más de $100, se aplica un cargo por servicio del 5 %.

cliente_fidelizado = False
total_factura = 120

if cliente_fidelizado and total_factura > 100:
    #give 20% discount
    total_factura = total_factura - (float(total_factura)/ 100) * 20
elif total_factura > 100:
    #give 10% discount
    total_factura = total_factura - (float(total_factura)/ 100) * 10
else:
    #sorry no discount, 5% service charge applied.
    total_factura = total_factura + (float(total_factura) / 100) * 5
    print('Sorry, no discount ...')

print('Total Factura: ', float(total_factura))

#El fragmento de código anterior primero verifica si el cliente forma parte del programa de fidelización y si está gastando más de $100. Si se cumplen ambas condiciones, se aplica un descuento del 20 % a la factura. La sentencia elif solo se ejecutará si no se cumple la primera condición if. El estado de cuenta elif solo verificará si la factura supera los $100 y si es así, aplicará un descuento del 10 % a la factura.

#La sentencia else final solo se ejecuta si no se cumple ninguna de las otras dos condiciones. En este caso, se aplica un cargo del 5 % a la factura.