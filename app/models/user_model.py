# User (enterprises, authorities, individuals) ORM model

from datetime import datetime

class User_Schema:
    def __init__(self, data: dict):  
        self.name = data.get("name")
        self.email = data.get("email")
        self.phone = data.get("phone")
        self.user_id = data.get("user_id")
        self.user_type = data.get("user_type")  # 'enterprise', 'authority', 'individual'
        self.user_name = f"{data.get("user_type")}_{data.get("name").lower().replace(' ', '_')}_{data.get("user_id")}"  # created on server-side

        # Common metadata
        self.created_at = datetime.now()

        # Optional fields depending on user type
        if self.user_type == "enterprise":
            self.company_name = data.get("company_name")
            self.industry = data.get("industry")
            self.fleet_size = data.get("fleet_size", 0)
            self.total_pilots = data.get("total_pilots",0)

        elif self.user_type == "authority":
            self.agency_name = data.get("agency_name")
            self.designation = data.get("designation")
            self.region = data.get("region")

        elif self.user_type == "individual":
            self.license_id = data.get("license_id")
            self.certifications = data.get("certifications", [])
            self.experience_years = data.get("experience_years", 0)
            self.specializations = data.get("specializations", [])

    def to_dict(self):
        return self.__dict__        