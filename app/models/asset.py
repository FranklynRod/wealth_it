from app import db

class Asset(db.Model):
    asset_id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    date = db.Column(db.date, nullable=False)
    savings = db.Column(db.numeric)
    home_equity = db.Column(db.numeric)
    retirement = db.Column(db.numeric)
    investments = db.Column(db.numeric)
    other = db.Column(db.numeric)
    account = db.relationship("Account", back_populates = "asset")
    
    def to_dict(self):
        result_dict = {}
        result_dict["id"] = self.asset_id
        result_dict["date"] = self.date
        result_dict["home_equity"] = self.home_equity
        result_dict["retirement"] = self.retirement
        result_dict["investments"] = self.investments
        result_dict["other"] = self.other


    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            username = data_dict["username"],
            home_equity = data_dict["home_equity"],
            retirement = data_dict["retirement"],
            investments = data_dict["investments"],
            other = data_dict["other"]
            )