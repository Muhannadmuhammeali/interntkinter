from github import Github

# Authentication with access token
auth = Auth.Token("your_access_token")
g = Github(auth=auth)

def edit_repo(repo_name, disable_wiki=True):
  """Edits a repository by disabling the wiki (optional).

  Args:
      repo_name (str): Name of the repository to edit.
      disable_wiki (bool, optional): Whether to disable the wiki (default: True).

  Returns:
      bool: True if edit was successful, False otherwise.
  """
  try:
      repo = g.get_repo(repo_name)  # Get the repository object
      if repo.owner.login == g.get_user().login:  # Check ownership
          repo.edit(has_wiki=disable_wiki)
          print(f"Successfully disabled wiki for {repo.name}")
          return True
      else:
          print(f"Insufficient permissions to edit {repo_name}")
          return False
  except Exception as e:
      print(f"Error editing repository {repo_name}: {e}")
      return False

# Edit specific repository (replace with your desired repository name)
if edit_repo("your_repo_name"):
  print("Edit successful!")
else:
  print("Edit failed.")
