



import httplib
import base64

xmlheader='<?xml version="1.0" encoding="UTF-8"?>\n'

class client():
    """Client class for managing connection"""
    def __init__(self, url, user, password):
        self.url=url
        self.user=user
        self.password=password
        self.con=self.connect()
        
    def connect(self):
        con = httplib.HTTPSConnection(self.url)
        #test connection
        b64string = base64.encodestring('%s:%s' % (username, password))[:-1]
        header=("Authorization", "Basic %s" % base64string)
        
        
        #return connection or error
        
    def get_invoice_list(self):
        """Return python list of invoice objects"""
        Pass
    def get_invoice(self, id):
        Pass
    def update_invoice(self, invoice):
        Pass
    def get_contact_list(self):
        Pass
    def get_contact(self, id):
        Pass
    def unroll(self, response):
        Pass
    def roll(self,  object):
        Pass

class invoiceItem():
    """An invoice item"""
    def __init__(self):
        """generate empty item"""
        self.id = None
        self.invoice_id = None
        self.project_id = None
        self.type = None
        self.description= ''
        self.price = None
        self.quantity = None
        self.tax_rate = None
        self.tax_value = None
class invoice():
    """ An Invoice"""
    def __init__(self):
        """generate empty item"""
        self.id = None
        
class contact():
    """<?xml version="1.0" encoding="UTF-8"?>
    <contact>
      <id type="integer">28</id>
      <organisation-name></organisation-name>
      <first-name>Andy</first-name>
      <last-name>Warhol</last-name>
      <address1></address1>
      <address2></address2>
      <address3></address3>
      <town></town>
      <region></region>
      <country>United Kingdom</country>
      <postcode></postcode>
      <phone-number></phone-number>
      <email></email>
      <contact-name-on-invoices type="boolean">true</contact-name-on-invoices>
      <sales-tax-registration-number></sales-tax-registration-number>
      <uses-contact-invoice-sequence type="boolean">true</uses-contact-invoice-sequence>
    </contact>"""
    def __init__(self):
        #TODO: ascertain sensible defaults
        self.id=0
        self.organization_name=''
        self.first_name=''
        self.last_name=''
        self.address1=''
        self.address2=''
        self.address3=''
        self.town=''
        self.region=''
        self.country=''
        self.postcode=''
        self.phone_number=''
        self.email=''
        self.contact_name_on_invoices=True
        self.sales_tax_number=''
        self.uses_contact_invoice_seq=True
        return 
        
    def __repr__(self):
        """Returns xml as string, if valid, otherwise returns error message"""
        xml=self.as_xml()
        if xml == False:
            return "Invalid Contact object"
        else:
            return xml
        
    
    def as_xml(self):
        """Returns correctly formatted xml of contact object, or False"""
        xml=''
        # blank entires are still expected, eg "<postcode></postcode>"
        if self.id=='0':
            #creating a new contact
            #TODO: check this behaviour
            Pass
        if ((self.first_name=='') | (self.last_name=='')):
            #these are both required - return an error
            return False
        
        xml =xmlheader+'<contact>\n'
        xml+=' <id type="integer">'+str(self.id)+'</id>\n'
        xml+=' <organisation-name>'+self.organization_name+'</organisation-name>\n'
        xml+=' <first-name>'+self.first_name+'</first-name>\n'
        xml+=' <last-name>'+self.first_name+'</last-name>\n'
        xml+=' <address1>'+self.address1+'</address1>\n'
        xml+=' <address2>'+self.address2+'</address2>\n'
        xml+=' <address3>'+self.address3+'</address3>\n'
        xml+=' <town>'+self.town+'</town>\n'
        xml+=' <region>'+self.region+'</region>\n'
        xml+=' <country>'+self.country+'</country>\n'
        xml+=' <postcode>'+self.postcode+'</postcode>\n'
        xml+=' <phone-number>'+self.phone_number+'</phone-number>\n'
        xml+=' <email>'+self.email+'</email>\n'
        xml+=' <contact-name-on-invoices type="boolean">'+str(self.contact_name_on_invoices).lower()+'</contact-name-on-invoices>\n'
        xml+=' <sales-tax-registration-number>'+self.sales_tax_number+'</sales-tax-registration-number>\n'
        xml+=' <uses-contact-invoice-sequence type="boolean">'+str(self.uses_contact_invoice_seq).lower()+'</uses-contact-invoice-sequence>\n'
        xml+='</contact>\n'
        return xml

    def as_dict(self):
        """Returns the object as a key-pair in Python dictionary format"""
        #TODO: is there any point in optionally creating a sparse dictionary, omitting null values?
        Pass
    
    def update(self, connection):
        """Updates an existing contact"""
        #TODO: This
        Pass
    def create(self, connection):
        """Creates a new contact """
        #TODO: This
        Pass
    def delete(self, connection):
        """Delete contact """
        #TODO: This
        Pass
