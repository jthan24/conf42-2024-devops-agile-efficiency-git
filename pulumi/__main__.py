"""A Python Pulumi program"""

import pulumi
import pulumi_github as github

config = pulumi.Config()
github_owner = config.require("githubOwner")
org_user = config.require("orgUser")

stack = pulumi.get_stack()

# Global variables
template_repository = None
first_org_repository = None
main_branch = None
org_dev_team = None


def template_repository():
    template_repository = github.Repository("template_repository",
        name="template_org_repository",
        description="This is the template repository for organization",
        is_template=True,
        visibility="private",
        auto_init=True,
        gitignore_template="Terraform")

def first_org_repository():
    first_org_repository = github.Repository("first_org_repository",
        name="first_repository_for_organization",
        description="This is my first repository based on template_repository",
        visibility="public",
        template=github.RepositoryTemplateArgs(
            owner=github_owner,
            repository="template_org_repository",
            include_all_branches=True,
        ))
    return first_org_repository

def main_branch():
    main_branch = github.Branch("main_branch",
        repository=first_org_repository.name,
        branch="main")
    return main_branch

def default_branch():
    default_branch = github.BranchDefault("default_branch",
        repository=first_org_repository.name,
        branch=main_branch.branch)

def org_dev_team():
    org_dev_team = github.Team("org_dev_team",
        name="development org team",
        description="This is a development team",
        privacy="closed")
    return org_dev_team

def dev_repository():
    dev_repository = github.TeamRepository("dev_repository",
        team_id=org_dev_team.id,
        repository=first_org_repository.name,
        permission="pull")

def add_member_to_team():
    add_member_to_team = github.TeamMembers("add_member_to_team",
        team_id=org_dev_team.id,
        members=[github.TeamMembersMemberArgs(
            username=org_user,
            role="maintainer",
        )])

def branch_protection():
    branch_protection = github.BranchProtectionV3("branch_protection",
        repository=first_org_repository.name,
        branch=main_branch.branch,
        enforce_admins=True,
        require_signed_commits=True,
        required_pull_request_reviews=github.BranchProtectionV3RequiredPullRequestReviewsArgs(
            dismiss_stale_reviews=True,
            dismissal_teams=[org_dev_team.slug],
        ))

template_repository()
first_org_repository = first_org_repository()
main_branch = main_branch()
default_branch()
org_dev_team = org_dev_team()
dev_repository()
add_member_to_team()
branch_protection()
