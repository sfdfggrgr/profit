

from github import Github
from apscheduler.schedulers.background import BackgroundScheduler



def updatee():
    owner = "sfdfggrgr"
    repo_name = "cookie"
    file_path = 'account_1.json'
    commit_message = 'Update file content'
    github_token = "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"
    g = Github(github_token)
    repo = g.get_repo(f"{owner}/{repo_name}")
    # Get the current content of the file you want to update
    file = repo.get_contents(file_path)
    existing_file_content = file.decoded_content.decode('utf-8')
    with open(file_path, 'rb') as f1:
        new_content = f1.read()
    # Update the file on GitHub
    repo.update_file(
        path=file_path,
        message=commit_message,
        content=new_content,
        sha=file.sha,
        branch='main'  # Replace with your branch name
    )




scheduler1 = BackgroundScheduler()
scheduler1.add_job(updatee, 'interval', seconds=600)  # run every 5 minutes
scheduler1.start()



if __name__ == '__main__':
    # This block will only be executed when the script is run directly, not when imported
    try:
        while True:
            pass  # Keep the main thread alive
    except KeyboardInterrupt:
        scheduler.shutdown()
