


debt_bp = Blueprint("debt", __name__, url_prefix="/debts")

# READ debt entry
@debt_bp.route("/<debt_id>", strict_slashes=False, methods=["GET"])
def read_one_debt(debt_id):


# DELETE debt entry
@debt_bp.route("/<debt_id>", strict_slashes=False, methods=["DELETE"])
def delete_one_debt(debt_id):

# Update debt entry
@debt_bp.route("/<debt_id>", strict_slashes=False, methods=["PUT"])
def update_one_debt(debt_id):

# Create debt entry
@debt_bp.route("/<debt_id>", strict_slashes=False, methods=["POST"])
def create_one_debt():