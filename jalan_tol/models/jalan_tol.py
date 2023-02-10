from odoo import models, fields, api

class JalanTol(models.Model):
    _name = "jalan.tol"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Jalan Tol"

    name_jalan = fields.Char(string="Nama Jalan Tol",required=True)
    lokasi = fields.Char(string="Lokasi",required=True)
    panjang = fields.Integer(string="Panjang (km)")
    lebar = fields.Integer(string="Lebar (m)")
    status = fields.Selection([("bisa_digunakan","Bisa Digunakan"),("perlu_diperbaiki","Perlu Diperbaiki"),("tidak_bisa_digunakan","Tidak Bisa Digunakan")], string="Status")
    kontraktor = fields.Selection([("pt_bangun_jaya","PT Bangun Jaya"),("pt_bangun_maju","PT Bangun Maju"),("pt_bangun_sejahtera","PT Bangun Sejahtera")], string="Kontraktor")