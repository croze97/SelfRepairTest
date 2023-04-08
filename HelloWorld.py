import requests
import zipfile

# Download the artifact
url = f"{os.environ['GITHUB_SERVER_URL']}/{os.environ['GITHUB_REPOSITORY']}/actions/artifacts/<artifact-id>/zip"
headers = {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"}
response = requests.get(url, headers=headers)

# Extract the error log file from the zip archive
with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
    error_log_file = zip_file.read("logs/error.log")
    error_log = error_log_file.decode("utf-8")
    print(error_log)

print("Hello :)")
