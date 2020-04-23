from django.db import models

cbd_lead_names = (
    ("Simon Woodford", "Simon Woodford"),
    ("Vin Bolisetti", "Vin Bolisetti"),
)

term_type = (
    ("Cloud Subscription", "Cloud Subscription"),
    ("Cloud Perpetual", "Cloud Perpetual"),
    ("SaaS", "SaaS"),
)

prod_name = (
    ('OpenText ContentSuite', 'OpenText ContentSuite'),
    ('OpenText Experience Suite', 'OpenText Experience Suite'),
    ('OpenText Process Suite', 'OpenText Process Suite'),
    ('OpenText Information Exchange Suite', 'OpenText Information Exchange Suite'),
    ('OpenText Discovery Suite', 'OpenText Discovery Suite'),
    ('OpenText Suite for SAP', 'OpenText Suite for SAP'),
    ('OpenText Suite for Oracle', 'OpenText Suite for Oracle'),
    ('OpenText Suite for Microsoft', 'OpenText Suite for Microsoft'),
    ('OpenText Appworks', 'OpenText Appworks'),
    ('OpenText Cloud', 'OpenText Cloud'),
)

bool_val = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)


class AddQuote(models.Model):
    o_id = models.CharField(max_length=120)
    customer_name = models.CharField(max_length=120, default='Enter Account Name')
    lead_name = models.CharField(max_length=56, choices=cbd_lead_names)
    term_type = models.CharField(max_length=120, choices=term_type)
    product = models.CharField(max_length=120, choices=prod_name)
    penalties = models.CharField(max_length=20, choices=bool_val)

    def __str__(self):
        return f'{self.o_id} : {self.customer_name} : {self.lead_name}'
