from odoo import models, fields, api
import requests
import json

class CongViec(models.Model):
    _name = 'cong_viec'
    _description = 'Quản lý Công việc và Tương tác'
    _rec_name = 'tieu_de'

    tieu_de = fields.Char(string="Tiêu đề công việc", required=True)
    mo_ta = fields.Text(string="Mô tả chi tiết")
    
    # Đây chính là trường dữ liệu đang bị thiếu gây ra lỗi
    khach_hang_id = fields.Many2one('khach_hang', string="Khách hàng liên quan", required=True)
    nhan_vien_thuc_hien_id = fields.Many2one('nhan_vien', string="Người thực hiện")
    han_chot = fields.Date(string="Hạn chót (Deadline)")
    trang_thai = fields.Selection([
        ('moi', 'Mới tạo'),
        ('dang_lam', 'Đang xử lý'),
        ('hoan_thanh', 'Hoàn thành'),
        ('huy', 'Hủy bỏ')
    ], string="Trạng thái", default='moi')
    
    noi_dung_ai_soan = fields.Text(string="Nội dung AI gợi ý")

    def action_tao_noi_dung_ai(self):
        for rec in self:
            ten_kh = rec.khach_hang_id.ten_khach_hang if rec.khach_hang_id else "Khách hàng"
            yeu_cau = rec.mo_ta or rec.tieu_de
            
            prompt = f"Hãy đóng vai một nhân viên sale chuyên nghiệp. Viết một email hoặc kịch bản chăm sóc khách hàng thật ngắn gọn, lịch sự gửi cho khách hàng tên '{ten_kh}'. Yêu cầu công việc là: {yeu_cau}."
            
            # --- BẠN NHỚ DÁN LẠI API KEY VÀO DÒNG DƯỚI NÀY NHÉ ---
            api_key = ""
            
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-lite:generateContent?key={api_key}"
            headers = {'Content-Type': 'application/json'}
            data = {
                "contents": [{"parts": [{"text": prompt}]}]
            }
            
            try:
                response = requests.post(url, headers=headers, json=data)
                if response.status_code == 200:
                    result = response.json()
                    generated_text = result['candidates'][0]['content']['parts'][0]['text']
                    rec.noi_dung_ai_soan = generated_text
                else:
                    rec.noi_dung_ai_soan = f"Lỗi gọi API. Mã lỗi: {response.status_code}\nChi tiết: {response.text}"
            except Exception as e:
                rec.noi_dung_ai_soan = f"Hệ thống không thể kết nối tới AI: {str(e)}"from odoo import models, fields, api
import requests
import json

class CongViec(models.Model):
    _name = 'cong_viec'
    _description = 'Quản lý Công việc và Tương tác'
    _rec_name = 'tieu_de'

    tieu_de = fields.Char(string="Tiêu đề công việc", required=True)
    mo_ta = fields.Text(string="Mô tả chi tiết")
    
    # Đây chính là trường dữ liệu đang bị thiếu gây ra lỗi
    khach_hang_id = fields.Many2one('khach_hang', string="Khách hàng liên quan", required=True)
    nhan_vien_thuc_hien_id = fields.Many2one('nhan_vien', string="Người thực hiện")
    han_chot = fields.Date(string="Hạn chót (Deadline)")
    trang_thai = fields.Selection([
        ('moi', 'Mới tạo'),
        ('dang_lam', 'Đang xử lý'),
        ('hoan_thanh', 'Hoàn thành'),
        ('huy', 'Hủy bỏ')
    ], string="Trạng thái", default='moi')
    
    noi_dung_ai_soan = fields.Text(string="Nội dung AI gợi ý")

    def action_tao_noi_dung_ai(self):
        for rec in self:
            ten_kh = rec.khach_hang_id.ten_khach_hang if rec.khach_hang_id else "Khách hàng"
            yeu_cau = rec.mo_ta or rec.tieu_de
            
            prompt = f"Hãy đóng vai một nhân viên sale chuyên nghiệp. Viết một email hoặc kịch bản chăm sóc khách hàng thật ngắn gọn, lịch sự gửi cho khách hàng tên '{ten_kh}'. Yêu cầu công việc là: {yeu_cau}."
            
            # --- BẠN NHỚ DÁN LẠI API KEY VÀO DÒNG DƯỚI NÀY NHÉ ---
            api_key = "AQ.Ab8RN6LmedMZklW399Iq9i8g2S2814f4YcJgCxy94YB2W_Ml5Q"
            
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-lite:generateContent?key={api_key}"
            headers = {'Content-Type': 'application/json'}
            data = {
                "contents": [{"parts": [{"text": prompt}]}]
            }
            
            try:
                response = requests.post(url, headers=headers, json=data)
                if response.status_code == 200:
                    result = response.json()
                    generated_text = result['candidates'][0]['content']['parts'][0]['text']
                    rec.noi_dung_ai_soan = generated_text
                else:
                    rec.noi_dung_ai_soan = f"Lỗi gọi API. Mã lỗi: {response.status_code}\nChi tiết: {response.text}"
            except Exception as e:
                rec.noi_dung_ai_soan = f"Hệ thống không thể kết nối tới AI: {str(e)}"from odoo import models, fields, api
import requests
import json

class CongViec(models.Model):
    _name = 'cong_viec'
    _description = 'Quản lý Công việc và Tương tác'
    _rec_name = 'tieu_de'

    tieu_de = fields.Char(string="Tiêu đề công việc", required=True)
    mo_ta = fields.Text(string="Mô tả chi tiết")
    
    # Đây chính là trường dữ liệu đang bị thiếu gây ra lỗi
    khach_hang_id = fields.Many2one('khach_hang', string="Khách hàng liên quan", required=True)
    nhan_vien_thuc_hien_id = fields.Many2one('nhan_vien', string="Người thực hiện")
    han_chot = fields.Date(string="Hạn chót (Deadline)")
    trang_thai = fields.Selection([
        ('moi', 'Mới tạo'),
        ('dang_lam', 'Đang xử lý'),
        ('hoan_thanh', 'Hoàn thành'),
        ('huy', 'Hủy bỏ')
    ], string="Trạng thái", default='moi')
    
    noi_dung_ai_soan = fields.Text(string="Nội dung AI gợi ý")

    def action_tao_noi_dung_ai(self):
        for rec in self:
            ten_kh = rec.khach_hang_id.ten_khach_hang if rec.khach_hang_id else "Khách hàng"
            yeu_cau = rec.mo_ta or rec.tieu_de
            
            prompt = f"Hãy đóng vai một nhân viên sale chuyên nghiệp. Viết một email hoặc kịch bản chăm sóc khách hàng thật ngắn gọn, lịch sự gửi cho khách hàng tên '{ten_kh}'. Yêu cầu công việc là: {yeu_cau}."
            
            # --- BẠN NHỚ DÁN LẠI API KEY VÀO DÒNG DƯỚI NÀY NHÉ ---
            #api_key = "AQ.Ab8RN6LmedMZklW399Iq9i8g2S2814f4YcJgCxy94YB2W_Ml5Q"
            
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-lite:generateContent?key={api_key}"
            headers = {'Content-Type': 'application/json'}
            data = {
                "contents": [{"parts": [{"text": prompt}]}]
            }
            
            try:
                response = requests.post(url, headers=headers, json=data)
                if response.status_code == 200:
                    result = response.json()
                    generated_text = result['candidates'][0]['content']['parts'][0]['text']
                    rec.noi_dung_ai_soan = generated_text
                else:
                    rec.noi_dung_ai_soan = f"Lỗi gọi API. Mã lỗi: {response.status_code}\nChi tiết: {response.text}"
            except Exception as e:
                rec.noi_dung_ai_soan = f"Hệ thống không thể kết nối tới AI: {str(e)}"from odoo import models, fields, api
import requests
import json

class CongViec(models.Model):
    _name = 'cong_viec'
    _description = 'Quản lý Công việc và Tương tác'
    _rec_name = 'tieu_de'

    tieu_de = fields.Char(string="Tiêu đề công việc", required=True)
    mo_ta = fields.Text(string="Mô tả chi tiết")
    
    # Đây chính là trường dữ liệu đang bị thiếu gây ra lỗi
    khach_hang_id = fields.Many2one('khach_hang', string="Khách hàng liên quan", required=True)
    nhan_vien_thuc_hien_id = fields.Many2one('nhan_vien', string="Người thực hiện")
    han_chot = fields.Date(string="Hạn chót (Deadline)")
    trang_thai = fields.Selection([
        ('moi', 'Mới tạo'),
        ('dang_lam', 'Đang xử lý'),
        ('hoan_thanh', 'Hoàn thành'),
        ('huy', 'Hủy bỏ')
    ], string="Trạng thái", default='moi')
    
    noi_dung_ai_soan = fields.Text(string="Nội dung AI gợi ý")

    def action_tao_noi_dung_ai(self):
        for rec in self:
            ten_kh = rec.khach_hang_id.ten_khach_hang if rec.khach_hang_id else "Khách hàng"
            yeu_cau = rec.mo_ta or rec.tieu_de
            
            prompt = f"Hãy đóng vai một nhân viên sale chuyên nghiệp. Viết một email hoặc kịch bản chăm sóc khách hàng thật ngắn gọn, lịch sự gửi cho khách hàng tên '{ten_kh}'. Yêu cầu công việc là: {yeu_cau}."
            
            # --- BẠN NHỚ DÁN LẠI API KEY VÀO DÒNG DƯỚI NÀY NHÉ ---
            api_key = "AQ.Ab8RN6LmedMZklW399Iq9i8g2S2814f4YcJgCxy94YB2W_Ml5Q"
            
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-lite:generateContent?key={api_key}"
            headers = {'Content-Type': 'application/json'}
            data = {
                "contents": [{"parts": [{"text": prompt}]}]
            }
            
            try:
                response = requests.post(url, headers=headers, json=data)
                if response.status_code == 200:
                    result = response.json()
                    generated_text = result['candidates'][0]['content']['parts'][0]['text']
                    rec.noi_dung_ai_soan = generated_text
                else:
                    rec.noi_dung_ai_soan = f"Lỗi gọi API. Mã lỗi: {response.status_code}\nChi tiết: {response.text}"
            except Exception as e:
                rec.noi_dung_ai_soan = f"Hệ thống không thể kết nối tới AI: {str(e)}"from odoo import models, fields, api
import requests
import json

class CongViec(models.Model):
    _name = 'cong_viec'
    _description = 'Quản lý Công việc và Tương tác'
    _rec_name = 'tieu_de'

    tieu_de = fields.Char(string="Tiêu đề công việc", required=True)
    mo_ta = fields.Text(string="Mô tả chi tiết")
    
    # Đây chính là trường dữ liệu đang bị thiếu gây ra lỗi
    khach_hang_id = fields.Many2one('khach_hang', string="Khách hàng liên quan", required=True)
    nhan_vien_thuc_hien_id = fields.Many2one('nhan_vien', string="Người thực hiện")
    han_chot = fields.Date(string="Hạn chót (Deadline)")
    trang_thai = fields.Selection([
        ('moi', 'Mới tạo'),
        ('dang_lam', 'Đang xử lý'),
        ('hoan_thanh', 'Hoàn thành'),
        ('huy', 'Hủy bỏ')
    ], string="Trạng thái", default='moi')
    
    noi_dung_ai_soan = fields.Text(string="Nội dung AI gợi ý")

    def action_tao_noi_dung_ai(self):
        for rec in self:
            ten_kh = rec.khach_hang_id.ten_khach_hang if rec.khach_hang_id else "Khách hàng"
            yeu_cau = rec.mo_ta or rec.tieu_de
            
            prompt = f"Hãy đóng vai một nhân viên sale chuyên nghiệp. Viết một email hoặc kịch bản chăm sóc khách hàng thật ngắn gọn, lịch sự gửi cho khách hàng tên '{ten_kh}'. Yêu cầu công việc là: {yeu_cau}."
            
            # --- BẠN NHỚ DÁN LẠI API KEY VÀO DÒNG DƯỚI NÀY NHÉ ---
            #api_key = ""
            
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-lite:generateContent?key={api_key}"
            headers = {'Content-Type': 'application/json'}
            data = {
                "contents": [{"parts": [{"text": prompt}]}]
            }
            
            try:
                response = requests.post(url, headers=headers, json=data)
                if response.status_code == 200:
                    result = response.json()
                    generated_text = result['candidates'][0]['content']['parts'][0]['text']
                    rec.noi_dung_ai_soan = generated_text
                else:
                    rec.noi_dung_ai_soan = f"Lỗi gọi API. Mã lỗi: {response.status_code}\nChi tiết: {response.text}"
            except Exception as e:
                rec.noi_dung_ai_soan = f"Hệ thống không thể kết nối tới AI: {str(e)}"from odoo import models, fields, api
import requests
import json

class CongViec(models.Model):
    _name = 'cong_viec'
    _description = 'Quản lý Công việc và Tương tác'
    _rec_name = 'tieu_de'

    tieu_de = fields.Char(string="Tiêu đề công việc", required=True)
    mo_ta = fields.Text(string="Mô tả chi tiết")
    
    # Đây chính là trường dữ liệu đang bị thiếu gây ra lỗi
    khach_hang_id = fields.Many2one('khach_hang', string="Khách hàng liên quan", required=True)
    nhan_vien_thuc_hien_id = fields.Many2one('nhan_vien', string="Người thực hiện")
    han_chot = fields.Date(string="Hạn chót (Deadline)")
    trang_thai = fields.Selection([
        ('moi', 'Mới tạo'),
        ('dang_lam', 'Đang xử lý'),
        ('hoan_thanh', 'Hoàn thành'),
        ('huy', 'Hủy bỏ')
    ], string="Trạng thái", default='moi')
    
    noi_dung_ai_soan = fields.Text(string="Nội dung AI gợi ý")

    def action_tao_noi_dung_ai(self):
        for rec in self:
            ten_kh = rec.khach_hang_id.ten_khach_hang if rec.khach_hang_id else "Khách hàng"
            yeu_cau = rec.mo_ta or rec.tieu_de
            
            prompt = f"Hãy đóng vai một nhân viên sale chuyên nghiệp. Viết một email hoặc kịch bản chăm sóc khách hàng thật ngắn gọn, lịch sự gửi cho khách hàng tên '{ten_kh}'. Yêu cầu công việc là: {yeu_cau}."
            
            # --- BẠN NHỚ DÁN LẠI API KEY VÀO DÒNG DƯỚI NÀY NHÉ ---
            api_key = "AQ.Ab8RN6LmedMZklW399Iq9i8g2S2814f4YcJgCxy94YB2W_Ml5Q"
            
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-lite:generateContent?key={api_key}"
            headers = {'Content-Type': 'application/json'}
            data = {
                "contents": [{"parts": [{"text": prompt}]}]
            }
            
            try:
                response = requests.post(url, headers=headers, json=data)
                if response.status_code == 200:
                    result = response.json()
                    generated_text = result['candidates'][0]['content']['parts'][0]['text']
                    rec.noi_dung_ai_soan = generated_text
                else:
                    rec.noi_dung_ai_soan = f"Lỗi gọi API. Mã lỗi: {response.status_code}\nChi tiết: {response.text}"
            except Exception as e:
                rec.noi_dung_ai_soan = f"Hệ thống không thể kết nối tới AI: {str(e)}"from odoo import models, fields, api
import requests
import json

class CongViec(models.Model):
    _name = 'cong_viec'
    _description = 'Quản lý Công việc và Tương tác'
    _rec_name = 'tieu_de'

    tieu_de = fields.Char(string="Tiêu đề công việc", required=True)
    mo_ta = fields.Text(string="Mô tả chi tiết")
    
    # Đây chính là trường dữ liệu đang bị thiếu gây ra lỗi
    khach_hang_id = fields.Many2one('khach_hang', string="Khách hàng liên quan", required=True)
    nhan_vien_thuc_hien_id = fields.Many2one('nhan_vien', string="Người thực hiện")
    han_chot = fields.Date(string="Hạn chót (Deadline)")
    trang_thai = fields.Selection([
        ('moi', 'Mới tạo'),
        ('dang_lam', 'Đang xử lý'),
        ('hoan_thanh', 'Hoàn thành'),
        ('huy', 'Hủy bỏ')
    ], string="Trạng thái", default='moi')
    
    noi_dung_ai_soan = fields.Text(string="Nội dung AI gợi ý")

    def action_tao_noi_dung_ai(self):
        for rec in self:
            ten_kh = rec.khach_hang_id.ten_khach_hang if rec.khach_hang_id else "Khách hàng"
            yeu_cau = rec.mo_ta or rec.tieu_de
            
            prompt = f"Hãy đóng vai một nhân viên sale chuyên nghiệp. Viết một email hoặc kịch bản chăm sóc khách hàng thật ngắn gọn, lịch sự gửi cho khách hàng tên '{ten_kh}'. Yêu cầu công việc là: {yeu_cau}."
            
            # --- BẠN NHỚ DÁN LẠI API KEY VÀO DÒNG DƯỚI NÀY NHÉ ---
            #api_key = "AQ.Ab8RN6LmedMZklW399Iq9i8g2S2814f4YcJgCxy94YB2W_Ml5Q"
            
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-lite:generateContent?key={api_key}"
            headers = {'Content-Type': 'application/json'}
            data = {
                "contents": [{"parts": [{"text": prompt}]}]
            }
            
            try:
                response = requests.post(url, headers=headers, json=data)
                if response.status_code == 200:
                    result = response.json()
                    generated_text = result['candidates'][0]['content']['parts'][0]['text']
                    rec.noi_dung_ai_soan = generated_text
                else:
                    rec.noi_dung_ai_soan = f"Lỗi gọi API. Mã lỗi: {response.status_code}\nChi tiết: {response.text}"
            except Exception as e:
                rec.noi_dung_ai_soan = f"Hệ thống không thể kết nối tới AI: {str(e)}"from odoo import models, fields, api
import requests
import json

class CongViec(models.Model):
    _name = 'cong_viec'
    _description = 'Quản lý Công việc và Tương tác'
    _rec_name = 'tieu_de'

    tieu_de = fields.Char(string="Tiêu đề công việc", required=True)
    mo_ta = fields.Text(string="Mô tả chi tiết")
    
    # Đây chính là trường dữ liệu đang bị thiếu gây ra lỗi
    khach_hang_id = fields.Many2one('khach_hang', string="Khách hàng liên quan", required=True)
    nhan_vien_thuc_hien_id = fields.Many2one('nhan_vien', string="Người thực hiện")
    han_chot = fields.Date(string="Hạn chót (Deadline)")
    trang_thai = fields.Selection([
        ('moi', 'Mới tạo'),
        ('dang_lam', 'Đang xử lý'),
        ('hoan_thanh', 'Hoàn thành'),
        ('huy', 'Hủy bỏ')
    ], string="Trạng thái", default='moi')
    
    noi_dung_ai_soan = fields.Text(string="Nội dung AI gợi ý")

    def action_tao_noi_dung_ai(self):
        for rec in self:
            ten_kh = rec.khach_hang_id.ten_khach_hang if rec.khach_hang_id else "Khách hàng"
            yeu_cau = rec.mo_ta or rec.tieu_de
            
            prompt = f"Hãy đóng vai một nhân viên sale chuyên nghiệp. Viết một email hoặc kịch bản chăm sóc khách hàng thật ngắn gọn, lịch sự gửi cho khách hàng tên '{ten_kh}'. Yêu cầu công việc là: {yeu_cau}."
            
            # --- BẠN NHỚ DÁN LẠI API KEY VÀO DÒNG DƯỚI NÀY NHÉ ---
            api_key = "AQ.Ab8RN6LmedMZklW399Iq9i8g2S2814f4YcJgCxy94YB2W_Ml5Q"
            
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-3.1-flash-lite:generateContent?key={api_key}"
            headers = {'Content-Type': 'application/json'}
            data = {
                "contents": [{"parts": [{"text": prompt}]}]
            }
            
            try:
                response = requests.post(url, headers=headers, json=data)
                if response.status_code == 200:
                    result = response.json()
                    generated_text = result['candidates'][0]['content']['parts'][0]['text']
                    rec.noi_dung_ai_soan = generated_text
                else:
                    rec.noi_dung_ai_soan = f"Lỗi gọi API. Mã lỗi: {response.status_code}\nChi tiết: {response.text}"
            except Exception as e:
                rec.noi_dung_ai_soan = f"Hệ thống không thể kết nối tới AI: {str(e)}"