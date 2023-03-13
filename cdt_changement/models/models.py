# -*- coding: utf-8 -*-


from email.policy import default
from unicodedata import name
from unittest import result
from odoo import models, fields, api, _

class PartiePrenante(models.Model):
    _name = 'cdt.partieprenante'    
    _description = 'Partie prenante'

    Id = fields.Char(String='ID', readonly=True, required=True, copy=False , default=lambda self: _('Nouveau'))
    name = fields.Many2one('res.users',
        ondelete='cascade', string="Nom", required=True)
    projet = fields.Many2one('project.project',
        ondelete='cascade', string="Projet", required=True)
    type = fields.Selection([('a', 'interne'), ('b', 'externe')], string="Type")
    role = fields.Char(string="Rôle", required=True)
    interet = fields.Selection([('a', 'Faible'), ('b', 'Élevé')], string="Intérêt")
    pouvoir = fields.Selection([('a', 'Faible'), ('b', 'Élevé')], string="Pouvoir")
    strategie = fields.Selection([('a', 'Effort minimal'), ('b', 'Garder satisfait'),('c', 'Garder informé'),('d', 'Acteur clé')], readonly=True, string="Stratégie")
    contribution = fields.Char(string="Contribution", required=False)
    attentes = fields.Char(string="Attentes", required=False)
    action = fields.Text(string="Actions", required=False)
    contact = fields.Text(string="Contact", required=False)
    state = fields.Selection([
        ('i', 'Inconscient'),
        ('r', 'Resistant'),
        ('n', 'Neutre'),
        ('s', 'Supporteur'),
        ('l', 'Leader')

    ],string="Status", default='i')
    def action_Resistant(self):
        self.state = "r"
    def action_Neutre(self):
        self.state = "n"
    def action_Supporteur(self):
        self.state = "s"
    def action_Leader(self):
        self.state = "l"

    @api.model
    def create(self, vals):
        if vals.get('Id' , _('Nouveau')) == _('Nouveau') :
           vals['Id'] = self.env['ir.sequence'].next_by_code('cdt.partieprenante') or _('Nouveau')
        result = super(PartiePrenante, self).create(vals)
        return result

    @api.onchange('pouvoir','interet')
    def Onchange_strategie(self):
            if self.pouvoir == 'a' and self.interet == 'a' :
                self.strategie = 'a'
            if self.pouvoir == 'b' and self.interet == 'a' :
                self.strategie = 'b'
            if self.pouvoir == 'a' and self.interet == 'b' :
                self.strategie = 'c'
            if self.pouvoir == 'b' and self.interet == 'b' :
                self.strategie = 'd'	

   
    
   


class Risque(models.Model):
    _name = "cdt.risque"
    _description = "Risque"

    id = fields.Char("ID", readonly=True, required=True, copy=False , default='Nouveau')
    name = fields.Text(string="Contenu", required=True)
    projet = fields.Many2one('project.project',
        ondelete='cascade', string="Projet", required=True)

class Solution(models.Model):
    _name = "cdt.solution"
    _description = "Solution au risque"
   
    id = fields.Char("ID", readonly=True, required=True, copy=False , default='Nouveau')
    name = fields.Text(string="Contenu", required=True)
    risque_id = fields.Many2one('cdt.risque',
        ondelete='cascade', string="Risque", required=True)
    projet = fields.Many2one('project.project',
        ondelete='cascade', string="Projet", required=True)