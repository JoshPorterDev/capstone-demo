from django.db import models

# Create your models here.

# Electronics
class EHRComputer(models.Model):
    code = models.IntegerField(unique=True)

    def __str__(self):
        return f"EHR Computer -{self.code}"


class CADTablet(models.Model):
    code = models.IntegerField(unique=True)

    def __str__(self):
        return f"CAD Tablet -{self.code}"


class EightHundredMHZRadio(models.Model):
    code = models.IntegerField(unique=True)

    def __str__(self):
        return f"800MHz -{self.code}"


class VHFRadio(models.Model):
    code = models.IntegerField(unique=True)

    def __str__(self):
        return f"VHF Radio -{self.code}"


class ElectronicMonitor(models.Model):
    code = models.IntegerField(unique=True)

    def __str__(self):
        return f"Electronic Monitor -{self.code}"


class ElectronicRadio(models.Model):
    code = models.IntegerField(unique=True)

    def __str__(self):
        return f"Electronic Radio -{self.code}"


# Equipment
class NarcoticBox(models.Model):
    code = models.IntegerField(unique=True)

    def __str__(self):
        return f"Narcotic Box -{self.code}"


class Cot(models.Model):
    code = models.IntegerField(unique=True)

    def __str__(self):
        return f"Cot -{self.code}"


class ECG(models.Model):
    code = models.IntegerField(unique=True)

    def __str__(self):
        return f"ECG electrocardiogram -{self.code}"


class Glucometer(models.Model):
    code = models.IntegerField(unique=True)

    def __str__(self):
        return f"Glucometer -{self.code}"


class Suction(models.Model):
    code = models.IntegerField(unique=True)

    def __str__(self):
        return f"Suction -{self.code}"


class AutoPulse(models.Model):
    code = models.IntegerField(unique=True)

    def __str__(self):
        return f"Auto Pulse -{self.code}"


class Sonim(models.Model):
    code = models.IntegerField(unique=True)

    def __str__(self):
        return f"Sonim -{self.code}"


class SonimCharger(models.Model):
    code = models.IntegerField(unique=True)

    def __str__(self):
        return f"Sonim Charger -{self.code}"


class Ambulance(models.Model):
    LOCATIONS = (
        ("N", "North"),
        ("S", "South"),
        ("R", "Republic"),
        ("P", "Pre hospital"),
        ("RF", "RayFields"),
        ("BS", "Bodyshop"),
        ("O", "Other"),
    )

    STATUS = (
        ("IS", "In service"),
        ("B", "Backup"),
        ("OC", "On call"),
        ("ISO", "In service -other"),
        ("OOS-M", "Out of service -mechanical"),
        ("OOS-D", "Out of service -dead"),
        ("OOS-O", "Out of service -other"),
    )

    # Ambulance specific information
    code = models.IntegerField(unique=True)
    location = models.CharField(max_length=2, choices=LOCATIONS)
    status = models.CharField(max_length=5, choices=STATUS)
    mileage = models.IntegerField()
    insurance = models.BooleanField()
    avl = models.IntegerField()
    service_mileage = models.IntegerField()

    # Equipment and Electronics
    ehr_computer = models.OneToOneField(EHRComputer, blank=True, null=True, on_delete=models.SET_NULL, related_name='ambulance')
    cad_tablet = models.OneToOneField(CADTablet, blank=True, null=True, on_delete=models.SET_NULL, related_name='ambulance')
    eighthundredmhz_radio = models.OneToOneField(EightHundredMHZRadio, blank=True, null=True, on_delete=models.SET_NULL, related_name='ambulance')
    vhf_radio = models.OneToOneField(VHFRadio, blank=True, null=True, on_delete=models.SET_NULL, related_name='ambulance')
    electronic_monitor = models.OneToOneField(ElectronicMonitor, blank=True, null=True, on_delete=models.SET_NULL, related_name='ambulance')
    electronic_radio = models.OneToOneField(ElectronicRadio, blank=True, null=True, on_delete=models.SET_NULL, related_name='ambulance')

    narcotic_box = models.OneToOneField(NarcoticBox, blank=True, null=True, on_delete=models.SET_NULL, related_name='ambulance')
    cot = models.OneToOneField(Cot, blank=True, null=True, on_delete=models.SET_NULL, related_name='ambulance')
    ecg = models.OneToOneField(ECG, blank=True, null=True, on_delete=models.SET_NULL, related_name='ambulance')
    glucometer = models.OneToOneField(Glucometer, blank=True, null=True, on_delete=models.SET_NULL, related_name='ambulance')
    suction = models.OneToOneField(Suction, blank=True, null=True, on_delete=models.SET_NULL, related_name='ambulance')
    auto_pulse = models.OneToOneField(AutoPulse, blank=True, null=True, on_delete=models.SET_NULL, related_name='ambulance')
    sonim = models.OneToOneField(Sonim, blank=True, null=True, on_delete=models.SET_NULL, related_name='ambulance')
    sonim_charger = models.OneToOneField(SonimCharger, blank=True, null=True, on_delete=models.SET_NULL, related_name='ambulance')

    def __str__(self):
        return f"Ambulance -{self.code}"


class Maintenance(models.Model):
    ambulance = models.ForeignKey(Ambulance, on_delete=models.SET_NULL, null=True)
    issue = models.TextField()

