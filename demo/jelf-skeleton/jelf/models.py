from django.db.models import CharField
from jeevesdb.JeevesModel import JeevesModel as Model, JeevesForeignKey as ForeignKey
from jeevesdb.JeevesModel import label_for
from sourcetrans.macro_module import macros, jeeves
import JeevesLib

def pick_among(jeeves_id, replacement_set):
    return replacement_set[hash(jeeves_id) % len(replacement_set)]

# An example model.
# Right now self-reference is either impossible or difficult because JeevesForeignKey
# only supports a model class (not a string) as the related object. (TODO fix this.)
class UserProfile(Model):
	username = CharField(max_length=1024)
	email = CharField(max_length=1024)

	@staticmethod
	def jeeves_get_private_email(user):
		return "[redacted]"

        @staticmethod
        def jeeves_get_honeypot_email(jeeves_id):
            return pick_among(jeeves_id, ["alpha", "bravo", "charlie", "delta", "echo"])
            
	@staticmethod
	@label_for('email')
	@jeeves
	def jeeves_restrict_userprofilelabel(user, ctxt):
		return user == ctxt

class Password(Model):
    user = ForeignKey(UserProfile, null=True)
    site_url = CharField(max_length=1024)
    site_username = CharField(max_length=1024)
    site_password = CharField(max_length=1024)

    @staticmethod
    def jeeves_get_private_site_password(pwd):
        return "[redacted]"

    @staticmethod
    def jeeves_get_honeypot_site_password(jeeves_id):
        return pick_among(jeeves_id, ["p@ssw0rd", "hunter12", "iloveyou"])

    @staticmethod
    def jeeves_get_private_site_username(pwd):
        return "[redacted]"

    @staticmethod
    def jeeves_get_honeypot_site_username(jeeves_id):
        return pick_among(jeeves_id, ["myname1", "user2531", "urboi1121"])

    @staticmethod
    def jeeves_get_private_site_url(pwd):
        return "[redacted]"

    @staticmethod
    def jeeves_get_honeypot_site_url(jeeves_id):
        return pick_among(jeeves_id, ["http://ashton.honeypot.com", 
            "http://another.honeypot.com", "banana.honeypot.com"])

    @staticmethod
    @label_for('site_url', 'site_username', 'site_password')
    @jeeves
    def jeeves_restrict_passwordlabel(pwd, context):
        # for now, only the owner user can see their
        # passwords
        return pwd.user == context
