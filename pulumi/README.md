# Pulumi
Start with pulumi's project
```bash
pulumi new python -y
Passphrase for secrets: ThisIsASecret
export PULUMI_CONFIG_PASSPHRASE=ThisIsASecret
```

# In to venv on python
```bash
source venv/bin/activate 
```

# Install a provider
```bash
pip3 install pulumi-github
```

# Generate the requirements.txt file
```bash
pip3 freeze > requirementst.txt
```

# Execute the stacks

- Create a template repository
```bash
pulumi up -s dev -y -t urn:pulumi:dev::pulumi::github:index/repository:Repository::template_repository
```

- Create your first repository
```bash
pulumi up -s dev -y -t urn:pulumi:dev::pulumi::github:index/repository:Repository::first_org_repository
```

- Define your main branch
```bash
pulumi up -s dev -y -t urn:pulumi:dev::pulumi::github:index/branch:Branch::main_branch
```

- Set up default branch
```bash
pulumi up -s dev -y -t urn:pulumi:dev::pulumi::github:index/branchDefault:BranchDefault::default_branch
```

- Create a development team
```bash
pulumi up -s dev -y -t urn:pulumi:dev::pulumi::github:index/team:Team::org_dev_team
```

- Add reposiroty to your team
```bash
pulumi up -s dev -y -t urn:pulumi:dev::pulumi::github:index/teamRepository:TeamRepository::dev_repository
```

- Add people to your development team
```bash
pulumi up -s dev -y -t urn:pulumi:dev::pulumi::github:index/teamMembers:TeamMembers::add_member_to_team
```

- Define protection to branch
```bash
pulumi up -s dev -y -t urn:pulumi:dev::pulumi::github:index/branchProtectionV3:BranchProtectionV3::branch_protection
```

# Clean resources
pulumi destroy -s dev -y -e 

# References
https://www.pulumi.com/registry/packages/github/api-docs/branch/
https://www.pulumi.com/docs/cli/commands/pulumi_up/

