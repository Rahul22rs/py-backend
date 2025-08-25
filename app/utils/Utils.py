class Utils:
    @staticmethod
    def formateddResponse(data=None, message="Success", status=True, errors=None):
        return {
            "status": status,
            "message": message,
            "data": data,
            "errors": errors,
        }
