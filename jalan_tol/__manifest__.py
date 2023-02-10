#yang boleh diganti name dan data 
{
    'name' : 'Jalan Tol',
    'version' : '1.0',
    'summary':'Modul ini merupakan modul yang dapat menghitung biaya jalan tol',
    'sequence':1,
    'description':""" Kalkulasi Jalan Tol """,
    'category':'Productivity',
    'website':'',
    'license': 'LGPL-3',
    'depends':['mail'],#untuk modul yang di butuhkan
    'data':[ 
        'views/jalan_tol.xml',
        'views/menu.xml',
        'security/ir.model.access.csv'
    ],#untuk xml
    'demo':[], #untuk data demo
    'qweb':[],
    'installable':True, #untuk bisa di install
    'application':True ,#untuk bisa di buka
    'auto_install':False, #untuk bisa di install otomatis
}