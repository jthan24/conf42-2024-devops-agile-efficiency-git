resource "github_repository" "template_repository" {
  name               = "template_org_repository"
  description        = "This is the template repository for organization"
  is_template        = true
  visibility         = "private"
  auto_init          = true
  gitignore_template = "Terraform"
}

resource "github_repository" "first_org_repository" {
  name        = "first_repository_for_organization"
  description = "This is my first repository based on template_repository"
  visibility  = "public"

  template {
    owner                = var.github_owner
    repository           = "template_org_repository"
    include_all_branches = true
  }
}

resource "github_branch" "main_branch" {
  repository = github_repository.first_org_repository.name
  branch     = "main"
}

resource "github_branch_default" "default_branch" {
  repository = github_repository.first_org_repository.name
  branch     = github_branch.main_branch.branch
}

resource "github_team" "org_dev_team" {
  name        = "Development org team"
  description = "This is a development team"
  privacy     = "closed"
}

resource "github_team_repository" "dev_repository" {
  team_id    = github_team.org_dev_team.id
  repository = github_repository.first_org_repository.name
  permission = "pull"
}

resource "github_team_members" "add_member_to_team" {
  team_id = github_team.org_dev_team.id

  members {
    username = var.org_user
    role     = "maintainer"
  }
}

resource "github_branch_protection_v3" "branch_protection" {
  repository             = github_repository.first_org_repository.name
  branch                 = github_branch.main_branch.branch
  enforce_admins         = true
  require_signed_commits = true

  required_pull_request_reviews {
    dismiss_stale_reviews = true
    dismissal_teams       = [github_team.org_dev_team.slug]
  }
}