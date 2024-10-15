{
    'name': 'Gravity Online Sale Discount',
    'version': '16.1.0',
    'category': '',
    'summary': 'This module is used  to add the discount feature for online sale ',
    'author': 'Anand/Gravity',
    'sequence': 1,
    "website":'',
    'description': """
   This module is used to add the discount feature in e_commerce sale. 
        """,
    'depends': ['product','sale','website_sale','sales_team'],
    'data': ['views/product_template_discount_view.xml',
             'views/website_templates_inherit_view.xml'
             ],
    'images': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {
    },
}
