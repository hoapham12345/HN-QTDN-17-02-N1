from odoo import models, fields

class KhachHang(models.Model):
    _name = 'khach_hang'
    _description = 'Quản lý thông tin Khách hàng'
    _rec_name = 'ten_khach_hang'

    ten_khach_hang = fields.Char(string="Tên khách hàng/Công ty", required=True)
    so_dien_thoai = fields.Char(string="Số điện thoại")
    email = fields.Char(string="Email")
    dia_chi = fields.Text(string="Địa chỉ")
    
    # Kéo dữ liệu từ module nhân sự sang để biết ai chăm sóc khách hàng này
    nhan_vien_phu_trach_id = fields.Many2one('nhan_vien', string="Nhân viên phụ trách")
    
    # Mối quan hệ 1-N: Một khách hàng có thể có nhiều công việc/lịch sử tương tác
    cong_viec_ids = fields.One2many('cong_viec', 'khach_hang_id', string="Lịch sử công việc")