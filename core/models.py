from django.db import models
from django.contrib.auth.models import User

class AuditModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="%(app_label)s_%(class)s_created")
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="%(app_label)s_%(class)s_updated")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class Partner(AuditModel):
    name = models.CharField(max_length=100)
    logo_domain = models.URLField(help_text="e.g., https://barrick.com")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        
    def __str__(self):
        return self.name

class Testimonial(AuditModel):
    author = models.CharField(max_length=200)
    quote = models.TextField()
    stars = models.IntegerField(default=5)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.author

class Statistic(AuditModel):
    value_number = models.CharField(max_length=50)
    value_suffix = models.CharField(max_length=10, blank=True, null=True, help_text="e.g. +, Y, %")
    label = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.value_number}{self.value_suffix or ''} {self.label}"

class Advantage(AuditModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_number = models.CharField(max_length=10, default="01")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class HeroContent(AuditModel):
    kicker = models.CharField(max_length=100, default="MINING & GEOTECHNICAL CONSULTING")
    title = models.TextField(default="Engineering<br>Operational Certainty.")
    description = models.TextField(default="We deliver practical, highly-specialized geotechnical solutions tailored to your individual operational and risk profile across the world's most demanding sites.")
    background_image = models.ImageField(upload_to='core/', blank=True, null=True)
    
    intro_statement = models.TextField(default="Unlocking the potential of mining projects with <span class='text-gold'>unparalleled expertise</span> and relentless innovation. Pejuni is your strategic partner in subsurface risk management.")
    why_choose_us_intro = models.TextField(default="When you choose Pejuni, you are selecting a trusted partner that combines specialized expertise, advanced technologies, and an unwavering commitment to safety. We increase the net value of your open-pit or underground project through innovative engineering solutions.")

    def __str__(self):
        return "Homepage Site Configuration"

class FooterContent(AuditModel):
    company_description = models.TextField(default="Engineering stability. Ensuring operational excellence. Pejuni Resources.")
    address_hq = models.TextField(default="Mwanza, Tanzania")
    phone_hq = models.CharField(max_length=50, default="+255 759 199 623")
    phone_aus = models.CharField(max_length=50, default="+61 470 578 151")
    email_primary = models.EmailField(default="admin@pejuni.com")
    email_secondary = models.EmailField(default="info@pejuni.com")
    linkedin_url = models.URLField(blank=True, default="#")
    twitter_url = models.URLField(blank=True, default="#")

    def __str__(self):
        return "Global Footer Configuration"
