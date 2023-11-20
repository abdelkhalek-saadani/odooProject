from odoo import models, fields, api

class LibraryBook(models.Model):
    _name = "library.book"
    
    _description = "for book records"


    name = fields.Char(string = "Title", required = True)
    cover = fields.Binary()
    pages = fields.Integer(string="Number of pages")
    qte = fields.Integer(string="Available books", required = True)
    author_ids = fields.Many2many("library.author",
                                  string="Authors")
    authors = fields.Char(compute ="_compute_authors")
    price = fields.Integer(string= "Price",required=False, default=0)
    purchase_price = fields.Integer(string= "Cost")
    is_used = fields.Boolean(string="To get borrowed?",default="False", required= True)
    category_id = fields.Many2one("library.category", string="Category")
    active = fields.Boolean(default="True")

    def name_get(self):
        res=[]
        for rec in self:
            new_name = f'{rec.name} By {rec.authors} ({rec.pages}page)'
            res.append((rec.id,new_name))
        return res
    
    @api.depends("author_ids")
    def _compute_authors(self):
        for rec in self:
            rec.authors=""
            for author in rec.author_ids:
                rec.authors = author.name + ", " + rec.authors 
            rec.authors = rec.authors[:-2]
