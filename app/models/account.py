from app import db

class Account(db.Model):
    account_id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    username = db.Column(db.String, nullable=False)
    # debt = db.relationship("Debt", back_populates = "account")
    # asset = db.relationship("Asset", back_populates = "account")
    
    def to_dict(self):
        result_dict = {}
        result_dict["id"] = self.account_id
        result_dict["username"] = self.username

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
           username = data_dict["username"]
        )