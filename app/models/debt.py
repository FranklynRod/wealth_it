from app import db

class Debt(db.Model):
    debt_id = db.Column(db.Integer, primary_key=True, autoincrement= True)
    date = db.Column(db.date, nullable=False)
    student_loan = db.Column(db.numeric)
    car_loan = db.Column(db.numeric)
    credit_card = db.Column(db.numeric)
    mortgage = db.Column(db.numeric)
    other = db.Column(db.numeric)
    account_id = db.Column(db.Integer, ForeignKey(""))
    account = db.relationship("Account", back_populates = "debt")
    
    def to_dict(self):
        result_dict = {}
        result_dict["id"] = self.debt_id
        result_dict["student_loan"] = self.student_loan
        result_dict["car_loan"] = self.car_loan
        result_dict["credit_card"] = self.credit_card
        result_dict["mortgage"] = self.mortgage
        result_dict["other"] = self.other


    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            username = data_dict["username"],
            student_loan = data_dict["student_loan"],
            car_loan = data_dict["car_loan"],
            credit_card = data_dict["credit_card"],
            mortgage = data_dict["mortgage"],
            other = data_dict["other"]
            )