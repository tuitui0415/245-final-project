import json
from bugswarm.common.rest_api.database_api import DatabaseAPI
from collections import Counter

bugswarmapi = DatabaseAPI(token='ECS245-TOKEN')

api_filter = json.dumps({
    "lang": "Java",
    "status": "active",
    "reproducibility_status.status": "Reproducible"
})

artifacts = bugswarmapi.filter_artifacts(api_filter)

# Get all exception type
exceptions = []

for a in artifacts:
    if 'classification' in a:
        if 'exceptions' in a['classification']:
            exceptions.extend(a['classification']['exceptions'])

print("\n=== Exceptions ===")
for exc, count in Counter(exceptions).most_common():
    print(f"{exc}: {count}")