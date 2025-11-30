from bugswarm.common.rest_api.database_api import DatabaseAPI
import json
bugswarmapi = DatabaseAPI(token='ECS245-TOKEN')

api_filter = json.dumps({
    "lang": "Java",
    "classification.exceptions": "ArrayIndexOutOfBoundsException",
    "status": "active",
    "reproducibility_status.status": "Reproducible"
})

test_artifacts = bugswarmapi.filter_artifacts(api_filter)
# test_artifacts = test_artifacts[:10]
image_tags = [a['image_tag'] for a in test_artifacts]
print(len(test_artifacts))
print(image_tags)

# with open("/bugswarm-sandbox/artifact_list.txt", "w", encoding="utf-8") as f:
#     for tag in image_tags:
#         f.write(tag + "\n")


