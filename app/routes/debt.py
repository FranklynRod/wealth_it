

asset_bp = Blueprint("asset", __name__, url_prefix="/assets")
# Create debt entry
@asset_bp.route("/<asset_id>", strict_slashes=False, methods=["POST"])
def create_one_asset():
    
# READ debt entry
@asset_bp.route("/<asset_id>", strict_slashes=False, methods=[""])
def read_one_asset(asset_id):


# DELETE debt entry
@asset_bp.route("/<asset_id>", strict_slashes=False, methods=["DELETE"])
def delete_one_asset(asset_id):

# Update debt entry
@asset_bp.route("/<asset_id>", strict_slashes=False, methods=["PUT"])
def update_one_asset(asset_id):