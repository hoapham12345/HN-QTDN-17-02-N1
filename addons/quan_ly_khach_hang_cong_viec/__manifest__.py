{
    'name': 'Quản lý Khách hàng & Công việc (BTL)',
    'version': '1.0',
    'category': 'Sales',
    'depends': ['base', 'nhan_su'],
    'data': [
        'security/ir.model.access.csv',
        'views/khach_hang_view.xml',
        'views/cong_viec_view.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}