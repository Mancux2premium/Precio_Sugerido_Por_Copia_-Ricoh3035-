### Precio de los insumos de la Ricoh 3035 ###
resma = 65999 
toner = 27000 
unidad_de_imagen = 70620 
cuchilla_de_transferencia = 29188 
fusor = 38520 
rodillo_precion = 34700 

### Rendimiento de los insumos de la Ricoh 3035 ###
resma_rendimiento = 5000
toner_rendimiento = 17000
unidad_de_imagen_rendimiento = 18000
cuchilla_de_transferencia_rendimiento = 25000
fusor_rendimiento = 60000
rodillo_precion_rendimiento = 60000

### Calculo de los costos de impresion ### 
precio_recomendado = (resma// resma_rendimiento) + (toner // toner_rendimiento)  + (unidad_de_imagen//unidad_de_imagen_rendimiento) +(cuchilla_de_transferencia//cuchilla_de_transferencia_rendimiento) + (fusor//fusor_rendimiento + (rodillo_precion//rodillo_precion_rendimiento) )

### Muestra el mensaje del costo total mas el precio recomendado de por  copia ###
print( "El costo de copia es:",precio_recomendado, "\n" "Precio recomendado:", precio_recomendado*2)

print("### ### ### ### ### ### ")

### Muestra el rendimiento de los insumos de la fototocopiadora Ricoh 3035 ###
print("Rendimiento toner:",toner_rendimiento,"\n""Rendimiento unidad de imagen:", unidad_de_imagen_rendimiento,"\n""Rendimiento cuchilla de transferencia:", cuchilla_de_transferencia_rendimiento,"\n""Rendimiento fusor:",fusor_rendimiento,"\n""Rendimiento rodillo de presion:", rodillo_precion_rendimiento)