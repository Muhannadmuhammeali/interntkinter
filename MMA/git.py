from github import Github, Issue, PullRequest, Project,Auth

# Authentication with access token
access_token = "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"
auth = Auth.Token(access_token)
g = Github(auth=auth)

# Function to get a repository object
def get_repo(username, repo_name):
  try:
    return g.get_repo(f"{username}/{repo_name}")
  except Exception as e:
    print(f"Error retrieving repository: {e}")
    return None

# Function to create an issue
def create_issue(repo, title, body, labels=[]):
  try:
    issue = repo.create_issue(title=title, body=body, labels=labels)
    print(f"Issue created: {issue.url}")
    return issue
  except Exception as e:
    print(f"Error creating issue: {e}")
    return None

# Function to create and link an issue to a pull request
def create_and_link_issue(repo, title, body, pull_request):
  issue = create_issue(repo, title, body, labels=["issue"])
  if issue:
    pull_request.add_to_labels("issue")
    issue.create_pull_request_review(pull_request.url)

# Function to link a pull request to a project
def link_pull_request_to_project(pull_request, project_number):
  try:
    project = g.get_project(pull_request.base.repo.id, project_number)
    project.create_card(content_id=pull_request.id, content_type="PullRequest")
    print(f"Pull request linked to project {project_number}")
  except Exception as e:
    print(f"Error linking pull request to project: {e}")

# Function to get comments on an issue or pull request (optional)
def get_comments(obj):
  try:
    comments = obj.get_comments()
    for comment in comments:
      print(f"Comment by {comment.user.login}: {comment.body}")
  except Exception as e:
    print(f"Error getting comments: {e}")

# Function to list all open issues in a repository
def list_open_issues(repo):
  try:
    issues = repo.get_issues(state="open")
    for issue in issues:
      print(f"Issue #{issue.number}: {issue.title}")
  except Exception as e:
    print(f"Error listing issues: {e}")

# Function to get an issue by number
def get_issue_by_number(repo, issue_number):
  try:
    issue = repo.get_issue(number=issue_number)
    print(f"Issue #{issue.number}: {issue.title}")
    print(f"Description: {issue.body}")
    return issue
  except Exception as e:
    print(f"Error getting issue #{issue_number}: {e}")
    return None

# Example usage
username = "Muhannadmuhammeali"
repo_name = "DS"

repo = get_repo(username, repo_name)

if repo:
  # Get a specific pull request (replace with pull request number)
  pull_request = repo.get_pull(number=123)

  # Create and link an issue to the pull request
  create_and_link_issue(repo, "Fix needed", "Some details about the fix", pull_request)

  # Link the pull request to a project (replace with project ID)
  link_pull_request_to_project(pull_request, 1)

  # Get comments on the pull request (optional)
  get_comments(pull_request)

  # List all open issues
  list_open_issues(repo)

  # Get a specific issue by number (replace with issue number)
  get_issue_by_number(repo, 456)
else:
  print(f"Failed to retrieve repository: {username}/{repo_name}")

# Close connections after use
g.get_rate_limit().reset_on_rate_limit = True
