
# opentofu
This folder contains needed files to execute your devops starter pack for your dev team

# Instructions 

- Initialize tofu modules based on terraform code
```bash
tofu init
```

- Create a template repository
```bash
tofu apply -target=github_repository.template_repository
```

- Create your first repository
```bash
tofu apply -target=github_repository.first_org_repository
```

- Define your main branch
```bash
tofu apply -target=github_branch.main_branch
```

- Set up default branch
```bash
tofu apply -target=github_branch_default.default_branch
```

- Create a development team
```bash
tofu apply -target=github_team.org_dev_team
```

- Add reposiroty to your team
```bash
tofu apply -target=github_team_repository.dev_repository
```

- Add people to your development team
```bash
tofu apply -target=github_team_members.add_member_to_team
```

- Define protection to branch
```bash
tofu apply -target=github_branch_protection_v3.branch_protection
```

# Clean up resources generated
```bash
tofu destroy -auto-approve
```

# References
https://registry.terraform.io/providers/integrations/github/latest/docs/resources/repository


<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_github"></a> [github](#requirement\_github) | ~> 5.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_github"></a> [github](#provider\_github) | 5.44.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [github_branch.main_branch](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/branch) | resource |
| [github_branch_default.default_branch](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/branch_default) | resource |
| [github_branch_protection_v3.branch_protection](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/branch_protection_v3) | resource |
| [github_repository.first_org_repository](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/repository) | resource |
| [github_repository.template_repository](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/repository) | resource |
| [github_team.org_dev_team](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/team) | resource |
| [github_team_members.add_menber_to_team](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/team_members) | resource |
| [github_team_repository.dev_repository](https://registry.terraform.io/providers/integrations/github/latest/docs/resources/team_repository) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_github_owner"></a> [github\_owner](#input\_github\_owner) | This is a owner for org | `string` | `"conf42-2024-devops"` | no |
| <a name="input_org_user"></a> [org\_user](#input\_org\_user) | This is a user added on your org | `string` | `"this_is_your_user"` | no |

## Outputs

No outputs.
<!-- END_TF_DOCS -->