from datetime import datetime
import json


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o): # type: ignore
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)
