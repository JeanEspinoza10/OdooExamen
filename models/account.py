from odoo import api, fields, models
import io  # Para manejar datos binarios en memoria con BytesIO
import base64  # Para codificar la imagen del QR en formato Base64
import qrcode  # Para generar el código QR

class Account(models.Model):
    _inherit = 'account.move'

    code_qr_new = fields.Binary(string='QR Code', compute='_generate_qr_code', store=True)
    total_quantity = fields.Integer(string='Total Quantity', compute='get_total_quantity', store=True)

    #add serial number and correlative
    serial_number = fields.Char(string='Serial Number', compute='get_serial_number', store=True)
    correlative = fields.Char(string='Correlative')

    ## Add sales channerl
    sales_channel_id = fields.Many2one('sales.channel', string='Sales Channel')

    # Add new field date_issue
    date_issue = fields.Datetime(string='Date Issue')


    @api.depends('name')
    def get_serial_number(self):
        for record in self:
            record.serial_number = record.name.replace("/", "")

    def create(self, vals_list):
            sequence_obj = self.env['ir.sequence']
            correlative = sequence_obj.next_by_code('model.sequence')  
            vals_list['correlative'] = correlative

            # Llamar al método original para crear el registro
            return super(Account, self).create(vals_list)

    @api.depends('line_ids')
    def get_total_quantity(self):
        for record in self:
            record.total_quantity = sum(line.quantity for line in record.invoice_line_ids)

    @api.depends('name', 'partner_id', 'invoice_date', 'total_quantity', 'amount_total')
    def _generate_qr_code(self):
        for record in self:
            qr_string = "|".join([
                str(record.name or ''),
                str(record.partner_id.display_name or ''),
                str(record.invoice_date or ''),
                str(record.total_quantity or 0),
                str(record.amount_total or 0.0)
            ])

            qr = qrcode.QRCode(version=4, box_size=4, border=1)
            qr.add_data(qr_string)
            qr.make(fit=True)
            img = qr.make_image()

            buffer = io.BytesIO()
            img.save(buffer)
            img_str = base64.b64encode(buffer.getvalue())

            # Guardamos la imagen en el campo binario
            record.code_qr_new = img_str