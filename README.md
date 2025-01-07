# Pregunta 1: 
Agregar al listado de clientes una columna con el campo “Idioma” de contacto (módulo point_of_sale)


    Se realizo la insección del campo al modelo en el archivo point_sale.py, mientras la vista esta en la views.xml

# Pregunta 4: 
Crear un módulo que agregue un código QR al impreso de la factura por defecto (módulo account). La imagen correspondiente debe ser un campo en el modelo account.move El código QR debe estar formado los siguiente campos separados del caracter “|”. Número factura + “|” + Nombre Cliente + “|” + Fecha Factura + “|” + [TOTAL CANTIDADES DE LÍNEA] + “|” + Total a pagar ////    [TOTAL CANTIDADES DE LÍNEA] = Sumatoria de las cantidades de cada línea el cual debería ser un campo “compute”

    En el archivo account.py de models se encuetra la creación de los campos y cálculo.


# Pregunta: 5
Agregar dos campos a la factura (módulo account):
Número de serie y número correlativo. El número de serie se debe formar a partir del campo
“Number” (Ejemplo FV/2019/001)
Número de serie: FV2019
Número correlativo: 00000001

    En el archivo account.py se encuentra el cálculo de número de serie para la secuencia se utiliza el template ./data/sequences.xml.


# Pregunta: 6
Agregar un campo Canal de ventas, colocarlo debajo del campo Vendedor. (módulo account) este campo debe pertenecer a un nuevo modelo cuya data debe ser cargada cuando se instala el módulo.

    Se creaa un modelo de "sales.channel" y déspues agregamos la data predeterminada mediante el template ./data/sales_channel.xml

# Pregunta: 7
Ocultar el campo Fecha de la factura y reemplazarlo por Fecha de emisión, este nuevo campo no solo debe tener la fecha sino también la hora. (módulo account)

    Para este caso, heredamos la vista account.view_move_form y ocultamos el campo invoice_date y luego añadimos el campo date_issue del archivo account.py.